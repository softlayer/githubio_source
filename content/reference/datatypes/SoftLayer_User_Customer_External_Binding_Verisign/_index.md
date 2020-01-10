---
title: "SoftLayer_User_Customer_External_Binding_Verisign"
description: "The SoftLayer_User_Customer_External_Binding_Verisign data type contains information about a single VeriSign external bi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Verisign"
---

# SoftLayer_User_Customer_External_Binding_Verisign
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_External_Binding_Verisign' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_External_Binding_Verisign' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_User_Customer_External_Binding_Verisign data type contains information about a single VeriSign external binding.  The external binding information is used when a SoftLayer customer logs into the SoftLayer customer portal to authenticate them against a 3rd party, in this case VeriSign. 

The information provided by the VeriSign external binding data type includes: 
* The type of credential
* The current state of the credential
** Enabled
** Disabled
** Locked
* The credential's expiration date
* The last time the credential was updated


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
[credentialExpirationDate]: #credentialexpirationdate
#### [credentialExpirationDate]
The date that a VeriSign credential expires.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[credentialLastUpdateDate]: #credentiallastupdatedate
#### [credentialLastUpdateDate]
The last time a VeriSign credential was updated.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[credentialState]: #credentialstate
#### [credentialState]
The current state of a VeriSign credential. This can be 'Enabled', 'Disabled', or 'Locked'.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[credentialType]: #credentialtype
#### [credentialType]
The type of VeriSign credential. This can be either 'Hardware' or 'Software'.  
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


