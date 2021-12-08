---
title: "McAfee_Epolicy_Orchestrator_Version45_Event_Version7"
description: "The McAfee_Epolicy_Orchestrator_Version45_Event_Version7 data type represents a single event. It contains details about... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Epolicy"
classes:
    - "McAfee_Epolicy_Orchestrator_Version45_Event_Version7"
---

# McAfee_Epolicy_Orchestrator_Version45_Event_Version7
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/McAfee_Epolicy_Orchestrator_Version45_Event_Version7' >Datatype</a></li>
    </ul>
</div>

## Description 


The McAfee_Epolicy_Orchestrator_Version45_Event_Version7 data type represents a single event. It contains details about the event such as the date the event occurred, the virus or intrusion that is detected and the action that is taken. 





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
[detectedUtc]: #detectedutc
#### [detectedUtc]
The time that an event was detected.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[sourceIpv4]: #sourceipv4
#### [sourceIpv4]
The IP address of the source that generated an event.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[sourceProcessName]: #sourceprocessname
#### [sourceProcessName]
The name of the process that generated an event.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[targetFilename]: #targetfilename
#### [targetFilename]
The name of the file that was the target of the event.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[threatActionTaken]: #threatactiontaken
#### [threatActionTaken]
The action taken regarding a threat.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[threatName]: #threatname
#### [threatName]
The name of the threat.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[threatSeverityLabel]: #threatseveritylabel
#### [threatSeverityLabel]
The textual representation of the severity level.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[threatType]: #threattype
#### [threatType]
The type of threat.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[agentDetails]: #agentdetails
#### [agentDetails]
Additional information about an agent.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version45_Agent_Details**  



</div>
<div class="prop-row">

-----
[signature]: #signature
#### [signature]
The signature information for an event.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version45_Hips_Event_Signature_Version7**  



</div>
<div class="prop-row">

-----
[virusActionTaken]: #virusactiontaken
#### [virusActionTaken]
The action taken when a virus is detected.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version45_Event_Filter_Description**  



</div>

## Count
</div>


