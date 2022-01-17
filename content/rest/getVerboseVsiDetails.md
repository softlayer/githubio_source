---
title: "Get verbose details about a Virtual Guest"
description: "Retrieve the packages, categories and items associated with a Virtual Guest."

date: "2016-12-29"
classes: ["SoftLayer_Virtual_Guest"]
tags:
  - "objectmask"
  - "getobject"
---

Operation: `GET`

Method: [`SoftLayer_Virtual_Guest::getObject()`](http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject)

URL: SoftLayer_Virtual_Guest/getObject

Example CURL:

```
https://$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY@api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/$virtualGuestId/getObject.json?objectMask=mask[billingItem[item,category,children[item,category]]]

```
