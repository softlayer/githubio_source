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
The date that an access protection event occurs.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[filename]: #filename
#### [filename]
The name of the file that was protected from access.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[processName]: #processname
#### [processName]
The name of the process that was protected from access.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[ruleName]: #rulename
#### [ruleName]
The name of the rule that triggered an access protection event.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[source]: #source
#### [source]
The IP address that caused an access protection event.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


