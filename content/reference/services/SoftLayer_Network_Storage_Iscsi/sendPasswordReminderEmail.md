---
title: "sendPasswordReminderEmail"
description: "The method will retrieve the password for the StorageLayer or Virtual Server Storage Account and email the password.  Th... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Iscsi"
---
# SoftLayer_Network_Storage_Iscsi::sendPasswordReminderEmail
## Overview 
The method will retrieve the password for the StorageLayer or Virtual Server Storage Account and email the password.  The Storage Account passwords will be emailed to the master user.  For Virtual Server Storage, the password will be sent to the email address used as the username. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|username| string| Username of the Storage/Virtual Server Storage account to send the password reminder for|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean

