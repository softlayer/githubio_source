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
[agreementTypeId]: #agreementtypeid
#### [agreementTypeId]
The type of agreement identifier.  
<span class="type-label">Type: </span>**integer**

-----
[autoRenew]: #autorenew
#### [autoRenew]
  
<span class="type-label">Type: </span>**integer**

-----
[cancellationFee]: #cancellationfee
#### [cancellationFee]
  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The date an agreement was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[durationMonths]: #durationmonths
#### [durationMonths]
The duration in months of an agreement.  
<span class="type-label">Type: </span>**integer**

-----
[endDate]: #enddate
#### [endDate]
The end date of an agreement.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
An agreement's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[startDate]: #startdate
#### [startDate]
The effective start date of an agreement.  
<span class="type-label">Type: </span>**dateTime**

-----
[statusId]: #statusid
#### [statusId]
The status identifier for an agreement.  
<span class="type-label">Type: </span>**integer**

-----
[title]: #title
#### [title]
The title of an agreement.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[agreementType]: #agreementtype
#### [agreementType]
The type of agreement.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement_Type'>SoftLayer_Account_Agreement_Type </a>**

-----
[attachedBillingAgreementFiles]: #attachedbillingagreementfiles
#### [attachedBillingAgreementFiles]
The files attached to an agreement.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_MasterServiceAgreement'>SoftLayer_Account_MasterServiceAgreement[] </a>**

-----
[billingItems]: #billingitems
#### [billingItems]
The billing items associated with an agreement.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**

-----
[status]: #status
#### [status]
The status of the agreement.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Agreement_Status'>SoftLayer_Account_Agreement_Status </a>**

-----
[topLevelBillingItems]: #toplevelbillingitems
#### [topLevelBillingItems]
The top level billing item associated with an agreement.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item[] </a>**


## Count

-----
[attachedBillingAgreementFileCount]: #attachedbillingagreementfilecount
#### [attachedBillingAgreementFileCount]
A count of the files attached to an agreement.   
<span class="type-label">Type: </span>**unsigned long**


-----
[billingItemCount]: #billingitemcount
#### [billingItemCount]
A count of the billing items associated with an agreement.   
<span class="type-label">Type: </span>**unsigned long**


-----
[topLevelBillingItemCount]: #toplevelbillingitemcount
#### [topLevelBillingItemCount]
A count of the top level billing item associated with an agreement.   
<span class="type-label">Type: </span>**unsigned long**

</div>


