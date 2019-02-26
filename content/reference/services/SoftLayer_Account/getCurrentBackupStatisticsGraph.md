---
title: "getCurrentBackupStatisticsGraph"
description: "This method returns a SoftLayer_Container_Account_Graph_Outputs containing a base64 string PNG image. The optional param... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getCurrentBackupStatisticsGraph"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getCurrentBackupStatisticsGraph

This method retrieves a pie chart for today's backup statistics.


## Overview 
This method returns a SoftLayer_Container_Account_Graph_Outputs containing a base64 string PNG image. The optional parameter, detailedGraph, can be passed to get a more detailed graph. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|detailedGraph| boolean| True to retrieve a detailed graph.|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Account_Graph_Outputs'>SoftLayer_Container_Account_Graph_Outputs </a>


### Associated Methods

*  [SoftLayer_Account::getHistoricalBackupGraph](/reference/services/SoftLayer_Account/getHistoricalBackupGraph )
*  [SoftLayer_Account::getAccountBackupHistory](/reference/services/SoftLayer_Account/getAccountBackupHistory )




