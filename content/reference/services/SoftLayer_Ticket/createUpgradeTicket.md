---
title: "createUpgradeTicket"
description: "Create a ticket for the SoftLayer sales team to perform a hardware or service upgrade. Our sales team will work with you... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket"
---
# [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket)::createUpgradeTicket

Create an upgrade request ticket for the SoftLayer sales team.


## Overview 
Create a ticket for the SoftLayer sales team to perform a hardware or service upgrade. Our sales team will work with you on upgrade feasibility and pricing and then send the upgrade ticket to the proper department to perform the actual upgrade. Service affecting upgrades, such as server hardware or CloudLayer Computing Instance upgrades that require the server powered down must have a two hour maintenance specified for our datacenter engineers to perform your upgrade. Account level upgrades, such as adding PPTP VPN users, CDNLayer accounts, and monitoring services are processed much faster and do not require a maintenance window. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|attachmentId| integer| An optional hardware identifier if your upgrade request is related to a specific resource(server, vsi, firewall, etc..) on your account.|
|genericUpgrade| string| A brief description of what you wish to upgrade or add to your account. Descriptions like "CPU", "RAM", "RAID cards", "PPTP VPN users", and "StorageLayer".|
|upgradeMaintenanceWindow| string| If your upgrade is service affecting then please provide an appropriate two hour maintenance window in which SoftLayer's staff can upgrade your server.|
|details| string| A detailed description of the the server or account upgrade you wish to perform.|
|attachmentType| string| <ul type="xsd:string"> <li title="HARDWARE">HARDWARE</li> <li title="VIRTUAL_GUEST">VIRTUAL_GUEST</li> <li title="FIREWALL_APPLIANCE">FIREWALL_APPLIANCE</li> <li title="NONE">NONE</li> </ul>|
|title| string| A custom ticket title|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_TicketObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a>

