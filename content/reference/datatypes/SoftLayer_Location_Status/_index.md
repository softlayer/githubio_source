---
title: "SoftLayer_Location_Status"
description: "SoftLayer_Location_Status models the state of any location. SoftLayer uses the following status codes: 


*'''ACTIVE''':... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Status"
---

# SoftLayer_Location_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Location_Status' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Location_Status models the state of any location. SoftLayer uses the following status codes: 


*'''ACTIVE''': The location is currently active and available for public usage.
*'''PLANNED''': Used when a location is planned but not yet active.
*'''RETIRED''': Used when a location has been retired and no longer active.


Locations in use should stay in the ACTIVE state. If a locations status ever reads anything else and contains active hardware then please contact SoftLayer support. 



### seeAlso

* [SoftLayer_Location](/reference/services/SoftLayer_Location )




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
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A locations status's internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#status" name=status>status</a>
            </span>
            <div class='views-field-body'>A Location's status code. See the SoftLayer_Locaiton_Status Overview for ''status''' possible values. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


