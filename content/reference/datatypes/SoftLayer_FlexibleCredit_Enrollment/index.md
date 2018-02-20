---
title: "SoftLayer_FlexibleCredit_Enrollment"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "FlexibleCredit"
classes:
    - "SoftLayer_FlexibleCredit_Enrollment"
---

# SoftLayer_FlexibleCredit_Enrollment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_FlexibleCredit_Enrollment' >Datatype</a></li>
    </ul>
</div>

## Description 

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
            <div class='views-field-body'>Account ID associated with this enrollment </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#affiliateId" name=affiliateId>affiliateId</a></span>
            <div class='views-field-body'>ID of the corresponding Flexible Credit Program Affiliate </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#agreementCompleteFlag" name=agreementCompleteFlag>agreementCompleteFlag</a></span>
            <div class='views-field-body'>Indicates signing of Flexible Credit agreement (independent from MSA) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#companyDescription" name=companyDescription>companyDescription</a></span>
            <div class='views-field-body'>Brief description of the company </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#companyTypeId" name=companyTypeId>companyTypeId</a></span>
            <div class='views-field-body'>ID of the Flexible Credit Program Company classification for this enrollment </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#enrollmentDate" name=enrollmentDate>enrollmentDate</a></span>
            <div class='views-field-body'>Date when participation in the Flexible Credit program began </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#graduationDate" name=graduationDate>graduationDate</a></span>
            <div class='views-field-body'>Date Flexible Credit Program benefits end. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#monthlyCreditAmount" name=monthlyCreditAmount>monthlyCreditAmount</a></span>
            <div class='views-field-body'>Amount of monthly credit (USD) given to the account </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#representativeEmployeeId" name=representativeEmployeeId>representativeEmployeeId</a></span>
            <div class='views-field-body'>ID of the employee representing this account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#account" name=account>account</a></span>
            <div class='views-field-body'>Account the enrollment belongs to </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#affiliate" name=affiliate>affiliate</a></span>
            <div class='views-field-body'>Affiliate associated with the account enrollment </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_FlexibleCredit_Affiliate'>SoftLayer_FlexibleCredit_Affiliate </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#companyType" name=companyType>companyType</a></span>
            <div class='views-field-body'>Category which best describes the company </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_FlexibleCredit_Company_Type'>SoftLayer_FlexibleCredit_Company_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#flexibleCreditProgram" name=flexibleCreditProgram>flexibleCreditProgram</a></span>
            <div class='views-field-body'>Discount program the enrollment belongs to </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_FlexibleCredit_Program'>SoftLayer_FlexibleCredit_Program </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isActiveFlag" name=isActiveFlag>isActiveFlag</a></span>
            <div class='views-field-body'>Flag indicating whether an enrollment is active (true) or inactive (false) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#representative" name=representative>representative</a></span>
            <div class='views-field-body'>Employee overseeing the enrollment </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a></p></div>
        </div>
            </div>
</div>


