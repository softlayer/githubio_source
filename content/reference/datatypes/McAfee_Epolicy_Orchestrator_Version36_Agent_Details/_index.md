---
title: "McAfee_Epolicy_Orchestrator_Version36_Agent_Details"
description: "The McAfee_Epolicy_Orchestrator_Version36_Agent_Details data type represents a virus scan agent and contains details abo... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Epolicy"
classes:
    - "McAfee_Epolicy_Orchestrator_Version36_Agent_Details"
---

# McAfee_Epolicy_Orchestrator_Version36_Agent_Details
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/McAfee_Epolicy_Orchestrator_Version36_Agent_Details' >Datatype</a></li>
    </ul>
</div>

## Description 
The McAfee_Epolicy_Orchestrator_Version36_Agent_Details data type represents a virus scan agent and contains details about its version.





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
[agentVersion]: #agentversion
#### [agentVersion]
Version number of the anti-virus scan agent.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[lastUpdate]: #lastupdate
#### [lastUpdate]
The date of the last time the anti-virus agent checked in.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[currentPolicy]: #currentpolicy
#### [currentPolicy]
The current anti-virus policy of an agent.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Agent_Parent_Details**


</div>

## Count
</div>


