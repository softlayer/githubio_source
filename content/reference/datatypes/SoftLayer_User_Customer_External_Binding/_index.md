---
title: "SoftLayer_User_Customer_External_Binding"
description: "The SoftLayer_User_Customer_External_Binding data type contains general information for a single external binding.  This... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding"
---

# SoftLayer_User_Customer_External_Binding
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer_External_Binding' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_External_Binding' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_User_Customer_External_Binding data type contains general information for a single external binding.  This includes the 3rd party vendor, type of binding, and a unique identifier and password that is used to authenticate against the 3rd party service. 





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
[active]: #active
#### [active]
The flag that determines whether the external binding is active will be used for authentication or not.   
<span class="type-label">Type: </span>**boolean**

-----
[createDate]: #createdate
#### [createDate]
The date that the external authentication binding was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[externalId]: #externalid
#### [externalId]
The identifier used to identify this binding to an external authentication source.   
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
An external authentication binding's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[password]: #password
#### [password]
The password used to authenticate the external id at an external authentication source.   
<span class="type-label">Type: </span>**string**

-----
[typeId]: #typeid
#### [typeId]
The [SoftLayer_User_External_Binding_Type]({{<ref "reference/datatypes/SoftLayer_User_External_Binding_Type">}}) identifier of an external authentication binding.   
<span class="type-label">Type: </span>**integer**

-----
[userId]: #userid
#### [userId]
An external authentication binding's associated [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}) id.   
<span class="type-label">Type: </span>**integer**

-----
[vendorId]: #vendorid
#### [vendorId]
The [SoftLayer_User_External_Binding_Vendor]({{<ref "reference/datatypes/SoftLayer_User_External_Binding_Vendor">}}) identifier of an external authentication binding.   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[attributes]: #attributes
#### [attributes]
Attributes of an external authentication binding.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_External_Binding_Attribute'>SoftLayer_User_External_Binding_Attribute[] </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
Information regarding the billing item for external authentication.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[note]: #note
#### [note]
An optional note for identifying the external binding.  
<span class="type-label">Type: </span>**string**

-----
[type]: #type
#### [type]
The type of external authentication binding.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_External_Binding_Type'>SoftLayer_User_External_Binding_Type </a>**

-----
[user]: #user
#### [user]
The SoftLayer user that the external authentication binding belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[vendor]: #vendor
#### [vendor]
The vendor of an external authentication binding.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_External_Binding_Vendor'>SoftLayer_User_External_Binding_Vendor </a>**


## Count

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of attributes of an external authentication binding.   
<span class="type-label">Type: </span>**unsigned long**

</div>


