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



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [activate](/reference/services/SoftLayer_Monitoring_Agent/activate)
Activates a monitoring agent
</div>

<div class="method-row">

#### [addConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile)
Creates a transaction that for adding additional monitoring configuration.
</div>

<div class="method-row">

#### [applyConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues)
Creates a transaction that applies monitoring configuration value changes to a monitoring agent's configuration for fixed sections. 
</div>

<div class="method-row">

#### [deactivate](/reference/services/SoftLayer_Monitoring_Agent/deactivate)
Deactivates a monitoring agent.
</div>

<div class="method-row">

#### [deleteConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/deleteConfigurationProfile)
This method deletes a configuration profile from a monitoring agent.
</div>

<div class="method-row">

#### [deployMonitoringAgent](/reference/services/SoftLayer_Monitoring_Agent/deployMonitoringAgent)
Initialize a monitoring agent and deploy it with the specified configuration template. 
</div>

<div class="method-row">

#### [getActiveAlarmSubscribers](/reference/services/SoftLayer_Monitoring_Agent/getActiveAlarmSubscribers)
Retrieves all active users that are receiving alarm notifications.
</div>

<div class="method-row">

#### [getAgentStatus](/reference/services/SoftLayer_Monitoring_Agent/getAgentStatus)
Retrieve the current status of the corresponding agent
</div>

<div class="method-row">

#### [getAvailableConfigurationTemplates](/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationTemplates)
Returns available configuration templates for this monitoring agent.
</div>

<div class="method-row">

#### [getAvailableConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationValues)
Returns an array of available configuration values that are specific to a server or a Virtual that this monitoring agent is running on. 
</div>

<div class="method-row">

#### [getConfigurationProfiles](/reference/services/SoftLayer_Monitoring_Agent/getConfigurationProfiles)
Retrieve all custom configuration profiles associated with the corresponding agent
</div>

<div class="method-row">

#### [getConfigurationTemplate](/reference/services/SoftLayer_Monitoring_Agent/getConfigurationTemplate)
Retrieve a template of an agent's current configuration which contains information about the structure of the configuration values.
</div>

<div class="method-row">

#### [getConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/getConfigurationValues)
Retrieve the values associated with the corresponding Agent configuration.
</div>

<div class="method-row">

#### [getEligibleAlarmSubscibers](/reference/services/SoftLayer_Monitoring_Agent/getEligibleAlarmSubscibers)
Returns all users that are eligible to receive alarm notifications.
</div>

<div class="method-row">

#### [getGraph](/reference/services/SoftLayer_Monitoring_Agent/getGraph)
Retrieves a graph for configuration values within the date range.
</div>

<div class="method-row">

#### [getGraphData](/reference/services/SoftLayer_Monitoring_Agent/getGraphData)
This method returns the metric data for each of the configuration values provided during the given time range.
</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Monitoring_Agent/getHardware)
Retrieve softLayer hardware related to the agent.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Monitoring_Agent/getObject)
Retrieve a SoftLayer_Monitoring_Agent record.
</div>

<div class="method-row">

#### [getProductItem](/reference/services/SoftLayer_Monitoring_Agent/getProductItem)
Retrieve contains general information relating to a single SoftLayer product.
</div>

<div class="method-row">

#### [getSoftwareDescription](/reference/services/SoftLayer_Monitoring_Agent/getSoftwareDescription)
Retrieve a description for a specific installation of a Software Component
</div>

<div class="method-row">

#### [getStatusName](/reference/services/SoftLayer_Monitoring_Agent/getStatusName)
Retrieve monitoring agent status name.
</div>

<div class="method-row">

#### [getVirtualGuest](/reference/services/SoftLayer_Monitoring_Agent/getVirtualGuest)
Retrieve softlayer_Virtual_Guest object related to the monitoring agent, which this virtual guest object and hardware is on the server of the running agent.
</div>

<div class="method-row">

#### [removeActiveAlarmSubscriber](/reference/services/SoftLayer_Monitoring_Agent/removeActiveAlarmSubscriber)
Removes the selected user from receiving the alarms for this monitoring agent. 
</div>

<div class="method-row">

#### [removeAllAlarmSubscribers](/reference/services/SoftLayer_Monitoring_Agent/removeAllAlarmSubscribers)
Removes all users from receiving the alarms for this monitoring agent.
</div>

<div class="method-row">

#### [restartMonitoringAgent](/reference/services/SoftLayer_Monitoring_Agent/restartMonitoringAgent)
This method restarts a monitoring agent.
</div>

<div class="method-row">

#### [setActiveAlarmSubscriber](/reference/services/SoftLayer_Monitoring_Agent/setActiveAlarmSubscriber)
Subscribes a user to receive monitoring alarm alerts
</div>
</div>

</div>

