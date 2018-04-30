---
title: "SoftLayer_Container_Network_Storage_Evault_Vault_Task"
description: "SoftLayer's StorageLayer Evault services provides details regarding the the purchased vault. 

When a job is created usi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_Storage_Evault_Vault_Task"
---

# SoftLayer_Container_Network_Storage_Evault_Vault_Task
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_Storage_Evault_Vault_Task' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer's StorageLayer Evault services provides details regarding the the purchased vault. 

When a job is created using the Webcc Console, the job created is identified as a task on the vault. Using this service, information regarding the task can be retrieved. 




### associatedMethods

*  [SoftLayer_Network_Storage_Backup_Evault::getBackupJobDetails](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getBackupJobDetails )
*  [SoftLayer_Network_Storage_Backup_Evault::getRestoreJobDetails](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getRestoreJobDetails )
*  [SoftLayer_Network_Storage_Backup_Evault::getAgentStatuses](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getAgentStatuses )



### seeAlso

* [SoftLayer_Network_Storage](/reference/services/SoftLayer_Network_Storage )




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
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Unique identifier for the task. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsigned integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>The hostname provided at time of agent registration. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#usedPoolsize" name=usedPoolsize>usedPoolsize</a>
            </span>
            <div class='views-field-body'>Total compressed bytes used for the task. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsigned long</p>
            </div>
        </div>
            </div>
    </div>


