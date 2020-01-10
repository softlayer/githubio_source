---
title: "SoftLayer_Container_Account_ProofOfConcept_Review"
description: "Full details presented to reviewers when determining whether or not to accept a proof of concept request. Note that revi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_ProofOfConcept_Review"
---

# SoftLayer_Container_Account_ProofOfConcept_Review
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Review' >Datatype</a></li>
    </ul>
</div>

## Description 
Full details presented to reviewers when determining whether or not to accept a proof of concept request. Note that reviewers are internal IBM employees and reviews are not exposed to external users. 


### associatedMethods

*  [SoftLayer_Account_ProofOfConcept::requestAccount](/reference/services/SoftLayer_Account_ProofOfConcept/requestAccount )





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
[accountType]: #accounttype
#### [accountType]
Type of brand the account will use  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[costRecoveryCodes]: #costrecoverycodes
#### [costRecoveryCodes]
Internal billing codes  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Request_CostRecovery'>SoftLayer_Container_Account_ProofOfConcept_Request_CostRecovery </a>**


</div>
<div class="prop-row">

-----
[customer]: #customer
#### [customer]
Customer intended to take over billing after the proof of concept period  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Customer'>SoftLayer_Container_Account_ProofOfConcept_Contact_Customer </a>**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
Describes the purpose and rationale of the request  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[endDate]: #enddate
#### [endDate]
Expected end date of the proof of concept period  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[fundingAmount]: #fundingamount
#### [fundingAmount]
Dollar amount of funding requested  
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[fundingType]: #fundingtype
#### [fundingType]
Funding option chosen for the request  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
System id of the request  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[iotLeadName]: #iotleadname
#### [iotLeadName]
Name of the integrated offering team lead reviewing the request  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[iotRegionName]: #iotregionname
#### [iotRegionName]
Name of the integrated offering team region  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[managerName]: #managername
#### [managerName]
Name of requesting IBMer's manager  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[opportunity]: #opportunity
#### [opportunity]
Internal opportunity tracking information  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Request_Opportunity'>SoftLayer_Container_Account_ProofOfConcept_Request_Opportunity </a>**


</div>
<div class="prop-row">

-----
[projectName]: #projectname
#### [projectName]
Project name chosen by the requesting IBMer  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[requester]: #requester
#### [requester]
IBMer requesting the account on behalf of a customer  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Requester'>SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Requester </a>**


</div>
<div class="prop-row">

-----
[reviewHistory]: #reviewhistory
#### [reviewHistory]
Summary of request's review activity  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Review_History'>SoftLayer_Container_Account_ProofOfConcept_Review_History </a>**


</div>
<div class="prop-row">

-----
[reviewUrl]: #reviewurl
#### [reviewUrl]
URL for the individual review  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[startDate]: #startdate
#### [startDate]
Expected start date of the proof of concept period  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[technicalContact]: #technicalcontact
#### [technicalContact]
Additional IBMer responsible for configuring the cloud capabilities  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Technical'>SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Technical </a>**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


