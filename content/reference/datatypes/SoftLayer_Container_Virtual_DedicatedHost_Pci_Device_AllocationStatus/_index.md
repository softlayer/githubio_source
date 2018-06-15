---
title: "SoftLayer_Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus"
description: "This data type represents PCI device allocation properties of a [[SoftLayer_Virtual_DedicatedHost]]."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus"
---

# SoftLayer_Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus' >Datatype</a></li>
    </ul>
</div>

## Description 
This data type represents PCI device allocation properties of a [[SoftLayer_Virtual_DedicatedHost]]. 





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
                <a href="#deviceCount" name=deviceCount>deviceCount</a>
            </span>
            <div class='views-field-body'>The number of PCI devices on the host. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#devicesAllocated" name=devicesAllocated>devicesAllocated</a>
            </span>
            <div class='views-field-body'>The number of PCI devices currently allocated to guests. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#devicesAvailable" name=devicesAvailable>devicesAvailable</a>
            </span>
            <div class='views-field-body'>The number of PCI devices available for allocation. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareComponentModelGenericId" name=hardwareComponentModelGenericId>hardwareComponentModelGenericId</a>
            </span>
            <div class='views-field-body'>The generic component model ID of the PCI device. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hostId" name=hostId>hostId</a>
            </span>
            <div class='views-field-body'>The ID of the host that the dedicated host is on. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
    </div>


