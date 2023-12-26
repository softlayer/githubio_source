---
title: "getCustomerInvoicingMetrics"
description: "Get the static & dynamic bandwidth and mapping hits of predetermined statistics for direct display (no graph) for a customer's account over a given period of time. Frequency can be 'day', 'aggregate'. If the value 'day' is specified for Frequency, return data will be ordered based on startDate to endDate, and if the value 'aggregate' is specified for Frequency, aggregated data from startDate to endDate will be returned. There is a delay within 3 days(including today) for fetching the metrics data. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Metrics"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_CdnMarketplace_Metrics"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, int, int, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_CdnMarketplace_Metrics/getCustomerInvoicingMetrics'
```
