---
title: "SoftLayer_Billing_Item_Association_History"
description: "The SoftLayer_Billing_Item_Association_History type keeps a record of which server billing items an 'orphan' item has been associated with. Orphan billing items are billable items for secondary portable services (such as secondary subnets and StorageLayer accounts) that are not associated with a server and appear at the bottom of a SoftLayer invoice. The [SoftLayer_Billing_Item::setAssociationId](reference/datatypes/$1/#$2) method allows you to associate these kinds of items with servers, making them appear as a child item of the server on your invoice. A SoftLayer_Billing_Item_Association_History record is created every time one of these associations are set. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Association_History"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Billing_Item_Association_History"
---
