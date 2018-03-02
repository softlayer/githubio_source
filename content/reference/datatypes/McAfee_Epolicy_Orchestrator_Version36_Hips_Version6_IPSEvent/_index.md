---
title: "McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_IPSEvent"
description: "The McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_IPSEvent data type represents a single IPS event.  It contains d... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Epolicy"
classes:
    - "McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_IPSEvent"
---

# McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_IPSEvent
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_IPSEvent' >Datatype</a></li>
    </ul>
</div>

## Description 
The McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_IPSEvent data type represents a single IPS event.  It contains details about the event such as the date the event occurred, the process that generated it, the severity of the event, and the action taken. 





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
            <span class='views-field-title'><a href="#incidentTime" name=incidentTime>incidentTime</a></span>
            <div class='views-field-body'>The time when an IPS event occurred. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#processName" name=processName>processName</a></span>
            <div class='views-field-body'>Name of the process that generated an IPS event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#reactionText" name=reactionText>reactionText</a></span>
            <div class='views-field-body'>The action taken because of an IPS event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#remoteIpAddress" name=remoteIpAddress>remoteIpAddress</a></span>
            <div class='views-field-body'>The IP address that generated an IPS event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#severityText" name=severityText>severityText</a></span>
            <div class='views-field-body'>The severity level for an IPS event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#signature" name=signature>signature</a></span>
            <div class='views-field-body'>The signature that generated an IPS event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_Event_Signature</p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


