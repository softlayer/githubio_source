---
title: "McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event_AccessProtection"
description: "The McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event_AccessProtection data type represents an access protection eve... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Epolicy"
classes:
    - "McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event_AccessProtection"
---

# McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event_AccessProtection
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event_AccessProtection' >Datatype</a></li>
    </ul>
</div>

## Description 
The McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event_AccessProtection data type represents an access protection event. It contains details about the event such as when it occurs, the process that caused it, and the rule that triggered the event. 





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
                <a href="#eventLocalDateTime" name=eventLocalDateTime>eventLocalDateTime</a>
            </span>
            <div class='views-field-body'>The date that an access protection event occurs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#filename" name=filename>filename</a>
            </span>
            <div class='views-field-body'>The name of the file that was protected from access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#processName" name=processName>processName</a>
            </span>
            <div class='views-field-body'>The name of the process that was protected from access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ruleName" name=ruleName>ruleName</a>
            </span>
            <div class='views-field-body'>The name of the rule that triggered an access protection event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#source" name=source>source</a>
            </span>
            <div class='views-field-body'>The IP address that caused an access protection event. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


