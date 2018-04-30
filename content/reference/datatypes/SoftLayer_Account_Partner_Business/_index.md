---
title: "SoftLayer_Account_Partner_Business"
description: "The SoftLayer_Account_Partner_Business data type contains specific information concerning an Account's relationship with... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Partner_Business"
---

# SoftLayer_Account_Partner_Business
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Partner_Business' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Partner_Business' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Account_Partner_Business data type contains specific information concerning an Account's relationship with Business Partner Data, in the form of the Account's Country Experience Identifier (CEID), Channel ID, and Segment ID. 





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
                <a href="#channelId" name=channelId>channelId</a>
            </span>
            <div class='views-field-body'>The Channel ID associated with the Account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#countryEnterpriseCode" name=countryEnterpriseCode>countryEnterpriseCode</a>
            </span>
            <div class='views-field-body'>The Country Enterprise Code associated with the Account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#segmentId" name=segmentId>segmentId</a>
            </span>
            <div class='views-field-body'>The Segment ID associated with the Account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The SoftLayer customer account associated with this business partner data. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


