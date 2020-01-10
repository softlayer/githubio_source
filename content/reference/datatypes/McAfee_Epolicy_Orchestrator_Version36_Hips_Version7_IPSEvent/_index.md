---
title: "McAfee_Epolicy_Orchestrator_Version36_Hips_Version7_IPSEvent"
description: "The McAfee_Epolicy_Orchestrator_Version36_Hips_Version7_IPSEvent data type represents a single IPS event.  It contains d... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Epolicy"
classes:
    - "McAfee_Epolicy_Orchestrator_Version36_Hips_Version7_IPSEvent"
---

# McAfee_Epolicy_Orchestrator_Version36_Hips_Version7_IPSEvent
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/McAfee_Epolicy_Orchestrator_Version36_Hips_Version7_IPSEvent' >Datatype</a></li>
    </ul>
</div>

## Description 
The McAfee_Epolicy_Orchestrator_Version36_Hips_Version7_IPSEvent data type represents a single IPS event.  It contains details about the event such as the date the event occurred, the process that generated it, the severity of the event, and the action taken. 





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[incidentTime]: #incidenttime
#### [incidentTime]
The time when an IPS event occurred.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[processName]: #processname
#### [processName]
Name of the process that generated an IPS event.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[reactionText]: #reactiontext
#### [reactionText]
The action taken because of an IPS event.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[remoteIpAddress]: #remoteipaddress
#### [remoteIpAddress]
The IP address that generated an IPS event.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[severityText]: #severitytext
#### [severityText]
The severity level for an IPS event.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[signature]: #signature
#### [signature]
The signature that generated an IPS event.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Hips_Version7_Event_Signature**


</div>

## Count
</div>


