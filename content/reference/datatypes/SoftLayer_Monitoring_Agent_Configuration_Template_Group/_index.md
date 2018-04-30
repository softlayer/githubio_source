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
            <span class='views-field-title'>
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>Internal identifier of a SoftLayer account that this configuration template belongs to  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>Created date </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>Description of a monitoring agent configuration group </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Internal identifier of a monitoring agent configuration group </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemId" name=itemId>itemId</a>
            </span>
            <div class='views-field-body'>Internal identifier of a configuration template type </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>Last modified date </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>Name of a monitoring agent configuration group </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#configurationTemplateReferences" name=configurationTemplateReferences>configurationTemplateReferences</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference'>SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#configurationTemplates" name=configurationTemplates>configurationTemplates</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#item" name=item>item</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#configurationTemplateCount" name=configurationTemplateCount>configurationTemplateCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#configurationTemplateReferenceCount" name=configurationTemplateReferenceCount>configurationTemplateReferenceCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


