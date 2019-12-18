---
title: "SoftLayer_Container_Monitoring_Alarm_History"
description: "The SoftLayer_Container_Monitoring_Alarm_History data type contains information relating to SoftLayer monitoring alarm h... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Monitoring_Alarm_History"
---

# SoftLayer_Container_Monitoring_Alarm_History
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Monitoring_Alarm_History' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Monitoring_Alarm_History data type contains information relating to SoftLayer monitoring alarm history. 


### associatedMethods

*  [SoftLayer_Hardware::getMonitoringAlarmHistory](/reference/services/SoftLayer_Hardware/getMonitoringAlarmHistory )
*  [SoftLayer_Virtual_Guest::getMonitoringAlarmHistory](/reference/services/SoftLayer_Virtual_Guest/getMonitoringAlarmHistory )





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
Account ID that this alarm belongs to  
<span class="type-label">Type: </span>**integer**

-----
[agentId]: #agentid
#### [agentId]
ID of the monitoring agent that triggered this alarm  
<span class="type-label">Type: </span>**integer**

-----
[alarmId]: #alarmid
#### [alarmId]
Alarm ID  
<span class="type-label">Type: </span>**string**

-----
[closedDate]: #closeddate
#### [closedDate]
Time that an alarm was closed.  
<span class="type-label">Type: </span>**dateTime**

-----
[createDate]: #createdate
#### [createDate]
Time that an alarm was triggered  
<span class="type-label">Type: </span>**dateTime**

-----
[message]: #message
#### [message]
Alarm message  
<span class="type-label">Type: </span>**string**

-----
[robotId]: #robotid
#### [robotId]
Robot ID  
<span class="type-label">Type: </span>**integer**

-----
[severity]: #severity
#### [severity]
Severity of an alarm  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


