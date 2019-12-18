---
title: "SoftLayer_Container_Hardware_Server_Configuration"
description: "The SoftLayer_Container_Hardware_Server_Configuration data type contains information relating to a server's item price i... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Hardware_Server_Configuration"
---

# SoftLayer_Container_Hardware_Server_Configuration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Hardware_Server_Configuration data type contains information relating to a server's item price information, and hard drive partition information. 


### associatedMethods

*  [SoftLayer_Hardware::getObject](/reference/services/SoftLayer_Hardware/getObject )





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
[addToSparePoolAfterOsReload]: #addtosparepoolafterosreload
#### [addToSparePoolAfterOsReload]
A flag indicating that the server will be moved into the spare pool after an Operating system reload.  
<span class="type-label">Type: </span>**integer**

-----
[customProvisionScriptUri]: #customprovisionscripturi
#### [customProvisionScriptUri]
The customer provision uri will be used to download and execute a customer defined script on the host at the end of provisioning.  
<span class="type-label">Type: </span>**string**

-----
[driveRetentionFlag]: #driveretentionflag
#### [driveRetentionFlag]
A flag indicating that the primary drive will be converted to a portable storage volume during an Operating System reload.  
<span class="type-label">Type: </span>**boolean**

-----
[eraseHardDrives]: #eraseharddrives
#### [eraseHardDrives]
A flag indicating that all data will be erased from drives during an Operating System reload.  
<span class="type-label">Type: </span>**integer**

-----
[hardDrives]: #harddrives
#### [hardDrives]
The hard drive partitions that a server can be partitioned with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**

-----
[imageTemplateId]: #imagetemplateid
#### [imageTemplateId]
An Image Template ID [SoftLayer_Virtual_Guest_Block_Device_Template_Group]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group">}}) that will be deployed to the host.  If provided no item prices are required.  
<span class="type-label">Type: </span>**integer**

-----
[itemPrices]: #itemprices
#### [itemPrices]
The item prices that a server can be configured with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a>**

-----
[lvmFlag]: #lvmflag
#### [lvmFlag]
A flag indicating that the provision should use LVM for all logical drives.  
<span class="type-label">Type: </span>**integer**

-----
[resetIpmiPassword]: #resetipmipassword
#### [resetIpmiPassword]
A flag indicating that the remote management cards password will be reset.  
<span class="type-label">Type: </span>**integer**

-----
[serviceToken]: #servicetoken
#### [serviceToken]
The token of the requesting service. Do not set.  
<span class="type-label">Type: </span>**string**

-----
[sshKeyIds]: #sshkeyids
#### [sshKeyIds]
IDs to SoftLayer_Security_Ssh_Key objects on the current account which will be added to the server for authentication. SSH Keys will not be added to servers with Microsoft Windows.   
<span class="type-label">Type: </span>**array of integers**

-----
[upgradeBios]: #upgradebios
#### [upgradeBios]
A flag indicating that the BIOS will be updated when installing the operating system.  
<span class="type-label">Type: </span>**integer**

-----
[upgradeHardDriveFirmware]: #upgradeharddrivefirmware
#### [upgradeHardDriveFirmware]
A flag indicating that the firmware on all hard drives will be updated when installing the operating system.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

</div>


