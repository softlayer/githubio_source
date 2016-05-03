---
title: "Create a new Bandwidth Pool"
description: "Creating a new Bandwidth pool. This allows you to optimize your bandwidth usage by _pooling_ all of the bandwidth together for servers in a the Pool."
date: "2016-05-02"
classes: ["SoftLayer_Network_Bandwidth_Version1_Allotment"]
tags:
    - "createObject"
    - "bandwidthPool"
---

Operation: `POST`

Method: [`SoftLayer_Network_Bandwidth_Version1_Allotment::createObject()`](http://sldn.softlayer.com/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/createObject)

URL: SoftLayer_Network_Bandwidth_Version1_Allotment/createObject

Example Payload:

```json
{
	"parameters": [{
		"accountId": 111111,
		"bandwidthAllotmentTypeId": 2,
		"locationGroupId": 1,
		"name": "My_new_Bancwidth_Pool",
		"serviceProviderId": 1
	}]
}
```

Example CURL:

```
curl -H "Content-Type: application/json" --data @createpool.json "https://$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY@api.softlayer.com/rest/v3/SoftLayer_Network_Bandwidth_Version1_Allotment/createObject"
```
