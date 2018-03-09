---
title: "SoftLayer_Network_Monitor_Version1_Query_Result"
description: "The monitoring result object is used to show the status of the actions taken by the monitoring system. 

In general, onl... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Result"
---

# SoftLayer_Network_Monitor_Version1_Query_Result
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Result' >Datatype</a></li>
    </ul>
</div>

## Description 
The monitoring result object is used to show the status of the actions taken by the monitoring system. 

In general, only the responseStatus variable is needed, as it holds the information on the status of the service. 





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
                <a href="#finishTime" name=finishTime>finishTime</a>
            </span>
            <div class='views-field-body'>The timestamp of when this monitor was co </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#responseStatus" name=responseStatus>responseStatus</a>
            </span>
            <div class='views-field-body'>The response status for this server.  The response status meanings are: 0:  Down/Critical: Server is down and/or has passed the critical response threshold (extremely long ping response, abnormal behavior, etc.) 1:  Warning - Server may be recovering from a previous down state, or may have taken too long to respond 2:  Up 3:  Not used 4:  Unknown - An unknown error has occurred.  If the problem persists, contact support. 5:  Unknown - An unknown error has occurred.  If the problem persists, contact support.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#responseTime" name=responseTime>responseTime</a>
            </span>
            <div class='views-field-body'>The length of time it took the server to respond </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#queryHost" name=queryHost>queryHost</a>
            </span>
            <div class='views-field-body'>References the queryHost that this response relates to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host'>SoftLayer_Network_Monitor_Version1_Query_Host </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


