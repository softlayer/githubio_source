---
title: "McAfee_Epolicy_Orchestrator_Version45_Event_Version8"
description: "The McAfee_Epolicy_Orchestrator_Version45_Event_Version8 data type represents a single event. It contains details about... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Epolicy"
classes:
    - "McAfee_Epolicy_Orchestrator_Version45_Event_Version8"
---

# McAfee_Epolicy_Orchestrator_Version45_Event_Version8
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/McAfee_Epolicy_Orchestrator_Version45_Event_Version8' >Datatype</a></li>
    </ul>
</div>

## Description 
The McAfee_Epolicy_Orchestrator_Version45_Event_Version8 data type represents a single event. It contains details about the event such as the date the event occurred, the virus or intrusion that is detected and the action that is taken. 





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
            <span class='views-field-title'><a href="#detectedUtc" name=detectedUtc>detectedUtc</a></span>
            <div class='views-field-body'>The time that an event was detected. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sourceIpv4" name=sourceIpv4>sourceIpv4</a></span>
            <div class='views-field-body'>The IP address of the source that generated an event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sourceProcessName" name=sourceProcessName>sourceProcessName</a></span>
            <div class='views-field-body'>The name of the process that generated an event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#targetFilename" name=targetFilename>targetFilename</a></span>
            <div class='views-field-body'>The name of the file that was the target of the event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#threatActionTaken" name=threatActionTaken>threatActionTaken</a></span>
            <div class='views-field-body'>The action taken regarding a threat. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#threatName" name=threatName>threatName</a></span>
            <div class='views-field-body'>The name of the threat. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#threatSeverityLabel" name=threatSeverityLabel>threatSeverityLabel</a></span>
            <div class='views-field-body'>The textual representation of the severity level. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#threatType" name=threatType>threatType</a></span>
            <div class='views-field-body'>The type of threat. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#agentDetails" name=agentDetails>agentDetails</a></span>
            <div class='views-field-body'>Additional information about an agent. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>McAfee_Epolicy_Orchestrator_Version45_Agent_Details</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#signature" name=signature>signature</a></span>
            <div class='views-field-body'>The signature information for an event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>McAfee_Epolicy_Orchestrator_Version45_Hips_Event_Signature_Version8</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virusActionTaken" name=virusActionTaken>virusActionTaken</a></span>
            <div class='views-field-body'>The action taken when a virus is detected. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>McAfee_Epolicy_Orchestrator_Version45_Event_Filter_Description</p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


