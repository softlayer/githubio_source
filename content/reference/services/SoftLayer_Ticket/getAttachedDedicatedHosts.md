---
title: "getAttachedDedicatedHosts"
description: "Retrieve the Dedicated Hosts associated with a ticket. This is used in cases where a ticket is directly associated with... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
aliases:
    - "/reference/services/softlayer_ticket/getAttachedDedicatedHosts"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::getAttachedDedicatedHosts

Retrieve the Dedicated Hosts associated with a ticket. This is used in cases where a ticket is directly associated with one or more Dedicated Hosts.


## Overview 
Retrieve the Dedicated Hosts associated with a ticket. This is used in cases where a ticket is directly associated with one or more Dedicated Hosts.

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* SoftLayer_TicketInitParameters
* authenticate

### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_TicketObjectFilter
* resultLimit
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost[] </a>

