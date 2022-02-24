# Salesforce Prometheus Exporter

This repo fetches logs from Salesforce & creates a custom exporter, which can be scraped by prometheus.

### Getting Started

To Build the docker:
```shell
docker build -t salesforce-prometheus-exporter .
```

Create a file with following environment variables.  For e.g. `/tmp/env.list` 
```shell
SF_URL=<salesforce url>
SF_VERSION=<salesforce version>
CONSUMER_ID=<salesforce consumer/client ID>
CONSUMER_SECRET=<salesforce consumer/client secret>
AUTH_USERNAME=<salesforce username>
AUTH_PASSWORD=<salesforce password>
ENVIRONMENT=<dev|qa|production> # default is set to `local`.
```
Then, start server command:

```shell
docker run -p 3000:3000 --env-file /tmp/env.list salesforce-prometheus-exporter:latest
```
Go to http://localhost:3000/metrics to view the metrics.

### Available Routes:
<b>Home:</b> http://localhost:3000/ <br />
<b>Health:</b> http://localhost:3000/health <br />
<b>Metrics:</b> http://localhost:3000/metrics <br />

NOTE: The metrics will start with the prefix `sfdc`
