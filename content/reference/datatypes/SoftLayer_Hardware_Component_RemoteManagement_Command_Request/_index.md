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
The timestamp the remote management command was issued.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The hardware id the command was issued for.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The timestamp recorded when the remote management command returned a status of the command issued.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[processed]: #processed
#### [processed]
Execution status of the remote management command.  True is successful.  False is failure.  
<span class="type-label">Type: </span>**boolean**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The id of the hardware to perform the remote management or powerstrip command on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[networkComponent]: #networkcomponent
#### [networkComponent]
A hardware's network components. Network components are hardware components such as IPMI cards or Ethernet cards.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**  



</div>
<div class="prop-row">

-----
[remoteManagementCommand]: #remotemanagementcommand
#### [remoteManagementCommand]
The remote management command issued.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command'>SoftLayer_Hardware_Component_RemoteManagement_Command </a>**  



</div>
<div class="prop-row">

-----
[user]: #user
#### [user]
Information regarding the user who issued the remote management command.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>

## Count
</div>


