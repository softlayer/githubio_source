---
title: "SoftLayer_Service_External_Resource"
description: "The SoftLayer_Service_External_Resource is a placeholder that references a service being provided outside of the standar... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Service"
classes:
    - "SoftLayer_Service_External_Resource"
---

# SoftLayer_Service_External_Resource
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Service_External_Resource' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Service_External_Resource is a placeholder that references a service being provided outside of the standard SoftLayer system. 





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
[accountId]: #accountid
#### [accountId]
The customer account that is consuming the related service.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[externalIdentifier]: #externalidentifier
#### [externalIdentifier]
The unique identifier in the service provider's system.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
An external resource's unique identifier in the SoftLayer system.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The customer account that is consuming the service.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>

## Count
</div>


