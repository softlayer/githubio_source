---
title: "getHistoricalTicketGraph"
description: "Given the start and end dates, this method will return a pie chart of ticket statistics in the form of SoftLayer_Contain... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::getHistoricalTicketGraph
## Overview 
Given the start and end dates, this method will return a pie chart of ticket statistics in the form of SoftLayer_Container_Account_Graph_Outputs object with a base64 PNG string. If an error occurs the graphError parameter will be populated. Possible errors include: SoftLayer_Exception_Public Thrown if an invalid start or end date is provided. SoftLayer_Exception Thrown if there is an error connecting to HBase. SoftLayer_Exception Thrown if there is no data available for the specified date range. SoftLayer_Exception Thrown if there is an error retrieving data or generating the graph. 

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
