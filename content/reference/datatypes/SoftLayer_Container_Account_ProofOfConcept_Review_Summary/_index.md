---
title: "SoftLayer_Container_Account_ProofOfConcept_Review_Summary"
description: "Summary presented to reviewers when determining whether or not to accept a proof of concept request. Note that reviewers... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_ProofOfConcept_Review_Summary"
---

# SoftLayer_Container_Account_ProofOfConcept_Review_Summary
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Review_Summary' >Datatype</a></li>
    </ul>
</div>

## Description 
Summary presented to reviewers when determining whether or not to accept a proof of concept request. Note that reviewers are internal IBM employees and reviews are not exposed to external users. 


### associatedMethods

*  [SoftLayer_Account_ProofOfConcept::requestAccount](/reference/services/SoftLayer_Account_ProofOfConcept/requestAccount )





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
[accountName]: #accountname
#### [accountName]
Account's companyName  
<span class="type-label">Type: </span>**string**

-----
[accountOwnerName]: #accountownername
#### [accountOwnerName]
Current account owner  
<span class="type-label">Type: </span>**string**

-----
[amount]: #amount
#### [amount]
Dollar amount requested  
<span class="type-label">Type: </span>**float**

-----
[createDate]: #createdate
#### [createDate]
Date the request was submitted  
<span class="type-label">Type: </span>**dateTime**

-----
[customerEmail]: #customeremail
#### [customerEmail]
Email of the customer receiving the proof of concept account  
<span class="type-label">Type: </span>**string**

-----
[customerName]: #customername
#### [customerName]
Name of the customer receiving the proof of concept account  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
Request record's id  
<span class="type-label">Type: </span>**integer**

-----
[lastUpdate]: #lastupdate
#### [lastUpdate]
Date of the last state change on the request  
<span class="type-label">Type: </span>**dateTime**

-----
[nextApproverEmail]: #nextapproveremail
#### [nextApproverEmail]
Email address of the reviewer, if any, currently reviewing the request  
<span class="type-label">Type: </span>**string**

-----
[requesterEmail]: #requesteremail
#### [requesterEmail]
Email address of the requester  
<span class="type-label">Type: </span>**string**

-----
[requesterName]: #requestername
#### [requesterName]
Requesting IBMer's full name  
<span class="type-label">Type: </span>**string**

-----
[reviewUrl]: #reviewurl
#### [reviewUrl]
URL for the individual review  
<span class="type-label">Type: </span>**string**

-----
[status]: #status
#### [status]
Request's current status (Pending, Denied, or Approved)  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


