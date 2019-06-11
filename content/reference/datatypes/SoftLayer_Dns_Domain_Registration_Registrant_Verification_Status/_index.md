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

* [SoftLayer_Dns_Domain_Registration](/reference/datatypes/SoftLayer_Dns_Domain_Registration )




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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>The description of the registrant verification status. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier of the registrant verification status </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#keyName" name=keyName>keyName</a>
            </span>
            <div class='views-field-body'>The unique keyname of the registrant verification status. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>The name of the registrant verification status. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


