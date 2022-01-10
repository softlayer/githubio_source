---
title: "SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute"
description: "This container data type contains extended attributes information for a domain of country code TLD."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute"
---

# SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute' >Datatype</a></li>
    </ul>
</div>

## Description 


This container data type contains extended attributes information for a domain of country code TLD. 


### associatedMethods

*  [SoftLayer_Dns_Domain_Registration::getExtendedAttributes](/reference/services/SoftLayer_Dns_Domain_Registration/getExtendedAttributes )





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
[childFlag]: #childflag
#### [childFlag]
Indicates if this is a child of another extended attribute.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
The description of an extended attribute.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of an extended attribute.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[options]: #options
#### [options]
The collection of options for an extended attribute.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute_Option'>SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute_Option[] </a>**  



</div>
<div class="prop-row">

-----
[requiredFlag]: #requiredflag
#### [requiredFlag]
Indicates if extended attribute is required.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[userDefinedFlag]: #userdefinedflag
#### [userDefinedFlag]
User defined indicates that the value is required from outside sources.  
<span class="type-label">Type: </span>**boolean**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


