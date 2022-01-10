---
title: "SoftLayer_User_Customer_External_Binding_Phone"
description: "The SoftLayer_User_Customer_External_Binding_Phone data type contains information about an external binding that uses a... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Phone"
---

# SoftLayer_User_Customer_External_Binding_Phone
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_External_Binding_Phone' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_External_Binding_Phone' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_User_Customer_External_Binding_Phone data type contains information about an external binding that uses a phone call, SMS or mobile app for 2 form factor authentication. The external binding information is used when a SoftLayer customer logs into the SoftLayer customer portal or VPN to authenticate them against a trusted 3rd party, in this case using a mobile phone, mobile phone application or land-line phone. 

SoftLayer users with an active external binding will be prohibited from using the API for security reasons. 





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
[active]: #active
#### [active]
The flag that determines whether the external binding is active will be used for authentication or not.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date that the external authentication binding was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[externalId]: #externalid
#### [externalId]
The identifier used to identify this binding to an external authentication source.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
An external authentication binding's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[password]: #password
#### [password]
The password used to authenticate the external id at an external authentication source.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
The [SoftLayer_User_External_Binding_Type]({{<ref "reference/datatypes/SoftLayer_User_External_Binding_Type">}}) identifier of an external authentication binding.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[userId]: #userid
#### [userId]
An external authentication binding's associated [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}) id.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[vendorId]: #vendorid
#### [vendorId]
The [SoftLayer_User_External_Binding_Vendor]({{<ref "reference/datatypes/SoftLayer_User_External_Binding_Vendor">}}) identifier of an external authentication binding.   
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
Attributes of an external authentication binding.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_External_Binding_Attribute'>SoftLayer_User_External_Binding_Attribute[] </a>**  



</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The current billing item for an external binding.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**  



</div>
<div class="prop-row">

-----
[bindingStatus]: #bindingstatus
#### [bindingStatus]
The current external binding status. It can be "ACTIVE" or "BLOCKED".  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[note]: #note
#### [note]
An optional note for identifying the external binding.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[pinLength]: #pinlength
#### [pinLength]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of external authentication binding.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_External_Binding_Type'>SoftLayer_User_External_Binding_Type </a>**  



</div>
<div class="prop-row">

-----
[user]: #user
#### [user]
The SoftLayer user that the external authentication binding belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[vendor]: #vendor
#### [vendor]
The vendor of an external authentication binding.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_External_Binding_Vendor'>SoftLayer_User_External_Binding_Vendor </a>**  



</div>

## Count
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of attributes of an external authentication binding.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


