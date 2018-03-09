---
title: "optIn"
description: "You will not receive a ticket survey if you are opted out. Use this method to opt back in if you wish to provide feedbac... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Survey"
---
# [SoftLayer_Ticket_Survey](/reference/services/SoftLayer_Ticket_Survey)::optIn

*DEPRICATED* Opt in for the ticket survey


## Overview 
You will not receive a ticket survey if you are opted out. Use this method to opt back in if you wish to provide feedback to our support team. You may use the [[SoftLayer_Ticket_Survey::getPreference|getPreference]] method to check your current opt status. 

This method is depricated. Use [[SoftLayer_User_Customer::changePreference]] instead. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Ticket_Survey_Preference'>SoftLayer_Container_Ticket_Survey_Preference </a>

