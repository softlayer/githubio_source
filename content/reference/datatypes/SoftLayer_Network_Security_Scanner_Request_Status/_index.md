---
title: "SoftLayer_Network_Security_Scanner_Request_Status"
description: "The SoftLayer_Network_Security_Scanner_Request_Status data type represents the current status of a vulnerability scan. T... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Security_Scanner_Request_Status"
---

# SoftLayer_Network_Security_Scanner_Request_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Security_Scanner_Request_Status' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Security_Scanner_Request_Status data type represents the current status of a vulnerability scan. The status messages are as follows: 
*Scan Pending
*Scan Processing
*Scan Complete
*Scan Cancelled
*Generating Report.


The status of a vulnerability scan will change over the course of a scan's execution. 


### associatedMethods

*  [SoftLayer_Network_Security_Scanner_Request::getStatus](/reference/services/SoftLayer_Network_Security_Scanner_Request/getStatus )



### seeAlso

* [SoftLayer_Network_Security_Scanner_Request](/reference/datatypes/SoftLayer_Network_Security_Scanner_Request )




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
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The identifier of a vulnerability scan's status. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The status message of a vulnerability scan. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


