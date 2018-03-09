---
title: "SoftLayer_Account_Regional_Registry_Detail_Property"
description: "Subnet registration properties are used to define various attributes of the [[SoftLayer_Account_Regional_Registry_Detail... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail_Property"
---

# SoftLayer_Account_Regional_Registry_Detail_Property
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Regional_Registry_Detail_Property' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property' >Datatype</a></li>
    </ul>
</div>

## Description 
Subnet registration properties are used to define various attributes of the [[SoftLayer_Account_Regional_Registry_Detail|detail objects]]. These properties are defined by the [[SoftLayer_Account_Regional_Registry_Detail_Property_Type]] objects, which describe the available value formats. 





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
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Unique ID of the property object  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#propertyTypeId" name=propertyTypeId>propertyTypeId</a>
            </span>
            <div class='views-field-body'>The numeric ID of the related [[SoftLayer_Account_Regional_Registry_Detail_Property_Type|property type object]]  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#registrationDetailId" name=registrationDetailId>registrationDetailId</a>
            </span>
            <div class='views-field-body'>The numeric ID of the related [[SoftLayer_Account_Regional_Registry_Detail|detail object]]  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sequencePosition" name=sequencePosition>sequencePosition</a>
            </span>
            <div class='views-field-body'>When multiple properties exist for a property type, defines the position in the sequence of those properties  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#value" name=value>value</a>
            </span>
            <div class='views-field-body'>The value of the property  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#detail" name=detail>detail</a>
            </span>
            <div class='views-field-body'>The [[SoftLayer_Account_Regional_Registry_Detail]] object this property belongs to </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail'>SoftLayer_Account_Regional_Registry_Detail </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#propertyType" name=propertyType>propertyType</a>
            </span>
            <div class='views-field-body'>The [[SoftLayer_Account_Regional_Registry_Detail_Property_Type]] object this property belongs to </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property_Type'>SoftLayer_Account_Regional_Registry_Detail_Property_Type </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


