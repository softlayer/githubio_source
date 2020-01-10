---
title: "SoftLayer_Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus"
description: "This data type represents PCI device allocation properties of a [SoftLayer_Virtual_DedicatedHost]({{<ref 'reference/data... "
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
This data type represents PCI device allocation properties of a [SoftLayer_Virtual_DedicatedHost]({{<ref "reference/datatypes/SoftLayer_Virtual_DedicatedHost">}}). 





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[deviceCount]: #devicecount
#### [deviceCount]
The number of PCI devices on the host.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[deviceName]: #devicename
#### [deviceName]
The name of the PCI devices on the host.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[devicesAllocated]: #devicesallocated
#### [devicesAllocated]
The number of PCI devices currently allocated to guests.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[devicesAvailable]: #devicesavailable
#### [devicesAvailable]
The number of PCI devices available for allocation.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hardwareComponentModelGenericId]: #hardwarecomponentmodelgenericid
#### [hardwareComponentModelGenericId]
The generic component model ID of the PCI device.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hostId]: #hostid
#### [hostId]
The ID of the host that the dedicated host is on.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


