---
title: "SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference"
description: "SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference class holds the reference information, essentially a S... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference"
---

# SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference class holds the reference information, essentially a SQL join, between a monitoring configuration group and agent configuration templates. 


### associatedMethods

*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group::getObject](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group/getObject )





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
Internal identifier of a configuration template  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Internal identifier of a configuration group reference record  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[templateGroupId]: #templategroupid
#### [templateGroupId]
Internal identifier of a monitoring agent configuration group  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[configurationTemplate]: #configurationtemplate
#### [configurationTemplate]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template </a>**


</div>
<div class="prop-row">

-----
[templateGroup]: #templategroup
#### [templateGroup]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group'>SoftLayer_Monitoring_Agent_Configuration_Template_Group </a>**


</div>

## Count
</div>


