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

## Local
-----
[detectedUtc]: #detectedutc
#### [detectedUtc]
The time that an event was detected.  
<span class="type-label">Type: </span>**dateTime**

-----
[sourceIpv4]: #sourceipv4
#### [sourceIpv4]
The IP address of the source that generated an event.  
<span class="type-label">Type: </span>**string**

-----
[sourceProcessName]: #sourceprocessname
#### [sourceProcessName]
The name of the process that generated an event.  
<span class="type-label">Type: </span>**string**

-----
[targetFilename]: #targetfilename
#### [targetFilename]
The name of the file that was the target of the event.  
<span class="type-label">Type: </span>**string**

-----
[threatActionTaken]: #threatactiontaken
#### [threatActionTaken]
The action taken regarding a threat.  
<span class="type-label">Type: </span>**string**

-----
[threatName]: #threatname
#### [threatName]
The name of the threat.  
<span class="type-label">Type: </span>**string**

-----
[threatSeverityLabel]: #threatseveritylabel
#### [threatSeverityLabel]
The textual representation of the severity level.  
<span class="type-label">Type: </span>**string**

-----
[threatType]: #threattype
#### [threatType]
The type of threat.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[agentDetails]: #agentdetails
#### [agentDetails]
Additional information about an agent.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version45_Agent_Details**

-----
[signature]: #signature
#### [signature]
The signature information for an event.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version45_Hips_Event_Signature_Version8**

-----
[virusActionTaken]: #virusactiontaken
#### [virusActionTaken]
The action taken when a virus is detected.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version45_Event_Filter_Description**


## Count
</div>


