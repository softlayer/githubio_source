---
title: "SoftLayer_Virtual_Host_PciDevice"
description: "This type represents a PCI device on a host."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Host_PciDevice"
---

# SoftLayer_Virtual_Host_PciDevice
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Host_PciDevice' >Datatype</a></li>
    </ul>
</div>

## Description 
This type represents a PCI device on a host. 





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
[id]: #id
#### [id]
ID of the PCI device.   
<span class="type-label">Type: </span>**integer**

-----
[uuid]: #uuid
#### [uuid]
The unique id of the PCI device's record on a virtualization platform.   
<span class="type-label">Type: </span>**string**

-----
[xenPciId]: #xenpciid
#### [xenPciId]
The BDF (Domain:Bus:Device.Function) id of the PCI device in XenServer.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[hardwareComponentModel]: #hardwarecomponentmodel
#### [hardwareComponentModel]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model </a>**

-----
[host]: #host
#### [host]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Host'>SoftLayer_Virtual_Host </a>**


## Count
</div>


