---
title: "SoftLayer_Container_Ticket_GraphOutputs"
description: "SoftLayer_Container_Ticket_GraphOutputs models a single outbound object for a given bandwidth graph."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Ticket_GraphOutputs"
---

# SoftLayer_Container_Ticket_GraphOutputs
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Ticket_GraphOutputs' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Ticket_GraphOutputs models a single outbound object for a given bandwidth graph.


### associatedMethods

*  [SoftLayer_Utility_Ticket_Graph::getTicketImage](/reference/services/SoftLayer_Utility_Ticket_Graph/getTicketImage )
*  [SoftLayer_Utility_Ticket_Graph::getTicketGraphParameters](/reference/services/SoftLayer_Utility_Ticket_Graph/getTicketGraphParameters )



### seeAlso

* [SoftLayer_Container_Ticket_GraphInputs](/reference/datatypes/SoftLayer_Container_Ticket_GraphInputs )




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
            <span class='views-field-title'><a href="#graphImage" name=graphImage>graphImage</a></span>
            <div class='views-field-body'>The raw PNG binary data to be displayed once the graph is drawn. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>binary data</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#graphTitle" name=graphTitle>graphTitle</a></span>
            <div class='views-field-body'>The title that ended up being displayed as part of the graph image. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#maxEndDate" name=maxEndDate>maxEndDate</a></span>
            <div class='views-field-body'>The maximum date included in this graph. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#minStartDate" name=minStartDate>minStartDate</a></span>
            <div class='views-field-body'>The minimum date included in this graph. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
            </div>
    </div>


