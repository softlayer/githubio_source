---
title: "SoftLayer_Container_Account_Discount_Program"
description: "SoftLayer_Container_Account_Discount_Program models a single outbound object for a graph of given data sets."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_Discount_Program"
---

# SoftLayer_Container_Account_Discount_Program
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_Discount_Program' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Account_Discount_Program models a single outbound object for a graph of given data sets.


### associatedMethods

*  [SoftLayer_Account::getBandwidthImage](/reference/services/SoftLayer_Account/getBandwidthImage )





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
[appliedCredit]: #appliedcredit
#### [appliedCredit]
The credit allowance that has already been applied during the current billing cycle. If the lifetime limit has been or soon will be reached, this amount may included credit applied in previous billing cycles.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[isParticipant]: #isparticipant
#### [isParticipant]
Flag to signify whether the account is a participant in the discount program.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[lifetimeAppliedCredit]: #lifetimeappliedcredit
#### [lifetimeAppliedCredit]
Credit allowance applied over the course of the entire program enrollment. For enrollments without a lifetime restriction, this property will not be populated as credit will be tracked on a purely monthly basis.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[lifetimeCredit]: #lifetimecredit
#### [lifetimeCredit]
Credit allowance available over the course of the entire program enrollment. If null, enrollment credit is applied on a strictly monthly basis and there is no lifetime maximum. Enrollments with non-null lifetime credit will receive the lesser of the remaining monthly credit or the remaining lifetime credit.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[lifetimeRemainingCredit]: #lifetimeremainingcredit
#### [lifetimeRemainingCredit]
Remaining credit allowance available over the remaining duration of the program enrollment. If null, enrollment credit is applied on a strictly monthly basis and there is no lifetime maximum. Enrollments with non-null remaining lifetime credit will receive the lesser of the remaining monthly credit or the remaining lifetime credit.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[maximumActiveOrders]: #maximumactiveorders
#### [maximumActiveOrders]
Maximum number of orders the enrolled account is allowed to have open at one time. If null, then the Flexible Credit Program does not impose an order limit.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[monthlyCredit]: #monthlycredit
#### [monthlyCredit]
The monthly credit allowance that is available at the beginning of the billing cycle.  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[postTaxRemainingCredit]: #posttaxremainingcredit
#### [postTaxRemainingCredit]
DEPRECATED: Taxes are calculated in real time and discount amounts are shown pre-tax in all cases. Tax values in the SoftLayer_Container_Account_Discount_Program container are now populated with the related pre-tax values.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[programEndDate]: #programenddate
#### [programEndDate]
The date at which the program expires in MM/DD/YYYY format.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[programName]: #programname
#### [programName]
Name of the Flexible Credit Program the account is enrolled in.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[remainingCredit]: #remainingcredit
#### [remainingCredit]
The credit allowance that is available during the current billing cycle. If the lifetime limit has been or soon will be reached, this amount may be reduced by credit applied in previous billing cycles.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[remainingCreditTax]: #remainingcredittax
#### [remainingCreditTax]
DEPRECATED: Taxes are calculated in real time and discount amounts are shown pre-tax in all cases. Tax values in the SoftLayer_Container_Account_Discount_Program container are now populated with the related pre-tax values.   
<span class="type-label">Type: </span>**decimal**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


