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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#addToSparePoolAfterOsReload" name=addToSparePoolAfterOsReload>addToSparePoolAfterOsReload</a>
            </span>
            <div class='views-field-body'>A flag indicating that the server will be moved into the spare pool after an Operating system reload. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#customProvisionScriptUri" name=customProvisionScriptUri>customProvisionScriptUri</a>
            </span>
            <div class='views-field-body'>The customer provision uri will be used to download and execute a customer defined script on the host at the end of provisioning. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#driveRetentionFlag" name=driveRetentionFlag>driveRetentionFlag</a>
            </span>
            <div class='views-field-body'>A flag indicating that the primary drive will be converted to a portable storage volume during an Operating System reload. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#eraseHardDrives" name=eraseHardDrives>eraseHardDrives</a>
            </span>
            <div class='views-field-body'>A flag indicating that all data will be erased from drives during an Operating System reload. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardDrives" name=hardDrives>hardDrives</a>
            </span>
            <div class='views-field-body'>The hard drive partitions that a server can be partitioned with. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#imageTemplateId" name=imageTemplateId>imageTemplateId</a>
            </span>
            <div class='views-field-body'>An Image Template ID [[SoftLayer_Virtual_Guest_Block_Device_Template_Group]] that will be deployed to the host.  If provided no item prices are required. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemPrices" name=itemPrices>itemPrices</a>
            </span>
            <div class='views-field-body'>The item prices that a server can be configured with. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Price'>SoftLayer_Product_Item_Price[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lvmFlag" name=lvmFlag>lvmFlag</a>
            </span>
            <div class='views-field-body'>A flag indicating that the provision should use LVM for all logical drives. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resetIpmiPassword" name=resetIpmiPassword>resetIpmiPassword</a>
            </span>
            <div class='views-field-body'>A flag indicating that the remote management cards password will be reset. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#serviceToken" name=serviceToken>serviceToken</a>
            </span>
            <div class='views-field-body'>The token of the requesting service. Do not set. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sshKeyIds" name=sshKeyIds>sshKeyIds</a>
            </span>
            <div class='views-field-body'>IDs to SoftLayer_Security_Ssh_Key objects on the current account which will be added to the server for authentication. SSH Keys will not be added to servers with Microsoft Windows.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>array of integers</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#upgradeBios" name=upgradeBios>upgradeBios</a>
            </span>
            <div class='views-field-body'>A flag indicating that the BIOS will be updated when installing the operating system. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#upgradeHardDriveFirmware" name=upgradeHardDriveFirmware>upgradeHardDriveFirmware</a>
            </span>
            <div class='views-field-body'>A flag indicating that the firmware on all hard drives will be updated when installing the operating system. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
    </div>


