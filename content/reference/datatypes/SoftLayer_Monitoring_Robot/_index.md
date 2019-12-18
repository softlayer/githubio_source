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

## Local
-----
[accountId]: #accountid
#### [accountId]
Internal identifier of a SoftLayer account that this robot belongs to  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
Internal identifier of a monitoring robot  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
Robot name  
<span class="type-label">Type: </span>**string**

-----
[statusId]: #statusid
#### [statusId]
Internal identifier of a monitoring robot status  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account associated with the corresponding robot.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[monitoringAgents]: #monitoringagents
#### [monitoringAgents]
The program (monitoring agent) that gets details of a system or application and reporting of the metric data and triggers alarms for predefined events.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Agent'>SoftLayer_Monitoring_Agent[] </a>**

-----
[robotStatus]: #robotstatus
#### [robotStatus]
The current status of the robot.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Robot_Status'>SoftLayer_Monitoring_Robot_Status </a>**

-----
[softwareComponent]: #softwarecomponent
#### [softwareComponent]
The SoftLayer_Software_Component that corresponds to the robot installation on the server.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**


## Count

-----
[monitoringAgentCount]: #monitoringagentcount
#### [monitoringAgentCount]
A count of the program (monitoring agent) that gets details of a system or application and reporting of the metric data and triggers alarms for predefined events.   
<span class="type-label">Type: </span>**unsigned long**

</div>


