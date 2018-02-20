---
title: "SoftLayer_Resource_Group_Member_Hardware"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Group_Member_Hardware"
---

# SoftLayer_Resource_Group_Member_Hardware
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Hardware' >Datatype</a></li>
    </ul>
</div>

## Description 

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
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>A resource group member's creation date. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A resource group member's ID. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#status" name=status>status</a></span>
            <div class='views-field-body'>A resource group member's status. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attributes" name=attributes>attributes</a></span>
            <div class='views-field-body'>A resource group member's associated attributes. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Attribute'>SoftLayer_Resource_Group_Member_Attribute[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#descendantMembers" name=descendantMembers>descendantMembers</a></span>
            <div class='views-field-body'>A resource group member's associated member descendants. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#group" name=group>group</a></span>
            <div class='views-field-body'>A resource group member's resource group. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group'>SoftLayer_Resource_Group </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#resource" name=resource>resource</a></span>
            <div class='views-field-body'>A resource group member's associated hardware. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#roles" name=roles>roles</a></span>
            <div class='views-field-body'>A resource group member's associated roles. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group_Role'>SoftLayer_Resource_Group_Role[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serverArbiterOnly" name=serverArbiterOnly>serverArbiterOnly</a></span>
            <div class='views-field-body'>A resource group hardware member's associated server arbiter-only state. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Attribute'>SoftLayer_Resource_Group_Member_Attribute </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serverHidden" name=serverHidden>serverHidden</a></span>
            <div class='views-field-body'>A resource group hardware member's associated server hidden state. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Attribute'>SoftLayer_Resource_Group_Member_Attribute </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serverPriority" name=serverPriority>serverPriority</a></span>
            <div class='views-field-body'>A resource group hardware member's associated server priority. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Attribute'>SoftLayer_Resource_Group_Member_Attribute </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serverSlaveDelay" name=serverSlaveDelay>serverSlaveDelay</a></span>
            <div class='views-field-body'>A resource group hardware member's associated server slave delay (in seconds). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Attribute'>SoftLayer_Resource_Group_Member_Attribute </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serverTags" name=serverTags>serverTags</a></span>
            <div class='views-field-body'>A resource group hardware member's associated server tags (in JSON format). </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Attribute'>SoftLayer_Resource_Group_Member_Attribute </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serverVotes" name=serverVotes>serverVotes</a></span>
            <div class='views-field-body'>A resource group hardware member's associated server vote count. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Attribute'>SoftLayer_Resource_Group_Member_Attribute </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>A resource group member's type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Type'>SoftLayer_Resource_Group_Member_Type </a></p></div>
        </div>
            </div>
</div>


