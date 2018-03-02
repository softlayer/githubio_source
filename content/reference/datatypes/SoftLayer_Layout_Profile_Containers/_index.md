---
title: "SoftLayer_Layout_Profile_Containers"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile_Containers"
---

# SoftLayer_Layout_Profile_Containers
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Profile_Containers' >Datatype</a></li>
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
            <div class='views-field-body'>Timestamp of when the reference was created </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The internal identifier of the container reference </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutContainerId" name=layoutContainerId>layoutContainerId</a></span>
            <div class='views-field-body'>The id of the referenced [[SoftLayer_Layout_Container]] </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutProfileId" name=layoutProfileId>layoutProfileId</a></span>
            <div class='views-field-body'>The id of the referenced [[SoftLayer_Layout_Profile]] </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>Timestamp of when the reference was last updated </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutContainerType" name=layoutContainerType>layoutContainerType</a></span>
            <div class='views-field-body'>The container to be contained </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Layout_Container'>SoftLayer_Layout_Container </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#layoutProfile" name=layoutProfile>layoutProfile</a></span>
            <div class='views-field-body'>The profile containing this container </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Layout_Profile'>SoftLayer_Layout_Profile </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


