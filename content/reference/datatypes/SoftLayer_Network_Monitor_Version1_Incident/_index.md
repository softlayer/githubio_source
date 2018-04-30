---
title: "SoftLayer_Network_Monitor_Version1_Incident"
description: "The SoftLayer_Network_Monitor_Version1_Incident data type models a single virtual server or physical hardware network mo... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Incident"
---

# SoftLayer_Network_Monitor_Version1_Incident
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Incident' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Monitor_Version1_Incident data type models a single virtual server or physical hardware network monitoring event. SoftLayer_Network_Monitor_Version1_Incidents are created when the SoftLayer monitoring system detects a service down on your hardware of virtual server. As the incident is resolved it's status changes from "SERVICE FAILURE" to "COMPLETED". 


### associatedMethods

*  [SoftLayer_Hardware::getNetworkMonitorIncidents](/reference/services/SoftLayer_Hardware/getNetworkMonitorIncidents )
*  [SoftLayer_Hardware::getActiveNetworkMonitorIncident](/reference/services/SoftLayer_Hardware/getActiveNetworkMonitorIncident )
*  [SoftLayer_Hardware::getLatestNetworkMonitorIncident](/reference/services/SoftLayer_Hardware/getLatestNetworkMonitorIncident )
*  [SoftLayer_Virtual_Guest::getNetworkMonitorIncidents](/reference/services/SoftLayer_Virtual_Guest/getNetworkMonitorIncidents )
*  [SoftLayer_Virtual_Guest::getActiveNetworkMonitorIncident](/reference/services/SoftLayer_Virtual_Guest/getActiveNetworkMonitorIncident )
*  [SoftLayer_Virtual_Guest::getLatestNetworkMonitorIncident](/reference/services/SoftLayer_Virtual_Guest/getLatestNetworkMonitorIncident )





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
                <a href="#status" name=status>status</a>
            </span>
            <div class='views-field-body'>A network monitoring incident's status, either the string "SERVICE FAILURE" denoting an ongoing incident or "COMPLETE" meaning the incident has been resolved.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


