---
title: "SoftLayer_Network_Pod"
description: "SoftLayer_Network_Pod refers to a portion of a data center that share a Backend Customer Router (BCR) and usually a fron... "
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
SoftLayer_Network_Pod refers to a portion of a data center that share a Backend Customer Router (BCR) and usually a front-end counterpart known as a Frontend Customer Router (FCR). A Pod primarily denotes a logical location within the network and the physical aspects that support networks. This is in contrast to representing a specific physical location. 

A ``Pod`` is identified by a ``name``, which is unique. A Pod name follows the format 'dddnn.podii', where 'ddd' is a data center code, 'nn' is the data center number, 'pod' is a literal string and 'ii' is a two digit, left-zero- padded number which corresponds to a Backend Customer Router (BCR) of the desired data center. Examples: 
* dal09.pod01 = Dallas 9, Pod 1 (ie. bcr01)
* sjc01.pod04 = San Jose 1, Pod 4 (ie. bcr04)
* ams01.pod01 = Amsterdam 1, Pod 1 (ie. bcr01)
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
            <span class='views-field-title'><a href="#backendRouterId" name=backendRouterId>backendRouterId</a></span>
            <div class='views-field-body'>Identifier for this Pod's Backend Customer Router (BCR) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#backendRouterName" name=backendRouterName>backendRouterName</a></span>
            <div class='views-field-body'>Host name of Pod's Backend Customer Router (BCR), e.g. bcr01a.dal09 </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#capabilities" name=capabilities>capabilities</a></span>
            <div class='views-field-body'>The list of capabilities this Pod has. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>array of strings</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#datacenterLongName" name=datacenterLongName>datacenterLongName</a></span>
            <div class='views-field-body'>Long form name of the data center in which this Pod resides, e.g. Dallas 9 </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#datacenterName" name=datacenterName>datacenterName</a></span>
            <div class='views-field-body'>Name of data center in which this Pod resides, e.g. dal09 </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#frontendRouterId" name=frontendRouterId>frontendRouterId</a></span>
            <div class='views-field-body'>(optional) Identifier for this Pod's Frontend Customer Router (FCR) </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#frontendRouterName" name=frontendRouterName>frontendRouterName</a></span>
            <div class='views-field-body'>Host name of Pod's Frontend Customer Router (FCR), e.g. fcr01a.dal09 </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The unique name of the Pod. See [[SoftLayer_Network_Pod (type)]] for details of the name's construction.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


