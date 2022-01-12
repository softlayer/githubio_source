---
title: "SoftLayer_Billing_Order_Quote"
description: "The SoftLayer_Billing_Order_Quote service controls the quoted orders that are created whenever a SoftLayer customer's places a purchase. Quotes exist in several states. The ones of concern are: 
*'''PENDING''': Quotes which have not been paid yet. Quotes pending approval from a Softlayer customer.


Once an order is placed from a quote it moves from PENDING to EXPIRED state 2 days after its creation and it is removed from the system after 5 days unless otherwise the SoftLayer customer saved the quote. 

Quotes could are created with contact information duplicated from the [SoftLayer_Account](/reference/datatypes/SoftLayer_Account) or by manual entry. We do this in order to maintain a history of an account's contact information as quotes are generated. 

Query the [SoftLayer_Account](/reference/datatypes/SoftLayer_Account) service to get a list of quotes for your account. "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Quote"
type: "reference"
layout: "service"
mainService : "SoftLayer_Billing_Order_Quote"
---
