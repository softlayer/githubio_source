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
[eventLocalDateTime]: #eventlocaldatetime
#### [eventLocalDateTime]
The date when an anti-virus event occurs.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[filename]: #filename
#### [filename]
Name of the file found to be infected.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[virusName]: #virusname
#### [virusName]
The name of a virus that is found.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[virusType]: #virustype
#### [virusType]
The type of virus that is found.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[virusActionTaken]: #virusactiontaken
#### [virusActionTaken]
The action taken when a virus is detected.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Antivirus_Event_Filter_Description**  



</div>

## Count
</div>


