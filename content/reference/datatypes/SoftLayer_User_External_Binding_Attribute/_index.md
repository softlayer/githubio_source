---
title: "SoftLayer_User_External_Binding_Attribute"
description: "The SoftLayer_User_External_Binding_Attribute data type contains the value for a single attribute associated with an ext... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_External_Binding_Attribute"
---

# SoftLayer_User_External_Binding_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_External_Binding_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_User_External_Binding_Attribute data type contains the value for a single attribute associated with an external binding. External binding attributes contain additional information about an external binding.  An attribute can be generic or specific to a 3rd party vendor.  For example these attributes relate to Verisign: 
*Credential Type
*Credential State
*Credential Expiration Date
*Credential Last Update Date





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
[value]: #value
#### [value]
The value of an external binding attribute.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[externalBinding]: #externalbinding
#### [externalBinding]
The external authentication binding an attribute belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_External_Binding'>SoftLayer_User_External_Binding </a>**


## Count
</div>


