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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#configurationTemplateId" name=configurationTemplateId>configurationTemplateId</a></span>
            <div class='views-field-body'>Internal identifier of a configuration template </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>Internal identifier of a configuration group reference record </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#templateGroupId" name=templateGroupId>templateGroupId</a></span>
            <div class='views-field-body'>Internal identifier of a monitoring agent configuration group </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#configurationTemplate" name=configurationTemplate>configurationTemplate</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#templateGroup" name=templateGroup>templateGroup</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group'>SoftLayer_Monitoring_Agent_Configuration_Template_Group </a></p></div>
        </div>
            </div>
</div>


