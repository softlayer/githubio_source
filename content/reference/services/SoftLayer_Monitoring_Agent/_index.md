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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [activate](/reference/services/SoftLayer_Monitoring_Agent/activate)
Activates a monitoring agent

#### [addConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/addConfigurationProfile)
Creates a transaction that for adding additional monitoring configuration.

#### [applyConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/applyConfigurationValues)
Creates a transaction that applies monitoring configuration value changes to a monitoring agent's configuration for fixed sections. 

#### [deactivate](/reference/services/SoftLayer_Monitoring_Agent/deactivate)
Deactivates a monitoring agent.

#### [deleteConfigurationProfile](/reference/services/SoftLayer_Monitoring_Agent/deleteConfigurationProfile)
This method deletes a configuration profile from a monitoring agent.

#### [deployMonitoringAgent](/reference/services/SoftLayer_Monitoring_Agent/deployMonitoringAgent)
Initialize a monitoring agent and deploy it with the specified configuration template. 

#### [getActiveAlarmSubscribers](/reference/services/SoftLayer_Monitoring_Agent/getActiveAlarmSubscribers)
Retrieves all active users that are receiving alarm notifications.

#### [getAgentStatus](/reference/services/SoftLayer_Monitoring_Agent/getAgentStatus)
Retrieve the current status of the corresponding agent

#### [getAvailableConfigurationTemplates](/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationTemplates)
Returns available configuration templates for this monitoring agent.

#### [getAvailableConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/getAvailableConfigurationValues)
Returns an array of available configuration values that are specific to a server or a Virtual that this monitoring agent is running on. 

#### [getConfigurationProfiles](/reference/services/SoftLayer_Monitoring_Agent/getConfigurationProfiles)
Retrieve all custom configuration profiles associated with the corresponding agent

#### [getConfigurationTemplate](/reference/services/SoftLayer_Monitoring_Agent/getConfigurationTemplate)
Retrieve a template of an agent's current configuration which contains information about the structure of the configuration values.

#### [getConfigurationValues](/reference/services/SoftLayer_Monitoring_Agent/getConfigurationValues)
Retrieve the values associated with the corresponding Agent configuration.

#### [getEligibleAlarmSubscibers](/reference/services/SoftLayer_Monitoring_Agent/getEligibleAlarmSubscibers)
Returns all users that are eligible to receive alarm notifications.

#### [getGraph](/reference/services/SoftLayer_Monitoring_Agent/getGraph)
Retrieves a graph for configuration values within the date range.

#### [getGraphData](/reference/services/SoftLayer_Monitoring_Agent/getGraphData)
This method returns the metric data for each of the configuration values provided during the given time range.

#### [getHardware](/reference/services/SoftLayer_Monitoring_Agent/getHardware)
Retrieve softLayer hardware related to the agent.

#### [getObject](/reference/services/SoftLayer_Monitoring_Agent/getObject)
Retrieve a SoftLayer_Monitoring_Agent record.

#### [getProductItem](/reference/services/SoftLayer_Monitoring_Agent/getProductItem)
Retrieve contains general information relating to a single SoftLayer product.

#### [getSoftwareDescription](/reference/services/SoftLayer_Monitoring_Agent/getSoftwareDescription)
Retrieve a description for a specific installation of a Software Component

#### [getStatusName](/reference/services/SoftLayer_Monitoring_Agent/getStatusName)
Retrieve monitoring agent status name.

#### [getVirtualGuest](/reference/services/SoftLayer_Monitoring_Agent/getVirtualGuest)
Retrieve softlayer_Virtual_Guest object related to the monitoring agent, which this virtual guest object and hardware is on the server of the running agent.

#### [removeActiveAlarmSubscriber](/reference/services/SoftLayer_Monitoring_Agent/removeActiveAlarmSubscriber)
Removes the selected user from receiving the alarms for this monitoring agent. 

#### [removeAllAlarmSubscribers](/reference/services/SoftLayer_Monitoring_Agent/removeAllAlarmSubscribers)
Removes all users from receiving the alarms for this monitoring agent.

#### [restartMonitoringAgent](/reference/services/SoftLayer_Monitoring_Agent/restartMonitoringAgent)
This method restarts a monitoring agent.

#### [setActiveAlarmSubscriber](/reference/services/SoftLayer_Monitoring_Agent/setActiveAlarmSubscriber)
Subscribes a user to receive monitoring alarm alerts

</div>

