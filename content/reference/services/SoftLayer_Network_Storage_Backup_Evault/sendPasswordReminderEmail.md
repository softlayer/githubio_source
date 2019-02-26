---
title: "sendPasswordReminderEmail"
description: "The method will retrieve the password for the StorageLayer or Virtual Server Storage Account and email the password.  Th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Backup_Evault"
aliases:
    - "/reference/services/softlayer_network_storage_backup_evault/sendPasswordReminderEmail"
---
# [SoftLayer_Network_Storage_Backup_Evault](/reference/services/SoftLayer_Network_Storage_Backup_Evault)::sendPasswordReminderEmail

Email the password for the Storage account to the master user.


## Overview 
The method will retrieve the password for the StorageLayer or Virtual Server Storage Account and email the password.  The Storage Account passwords will be emailed to the master user.  For Virtual Server Storage, the password will be sent to the email address used as the username. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| Username of the Storage/Virtual Server Storage account to send the password reminder for|


### Required Headers
* authenticate


### Return Values
* boolean




