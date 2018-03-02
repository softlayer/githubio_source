---
title: "McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event"
description: "The McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event data type represents a single anti-virus event. It contains de... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Epolicy"
classes:
    - "McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event"
---

# McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event' >Datatype</a></li>
    </ul>
</div>

## Description 
The McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event data type represents a single anti-virus event. It contains details about the event such as the date the event occurred, the virus that is detected and the action that is taken. 





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
            <span class='views-field-title'><a href="#eventLocalDateTime" name=eventLocalDateTime>eventLocalDateTime</a></span>
            <div class='views-field-body'>The date when an anti-virus event occurs. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#filename" name=filename>filename</a></span>
            <div class='views-field-body'>Name of the file found to be infected. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virusName" name=virusName>virusName</a></span>
            <div class='views-field-body'>The name of a virus that is found. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virusType" name=virusType>virusType</a></span>
            <div class='views-field-body'>The type of virus that is found. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#virusActionTaken" name=virusActionTaken>virusActionTaken</a></span>
            <div class='views-field-body'>The action taken when a virus is detected. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event_Filter_Description</p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


