---
title: "optOut"
description: "By default, customers will occasionally receive a ticket survey upon closing of a ticket. Use this method to opt out of... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Survey"
aliases:
    - "/reference/services/softlayer_ticket_survey/optOut"
---
# [SoftLayer_Ticket_Survey](/reference/services/SoftLayer_Ticket_Survey)::optOut

*DEPRICATED* Opt out of the customer satisfaction survey for the next 90 days


## Overview 
By default, customers will occasionally receive a ticket survey upon closing of a ticket. Use this method to opt out of it for the next 90 days. Ticket surveys may not be applicable for some customers. Use the [[SoftLayer_Ticket_Survey::getPreference|getPreference]] method to retrieve your survey preference. The "applicable" property of the [[SoftLayer_Container_Ticket_Survey_Preference|survey preference]] indicates if the survey is relevant to your account or not. 

This method is depricated. Use [[SoftLayer_User_Customer::changePreference]] instead. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Ticket_Survey_Preference'>SoftLayer_Container_Ticket_Survey_Preference </a>

