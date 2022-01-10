---
title: "SoftLayer_Hardware_Component_SecurityDevice"
description: "The SoftLayer_Hardware_Component_SecurityDevice is used to determine the security devices attached to the hardware compo... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_SecurityDevice"
---

# SoftLayer_Hardware_Component_SecurityDevice
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_SecurityDevice' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Hardware_Component_SecurityDevice is used to determine the security devices attached to the hardware component. 





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
[hardwareComponentModelId]: #hardwarecomponentmodelid
#### [hardwareComponentModelId]
The internal identifier of a hardware component's component model.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The internal identifier of the hardware that a hardware component resides inside.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A hardware component's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that a hardware component was last modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of this component as referenced by the operating system.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serialNumber]: #serialnumber
#### [serialNumber]
The component serial number.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
A hardware's internal identification number at its service provider  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[capacity]: #capacity
#### [capacity]
A component's capacity.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[children]: #children
#### [children]
A components sub components. Devices that are usually integrated or in some way attached to a component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**  



</div>
<div class="prop-row">

-----
[componentRevision]: #componentrevision
#### [componentRevision]
A component's Revision.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[downlinkHardwareComponents]: #downlinkhardwarecomponents
#### [downlinkHardwareComponents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**  



</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware object that this component belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[hardwareComponentModel]: #hardwarecomponentmodel
#### [hardwareComponentModel]
The general group of component models.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model </a>**  



</div>
<div class="prop-row">

-----
[hardwareComponentType]: #hardwarecomponenttype
#### [hardwareComponentType]
A components type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Type'>SoftLayer_Hardware_Component_Type </a>**  



</div>
<div class="prop-row">

-----
[isChildModule]: #ischildmodule
#### [isChildModule]
  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[logicalVolumeStorageGroups]: #logicalvolumestoragegroups
#### [logicalVolumeStorageGroups]
Returns the associated logic volume storage groups for the hardware component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group'>SoftLayer_Configuration_Storage_Group[] </a>**  



</div>
<div class="prop-row">

-----
[m2SataSlotCapacity]: #m2sataslotcapacity
#### [m2SataSlotCapacity]
A component's M.2 SATA capacity.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[moduleComponents]: #modulecomponents
#### [moduleComponents]
The module's hardware components  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**  



</div>
<div class="prop-row">

-----
[moduleHardwareComponents]: #modulehardwarecomponents
#### [moduleHardwareComponents]
The module's hardware components  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**  



</div>
<div class="prop-row">

-----
[moduleNetworkComponents]: #modulenetworkcomponents
#### [moduleNetworkComponents]
The module's network components  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**  



</div>
<div class="prop-row">

-----
[modules]: #modules
#### [modules]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**  



</div>
<div class="prop-row">

-----
[networkComponents]: #networkcomponents
#### [networkComponents]
The components local ethernet and remote management interfaces  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**  



</div>
<div class="prop-row">

-----
[owner]: #owner
#### [owner]
The account this component belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[parent]: #parent
#### [parent]
A components parent. Devices that are usually integrated or in some way attached to a component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a>**  



</div>
<div class="prop-row">

-----
[parentModule]: #parentmodule
#### [parentModule]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a>**  



</div>
<div class="prop-row">

-----
[prefixAttribute]: #prefixattribute
#### [prefixAttribute]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic_Attribute'>SoftLayer_Hardware_Component_Model_Generic_Attribute </a>**  



</div>
<div class="prop-row">

-----
[raidMode]: #raidmode
#### [raidMode]
A RAID controllers RAID mode.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[revision]: #revision
#### [revision]
The component revision designation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Revision'>SoftLayer_Hardware_Component_Revision </a>**  



</div>
<div class="prop-row">

-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**  



</div>
<div class="prop-row">

-----
[uplinkHardwareComponents]: #uplinkhardwarecomponents
#### [uplinkHardwareComponents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[childrenCount]: #childrencount
#### [childrenCount]
A count of a components sub components. Devices that are usually integrated or in some way attached to a component.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[downlinkHardwareComponentCount]: #downlinkhardwarecomponentcount
#### [downlinkHardwareComponentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[logicalVolumeStorageGroupCount]: #logicalvolumestoragegroupcount
#### [logicalVolumeStorageGroupCount]
A count of returns the associated logic volume storage groups for the hardware component.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[moduleComponentCount]: #modulecomponentcount
#### [moduleComponentCount]
A count of the module's hardware components   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[moduleCount]: #modulecount
#### [moduleCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[moduleHardwareComponentCount]: #modulehardwarecomponentcount
#### [moduleHardwareComponentCount]
A count of the module's hardware components   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[moduleNetworkComponentCount]: #modulenetworkcomponentcount
#### [moduleNetworkComponentCount]
A count of the module's network components   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[networkComponentCount]: #networkcomponentcount
#### [networkComponentCount]
A count of the components local ethernet and remote management interfaces   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[uplinkHardwareComponentCount]: #uplinkhardwarecomponentcount
#### [uplinkHardwareComponentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


