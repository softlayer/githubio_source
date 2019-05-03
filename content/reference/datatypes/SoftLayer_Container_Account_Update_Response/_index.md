---
title: "SoftLayer_Container_Account_Update_Response"
description: "Contains data related to an account after editing its information."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_Update_Response"
---

# SoftLayer_Container_Account_Update_Response
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_Update_Response' >Datatype</a></li>
    </ul>
</div>

## Description 
Contains data related to an account after editing its information. 


### associatedMethods

*  [SoftLayer_Account::editAccount](/reference/services/SoftLayer_Account/editAccount )





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
                <a href="#acceptedFlag" name=acceptedFlag>acceptedFlag</a>
            </span>
            <div class='views-field-body'>Whether or not the update was accepted and applied. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The updated SoftLayer_Account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ticket" name=ticket>ticket</a>
            </span>
            <div class='views-field-body'>If a manual review is required, this will be populated with the SoftLayer_Ticket for that review. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket </a></p>
            </div>
        </div>
            </div>
    </div>


