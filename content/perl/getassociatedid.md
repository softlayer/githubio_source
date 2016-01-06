---
title: "Associate a Billing ID with the service or item it corresponds to in the SoftLayer catalog"
description: "You can use getAssociatedBillingItem or getAssociatedParent along with an Object Mask."
date: "2016-01-06"
classes: ["SoftLayer_Billing_Item"]
tags:
  - "getAssociatedBillingItem"
  - "billing"
---


```perl
# https://api.softlayer.com/rest/v3/SoftLayer_Billing_Item/1234321/getAssociatedBillingItem
my $objectMask = {
   'id' =>''
};
$billing_client->setObjectMask($objectMask);
$result = $billing_client->getAssociatedParent();
print Dumper($result->result);

```
