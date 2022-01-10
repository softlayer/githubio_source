---
title: "SoftLayer_Hardware_Component_RemoteManagement_Command"
description: "The SoftLayer_Network_Storage_Evault_Version6 contains the names of the remote management commands.  Currently, only the... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_RemoteManagement_Command"
---

# SoftLayer_Hardware_Component_RemoteManagement_Command
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Storage_Evault_Version6 contains the names of the remote management commands.  Currently, only the reboot and power commands for the remote management card exist. 





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
[keyName]: #keyname
#### [keyName]
The name of the remote management command.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[requests]: #requests
#### [requests]
All requests issued for the remote management command.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[requestCount]: #requestcount
#### [requestCount]
A count of all requests issued for the remote management command.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


