---
title: "SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status"
description: "SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status models the state of the registrant. Here are the follow... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status"
---

# SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status models the state of the registrant. Here are the following status codes: 


*'''Admin Reviewing''': The registrant data has been submitted and being reviewed by compliance team.
*'''Pending''': The verification process has been inititated, and verification email will be sent.
*'''Suspended''': The registrant has failed verification and the domain has been suspended.
*'''Verified''': The registrant has been validated.
*'''Verifying''': The verification process has been initiated and is waiting for registrant response.
*'''Unverified''': The verification process has not been inititated.





### seeAlso

* [SoftLayer_Dns_Domain_Registration](/reference/services/SoftLayer_Dns_Domain_Registration )




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
[description]: #description
#### [description]
The description of the registrant verification status.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
The unique identifier of the registrant verification status  
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
The unique keyname of the registrant verification status.  
<span class="type-label">Type: </span>**string**

-----
[name]: #name
#### [name]
The name of the registrant verification status.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


