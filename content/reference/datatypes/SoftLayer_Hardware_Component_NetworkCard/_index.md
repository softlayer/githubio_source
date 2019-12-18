---
title: "SoftLayer_Hardware_Component_NetworkCard"
description: "The SoftLayer_Hardware_Component_NetworkCard data type abstracts information related to a network card."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_NetworkCard"
---

# SoftLayer_Hardware_Component_NetworkCard
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_NetworkCard' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_NetworkCard data type abstracts information related to a network card. 





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
[hardwareComponentModelId]: #hardwarecomponentmodelid
#### [hardwareComponentModelId]
The internal identifier of a hardware component's component model.  
<span class="type-label">Type: </span>**integer**

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The internal identifier of the hardware that a hardware component resides inside.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A hardware component's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date that a hardware component was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The name of this component as referenced by the operating system.  
<span class="type-label">Type: </span>**string**

-----
[serialNumber]: #serialnumber
#### [serialNumber]
The component serial number.  
<span class="type-label">Type: </span>**string**

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
A hardware's internal identification number at its service provider  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[capacity]: #capacity
#### [capacity]
A component's capacity.  
<span class="type-label">Type: </span>**decimal**

-----
[children]: #children
#### [children]
A components sub components. Devices that are usually integrated or in some way attached to a component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[componentRevision]: #componentrevision
#### [componentRevision]
A component's Revision.  
<span class="type-label">Type: </span>**string**

-----
[downlinkHardwareComponents]: #downlinkhardwarecomponents
#### [downlinkHardwareComponents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[hardware]: #hardware
#### [hardware]
The hardware object that this component belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[hardwareComponentModel]: #hardwarecomponentmodel
#### [hardwareComponentModel]
The general group of component models.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model </a>**

-----
[hardwareComponentType]: #hardwarecomponenttype
#### [hardwareComponentType]
A components type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Type'>SoftLayer_Hardware_Component_Type </a>**

-----
[isChildModule]: #ischildmodule
#### [isChildModule]
  
<span class="type-label">Type: </span>**boolean**

-----
[m2SataSlotCapacity]: #m2sataslotcapacity
#### [m2SataSlotCapacity]
A component's M.2 SATA capacity.  
<span class="type-label">Type: </span>**string**

-----
[moduleComponents]: #modulecomponents
#### [moduleComponents]
The module's hardware components  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[moduleHardwareComponents]: #modulehardwarecomponents
#### [moduleHardwareComponents]
The module's hardware components  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[moduleNetworkComponents]: #modulenetworkcomponents
#### [moduleNetworkComponents]
The module's network components  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[modules]: #modules
#### [modules]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[networkComponents]: #networkcomponents
#### [networkComponents]
The components local ethernet and remote management interfaces  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a>**

-----
[owner]: #owner
#### [owner]
The account this component belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[parent]: #parent
#### [parent]
A components parent. Devices that are usually integrated or in some way attached to a component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a>**

-----
[parentModule]: #parentmodule
#### [parentModule]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a>**

-----
[prefixAttribute]: #prefixattribute
#### [prefixAttribute]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic_Attribute'>SoftLayer_Hardware_Component_Model_Generic_Attribute </a>**

-----
[raidMode]: #raidmode
#### [raidMode]
A RAID controllers RAID mode.  
<span class="type-label">Type: </span>**string**

-----
[revision]: #revision
#### [revision]
The component revision designation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Revision'>SoftLayer_Hardware_Component_Revision </a>**

-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**

-----
[uplinkHardwareComponents]: #uplinkhardwarecomponents
#### [uplinkHardwareComponents]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


## Count

-----
[childrenCount]: #childrencount
#### [childrenCount]
A count of a components sub components. Devices that are usually integrated or in some way attached to a component.   
<span class="type-label">Type: </span>**unsigned long**


-----
[downlinkHardwareComponentCount]: #downlinkhardwarecomponentcount
#### [downlinkHardwareComponentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[moduleComponentCount]: #modulecomponentcount
#### [moduleComponentCount]
A count of the module's hardware components   
<span class="type-label">Type: </span>**unsigned long**


-----
[moduleCount]: #modulecount
#### [moduleCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[moduleHardwareComponentCount]: #modulehardwarecomponentcount
#### [moduleHardwareComponentCount]
A count of the module's hardware components   
<span class="type-label">Type: </span>**unsigned long**


-----
[moduleNetworkComponentCount]: #modulenetworkcomponentcount
#### [moduleNetworkComponentCount]
A count of the module's network components   
<span class="type-label">Type: </span>**unsigned long**


-----
[networkComponentCount]: #networkcomponentcount
#### [networkComponentCount]
A count of the components local ethernet and remote management interfaces   
<span class="type-label">Type: </span>**unsigned long**


-----
[uplinkHardwareComponentCount]: #uplinkhardwarecomponentcount
#### [uplinkHardwareComponentCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


