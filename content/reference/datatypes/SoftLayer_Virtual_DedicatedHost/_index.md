---
title: "SoftLayer_Virtual_DedicatedHost"
description: "This data type presents the structure for a dedicated host. The data type contains relational properties to distinguish... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_DedicatedHost"
---

# SoftLayer_Virtual_DedicatedHost
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_DedicatedHost' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost' >Datatype</a></li>
    </ul>
</div>

## Description 
This data type presents the structure for a dedicated host. The data type contains relational properties to distinguish a dedicated host and associate an account to it. 





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
[accountId]: #accountid
#### [accountId]
The dedicated host's associated account id.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[cpuCount]: #cpucount
#### [cpuCount]
The capacity that the dedicated host's CPU allocation is restricted to.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date that the dedicated host was created.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[diskCapacity]: #diskcapacity
#### [diskCapacity]
The capacity that the dedicated host's disk allocation is restricted to.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The dedicated host's associated unique id.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[memoryCapacity]: #memorycapacity
#### [memoryCapacity]
The capacity that the dedicated host's memory allocation is restricted to.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that the dedicated host was last modified.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The dedicated host's name.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
A note of up to 1,000 characters about a dedicated host.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that the dedicated host belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[allocationStatus]: #allocationstatus
#### [allocationStatus]
The container that represents allocations on the dedicated host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_DedicatedHost_AllocationStatus'>SoftLayer_Container_Virtual_DedicatedHost_AllocationStatus </a>**


</div>
<div class="prop-row">

-----
[backendRouter]: #backendrouter
#### [backendRouter]
The backend router behind dedicated host's pool of resources.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Router_Backend'>SoftLayer_Hardware_Router_Backend </a>**


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for the dedicated host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Virtual_DedicatedHost'>SoftLayer_Billing_Item_Virtual_DedicatedHost </a>**


</div>
<div class="prop-row">

-----
[datacenter]: #datacenter
#### [datacenter]
The datacenter that the dedicated host resides in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[guests]: #guests
#### [guests]
The guests associated with the dedicated host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[internalTagReferences]: #internaltagreferences
#### [internalTagReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**


</div>
<div class="prop-row">

-----
[pciDeviceAllocationStatus]: #pcideviceallocationstatus
#### [pciDeviceAllocationStatus]
The container that represents PCI device allocations on the dedicated host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus'>SoftLayer_Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus </a>**


</div>
<div class="prop-row">

-----
[pciDevices]: #pcidevices
#### [pciDevices]
A collection of SoftLayer_Virtual_Host_PciDevice objects on the host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Host_PciDevice'>SoftLayer_Virtual_Host_PciDevice[] </a>**


</div>
<div class="prop-row">

-----
[tagReferences]: #tagreferences
#### [tagReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**


</div>

## Count
<div class="prop-row">

-----
[guestCount]: #guestcount
#### [guestCount]
A count of the guests associated with the dedicated host.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[internalTagReferenceCount]: #internaltagreferencecount
#### [internalTagReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[pciDeviceCount]: #pcidevicecount
#### [pciDeviceCount]
A count of a collection of SoftLayer_Virtual_Host_PciDevice objects on the host.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[tagReferenceCount]: #tagreferencecount
#### [tagReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


