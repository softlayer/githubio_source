---
title: "SoftLayer_Network_Subnet_Registration_Status"
description: "Subnet Registration Status objects describe the current status of a subnet registration. 

The standard values for these... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration_Status"
---

# SoftLayer_Network_Subnet_Registration_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Subnet_Registration_Status' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Status' >Datatype</a></li>
    </ul>
</div>

## Description 
Subnet Registration Status objects describe the current status of a subnet registration. 

The standard values for these objects are as follows: <ul> <li><strong>OPEN</strong> - Indicates that the registration object is new and has yet to be submitted to the RIR</li> <li><strong>PENDING</strong> - Indicates that the registration object has been submitted to the RIR and is awaiting response</li> <li><strong>COMPLETE</strong> - Indicates that the RIR action has completed</li> <li><strong>DELETED</strong> - Indicates that the registration object has been gracefully removed is no longer valid</li> <li><strong>CANCELLED</strong> - Indicates that the registration object has been abruptly removed is no longer valid</li> </ul> 





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
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Unique numeric ID of the status object  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#keyName" name=keyName>keyName</a>
            </span>
            <div class='views-field-body'>Code-friendly string name of the status  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>Human-readable name of the status  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


