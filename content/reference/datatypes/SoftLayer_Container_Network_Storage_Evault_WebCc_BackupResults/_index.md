---
title: "SoftLayer_Container_Network_Storage_Evault_WebCc_BackupResults"
description: "The SoftLayer_Container_Network_Storage_Evault_WebCc_BackupResults will contain the timeframe of backups and the results... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_Storage_Evault_WebCc_BackupResults"
---

# SoftLayer_Container_Network_Storage_Evault_WebCc_BackupResults
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_Storage_Evault_WebCc_BackupResults' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Network_Storage_Evault_WebCc_BackupResults will contain the timeframe of backups and the results will also be returned. 


### associatedMethods

*  [SoftLayer_Account::getCurrentBackupData](/reference/services/SoftLayer_Account/getCurrentBackupData )





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
[beginTime]: #begintime
#### [beginTime]
Timestamp of begin time  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[conflict]: #conflict
#### [conflict]
Count of backups with conflicts.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[endTime]: #endtime
#### [endTime]
Timestamp of end time  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[failed]: #failed
#### [failed]
Count of failed backups.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[success]: #success
#### [success]
Count of successfull backups.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


