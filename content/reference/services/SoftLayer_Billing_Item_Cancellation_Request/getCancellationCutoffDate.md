---
title: "getCancellationCutoffDate"
description: "Services can be canceled 2 or 3 days prior to your next bill date. This service returns the time by which a cancellation... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Cancellation_Request"
aliases:
    - "/reference/services/softlayer_billing_item_cancellation_request/getCancellationCutoffDate"
---
# [SoftLayer_Billing_Item_Cancellation_Request](/reference/services/SoftLayer_Billing_Item_Cancellation_Request)::getCancellationCutoffDate

Returns service cancellation cut off date.


## Overview 
Services can be canceled 2 or 3 days prior to your next bill date. This service returns the time by which a cancellation request submission is permitted in the current billing cycle. If the current time falls into the cut off date, this will return next earliest cancellation cut off date. 

Available category codes are: service, server 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|accountId| integer| Your account id|
|categoryCode| string| The category code of this billing items that you wish to cancel|


### Required Headers
* authenticate

### Optional Headers

### Return Values
dateTime

