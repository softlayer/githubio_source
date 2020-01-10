---
title: "SoftLayer_Network_Message_Delivery"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Message_Delivery"
---

# SoftLayer_Network_Message_Delivery
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Message_Delivery' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Message_Delivery' >Datatype</a></li>
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
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[password]: #password
#### [password]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[username]: #username
#### [username]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[vendorId]: #vendorid
#### [vendorId]
  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The SoftLayer customer account that a network message delivery account belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a network message delivery account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The message delivery type of a network message delivery account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Message_Delivery_Type'>SoftLayer_Network_Message_Delivery_Type </a>**


</div>
<div class="prop-row">

-----
[vendor]: #vendor
#### [vendor]
The vendor for a network message delivery account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Message_Delivery_Vendor'>SoftLayer_Network_Message_Delivery_Vendor </a>**


</div>

## Count
</div>


