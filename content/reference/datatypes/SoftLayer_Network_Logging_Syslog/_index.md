---
title: "SoftLayer_Network_Logging_Syslog"
description: "The Syslog class holds a single line from the Networking Firewall 'Syslog' record, for firewall detected and blocked att... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Logging_Syslog"
---

# SoftLayer_Network_Logging_Syslog
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog' >Datatype</a></li>
    </ul>
</div>

## Description 
The Syslog class holds a single line from the Networking Firewall "Syslog" record, for firewall detected and blocked attempts on a server. 
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
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>Timestamp for when the connection was blocked by the firewall </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#destinationIpAddress" name=destinationIpAddress>destinationIpAddress</a></span>
            <div class='views-field-body'>The Destination IP Address of the blocked connection (your end) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#destinationPort" name=destinationPort>destinationPort</a></span>
            <div class='views-field-body'>The Destination Port of the blocked connection (your end) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#eventType" name=eventType>eventType</a></span>
            <div class='views-field-body'>This tells you what kind of firewall event this log line is for:  accept or deny. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#message" name=message>message</a></span>
            <div class='views-field-body'>Raw syslog message for the event </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#protocol" name=protocol>protocol</a></span>
            <div class='views-field-body'>Connection protocol used to make the call that was blocked (tcp, udp, etc) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sourceIpAddress" name=sourceIpAddress>sourceIpAddress</a></span>
            <div class='views-field-body'>The Source IP Address of the call that was blocked (attacker's end) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sourcePort" name=sourcePort>sourcePort</a></span>
            <div class='views-field-body'>The Source Port where the blocked connection was established (attacker's end) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#totalEvents" name=totalEvents>totalEvents</a></span>
            <div class='views-field-body'>If this is an aggregation of syslog events, this property shows the total events. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
    </div>


