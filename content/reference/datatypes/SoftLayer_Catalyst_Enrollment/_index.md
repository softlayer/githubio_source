---
title: "SoftLayer_Catalyst_Enrollment"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Catalyst"
classes:
    - "SoftLayer_Catalyst_Enrollment"
---

# SoftLayer_Catalyst_Enrollment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Catalyst_Enrollment' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Catalyst_Enrollment' >Datatype</a></li>
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
  
<span class="type-label">Type: </span>**integer**

-----
[affiliateId]: #affiliateid
#### [affiliateId]
  
<span class="type-label">Type: </span>**integer**

-----
[agreementCompleteFlag]: #agreementcompleteflag
#### [agreementCompleteFlag]
  
<span class="type-label">Type: </span>**integer**

-----
[companyDescription]: #companydescription
#### [companyDescription]
  
<span class="type-label">Type: </span>**string**

-----
[companyTypeId]: #companytypeid
#### [companyTypeId]
  
<span class="type-label">Type: </span>**integer**

-----
[enrollmentDate]: #enrollmentdate
#### [enrollmentDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[graduationDate]: #graduationdate
#### [graduationDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[monthlyCreditAmount]: #monthlycreditamount
#### [monthlyCreditAmount]
  
<span class="type-label">Type: </span>**decimal**

-----
[representativeEmployeeId]: #representativeemployeeid
#### [representativeEmployeeId]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[affiliate]: #affiliate
#### [affiliate]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Catalyst_Affiliate'>SoftLayer_Catalyst_Affiliate </a>**

-----
[companyType]: #companytype
#### [companyType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Catalyst_Company_Type'>SoftLayer_Catalyst_Company_Type </a>**

-----
[isActiveFlag]: #isactiveflag
#### [isActiveFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[representative]: #representative
#### [representative]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**


## Count
</div>


