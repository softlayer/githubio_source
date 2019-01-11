---
title: "SoftLayer_Container_Authentication_Response_IpAddressRestrictionCheckNeeded"
description: "The SoftLayer_Container_Authentication_Response_IpAddressRestrictionCheckNeeded data type indicates that the caller (IAM... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Authentication_Response_IpAddressRestrictionCheckNeeded"
---

# SoftLayer_Container_Authentication_Response_IpAddressRestrictionCheckNeeded
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_IpAddressRestrictionCheckNeeded' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Authentication_Response_IpAddressRestrictionCheckNeeded data type indicates that the caller (IAM presumably) needs to do an IP address check of the logging-in user against the restricted IP list kept in BSS.  We don't know the IP address of the user here (only IAM does) so we return an indicator of which user matched the username and expect IAM to come back with another login call that will include a mini-JWT token that contains an assertion that the IP address was checked. 





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
                <a href="#accounts" name=accounts>accounts</a>
            </span>
            <div class='views-field-body'>The list of linked accounts for the authenticated SoftLayer customer portal user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_Account'>SoftLayer_Container_Authentication_Response_Account[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#statusKeyName" name=statusKeyName>statusKeyName</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


