---
title: "SoftLayer_Account_External_Setup"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_External_Setup"
---

# SoftLayer_Account_External_Setup
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_External_Setup' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_External_Setup' >Datatype</a></li>
    </ul>
</div>

## Description 








<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[accountId]: #accountid
#### [accountId]
The SoftLayer customer account the request belongs to.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[currencyId]: #currencyid
#### [currencyId]
The currency requested after the billing switch.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique identifier for this setup request.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
The external system that will handle billing.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[statusCode]: #statuscode
#### [statusCode]
The status of the account setup request.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[typeCode]: #typecode
#### [typeCode]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[verifyCardTransactionId]: #verifycardtransactionid
#### [verifyCardTransactionId]
The related credit card transaction record for card verification.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[verifyCardTransaction]: #verifycardtransaction
#### [verifyCardTransaction]
The transaction information related to verifying the customer credit card.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Payment_Card_Transaction'>SoftLayer_Billing_Payment_Card_Transaction </a>**  



</div>

## Count
</div>


