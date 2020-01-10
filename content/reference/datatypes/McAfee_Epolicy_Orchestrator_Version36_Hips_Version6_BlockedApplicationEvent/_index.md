---
title: "McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_BlockedApplicationEvent"
description: "The McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_BlockedApplicationEvent data type contains a single blocked appl... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Epolicy"
classes:
    - "McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_BlockedApplicationEvent"
---

# McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_BlockedApplicationEvent
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_BlockedApplicationEvent' >Datatype</a></li>
    </ul>
</div>

## Description 
The McAfee_Epolicy_Orchestrator_Version36_Hips_Version6_BlockedApplicationEvent data type contains a single blocked application event. The details of the event are the time the event occurred, the process that generated the event and a brief description of the application that was blocked. 





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
[applicationDescription]: #applicationdescription
#### [applicationDescription]
A brief description of the application that is blocked.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[incidentTime]: #incidenttime
#### [incidentTime]
The time that an application is blocked.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[processName]: #processname
#### [processName]
The name of a process that is blocked.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


