---
title: "Get verbose details about a Bare Metal Server"
description: "Retrieve the packages, categories and items associated with a Bare Metal Server."

date: "2016-12-29"
classes: ["SoftLayer_Hardware"]
tags:
  - "objectmask"
  - "getobject"
---

Operation: `GET`

Method: [`SoftLayer_Hardware::getObject()`](http://sldn.softlayer.com/reference/services/SoftLayer_Hardware/getObject)

URL: SoftLayer_Hardware/getObject

Example CURL:

```
https://$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY@api.softlayer.com/rest/v3/SoftLayer_Hardware/$serverId/getObject.json?objectMask=mask[billingItem[item,category,children[item,category]]]

```