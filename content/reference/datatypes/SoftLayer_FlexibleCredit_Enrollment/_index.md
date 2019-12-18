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

## Local
-----
[accountId]: #accountid
#### [accountId]
Account ID associated with this enrollment  
<span class="type-label">Type: </span>**integer**

-----
[affiliateId]: #affiliateid
#### [affiliateId]
ID of the corresponding Flexible Credit Program Affiliate  
<span class="type-label">Type: </span>**integer**

-----
[agreementCompleteFlag]: #agreementcompleteflag
#### [agreementCompleteFlag]
Indicates signing of Flexible Credit agreement (independent from MSA)  
<span class="type-label">Type: </span>**integer**

-----
[companyDescription]: #companydescription
#### [companyDescription]
Brief description of the company  
<span class="type-label">Type: </span>**string**

-----
[companyTypeId]: #companytypeid
#### [companyTypeId]
ID of the Flexible Credit Program Company classification for this enrollment  
<span class="type-label">Type: </span>**integer**

-----
[enrollmentDate]: #enrollmentdate
#### [enrollmentDate]
Date when participation in the Flexible Credit program began  
<span class="type-label">Type: </span>**dateTime**

-----
[graduationDate]: #graduationdate
#### [graduationDate]
Date Flexible Credit Program benefits end.  
<span class="type-label">Type: </span>**dateTime**

-----
[monthlyCreditAmount]: #monthlycreditamount
#### [monthlyCreditAmount]
Amount of monthly credit (USD) given to the account  
<span class="type-label">Type: </span>**decimal**

-----
[representativeEmployeeId]: #representativeemployeeid
#### [representativeEmployeeId]
ID of the employee representing this account.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
Account the enrollment belongs to  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[affiliate]: #affiliate
#### [affiliate]
Affiliate associated with the account enrollment  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_FlexibleCredit_Affiliate'>SoftLayer_FlexibleCredit_Affiliate </a>**

-----
[companyType]: #companytype
#### [companyType]
Category which best describes the company  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_FlexibleCredit_Company_Type'>SoftLayer_FlexibleCredit_Company_Type </a>**

-----
[flexibleCreditProgram]: #flexiblecreditprogram
#### [flexibleCreditProgram]
Discount program the enrollment belongs to  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_FlexibleCredit_Program'>SoftLayer_FlexibleCredit_Program </a>**

-----
[isActiveFlag]: #isactiveflag
#### [isActiveFlag]
Flag indicating whether an enrollment is active (true) or inactive (false)  
<span class="type-label">Type: </span>**boolean**

-----
[representative]: #representative
#### [representative]
Employee overseeing the enrollment  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**


## Count
</div>


