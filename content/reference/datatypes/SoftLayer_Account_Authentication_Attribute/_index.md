---
title: "SoftLayer_Account_Authentication_Attribute"
description: "Account authentication has many different settings that can be set. This class allows the customer or employee to set th... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Authentication_Attribute"
---

# SoftLayer_Account_Authentication_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Authentication_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
Account authentication has many different settings that can be set. This class allows the customer or employee to set these settigns. 


### associatedMethods

*  [SoftLayer_Account_Authentication_Saml::getAttributes](/reference/services/SoftLayer_Account_Authentication_Saml/getAttributes )



### seeAlso

* [SoftLayer_Account_Authentication_Saml](/reference/datatypes/SoftLayer_Account_Authentication_Saml )


* [SoftLayer_Account_Authentication_Attribute_Type](/reference/datatypes/SoftLayer_Account_Authentication_Attribute_Type )




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
            <span class='views-field-title'><a href="#accountId" name=accountId>accountId</a></span>
            <div class='views-field-body'>The internal identifier of the SoftLayer customer account that is assigned an account authenction attribute.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A SoftLayer account authenction attribute's internal identifier.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#typeId" name=typeId>typeId</a></span>
            <div class='views-field-body'>The internal identifier of the type of attribute that a SoftLayer account authenction attribute belongs to.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#value" name=value>value</a></span>
            <div class='views-field-body'>A SoftLayer account authenction attribute's value.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The SoftLayer customer account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#authenticationRecord" name=authenticationRecord>authenticationRecord</a></span>
            <div class='views-field-body'>The SoftLayer account authentication that has an attribute. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account_Authentication_Saml'>SoftLayer_Account_Authentication_Saml </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>The type of attribute assigned to a SoftLayer account authentication. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account_Authentication_Attribute_Type'>SoftLayer_Account_Authentication_Attribute_Type </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


