---
title: "getAccountBackupHistory"
description: "This method returns an array of SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails objects for the given start... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getAccountBackupHistory"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getAccountBackupHistory


This method provides a history of account backups.


## Overview 
This method returns an array of SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails objects for the given start and end dates. Start and end dates should be be valid ISO 8601 dates. The backupStatus can be one of null, 'success', 'failed', or 'conflict'. The 'success' backupStatus returns jobs with a status of 'COMPLETED', the 'failed' backupStatus returns jobs with a status of 'FAILED', while the 'conflict' backupStatus will return jobs that are not 'COMPLETED' or 'FAILED'. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|startDate| dateTime| Timestamp of the starting date|
|endDate| dateTime| Timestamp of the ending date|
|backupStatus| string| $backupStatus Can be null, 'success', 'failed', or 'conflict'|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails'>SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails[] </a>


### Associated Methods

*  [SoftLayer_Account::getCurrentBackupStatisticsGraph](/reference/services/SoftLayer_Account/getCurrentBackupStatisticsGraph )
*  [SoftLayer_Account::getHistoricalBackupGraph](/reference/services/SoftLayer_Account/getHistoricalBackupGraph )



### Error Handling

* SoftLayer_Exception_Public 

> <<< EOT Thrown if there was an error while 



