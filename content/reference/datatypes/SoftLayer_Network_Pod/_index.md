---
title: "SoftLayer_Network_Pod"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Pod"
---

# SoftLayer_Network_Pod
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Pod' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Pod' >Datatype</a></li>
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
            <span class='views-field-title'>
                <a href="#backendRouterId" name=backendRouterId>backendRouterId</a>
            </span>
            <div class='views-field-body'>Identifier for this Pod's Backend Customer Router (BCR) </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#backendRouterName" name=backendRouterName>backendRouterName</a>
            </span>
            <div class='views-field-body'>Host name of Pod's Backend Customer Router (BCR), e.g. bcr01a.dal09 </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#capabilities" name=capabilities>capabilities</a>
            </span>
            <div class='views-field-body'>Property providing a means to filter Pods based on available capabitilies. See [[SoftLayer_Network_Pod/getAllObjects]] to filter for Pods with specific capabilities. See [[SoftLayer_Network_Pod/getCapabilities]] to retrieve capabilities of a specific Pod.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>array of strings</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#datacenterId" name=datacenterId>datacenterId</a>
            </span>
            <div class='views-field-body'>Identifier for the Data Center the Pod resides within </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#datacenterLongName" name=datacenterLongName>datacenterLongName</a>
            </span>
            <div class='views-field-body'>Long form name of the data center in which this Pod resides, e.g. Dallas 9 </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#datacenterName" name=datacenterName>datacenterName</a>
            </span>
            <div class='views-field-body'>Name of data center in which this Pod resides, e.g. dal09 </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#frontendRouterId" name=frontendRouterId>frontendRouterId</a>
            </span>
            <div class='views-field-body'>(optional) Identifier for this Pod's Frontend Customer Router (FCR) </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#frontendRouterName" name=frontendRouterName>frontendRouterName</a>
            </span>
            <div class='views-field-body'>(optional) Host name of Pod's Frontend Customer Router (FCR), e.g. fcr01a.dal09 </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>The unique name of the Pod. See [[SoftLayer_Network_Pod (type)]] for details of the name's construction.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


