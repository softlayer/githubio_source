---
title: "SoftLayer_Security_Certificate_Request"
description: "The SoftLayer_Security_Certificate_Request data type is used to view details about your SSL certificate order. This cont... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate_Request"
---

# SoftLayer_Security_Certificate_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Security_Certificate_Request' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Security_Certificate_Request' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Security_Certificate_Request data type is used to view details about your SSL certificate order. This contains data that is required by a Certificate Authority to place an SSL certificate order. 





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
This is a reference to your SoftLayer account.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[approverEmailAddress]: #approveremailaddress
#### [approverEmailAddress]
The email address of a person who will approve your SSL certificate order. This is usually an email address of your domain administrator.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[certificateSigningRequest]: #certificatesigningrequest
#### [certificateSigningRequest]
A Certificate Signing Request (CSR) string  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[commonName]: #commonname
#### [commonName]
A domain name of a SSL certificate request  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a SSL certificate request was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[effectiveDate]: #effectivedate
#### [effectiveDate]
The date of your SSL certificate went into effect  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[expirationDate]: #expirationdate
#### [expirationDate]
The expiration date of your SSL certificate  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The internal identifier of an SSL certificate request  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a SSL certificate request was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
A status id reflecting the state of a SSL certificate request  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[technicalContactEmailAddress]: #technicalcontactemailaddress
#### [technicalContactEmailAddress]
The technical contact email address.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account to which a SSL certificate request belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[order]: #order
#### [order]
The order contains the information related to a SSL certificate request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a>**


</div>
<div class="prop-row">

-----
[orderItem]: #orderitem
#### [orderItem]
The associated order item for this SSL certificate request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item </a>**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The status of a SSL certificate request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Certificate_Request_Status'>SoftLayer_Security_Certificate_Request_Status </a>**


</div>

## Count
</div>


