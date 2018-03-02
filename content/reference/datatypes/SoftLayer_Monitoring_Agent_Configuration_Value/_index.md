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
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Value' >Datatype</a></li>
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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#agentId" name=agentId>agentId</a></span>
            <div class='views-field-body'>Internal identifier of a monitoring Agent that this configuration value </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#configurationDefinitionId" name=configurationDefinitionId>configurationDefinitionId</a></span>
            <div class='views-field-body'>Internal identifier of a monitoring configuration definition by which </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>User-friendly description of a configuration value. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>Internal identifier of a monitoring configuration value. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#profileId" name=profileId>profileId</a></span>
            <div class='views-field-body'>Internal identifier of a configuration profile. Configuration profile is associated with a configuration section type of "Template section". 

A "Template section" defines skeleton configuration definitions. For instance, if you want to monitor additional hard disks with "CPU/Memory/Disk Monitoring Agent", you will have to add a new configuration profiles.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#value" name=value>value</a></span>
            <div class='views-field-body'>Configuration value </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#definition" name=definition>definition</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition'>SoftLayer_Configuration_Template_Section_Definition </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#metricDataType" name=metricDataType>metricDataType</a></span>
            <div class='views-field-body'>The metric data type used to retrieve metric data currently being tracked. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Container_Metric_Data_Type'>SoftLayer_Container_Metric_Data_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#monitoringAgent" name=monitoringAgent>monitoringAgent</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Monitoring_Agent'>SoftLayer_Monitoring_Agent </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#profile" name=profile>profile</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Profile'>SoftLayer_Configuration_Template_Section_Profile </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


