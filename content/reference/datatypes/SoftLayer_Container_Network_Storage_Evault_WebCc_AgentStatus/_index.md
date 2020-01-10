---
title: "SoftLayer_Container_Network_Storage_Evault_WebCc_AgentStatus"
description: "The SoftLayer_Container_Network_Storage_Evault_WebCc_AgentStatus will contain the timestamp of the last backup performed... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_Storage_Evault_WebCc_AgentStatus"
---

# SoftLayer_Container_Network_Storage_Evault_WebCc_AgentStatus
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_Storage_Evault_WebCc_AgentStatus' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Network_Storage_Evault_WebCc_AgentStatus will contain the timestamp of the last backup performed by the EVault agent.  The agent status will also be returned. 


### associatedMethods

*  [SoftLayer_Network_Storage_Backup_Evault::getBackupJobDetails](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getBackupJobDetails )
*  [SoftLayer_Network_Storage_Backup_Evault::getRestoreJobDetails](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getRestoreJobDetails )
*  [SoftLayer_Network_Storage_Backup_Evault::getTasks](/reference/services/SoftLayer_Network_Storage_Backup_Evault/getTasks )





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
[lastBackup]: #lastbackup
#### [lastBackup]
Timestamp of last backup performed by the EVault backup agent  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
Status indicating the accumulative status result of all jobs performed by the evault agent.  For example, if one job out three jobs failed agent status will by "Failed Backup(s)".   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


