---
title: "SoftLayer_Security_Ssh_Key"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Ssh_Key"
---

# SoftLayer_Security_Ssh_Key
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Security_Ssh_Key' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Security_Ssh_Key' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[createDate]: #createdate
#### [createDate]
The date a ssh key was added. 

This property is read only. Changes made will be silently ignored.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[fingerprint]: #fingerprint
#### [fingerprint]
A short sequence of bytes used to authenticate or lookup a longer ssh key. This will automatically be generated upon adding or modifying the ssh key. 

This property is read only. Changes made will be silently ignored.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The ID of the ssh key record.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[key]: #key
#### [key]
The ssh key.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[label]: #label
#### [label]
A descriptive name used to identify a ssh key.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a ssh key was last modified. 

This property is read only. Changes made will be silently ignored.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
A small note about a ssh key to use at your discretion.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[blockDeviceTemplateGroups]: #blockdevicetemplategroups
#### [blockDeviceTemplateGroups]
The image template groups that are linked to an SSH key.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group[] </a>**


</div>
<div class="prop-row">

-----
[softwarePasswords]: #softwarepasswords
#### [softwarePasswords]
The OS root users that are linked to an SSH key.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_Password'>SoftLayer_Software_Component_Password[] </a>**


</div>

## Count
<div class="prop-row">

-----
[blockDeviceTemplateGroupCount]: #blockdevicetemplategroupcount
#### [blockDeviceTemplateGroupCount]
A count of the image template groups that are linked to an SSH key.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[softwarePasswordCount]: #softwarepasswordcount
#### [softwarePasswordCount]
A count of the OS root users that are linked to an SSH key.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


