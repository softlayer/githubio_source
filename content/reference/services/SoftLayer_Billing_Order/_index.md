---
title: "SoftLayer_Billing_Order"
description: "The SoftLayer_Billing_Order service controls the orders that are created whenever a SoftLayer customer's places a purchase. Orders exist in several states. The ones of concern are: 
*'''QUOTE_PENDING''': Orders which have not been paid yet. Orders pending approval from a Softlayer customer.


Once an order is paid it moves from QUOTE_PENDING to PENDING_APPROVAL state. 

Orders are created with contact information duplicated from the [SoftLayer_Account](/reference/datatypes/SoftLayer_Account) or by manual entry. We do this in order to maintain a history of an account's contact information as orders are generated. 

Query the [SoftLayer_Account](/reference/datatypes/SoftLayer_Account) service to get a list of orders for your account. "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order"
type: "reference"
layout: "service"
mainService : "SoftLayer_Billing_Order"
---
