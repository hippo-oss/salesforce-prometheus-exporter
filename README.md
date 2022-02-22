# Salesforce Prometheus Exporter

This repo fetches logs from Salesforce & creates a custom exporter, which can be scraped by prometheus.

### Getting Started

```shell
pip install salesforce-prometheus-exporter
```

Set the following environment variables.
```shell
SF_URL=<salesforce url>
SF_VERSION=<salesforce version>
CONSUMER_ID=<salesforce consumer/client ID>
CONSUMER_SECRET=<salesforce consumer/client secret>
AUTH_USERNAME=<salesforce username>
AUTH_PASSWORD=<salesforce password>
```
Then, start server command:

```shell
salesforce-exporter start-server
```
Go to http://localhost:3000/metrics to view the metrics. The default port is `3000`, to change the port use `--port` option.

```shell
salesforce-exporter start-server --port <PORT>
```

NOTE: The metrics will start with the prefix `sfdc`
