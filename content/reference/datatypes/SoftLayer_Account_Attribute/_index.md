---
title: "SoftLayer_Account_Attribute"
description: "Many SoftLayer customer accounts have individual attributes assigned to them that describe features or special features... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Attribute"
---

# SoftLayer_Account_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
Many SoftLayer customer accounts have individual attributes assigned to them that describe features or special features for that account, such as special pricing, account statuses, and ordering instructions. The SoftLayer_Account_Attribute data type contains information relating to a single SoftLayer_Account attribute. 


### associatedMethods

*  [SoftLayer_Account::getAttributes](/reference/services/SoftLayer_Account/getAttributes )



### seeAlso

* [SoftLayer_Account](/reference/datatypes/SoftLayer_Account )


* [SoftLayer_Account_Attribute_Type](/reference/datatypes/SoftLayer_Account_Attribute_Type )




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
                <a href="#accountAttributeTypeId" name=accountAttributeTypeId>accountAttributeTypeId</a>
            </span>
            <div class='views-field-body'>The internal identifier of the type of attribute that a SoftLayer customer account attribute belongs to.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>The internal identifier of the SoftLayer customer account that is assigned an account attribute.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A SoftLayer customer account attribute's internal identifier.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#value" name=value>value</a>
            </span>
            <div class='views-field-body'>A SoftLayer account attribute's value.  </div>
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
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The SoftLayer customer account that has an attribute. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountAttributeType" name=accountAttributeType>accountAttributeType</a>
            </span>
            <div class='views-field-body'>The type of attribute assigned to a SoftLayer customer account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Attribute_Type'>SoftLayer_Account_Attribute_Type </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


