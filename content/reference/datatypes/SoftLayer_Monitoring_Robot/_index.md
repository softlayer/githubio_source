---
title: "SoftLayer_Monitoring_Robot"
description: "The SoftLayer_Monitoring_Robot data type contains general information relating to a monitoring robot."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Robot"
---

# SoftLayer_Monitoring_Robot
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Monitoring_Robot' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Monitoring_Robot' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Monitoring_Robot data type contains general information relating to a monitoring robot. 





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
[accountId]: #accountid
#### [accountId]
Internal identifier of a SoftLayer account that this robot belongs to  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Internal identifier of a monitoring robot  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Robot name  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
Internal identifier of a monitoring robot status  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account associated with the corresponding robot.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[robotStatus]: #robotstatus
#### [robotStatus]
The current status of the robot.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Robot_Status'>SoftLayer_Monitoring_Robot_Status </a>**


</div>
<div class="prop-row">

-----
[softwareComponent]: #softwarecomponent
#### [softwareComponent]
The SoftLayer_Software_Component that corresponds to the robot installation on the server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**


</div>

## Count
</div>


