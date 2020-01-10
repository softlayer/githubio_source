---
title: "SoftLayer_Container_Dns_Domain_Registration_List"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Dns_Domain_Registration_List"
---

# SoftLayer_Container_Dns_Domain_Registration_List
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Dns_Domain_Registration_List' >Datatype</a></li>
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
[domainName]: #domainname
#### [domainName]
The domain name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[encodingType]: #encodingtype
#### [encodingType]
Three-character language tag for the IDN domain that you're trying to register. This is only required for IDN domains.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[extendedAttributeConfiguration]: #extendedattributeconfiguration
#### [extendedAttributeConfiguration]
Data required by the Registry for some country code top level domains (i.e. example.us). 

In order to determine if a domain requires extended attributes, use [SoftLayer_Dns_Domain_Registration::getExtendedAttributes]({{<ref "reference/services/SoftLayer_Dns_Domain_Registration/getExtendedAttributes">}}) service.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute_Configuration'>SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute_Configuration[] </a>**


</div>
<div class="prop-row">

-----
[registrationPeriod]: #registrationperiod
#### [registrationPeriod]
The length of the registration period in years. Valid values are 1 – 10.   
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


