---
title: "Bandwidth"
description: "How to keep track of bandwidth for servers and virtual guests."
date: "2020-10-15"
tags:
    - "article"
    - "sldn"
    - "bandwidth"
---


# Bandwidth

Any device directly connected to the network will have its bandwidth tracked. This includes [Hardware_Server](/reference/datatypes/SoftLayer_Hardware_Server/), [Virtual_Guest](/reference/datatypes/SoftLayer_Virtual_Guest/), [Hardware_Firewall](/reference/datatypes/SoftLayer_Hardware_Firewall/), and [Network_Vlan_Firewall](/reference/datatypes/SoftLayer_Network_Vlan_Firewall/) objects. We collect the data periodically from the switch port (or virtual port in the case of Virutal_Guests) and store it in our [Metric_Tracking](/reference/datatypes/SoftLayer_Metric_Tracking_Object/) datastore. To interact with this raw data it is required to use the [Metric_Tracking_Object](/reference/services/SoftLayer_Metric_Tracking_Object/) service directly, as it wont be possible to pull in this information using a normal objectMask. Luckily there are a few summary fields that are available through objectMasks that can be used.


# Bandwidth Summaries

Since Outbound bandwidth is metered, it can be very important to know how much bandwidth you have consumed in the current billing cycle, and there are a few different ways to get this information.


## Key Properties
For these examples we will be talking about Hardware_Server objects, but the sae principles apply to any of the other objects that track bandwidth. Some of these properties might also have Private and Public versions which I wont include for the sake of brevity, but you can see the full property list on the objects datatype page if you filter by `bandwidth`

- [averageDailyBandwidthUsage](/reference/datatypes/SoftLayer_Hardware_Server/#averagedailybandwidthusage) Will give you an idea of how much bandwidth your server has used this billing cycle per day, letting you estimate future usage.
- [bandwidthAllocation](/reference/datatypes/SoftLayer_Hardware_Server/#bandwidthallocation) How much bandwidth this server has pre-paid for, in GB.
- [bandwidthAllotmentDetail](/reference/datatypes/SoftLayer_Hardware_Server/#bandwidthallotmentdetail) The raw details behind a server's bandwidth allotment, useful for servers in a bandwidth pool.
- [billingCycleBandwidthUsage](/reference/datatypes/SoftLayer_Hardware_Server/#billingcyclebandwidthusage) A quick summary of each interface and how much traffic each has processed this billing cycle. Will include the Metric_Tracking_Object as well.
- [currentBandwidthSummary](/reference/datatypes/SoftLayer_Hardware_Server/#currentbandwidthsummary) Will include the following information:

```json
{
    "allocationAmount": 500,
    "amountOut": "0",
    "averageDailyUsage": 0,
    "currentlyOverAllocationFlag": 0,
    "id": 35258395,  # Tracking Object ID
    "outboundBandwidthAmount": "0",
    "projectedBandwidthUsage": 0,
    "projectedOverAllocationFlag": 0
}
```
- [currentBillableBandwidthUsage](/reference/datatypes/SoftLayer_Hardware_Server/#currentbillablebandwidthusage) If this number is higher than your allocation, you will get an overage bill.
- [inboundBandwidthUsage](/reference/datatypes/SoftLayer_Hardware_Server/#inboundbandwidthusage) and [outboundBandwidthUsage](/reference/datatypes/SoftLayer_Hardware_Server/#outboundbandwidthusage) Just the raw numbers for how much traffic has gone in or out of the server.
- [projectedPublicBandwidthUsage](/reference/datatypes/SoftLayer_Hardware_Server/#projectedpublicbandwidthusage) Basically this is just the averageBandwidthUsage * (days left in the month).

## Example API call

In this example we force the objectMask to be a SoftLayer_Hardware_Server type because the default type of SoftLayer_Hardware doesn't have the `currentBandwidthSummary` property. This isn't required for `getVirtualGuests`.

```bash
$ slcli -vvv --format=table call-api SoftLayer_Account getHardware --mask="mask(SoftLayer_Hardware_Server)[id,hostname,currentBandwidthSummary[allocationAmount,amountOut,averageDailyUsage]]"
:..................................:................:.........:
:     currentBandwidthSummary      :    hostname    :    id   :
:..................................:................:.........:
: :...................:.........:  : host16.vmware  : 1134349 :
: :              name : value   :  :                :         :
: :...................:.........:  :                :         :
: :  allocationAmount : 500     :  :                :         :
: :         amountOut : 14.0303 :  :                :         :
: : averageDailyUsage : 1.2     :  :                :         :
: :...................:.........:  :                :         :
:..................................:................:.........:

$ slcli -vvv --format=table call-api SoftLayer_Account getVirtualGuests --mask="mask[id,hostname,currentBandwidthSummary[allocationAmount,amountOut,averageDailyUsage]]"
:.................................:.....................:...........:
:     currentBandwidthSummary     :       hostname      :     id    :
:.................................:.....................:...........:
: :...................:.........: :         adns        : 100250634 :
: :              name : value   : :                     :           :
: :...................:.........: :                     :           :
: :  allocationAmount : 250     : :                     :           :
: :         amountOut : 4.29497 : :                     :           :
: : averageDailyUsage : 0.37    : :                     :           :
: :...................:.........: :                     :           :
:.................................:.....................:...........:
```

Or in REST
```
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getHardware.json?objectMask=mask(SoftLayer_Hardware_Server)[id,hostname,currentBandwidthSummary[allocationAmount,amountOut,averageDailyUsage]]'
```


# Raw Data


The [SoftLayer_Metric_Tracking_Object](/reference/services/SoftLayer_Metric_Tracking_Object/) service is responsible for interacting with our metrics datastorage, which keeps track of bandwidth data, along with a few other metrics for Virtual servers. You will need your server's metricTrackingObjectId to start off with, [SoftLayer_Hardware_Server::getMetricTrackingObjectId](/reference/services/SoftLayer_Hardware_Server/getMetricTrackingObjectId/) is a quick way to get this id. Any object that keeps track of metrics will have a similar method or property and is not limited to just Hardware_Server.

## [SoftLayer_Metric_Tracking_Object::getMetricDataTypes](/reference/services/SoftLayer_Metric_Tracking_Object/getMetricDataTypes/)

`getMetricDataTypes` will let you know the different metrics a specific Id will provide.

### Example

```bash
$ slcli --format=json -vvv call-api SoftLayer_Metric_Tracking_Object getMetricDataTypes --id=35258287
Calling: SoftLayer_Metric_Tracking_Object::getMetricDataTypes(id=35258287, mask='', filter='{}', args=(), limit=None, offset=None))

[
    {
        "keyName": "PUBLICIN",
        "name": "publicIn",
        "summaryType": "average"
    },
    {
        "keyName": "PUBLICOUT",
        "name": "publicOut",
        "summaryType": "sum"
    },
]
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/35258287/getMetricDataTypes.json'
```

The `keyName` and `summaryType` fields are important here and will be used in some of the other methods. This will give you a good idea of what types of data you can ask about.

## [SoftLayer_Metric_Tracking_Object::getBandwidthData](/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthData/)

`getBandwidthData` exists to help quickly interact with this data if you are only concerned with bandwidth information. It takes 4 parameters, `startDateTime`, `endDateTime` to select a period of time you care about, `type` can be `'public'` or `'private'` and `rollupSeconds` to define a length of time in seconds as a single unit (300, 600, 1800, 3600, 43200 or 86400 seconds).

### Example

```bash
$ slcli --format=json -vvv call-api SoftLayer_Metric_Tracking_Object getBandwidthData --id=35258287 2020-09-01 2020-09-30 public  86400
Calling: SoftLayer_Metric_Tracking_Object::getBandwidthData(id=35258287, mask='', filter='{}', args=('2020-09-01', '2020-09-30', 'public', '86400'), limit=None, offset=None))
[
    {
        "counter": 34871813,
        "dateTime": "2020-08-31T23:00:00-06:00",
        "type": "publicIn_net_octet"
    },
    {
        "counter": 34858964,
        "dateTime": "2020-09-01T23:00:00-06:00",
        "type": "publicIn_net_octet"
    },
(ETC ETC)
]

curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": ["2020-09-01", "2020-09-30", "public", "86400"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/35258287/getBandwidthData.json'
```

You may notice I asked for `2020-09-01` as my start time, but I got back `2020-09-31T23:00:00-06:00`, this is due to fun with timezones. Currently I'm in the -05:00 timezone, so the backend converts my request to `2020-09-01T00:00:00-05:00` (`1598936400`), which is `2020-08-31T23:00:00-06:00`. Luckily, this API also accepts epoch time, so you can just use that value to be a bit more precise, just understand that when your bandwidth usage is calculated, it will be in the -06:00 timezone centric.


```bash
$  date +%s --date='2020-09-01T00:00:00-06:00'
1598940000
$  date +%s --date='2020-09-30T23:59:59-06:00'
1601531999
$ slcli --format=json -vvv call-api SoftLayer_Metric_Tracking_Object getBandwidthData --id=35258287 1598940000 1601531999 public  86400
Calling: SoftLayer_Metric_Tracking_Object::getBandwidthData(id=35258287, mask='', filter='{}', args=('1598940000', '1601531999', 'public', '86400'), limit=None, offset=None))
[
    {
        "counter": 34803077,
        "dateTime": "2020-09-01T00:00:00-06:00",
        "type": "publicIn_net_octet"
    },
    {
        "counter": 4037816161,
        "dateTime": "2020-09-30T00:00:00-06:00",
        "type": "publicOut_net_octet"
    }
]
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": ["1598940000", "1601531999", "public", "86400"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/35258287/getBandwidthData.json'
```


## [SoftLayer_Metric_Tracking_Object::getBandwidthGraph](/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthGraph/)

Takes in most of the same parameters as getBandwidthData, but will return a json object with 1 property, which contains a base64 encoded image. You will need to extract the data and base64 decode it into an image.

### Example

```bash
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": ["1598940000", "1601532000", "public", "14", "1200", "400"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/35258287/getBandwidthGraph.json'
{
    "graphImage":  "iVBORw0KGgoAAAANSUhEUgAABLAAAAGQCAIAAAAx1w4JAA.......LOTS MORE TEXT",
    "graphTitle": "host16.vmware.test.com",
    "maxEndDate": null,
    "minStartDate": null
}
```


## [SoftLayer_Metric_Tracking_Object::getSummaryData](/reference/services/SoftLayer_Metric_Tracking_Object/getSummaryData/)

getSummaryData is a more generic way to get bandwidth information. The third parameter can be a bit tricky to specify. The format is an array, containing an object for each bit of information you want returned. You need to specify the `keyName` and `summaryType` for each, although you can only get one metric per keyName in a single call.

### Example

```bash
$ slcli -v  --format=json call-api SoftLayer_Metric_Tracking_Object getSummaryData --id=35258287 1598940000 1601532000 '[{"keyName":"PUBLICIN","summaryType":"sum"}]' 86400
Calling: SoftLayer_Metric_Tracking_Object::getSummaryData(id=35258287, mask='', filter='{}', args=('1598940000', '1601532000', [{'keyName': 'PUBLICIN', 'summaryType': 'sum'}], '86400'), limit=None, offset=None))
[
    {
        "counter": 34803077,
        "dateTime": "2020-09-01T00:00:00-06:00",
        "type": "publicIn_net_octet"
    },
]
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": ["1598940000", "1601532000", [{"keyName": "PUBLICIN", "summaryType": "sum"}], "86400"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Metric_Tracking_Object/35258287/getSummaryData.json'

```
