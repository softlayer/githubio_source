---
title: "SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded"
description: "Proof of concept request using the global funding model. Note that proof of concept account request are available only t... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded"
---

# SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded' >Datatype</a></li>
    </ul>
</div>

## Description 


Proof of concept request using the global funding model. Note that proof of concept account request are available only to internal IBM employees. 


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
[amount]: #amount
#### [amount]
Dollar amount of funding requested for the proof of concept period  
<span class="type-label">Type: </span>**float**  



</div>
<div class="prop-row">

-----
[customer]: #customer
#### [customer]
Customer intended to take over ownership and and billing of the account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Customer'>SoftLayer_Container_Account_ProofOfConcept_Contact_Customer </a>**  



</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
Explanation of the purpose of the proof of concept request  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[endDate]: #enddate
#### [endDate]
End date for the proof of concept period  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[opportunity]: #opportunity
#### [opportunity]
Internal opportunity system details  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Request_Opportunity'>SoftLayer_Container_Account_ProofOfConcept_Request_Opportunity </a>**  



</div>
<div class="prop-row">

-----
[projectName]: #projectname
#### [projectName]
Name of the project or company and will become the account companyName  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[regionKeyName]: #regionkeyname
#### [regionKeyName]
IBM region responsible for overseeing the proof of concept account  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[requester]: #requester
#### [requester]
IBMer requesting the proof of concept account  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Requester'>SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Requester </a>**  



</div>
<div class="prop-row">

-----
[startDate]: #startdate
#### [startDate]
Start date for the proof of concept period  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[technicalContact]: #technicalcontact
#### [technicalContact]
IBMer assisting with technical aspects of account configuration  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Technical'>SoftLayer_Container_Account_ProofOfConcept_Contact_Ibmer_Technical </a>**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


