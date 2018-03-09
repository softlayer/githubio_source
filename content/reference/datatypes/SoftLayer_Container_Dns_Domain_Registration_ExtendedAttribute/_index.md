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
            <span class='views-field-title'>
                <a href="#childFlag" name=childFlag>childFlag</a>
            </span>
            <div class='views-field-body'>Indicates if this is a child of another extended attribute. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>The description of an extended attribute. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>The name of an extended attribute. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#options" name=options>options</a>
            </span>
            <div class='views-field-body'>The collection of options for an extended attribute. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute_Option'>SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute_Option[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#requiredFlag" name=requiredFlag>requiredFlag</a>
            </span>
            <div class='views-field-body'>Indicates if extended attribute is required. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userDefinedFlag" name=userDefinedFlag>userDefinedFlag</a>
            </span>
            <div class='views-field-body'>User defined indicates that the value is required from outside sources. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
            </div>
    </div>


