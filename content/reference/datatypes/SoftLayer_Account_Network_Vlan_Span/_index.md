---
title: "SoftLayer_Account_Network_Vlan_Span"
description: "The SoftLayer_Account_Network_Vlan_Span data type exposes the setting which controls the automatic spanning of private V... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Network_Vlan_Span"
---

# SoftLayer_Account_Network_Vlan_Span
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Network_Vlan_Span' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Account_Network_Vlan_Span data type exposes the setting which controls the automatic spanning of private VLANs attached to a given customers account. 


### associatedMethods

*  [SoftLayer_Account::setVlanSpan](/reference/services/SoftLayer_Account/setVlanSpan )





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
                <a href="#enabledFlag" name=enabledFlag>enabledFlag</a>
            </span>
            <div class='views-field-body'>Flag indicating whether the customer wishes to have all private network VLANs associated with account automatically joined [0 or 1] </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique internal identifier of the SoftLayer_Account_Network_Vlan_Span object. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lastAppliedDate" name=lastAppliedDate>lastAppliedDate</a>
            </span>
            <div class='views-field-body'>Timestamp of the last time the ACL for this account was applied. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lastVerifiedDate" name=lastVerifiedDate>lastVerifiedDate</a>
            </span>
            <div class='views-field-body'>Timestamp of the last time the subnet hash was verified for this VLAN span record. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>Timestamp of the last edit of the record. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The SoftLayer customer account associated with a VLAN. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


