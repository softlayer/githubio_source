---
title: "getHistoricalBandwidthGraph"
description: "[DEPRECATED] This method will return a SoftLayer_Container_Account_Graph_Outputs object containing a base64 string PNG i... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getHistoricalBandwidthGraph"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getHistoricalBandwidthGraph

[DEPRECATED] This method returns a line graph of bandwidth statistics.


## Overview 
[DEPRECATED] This method will return a SoftLayer_Container_Account_Graph_Outputs object containing a base64 string PNG image of a line graph of bandwidth statistics given the start and end dates. The start and end dates should be valid ISO 8601 date formatted strings. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| timestamp of the starting date|
|endDate| dateTime| timestamp of the ending date|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Account_Graph_Outputs'>SoftLayer_Container_Account_Graph_Outputs </a>


### Associated Methods

*  [SoftLayer_Account::getBandwidthList](/reference/services/SoftLayer_Account/getBandwidthList )




