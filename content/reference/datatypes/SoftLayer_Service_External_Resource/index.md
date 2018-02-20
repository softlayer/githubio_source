---
title: "SoftLayer_Service_External_Resource"
description: "The SoftLayer_Service_External_Resource is a placeholder that references a service being provided outside of the standar... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Service"
classes:
    - "SoftLayer_Service_External_Resource"
---

# SoftLayer_Service_External_Resource
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Service_External_Resource' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Service_External_Resource is a placeholder that references a service being provided outside of the standard SoftLayer system. 
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
            <div class='views-field-body'>The customer account that is consuming the related service. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#externalIdentifier" name=externalIdentifier>externalIdentifier</a></span>
            <div class='views-field-body'>The unique identifier in the service provider's system. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>An external resource's unique identifier in the SoftLayer system. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>The customer account that is consuming the service. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
            </div>
</div>


