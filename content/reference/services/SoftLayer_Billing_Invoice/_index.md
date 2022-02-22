---
title: "SoftLayer_Billing_Invoice"
description: "The SoftLayer_Billing_Invoice service controls the invoices that are created whenever a SoftLayer customer's account balance changes. Invoices exist in the following states: 
*'''OPEN''': Invoices which have not been paid yet. Invoices are created in the OPEN state.
*'''CLOSED''': Invoices that SoftLayer has received payment for.
*'''CLOSED_FAILED''': Invoices which were closed but were not paid for. Customers who are terminated for non-payment typically have invoices in this state.


Once an invoice is paid it moves from OPEN to CLOSED state. Invoices are created under varying types, which are defined in the type property of the [SoftLayer_Invoice](/reference/datatypes/SoftLayer_Invoice). Invoices are created under one of the following type categories: 
*'''NEW''': An invoice for new service. A SoftLayer customer's first invoice is of the NEW type.
*'''RECURRING''': Invoices that are generated on a SoftLayer customer's anniversary billing date for monthly services.
*'''ONE-TIME-CHARGE''': Invoices that are generated when one-time charges are applied to an account for fees incurred from products or services procured outside of the standard purchasing processes.
*'''CREDIT''': Invoices that are generated whenever SoftLayer applies a credit against an account's balance.
*'''REFUND''': Account credits that are applied against a customer's account balance along with the receivables on their account. REFUND type invoices are generated whenever a customer receives a service credit on their account balance and has their invoice items changed due to the credit.
*'''MANUAL_PAYMENT_CREDIT''': Invoice credits that are generated whenever a customer makes a manual payment.


Invoices are created with contact information duplicated from the [SoftLayer_Account](/reference/datatypes/SoftLayer_Account). We do this in order to maintain a history of an account's contact information as invoices are generated. Likewise each invoice record keeps track of an account's balance as the invoice is opened and closed. 

Query the [SoftLayer_Account](/reference/datatypes/SoftLayer_Account) service to get a list of invoices for your account. "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Invoice"
type: "reference"
layout: "service"
mainService : "SoftLayer_Billing_Invoice"
---
