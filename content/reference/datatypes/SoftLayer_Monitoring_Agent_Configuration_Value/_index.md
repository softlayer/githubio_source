---
title: "SoftLayer_Monitoring_Agent_Configuration_Value"
description: "Monitoring agent configuration value"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent_Configuration_Value"
---

# SoftLayer_Monitoring_Agent_Configuration_Value
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Monitoring_Agent_Configuration_Value' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value' >Datatype</a></li>
    </ul>
</div>

## Description 
Monitoring agent configuration value 





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
[agentId]: #agentid
#### [agentId]
Internal identifier of a monitoring Agent that this configuration value  
<span class="type-label">Type: </span>**integer**

-----
[configurationDefinitionId]: #configurationdefinitionid
#### [configurationDefinitionId]
Internal identifier of a monitoring configuration definition by which  
<span class="type-label">Type: </span>**integer**

-----
[description]: #description
#### [description]
User-friendly description of a configuration value.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
Internal identifier of a monitoring configuration value.  
<span class="type-label">Type: </span>**integer**

-----
[profileId]: #profileid
#### [profileId]
Internal identifier of a configuration profile. Configuration profile is associated with a configuration section type of "Template section". 

A "Template section" defines skeleton configuration definitions. For instance, if you want to monitor additional hard disks with "CPU/Memory/Disk Monitoring Agent", you will have to add a new configuration profiles.   
<span class="type-label">Type: </span>**integer**

-----
[value]: #value
#### [value]
Configuration value  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[definition]: #definition
#### [definition]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition'>SoftLayer_Configuration_Template_Section_Definition </a>**

-----
[metricDataType]: #metricdatatype
#### [metricDataType]
The metric data type used to retrieve metric data currently being tracked.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Metric_Data_Type'>SoftLayer_Container_Metric_Data_Type </a>**

-----
[monitoringAgent]: #monitoringagent
#### [monitoringAgent]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Agent'>SoftLayer_Monitoring_Agent </a>**

-----
[profile]: #profile
#### [profile]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Profile'>SoftLayer_Configuration_Template_Section_Profile </a>**


## Count
</div>


