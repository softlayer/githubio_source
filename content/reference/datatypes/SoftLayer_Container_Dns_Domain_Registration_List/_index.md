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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#domainName" name=domainName>domainName</a></span>
            <div class='views-field-body'>The domain name. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#encodingType" name=encodingType>encodingType</a></span>
            <div class='views-field-body'>Three-character language tag for the IDN domain that you're trying to register. This is only required for IDN domains.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#extendedAttributeConfiguration" name=extendedAttributeConfiguration>extendedAttributeConfiguration</a></span>
            <div class='views-field-body'>Data required by the Registry for some country code top level domains (i.e. example.us). 

In order to determine if a domain requires extended attributes, use [[SoftLayer_Dns_Domain_Registration::getExtendedAttributes|domain registration]] service.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute_Configuration'>SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute_Configuration[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#registrationPeriod" name=registrationPeriod>registrationPeriod</a></span>
            <div class='views-field-body'>The length of the registration period in years. Valid values are 1 – 10.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
    </div>


