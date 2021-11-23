---
title: "SoftLayer_Account_Lockdown_Request"
description: "This service allows approved brands the ability to disconnect, reconnect, and disable customer accounts under that brand. Brand customers are able to make requests on their customers through an API call to this service. 

Disconnecting a customer will disable all hardware resources (servers and virtual machines) via a lockdown event. The customer will continue to have control portal access as well as access to their private ports. 

Reconnecting a customer will restore all previously disconnected public access. The original lockdown event will be closed. 

Disabling an account is a PERMANENT action. All billable items under the account will be canceled, access to the control portal, all resources, network access and hardware will be permanently disabled and reclaimed. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Lockdown_Request"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Account_Lockdown_Request"
---
