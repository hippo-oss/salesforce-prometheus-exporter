from prometheus_client.core import GaugeMetricFamily
from SalesforcePy import client as sfdc_client
from os import environ
import logging
import requests

logging.basicConfig(level=logging.INFO)


class Collector(object):
    def __init__(self):
        self.salesforce_version = environ["SF_VERSION"]
        self.environment = environ.get("ENVIRONMENT") or "local"

        self.client = sfdc_client(
            username=environ["AUTH_USERNAME"],
            password=environ["AUTH_PASSWORD"],
            client_id=environ["CONSUMER_ID"],
            client_secret=environ["CONSUMER_SECRET"],
            login_url=environ["SF_URL"],
            version=self.salesforce_version,
            timeout="30",
        )

    def fetch_salesforce_logs(self):
        logging.info("Fetching Salesforce access credentials.")
        credentials = self.client.login()[0]

        if not credentials:
            raise ConnectionRefusedError("Incorrect credentials. Please try again....")

        headers = {
            "Authorization": f"Bearer {credentials['access_token']}",
        }

        logging.info("Fetching Salesforce logs.")
        response = requests.get(
            f"{credentials['instance_url']}/services/data/v{self.salesforce_version}/limits",
            headers=headers,
        )

        if response.status_code == 200:
            logging.info(f"[{response.status_code}]: Logs fetched successfully.")
            return response.json()
        else:
            raise ConnectionError(f"[{response.status_code}]: {response.text}")

    def iterator(self, logs: dict, parent=None):
        for key, value in logs.items():
            if parent:
                metric = f"{parent}".replace(" ", "_").replace(".", "_")
            if type(value) == dict:
                if parent:
                    new_parent = f"{parent}_{key}"
                else:
                    new_parent = key
                for log in self.iterator(logs=value, parent=new_parent):
                    yield log
            elif key == "Remaining":
                c = GaugeMetricFamily(
                    f"sfdc_remaining_{metric}",
                    f"{parent or ''} {key}",
                    labels=["env"],
                )
                c.add_metric([self.environment], value)
                yield c
            elif key == "Max":
                c = GaugeMetricFamily(
                    f"sfdc_limit_{metric}",
                    f"{parent or ''} {key}",
                    labels=["env"],
                )
                c.add_metric([self.environment], value)
                yield c

    def collect(self):
        logs = self.fetch_salesforce_logs()
        for log in self.iterator(logs=logs):
            yield log
