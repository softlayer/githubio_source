---
title: "SoftLayer_Network_Pod"
description: "SoftLayer_Network_Pod refers to a portion of a data center that share a Backend Customer Router (BCR) and usually a fron... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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

A ``Pod`` is identified by a ``name``, which is unique. A Pod name follows the format 'dddnn.podii', where 'ddd' is a data center code, 'nn' is the data center number, 'pod' is a literal string and 'ii' is a two digit, left-zero- padded number which corresponds to a Backend Customer Router (BCR) of the desired data center. Examples: <ul> <li>dal09.pod01 = Dallas 9, Pod 1 (ie. bcr01)</li> <li>sjc01.pod04 = San Jose 1, Pod 4 (ie. bcr04)</li> <li>ams01.pod01 = Amsterdam 1, Pod 1 (ie. bcr01)</li> </ul> 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [getAllObjects](/reference/services/SoftLayer_Network_Pod/getAllObjects)
Retrieve a list of Pods; optionally filtered via datacenter and/or capabilities.

</div>

<div class="method-row">

#### [getCapabilities](/reference/services/SoftLayer_Network_Pod/getCapabilities)
Retrieve capabilities for the Pod.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Pod/getObject)
Retrieve a Pod by name.

</div>

<div class="method-row">

#### [listCapabilities](/reference/services/SoftLayer_Network_Pod/listCapabilities)
Retrieve a list of all possible capabilities Pods may fulfill.

</div>
</div>

</div>

