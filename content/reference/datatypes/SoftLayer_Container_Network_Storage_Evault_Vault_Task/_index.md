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
[id]: #id
#### [id]
Unique identifier for the task.  
<span class="type-label">Type: </span>**unsigned integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The hostname provided at time of agent registration.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[usedPoolsize]: #usedpoolsize
#### [usedPoolsize]
Total compressed bytes used for the task.  
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


