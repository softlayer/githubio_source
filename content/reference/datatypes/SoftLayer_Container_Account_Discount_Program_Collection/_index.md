---
title: "SoftLayer_Container_Account_Discount_Program_Collection"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_Discount_Program_Collection"
---

# SoftLayer_Container_Account_Discount_Program_Collection
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_Discount_Program_Collection' >Datatype</a></li>
    </ul>
</div>

## Description 



### associatedMethods

*  [SoftLayer_Account::getFlexibleCreditProgramsInfo](/reference/services/SoftLayer_Account/getFlexibleCreditProgramsInfo )





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[accountLevelAppliedCredit]: #accountlevelappliedcredit
#### [accountLevelAppliedCredit]
The amount of credit that has been used by all account level enrollments in the billing cycle.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[accountLevelLifetimeAppliedCredit]: #accountlevellifetimeappliedcredit
#### [accountLevelLifetimeAppliedCredit]
Account level credit allowance applied over the course of entire active program enrollments. For enrollments without a lifetime restriction, this property will not be populated as credit will be tracked on a purely monthly basis.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[accountLevelLifetimeCredit]: #accountlevellifetimecredit
#### [accountLevelLifetimeCredit]
The total account level credit over the course of an entire program enrollment. This value may be null, in which case the enrollment credit is applied on a monthly basis and there is no lifetime maximum.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[accountLevelLifetimeRemainingCredit]: #accountlevellifetimeremainingcredit
#### [accountLevelLifetimeRemainingCredit]
Remaining account level credit allowance available over the remaining duration of the program enrollments. If null, enrollment credit is applied on a strictly monthly basis and there is no lifetime maximum. Enrollments with non-null remaining lifetime credit will receive the lesser of the remaining monthly credit or the remaining lifetime credit.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[accountLevelMonthlyCredit]: #accountlevelmonthlycredit
#### [accountLevelMonthlyCredit]
The total account level monthly credit allowance available at the beginning of a billing cycle.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[accountLevelRemainingCredit]: #accountlevelremainingcredit
#### [accountLevelRemainingCredit]
The total account level credit allowance still available during the current billing cycle.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[enrollments]: #enrollments
#### [enrollments]
The active enrollments for this account.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_FlexibleCredit_Enrollment'>SoftLayer_FlexibleCredit_Enrollment[] </a>**


</div>
<div class="prop-row">

-----
[isAccountLevelParticipantFlag]: #isaccountlevelparticipantflag
#### [isAccountLevelParticipantFlag]
Indicates whether or not the account is participating in any account level Flexible Credit programs.   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[isParticipantFlag]: #isparticipantflag
#### [isParticipantFlag]
Indicates whether or not the account is participating in any Flexible Credit programs.   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[isProductSpecificParticipantFlag]: #isproductspecificparticipantflag
#### [isProductSpecificParticipantFlag]
Indicates whether or not the account is participating in any product specific level Flexible Credit programs.   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[productSpecificAppliedCredit]: #productspecificappliedcredit
#### [productSpecificAppliedCredit]
The amount of credit that has been used by all product specific enrollments in the billing cycle.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[productSpecificLifetimeAppliedCredit]: #productspecificlifetimeappliedcredit
#### [productSpecificLifetimeAppliedCredit]
Product specific credit allowance applied over the course of entire active program enrollments. For enrollments without a lifetime restriction, this property will not be populated as credit will be tracked on a purely monthly basis.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[productSpecificLifetimeCredit]: #productspecificlifetimecredit
#### [productSpecificLifetimeCredit]
The total product specific credit over the course of an entire program enrollment. This value may be null, in which case the enrollment credit is applied on a monthly basis and there is no lifetime maximum.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[productSpecificLifetimeRemainingCredit]: #productspecificlifetimeremainingcredit
#### [productSpecificLifetimeRemainingCredit]
Remaining product specific level credit allowance available over the remaining duration of the program enrollments. If null, enrollment credit is applied on a strictly monthly basis and there is no lifetime maximum. Enrollments with non-null remaining lifetime credit will receive the lesser of the remaining monthly credit or the remaining lifetime credit.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[productSpecificMonthlyCredit]: #productspecificmonthlycredit
#### [productSpecificMonthlyCredit]
The total product specific monthly credit allowance available at the beginning of a billing cycle.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[productSpecificRemainingCredit]: #productspecificremainingcredit
#### [productSpecificRemainingCredit]
The total product specific credit allowance still available during the current billing cycle.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[totalAppliedCredit]: #totalappliedcredit
#### [totalAppliedCredit]
The credit allowance that has already been applied during the current billing cycle from all enrollments. If the lifetime limit has been or soon will be reached, this amount may included credit applied in previous billing cycles.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[totalRemainingCredit]: #totalremainingcredit
#### [totalRemainingCredit]
The credit allowance that is available during the current billing cycle from all enrollments. If the lifetime limit has been or soon will be reached, this amount may be reduced by credit applied in previous billing cycles.   
<span class="type-label">Type: </span>**decimal**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


