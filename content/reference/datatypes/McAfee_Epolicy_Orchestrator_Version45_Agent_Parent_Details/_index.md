---
title: "McAfee_Epolicy_Orchestrator_Version45_Agent_Parent_Details"
description: "The McAfee_Epolicy_Orchestrator_Version45_Agent_Parent_Details data type contains the name of an anti-virus policy."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Epolicy"
classes:
    - "McAfee_Epolicy_Orchestrator_Version45_Agent_Parent_Details"
---

# McAfee_Epolicy_Orchestrator_Version45_Agent_Parent_Details
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/McAfee_Epolicy_Orchestrator_Version45_Agent_Parent_Details' >Datatype</a></li>
    </ul>
</div>

## Description 


The McAfee_Epolicy_Orchestrator_Version45_Agent_Parent_Details data type contains the name of an anti-virus policy.





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
[name]: #name
#### [name]
The name of a policy.  
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
[policies]: #policies
#### [policies]
The current anti-virus policy of an agent.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version45_Agent_Parent_Details[]**  



</div>

## Count
<div class="prop-row">

-----
[policyCount]: #policycount
#### [policyCount]
A count of the current anti-virus policy of an agent.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


