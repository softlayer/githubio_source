---
title: "SoftLayer_Account_Attachment_Employee"
description: "A SoftLayer_Account_Attachment_Employee models an assignment of a single [[SoftLayer_User_Employee|employee]] with a sin... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Attachment_Employee"
---

# SoftLayer_Account_Attachment_Employee
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Attachment_Employee' >Datatype</a></li>
    </ul>
</div>

## Description 
A SoftLayer_Account_Attachment_Employee models an assignment of a single [[SoftLayer_User_Employee|employee]] with a single [[SoftLayer_Account|account]] 
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
            <span class='views-field-title'><a href="#roleId" name=roleId>roleId</a></span>
            <div class='views-field-body'>Role identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>A [[SoftLayer_Account|account]] that is assigned to a [[SoftLayer_User_Employee|employee]]. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#employee" name=employee>employee</a></span>
            <div class='views-field-body'>A [[SoftLayer_User_Employee|employee]] that is assigned to a [[SoftLayer_Account|account]]. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#employeeRole" name=employeeRole>employeeRole</a></span>
            <div class='views-field-body'>A [[SoftLayer_User_Employee|employee]] that is assigned to a [[SoftLayer_Account|account]]. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account_Attachment_Employee_Role'>SoftLayer_Account_Attachment_Employee_Role </a></p></div>
        </div>
            </div>
</div>


