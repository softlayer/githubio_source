---
title: "SoftLayer_Network_Monitor_Version1_Query_Host"
description: "The Monitoring_Query_Host type represents a monitoring instance.  It consists of a hardware ID to monitor, an IP address... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Host"
---

# SoftLayer_Network_Monitor_Version1_Query_Host
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host' >Datatype</a></li>
    </ul>
</div>

## Description 
The Monitoring_Query_Host type represents a monitoring instance.  It consists of a hardware ID to monitor, an IP address attached to that hardware ID, a method of monitoring, and what to do in the instance that the monitor ever fails. 
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
            <span class='views-field-title'><a href="#arg1Value" name=arg1Value>arg1Value</a></span>
            <div class='views-field-body'>The argument to be used for this monitor, if necessary.  The lowest monitoring levels (like ping) ignore this setting, but higher levels like HTTP custom use it. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guestId" name=guestId>guestId</a></span>
            <div class='views-field-body'>Virtual Guest Identification Number for the guest being monitored. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareId" name=hardwareId>hardwareId</a></span>
            <div class='views-field-body'>The ID of the hardware being monitored </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hostId" name=hostId>hostId</a></span>
            <div class='views-field-body'>Identification Number for the host being monitored. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The unique identifier for this object </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#ipAddress" name=ipAddress>ipAddress</a></span>
            <div class='views-field-body'>The IP address to be monitored.  Must be attached to the hardware on this object </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#queryTypeId" name=queryTypeId>queryTypeId</a></span>
            <div class='views-field-body'>The ID of the query type to use. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#responseActionId" name=responseActionId>responseActionId</a></span>
            <div class='views-field-body'>The ID of the response action to take when the monitor fails </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#status" name=status>status</a></span>
            <div class='views-field-body'>The status of this monitoring instance.  Anything other than "ON" means that the monitor has been disabled </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#waitCycles" name=waitCycles>waitCycles</a></span>
            <div class='views-field-body'>The number of 5-minute cycles to wait before the "responseAction" is taken.  If set to 0, the response action will be taken immediately </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardware" name=hardware>hardware</a></span>
            <div class='views-field-body'>The hardware that is being monitored by this monitoring instance </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#lastResult" name=lastResult>lastResult</a></span>
            <div class='views-field-body'>The most recent result for this particular monitoring instance. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Result'>SoftLayer_Network_Monitor_Version1_Query_Result </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#queryType" name=queryType>queryType</a></span>
            <div class='views-field-body'>The type of monitoring query that is executed when this hardware is monitored. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Type'>SoftLayer_Network_Monitor_Version1_Query_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#responseAction" name=responseAction>responseAction</a></span>
            <div class='views-field-body'>The action taken when a monitor fails. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_ResponseType'>SoftLayer_Network_Monitor_Version1_Query_ResponseType </a></p></div>
        </div>
            </div>
</div>


