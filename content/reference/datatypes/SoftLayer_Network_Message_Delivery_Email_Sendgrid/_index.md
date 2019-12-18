---
title: "SoftLayer_Network_Message_Delivery_Email_Sendgrid"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Message_Delivery_Email_Sendgrid"
---

# SoftLayer_Network_Message_Delivery_Email_Sendgrid
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Message_Delivery_Email_Sendgrid' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Message_Delivery_Email_Sendgrid' >Datatype</a></li>
    </ul>
</div>

## Description 






<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[accountId]: #accountid
#### [accountId]
  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[password]: #password
#### [password]
  
<span class="type-label">Type: </span>**string**

-----
[typeId]: #typeid
#### [typeId]
  
<span class="type-label">Type: </span>**integer**

-----
[username]: #username
#### [username]
  
<span class="type-label">Type: </span>**string**

-----
[vendorId]: #vendorid
#### [vendorId]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The SoftLayer customer account that a network message delivery account belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a network message delivery account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[emailAddress]: #emailaddress
#### [emailAddress]
The contact e-mail address used by SendGrid.  
<span class="type-label">Type: </span>**string**

-----
[smtpAccess]: #smtpaccess
#### [smtpAccess]
A flag that determines if a SendGrid e-mail delivery account has access to send mail through the SendGrid SMTP server.  
<span class="type-label">Type: </span>**string**

-----
[type]: #type
#### [type]
The message delivery type of a network message delivery account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Message_Delivery_Type'>SoftLayer_Network_Message_Delivery_Type </a>**

-----
[vendor]: #vendor
#### [vendor]
The vendor for a network message delivery account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Message_Delivery_Vendor'>SoftLayer_Network_Message_Delivery_Vendor </a>**


## Count
</div>


