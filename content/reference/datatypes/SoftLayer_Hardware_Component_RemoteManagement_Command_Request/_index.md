---
title: "SoftLayer_Hardware_Component_RemoteManagement_Command_Request"
description: "The SoftLayer_Hardware_Component_RemoteManagement_Command_Request contains details for remote management commands issued... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_RemoteManagement_Command_Request"
---

# SoftLayer_Hardware_Component_RemoteManagement_Command_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_RemoteManagement_Command_Request contains details for remote management commands issued to a server's remote management card.  Details for remote management commands such as powerOn, powerOff, powerCycle, rebootDefault, rebootSoft, rebootHard can be retrieved.  Details such as the user who issued the command, the id of the remote management card the command was issued, when the command was issued may be retrieved. 





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
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The timestamp the remote management command was issued. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareId" name=hardwareId>hardwareId</a>
            </span>
            <div class='views-field-body'>The hardware id the command was issued for. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The timestamp recorded when the remote management command returned a status of the command issued. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#processed" name=processed>processed</a>
            </span>
            <div class='views-field-body'>Execution status of the remote management command.  True is successful.  False is failure. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardware" name=hardware>hardware</a>
            </span>
            <div class='views-field-body'>The id of the hardware to perform the remote management or powerstrip command on. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#networkComponent" name=networkComponent>networkComponent</a>
            </span>
            <div class='views-field-body'>A hardware's network components. Network components are hardware components such as IPMI cards or Ethernet cards. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#remoteManagementCommand" name=remoteManagementCommand>remoteManagementCommand</a>
            </span>
            <div class='views-field-body'>The remote management command issued. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command'>SoftLayer_Hardware_Component_RemoteManagement_Command </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#user" name=user>user</a>
            </span>
            <div class='views-field-body'>Information regarding the user who issued the remote management command. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


