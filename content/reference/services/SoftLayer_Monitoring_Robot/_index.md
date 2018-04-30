---
title: "SoftLayer_Monitoring_Robot"
description: "A monitoring robot is a set of essential agents that lets SoftLayer monitoring management system to communicate with a s... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
A monitoring robot is a set of essential agents that lets SoftLayer monitoring management system to communicate with a server, a Cloud Computing Instance or a Bare Metal Instance. 

A monitoring robot must be installed in order for any monitoring agent to report monitoring data to a SoftLayer monitoring hub system. 

TCP ports from 48000 to 48020 should be open on your server or cloud instance for advanced monitoring robots and agents. 



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Robot/checkConnection'> checkConnection</a> </span>
            <div class='views-field-body'>Checks if a monitoring robot can communicate with SoftLayer monitoring management system </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Robot/deployMonitoringAgents'> deployMonitoringAgents</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Robot/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account associated with the corresponding robot.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Robot/getAvailableConfigurationGroups'> getAvailableConfigurationGroups</a> </span>
            <div class='views-field-body'>Returns available configuration template groups for this monitoring agent.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Robot/getMonitoringAgents'> getMonitoringAgents</a> </span>
            <div class='views-field-body'>Retrieve the program (monitoring agent) that gets details of a system or application and reporting of the metric data and triggers alarms for predefined events.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Robot/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Monitoring_Robot record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Robot/getRobotStatus'> getRobotStatus</a> </span>
            <div class='views-field-body'>Retrieve the current status of the robot.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Robot/getSoftwareComponent'> getSoftwareComponent</a> </span>
            <div class='views-field-body'>Retrieve the SoftLayer_Software_Component that corresponds to the robot installation on the server.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Robot/resetStatus'> resetStatus</a> </span>
            <div class='views-field-body'>Resets monitoring robot status to "Active"</div>
        </div>
        </div>
</div>

