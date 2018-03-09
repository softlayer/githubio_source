---
title: "getHistoricalUptimeGraph"
description: "The graph image is returned as a base64 PNG string. Start and end dates should be formatted using the ISO 8601 date stan... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getHistoricalUptimeGraph

This method returns a SoftLayer_Container_Account_Graph_Outputs object for the specified date range. 


## Overview 
The graph image is returned as a base64 PNG string. Start and end dates should be formatted using the ISO 8601 date standard. If there is an error retrieving graph data or generating the graph string a graphError attribute will be returned. The graphError attribute may contain any of the following error messages: SoftLayer_Exception_Public Thrown if an invalid start or end date is provided. SoftLayer_Exception Thrown if there is an error connecting to HBase. SoftLayer_Exception Thrown if there is no data available for the specified date range. SoftLayer_Exception Thrown if there is an error retrieving data or generating the graph. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| timestamp of the starting date|
|endDate| dateTime| timestamp of the ending date|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Account_Graph_Outputs'>SoftLayer_Container_Account_Graph_Outputs </a>

