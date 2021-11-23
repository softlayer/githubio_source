---
title: "requestCreditCardChange"
description: "Retrieve the record data associated with the submission of a Credit Card Change Request. Softlayer customers are permitted to request a change in Credit Card information. Part of the process calls for an attempt by SoftLayer to submit at $1.00 charge to the financial institution backing the credit card as a means of verifying that the information provided in the change request is valid.  The data associated with this change request returned to the calling function. 

If the onlyChangeNicknameFlag parameter is set to true, the nickname of the credit card will be changed immediately without requiring approval by an agent.  To change the nickname of the active payment method, pass the empty string for paymentRoleName.  To change the nickname for the alternate credit card, pass ALTERNATE_CREDIT_CARD as the paymentRoleName.  vatId must be set, but the value will not be used and the empty string is acceptable. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "requestCreditCardChange"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---
