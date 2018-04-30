---
title: "SoftLayer_Monitoring_Agent"
description: "A monitoring agent is a program that resides on a server and does the work of getting details of a system or application... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
---
# SoftLayer_Monitoring_Agent
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Monitoring_Agent' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Monitoring_Agent' >Datatype</a></li>
    </ul>
</div>

## Description
A monitoring agent is a program that resides on a server and does the work of getting details of a system or application and reporting of the metric data and triggers alarms for predefined events. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/activate'> activate</a> </span>
            <div class='views-field-body'>Activates a monitoring agent</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile'> addConfigurationProfile</a> </span>
            <div class='views-field-body'>Creates a transaction that for adding additional monitoring configuration.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues'> applyConfigurationValues</a> </span>
            <div class='views-field-body'>Creates a transaction that applies monitoring configuration value changes to a monitoring agent's configuration for fixed sections. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/deactivate'> deactivate</a> </span>
            <div class='views-field-body'>Deactivates a monitoring agent.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/deleteConfigurationProfile'> deleteConfigurationProfile</a> </span>
            <div class='views-field-body'>This method deletes a configuration profile from a monitoring agent.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/deployMonitoringAgent'> deployMonitoringAgent</a> </span>
            <div class='views-field-body'>Initialize a monitoring agent and deploy it with the specified configuration template. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getActiveAlarmSubscribers'> getActiveAlarmSubscribers</a> </span>
            <div class='views-field-body'>Retrieves all active users that are receiving alarm notifications.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getAgentStatus'> getAgentStatus</a> </span>
            <div class='views-field-body'>Retrieve the current status of the corresponding agent</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationTemplates'> getAvailableConfigurationTemplates</a> </span>
            <div class='views-field-body'>Returns available configuration templates for this monitoring agent.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationValues'> getAvailableConfigurationValues</a> </span>
            <div class='views-field-body'>Returns an array of available configuration values that are specific to a server or a Virtual that this monitoring agent is running on. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getConfigurationProfiles'> getConfigurationProfiles</a> </span>
            <div class='views-field-body'>Retrieve all custom configuration profiles associated with the corresponding agent</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getConfigurationTemplate'> getConfigurationTemplate</a> </span>
            <div class='views-field-body'>Retrieve a template of an agent's current configuration which contains information about the structure of the configuration values.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getConfigurationValues'> getConfigurationValues</a> </span>
            <div class='views-field-body'>Retrieve the values associated with the corresponding Agent configuration.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getEligibleAlarmSubscibers'> getEligibleAlarmSubscibers</a> </span>
            <div class='views-field-body'>Returns all users that are eligible to receive alarm notifications.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getGraph'> getGraph</a> </span>
            <div class='views-field-body'>Retrieves a graph for configuration values within the date range.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getGraphData'> getGraphData</a> </span>
            <div class='views-field-body'>This method returns the metric data for each of the configuration values provided during the given time range.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getHardware'> getHardware</a> </span>
            <div class='views-field-body'>Retrieve softLayer hardware related to the agent.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Monitoring_Agent record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getProductItem'> getProductItem</a> </span>
            <div class='views-field-body'>Retrieve contains general information relating to a single SoftLayer product.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getSoftwareDescription'> getSoftwareDescription</a> </span>
            <div class='views-field-body'>Retrieve a description for a specific installation of a Software Component</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getStatusName'> getStatusName</a> </span>
            <div class='views-field-body'>Retrieve monitoring agent status name.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/getVirtualGuest'> getVirtualGuest</a> </span>
            <div class='views-field-body'>Retrieve softlayer_Virtual_Guest object related to the monitoring agent, which this virtual guest object and hardware is on the server of the running agent.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/removeActiveAlarmSubscriber'> removeActiveAlarmSubscriber</a> </span>
            <div class='views-field-body'>Removes the selected user from receiving the alarms for this monitoring agent. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/removeAllAlarmSubscribers'> removeAllAlarmSubscribers</a> </span>
            <div class='views-field-body'>Removes all users from receiving the alarms for this monitoring agent.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/restartMonitoringAgent'> restartMonitoringAgent</a> </span>
            <div class='views-field-body'>This method restarts a monitoring agent.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Monitoring_Agent/setActiveAlarmSubscriber'> setActiveAlarmSubscriber</a> </span>
            <div class='views-field-body'>Subscribes a user to receive monitoring alarm alerts</div>
        </div>
        </div>
</div>

