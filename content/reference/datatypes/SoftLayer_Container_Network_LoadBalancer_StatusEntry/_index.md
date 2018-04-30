---
title: "SoftLayer_Container_Network_LoadBalancer_StatusEntry"
description: "The LoadBalancer_StatusEntry object stores information about the current status of a particular load balancer service.... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_LoadBalancer_StatusEntry"
---

# SoftLayer_Container_Network_LoadBalancer_StatusEntry
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_LoadBalancer_StatusEntry' >Datatype</a></li>
    </ul>
</div>

## Description 
The LoadBalancer_StatusEntry object stores information about the current status of a particular load balancer service. 

It is a data container that cannot be edited, deleted, or saved. 

It is returned exclusively by the getStatus method on the [[SoftLayer_Network_LoadBalancer_Service]] service 





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
                <a href="#content" name=content>content</a>
            </span>
            <div class='views-field-body'>The value of the entry. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#label" name=label>label</a>
            </span>
            <div class='views-field-body'>Text description of the status entry </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


