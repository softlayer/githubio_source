---
title: "SoftLayer_Container_Ticket_GraphInputs"
description: "SoftLayer_Container_Ticket_GraphInputs models a single inbound object for a given ticket graph."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Ticket_GraphInputs"
---

# SoftLayer_Container_Ticket_GraphInputs
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Ticket_GraphInputs' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Ticket_GraphInputs models a single inbound object for a given ticket graph.
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
            <span class='views-field-title'><a href="#endDate" name=endDate>endDate</a></span>
            <div class='views-field-body'>This is a unix timestamp that represents the stop date/time for a graph. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkInterfaceId" name=networkInterfaceId>networkInterfaceId</a></span>
            <div class='views-field-body'>The front-end or back-end network uplink interface associated with this server. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#pod" name=pod>pod</a></span>
            <div class='views-field-body'>* </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serverName" name=serverName>serverName</a></span>
            <div class='views-field-body'>This is a human readable name for the server or rack being graphed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#startDate" name=startDate>startDate</a></span>
            <div class='views-field-body'>This is a unix timestamp that represents the begin date/time for a graph. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
            </div>
    </div>


