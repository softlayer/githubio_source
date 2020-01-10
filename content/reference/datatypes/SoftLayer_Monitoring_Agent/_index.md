---
title: "SoftLayer_Monitoring_Agent"
description: "A monitoring agent object contains information describing the agent."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
---

# SoftLayer_Monitoring_Agent
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Monitoring_Agent' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Monitoring_Agent' >Datatype</a></li>
    </ul>
</div>

## Description 
A monitoring agent object contains information describing the agent. 


### associatedMethods

*  [SoftLayer_Monitoring_Agent::getObject](/reference/services/SoftLayer_Monitoring_Agent/getObject )





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
[configurationTemplateId]: #configurationtemplateid
#### [configurationTemplateId]
Internal identifier of a configuration template that is used to configure this agent  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
Created date  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Internal identifier of a monitoring agent  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Last modified date  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Monitoring agent name  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[remoteMonitoringAgentFlag]: #remotemonitoringagentflag
#### [remoteMonitoringAgentFlag]
Indicates if this monitoring agent resides on your local box or on a SoftLayer monitoring cluster.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[robotId]: #robotid
#### [robotId]
Internal identifier of a monitoring robot that this agent belongs to  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
Internal identifier of a monitoring agent status  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[agentStatus]: #agentstatus
#### [agentStatus]
The current status of the corresponding agent  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Status'>SoftLayer_Monitoring_Agent_Status </a>**


</div>
<div class="prop-row">

-----
[configurationProfiles]: #configurationprofiles
#### [configurationProfiles]
All custom configuration profiles associated with the corresponding agent  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Profile'>SoftLayer_Configuration_Template_Section_Profile[] </a>**


</div>
<div class="prop-row">

-----
[configurationTemplate]: #configurationtemplate
#### [configurationTemplate]
A template of an agent's current configuration which contains information about the structure of the configuration values.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template </a>**


</div>
<div class="prop-row">

-----
[configurationValues]: #configurationvalues
#### [configurationValues]
The values associated with the corresponding Agent configuration.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value'>SoftLayer_Monitoring_Agent_Configuration_Value[] </a>**


</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
SoftLayer hardware related to the agent.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[productItem]: #productitem
#### [productItem]
Contains general information relating to a single SoftLayer product.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>
<div class="prop-row">

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
A description for a specific installation of a Software Component  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**


</div>
<div class="prop-row">

-----
[statusName]: #statusname
#### [statusName]
Monitoring agent status name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
Softlayer_Virtual_Guest object related to the monitoring agent, which this virtual guest object and hardware is on the server of the running agent.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**


</div>

## Count
<div class="prop-row">

-----
[configurationProfileCount]: #configurationprofilecount
#### [configurationProfileCount]
A count of all custom configuration profiles associated with the corresponding agent   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[configurationValueCount]: #configurationvaluecount
#### [configurationValueCount]
A count of the values associated with the corresponding Agent configuration.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


