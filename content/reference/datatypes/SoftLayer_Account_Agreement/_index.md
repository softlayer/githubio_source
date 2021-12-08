---
title: "SoftLayer_Account_Agreement"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Agreement"
---

# SoftLayer_Account_Agreement
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Agreement' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Agreement' >Datatype</a></li>
    </ul>
</div>

## Description 








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
[agreementTypeId]: #agreementtypeid
#### [agreementTypeId]
The type of agreement identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[autoRenew]: #autorenew
#### [autoRenew]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[cancellationFee]: #cancellationfee
#### [cancellationFee]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date an agreement was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[durationMonths]: #durationmonths
#### [durationMonths]
The duration in months of an agreement.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[endDate]: #enddate
#### [endDate]
The end date of an agreement.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
An agreement's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[startDate]: #startdate
#### [startDate]
The effective start date of an agreement.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
The status identifier for an agreement.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[title]: #title
#### [title]
The title of an agreement.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[agreementType]: #agreementtype
#### [agreementType]
The type of agreement.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement_Type'>SoftLayer_Account_Agreement_Type </a>**  



</div>
<div class="prop-row">

-----
[attachedBillingAgreementFiles]: #attachedbillingagreementfiles
#### [attachedBillingAgreementFiles]
The files attached to an agreement.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_MasterServiceAgreement'>SoftLayer_Account_MasterServiceAgreement[] </a>**  



</div>
<div class="prop-row">

-----
[billingItems]: #billingitems
#### [billingItems]
The billing items associated with an agreement.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**  



</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The status of the agreement.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement_Status'>SoftLayer_Account_Agreement_Status </a>**  



</div>
<div class="prop-row">

-----
[topLevelBillingItems]: #toplevelbillingitems
#### [topLevelBillingItems]
The top level billing item associated with an agreement.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[attachedBillingAgreementFileCount]: #attachedbillingagreementfilecount
#### [attachedBillingAgreementFileCount]
A count of the files attached to an agreement.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[billingItemCount]: #billingitemcount
#### [billingItemCount]
A count of the billing items associated with an agreement.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[topLevelBillingItemCount]: #toplevelbillingitemcount
#### [topLevelBillingItemCount]
A count of the top level billing item associated with an agreement.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


