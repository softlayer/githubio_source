---
title: "SoftLayer_User_Customer_AdditionalEmail"
description: "The SoftLayer_User_Customer_AdditionalEmail data type contains the additional email for use in ticket update notificatio... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_AdditionalEmail"
---

# SoftLayer_User_Customer_AdditionalEmail
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer_AdditionalEmail' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_User_Customer_AdditionalEmail data type contains the additional email for use in ticket update notifications. 


### associatedMethods

*  [SoftLayer_User_Customer_AdditionalEmail::getObject](/reference/services/SoftLayer_User_Customer_AdditionalEmail/getObject )
*  [SoftLayer_Ticket::attachedAdditionalEmails](/reference/services/SoftLayer_Ticket/attachedAdditionalEmails )
*  [SoftLayer_User_Customer::additionalEmails](/reference/services/SoftLayer_User_Customer/additionalEmails )





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
                <a href="#email" name=email>email</a>
            </span>
            <div class='views-field-body'>Email assigned to user for use in ticket update notifications. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userId" name=userId>userId</a>
            </span>
            <div class='views-field-body'>An internal identifier for the portal user who this additional email belongs to. </div>
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
                <a href="#user" name=user>user</a>
            </span>
            <div class='views-field-body'>The portal user that owns this additional email address. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


