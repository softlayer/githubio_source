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

## Local
-----
[accountId]: #accountid
#### [accountId]
The dedicated host's associated account id.   
<span class="type-label">Type: </span>**integer**

-----
[cpuCount]: #cpucount
#### [cpuCount]
The capacity that the dedicated host's CPU allocation is restricted to.   
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The date that the dedicated host was created.   
<span class="type-label">Type: </span>**dateTime**

-----
[diskCapacity]: #diskcapacity
#### [diskCapacity]
The capacity that the dedicated host's disk allocation is restricted to.   
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
The dedicated host's associated unique id.   
<span class="type-label">Type: </span>**integer**

-----
[memoryCapacity]: #memorycapacity
#### [memoryCapacity]
The capacity that the dedicated host's memory allocation is restricted to.   
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that the dedicated host was last modified.   
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The dedicated host's name.   
<span class="type-label">Type: </span>**string**

-----
[notes]: #notes
#### [notes]
A note of up to 1,000 characters about a dedicated host.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that the dedicated host belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[allocationStatus]: #allocationstatus
#### [allocationStatus]
The container that represents allocations on the dedicated host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_DedicatedHost_AllocationStatus'>SoftLayer_Container_Virtual_DedicatedHost_AllocationStatus </a>**

-----
[backendRouter]: #backendrouter
#### [backendRouter]
The backend router behind dedicated host's pool of resources.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Router_Backend'>SoftLayer_Hardware_Router_Backend </a>**

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for the dedicated host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Virtual_DedicatedHost'>SoftLayer_Billing_Item_Virtual_DedicatedHost </a>**

-----
[datacenter]: #datacenter
#### [datacenter]
The datacenter that the dedicated host resides in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[guests]: #guests
#### [guests]
The guests associated with the dedicated host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[internalTagReferences]: #internaltagreferences
#### [internalTagReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**

-----
[pciDeviceAllocationStatus]: #pcideviceallocationstatus
#### [pciDeviceAllocationStatus]
The container that represents PCI device allocations on the dedicated host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus'>SoftLayer_Container_Virtual_DedicatedHost_Pci_Device_AllocationStatus </a>**

-----
[pciDevices]: #pcidevices
#### [pciDevices]
A collection of SoftLayer_Virtual_Host_PciDevice objects on the host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Host_PciDevice'>SoftLayer_Virtual_Host_PciDevice[] </a>**

-----
[tagReferences]: #tagreferences
#### [tagReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**


## Count

-----
[guestCount]: #guestcount
#### [guestCount]
A count of the guests associated with the dedicated host.   
<span class="type-label">Type: </span>**unsigned long**


-----
[internalTagReferenceCount]: #internaltagreferencecount
#### [internalTagReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[pciDeviceCount]: #pcidevicecount
#### [pciDeviceCount]
A count of a collection of SoftLayer_Virtual_Host_PciDevice objects on the host.   
<span class="type-label">Type: </span>**unsigned long**


-----
[tagReferenceCount]: #tagreferencecount
#### [tagReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


