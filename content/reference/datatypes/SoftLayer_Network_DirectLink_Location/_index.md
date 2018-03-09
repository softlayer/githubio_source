---
title: "SoftLayer_Network_DirectLink_Location"
description: "The SoftLayer_Network_DirectLink_Location presents a structure containing attributes of a Direct Link location, and its... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_DirectLink_Location"
---

# SoftLayer_Network_DirectLink_Location
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_DirectLink_Location' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_DirectLink_Location' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_DirectLink_Location presents a structure containing attributes of a Direct Link location, and its related object SoftLayer location. 





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
                <a href="#buildingColocationOwner" name=buildingColocationOwner>buildingColocationOwner</a>
            </span>
            <div class='views-field-body'>The Direct Link specific location owner for POP/DC facilities. Like Equinix, Pacnet, Verizon etc.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier of a Direct Link location. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#isRedundantXcr" name=isRedundantXcr>isRedundantXcr</a>
            </span>
            <div class='views-field-body'>Specifies if The Direct Link specific location has Redundancy:secondary XCR availability.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locationId" name=locationId>locationId</a>
            </span>
            <div class='views-field-body'>The Direct Link specific location ie. Data Center & Network POP facility. Refer to location object Like Dallas in US, London in England etc.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#marketGeography" name=marketGeography>marketGeography</a>
            </span>
            <div class='views-field-body'>The Direct Link Market location used in Direct Link Order. Like Europe, North America, Asia pacific etc.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cloudExchangeProvider" name=cloudExchangeProvider>cloudExchangeProvider</a>
            </span>
            <div class='views-field-body'>The Id of Direct Link cloud exchange provider. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_DirectLink_CloudExchangeProvider'>SoftLayer_Network_DirectLink_CloudExchangeProvider </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#location" name=location>location</a>
            </span>
            <div class='views-field-body'>The location of Direct Link facility. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#provider" name=provider>provider</a>
            </span>
            <div class='views-field-body'>The Id of Direct Link provider. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_DirectLink_Provider'>SoftLayer_Network_DirectLink_Provider </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


