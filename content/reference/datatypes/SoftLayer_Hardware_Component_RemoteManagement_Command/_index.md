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
                <a href="#keyName" name=keyName>keyName</a>
            </span>
            <div class='views-field-body'>The name of the remote management command. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#requests" name=requests>requests</a>
            </span>
            <div class='views-field-body'>All requests issued for the remote management command. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request[] </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#requestCount" name=requestCount>requestCount</a>
            </span>
            <div class='views-field-body'>A count of all requests issued for the remote management command. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


