---
title: "SoftLayer_Network_Subnet_Swip_Transaction"
description: "
**DEPRECATED**
The SoftLayer_Network_Subnet_Swip_Transaction data type contains basic information tracked at SoftLayer to allow automation of Swip creation, update, and removal requests.  A specific transaction is attached to an accountId and a subnetId. This also contains a 'Status Name' which tells the customer what the transaction is doing: 


* REQUEST QUEUED:  Request is queued up to be sent to ARIN
* REQUEST SENT:  The email request has been sent to ARIN
* REQUEST CONFIRMED:  ARIN has confirmed that the request is good, and should be available in 24 hours
* OK:  The subnet has been checked with WHOIS and it the SWIP transaction has completed correctly
* REMOVE QUEUED:  A subnet is queued to be removed from ARIN's systems
* REMOVE SENT:  The removal email request has been sent to ARIN
* REMOVE CONFIRMED:  ARIN has confirmed that the removal request is good, and the subnet should be clear in WHOIS in 24 hours
* DELETED:  This specific SWIP Transaction has been removed from ARIN and is no longer in effect
* SOFTLAYER MANUALLY PROCESSING:  Sometimes a request doesn't go through correctly and has to be manually processed by SoftLayer.  This may take some time."
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Swip_Transaction"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Network_Subnet_Swip_Transaction"
---
