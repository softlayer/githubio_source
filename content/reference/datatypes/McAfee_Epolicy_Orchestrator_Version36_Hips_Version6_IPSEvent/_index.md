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

## Local
-----
[incidentTime]: #incidenttime
#### [incidentTime]
The time when an IPS event occurred.  
<span class="type-label">Type: </span>**dateTime**

-----
[processName]: #processname
#### [processName]
Name of the process that generated an IPS event.  
<span class="type-label">Type: </span>**string**

-----
[reactionText]: #reactiontext
#### [reactionText]
The action taken because of an IPS event.  
<span class="type-label">Type: </span>**string**

-----
[remoteIpAddress]: #remoteipaddress
#### [remoteIpAddress]
The IP address that generated an IPS event.  
<span class="type-label">Type: </span>**string**

-----
[severityText]: #severitytext
#### [severityText]
The severity level for an IPS event.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[signature]: #signature
#### [signature]
The signature that generated an IPS event.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_Event_Signature**


## Count
</div>


