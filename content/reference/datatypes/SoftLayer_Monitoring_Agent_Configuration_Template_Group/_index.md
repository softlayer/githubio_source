---
title: "SoftLayer_Monitoring_Agent_Configuration_Template_Group"
description: "The SoftLayer_Monitoring_Agent_Configuration_Template_Group class is consisted of configuration templates for agents in... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group"
---

# SoftLayer_Monitoring_Agent_Configuration_Template_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Monitoring_Agent_Configuration_Template_Group class is consisted of configuration templates for agents in a monitoring package. 


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
[accountId]: #accountid
#### [accountId]
Internal identifier of a SoftLayer account that this configuration template belongs to   
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
[description]: #description
#### [description]
Description of a monitoring agent configuration group  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Internal identifier of a monitoring agent configuration group  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[itemId]: #itemid
#### [itemId]
Internal identifier of a configuration template type  
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
Name of a monitoring agent configuration group  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[configurationTemplateReferences]: #configurationtemplatereferences
#### [configurationTemplateReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference'>SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference[] </a>**


</div>
<div class="prop-row">

-----
[configurationTemplates]: #configurationtemplates
#### [configurationTemplates]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template[] </a>**


</div>
<div class="prop-row">

-----
[item]: #item
#### [item]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>

## Count
<div class="prop-row">

-----
[configurationTemplateCount]: #configurationtemplatecount
#### [configurationTemplateCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[configurationTemplateReferenceCount]: #configurationtemplatereferencecount
#### [configurationTemplateReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


