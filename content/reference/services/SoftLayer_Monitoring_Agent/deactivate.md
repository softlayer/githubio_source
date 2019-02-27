---
title: "deactivate"
description: "This method will deactivate the monitoring agent, preventing it from generating any further alarms."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent"
aliases:
    - "/reference/services/softlayer_monitoring_agent/deactivate"
---
# [SoftLayer_Monitoring_Agent](/reference/services/SoftLayer_Monitoring_Agent)::deactivate

Deactivates a monitoring agent.


## Overview 
This method will deactivate the monitoring agent, preventing it from generating any further alarms. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Monitoring_AgentInitParameters


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Monitoring_Agent::activate](/reference/services/SoftLayer_Monitoring_Agent/activate )
*  [SoftLayer_Monitoring_Agent::restart](/reference/services/SoftLayer_Monitoring_Agent/restart )



### Error Handling

* SoftLayer_Exception 

> Throws 'Access Denied. "Manage Server Monitoring" is required.' if the active user is an instance of SoftLayer_User_Customer and does not have the 'PRIV_MONITORING_MANAGE' permission and the monitoring agent is for a 'HARDWARE' device. 

* SoftLayer_Exception 

> Throws 'Access Denied. "Manage Server Monitoring" is required.' if the active user is an instance of SoftLayer_User_Customer and does not have the 'PRIV_MONITORING_MANAGE' permission and the monitoring agent is not for a 'HARDWARE' device. 

* SoftLayer_Exception 

> Throws '{monitoringAgentName} does not have an active billing item.' if the active user is an instance of SoftLayer_User_Customer and the hardware or virtual guest device does not have a 'monitoring_package' billing item. 

* SoftLayer_Exception 

> Throws 'Hardware "{monitoringAgent->hardware->fullyQualifiedDomainName}" has an active transaction #{$this->hardware->activeTransaction->id}' if this SoftLayer_Monitoring_Agent belongs to a SoftLayer_Hardware object and the SoftLayer_Hardware object has an active SoftLayer_Provisioning_Version1_Transaction. 

* SoftLayer_Exception 

> Throws 'Virtual Server "{virtualGuestFullyQualifiedDomainName}" has an active transaction 
#{$activeTransactionIdentifier}' if this SoftLayer_Monitoring_Agent belongs to a SoftLayer_Virtual_Guest and
there is a SoftLayer_Provisioning_Version1_Transaction with the same guestId as the SoftLayer_Virtual_Guest and a SoftLayer_Provisioning_Version1_Transaction_Status name that is not 'COMPLETE', 'CANCELLED', or 'FAILED'. 

* SoftLayer_Exception 

> Throws 'Your monitoring agent "{monitoringAgentName}" is inactive.' if this SoftLayer_Monitoring_Agent has a SoftLayer_Monitoring_Agent_Status with a status code other than 'ACTIVE'. 

* SoftLayer_Exception 

> Throws 'Failed to find a remote monitoring resource.' if the remote monitoring identifier is not found. 

* SoftLayer_Exception 

> Throws 'Monitoring agent cannot be found on a remote resource. Please contact development .' if the configuration deleted by the agent is not found. 

* SoftLayer_Exception 

> Throws 'Failed to delete configuration profile "{profileName}".' if an exception is caught while attempted to delete the configuration section. 

* SoftLayer_Exception 

> Throws 'No profile was found.' if no profile was found. 

* SoftLayer_Exception 

> Throws 'Failed to deactivate monitoring agent "{monitoringAgentName}".' if this SoftLayer_Monitoring_Agent has a SoftLayer_Monitoring_Agent_Status with a status code of 'ACTIVE' and does not have a robot and an error occurred while deactivating the monitoring agent. 

* SoftLayer_Exception_Public 

> Throws 'You cannot delete a profile in "{sectionName}" configuration section.' if the section has the disallowedDeletionFlag property set to true. 

* SoftLayer_Exception_Public 

> Throws 'All configuration profiles must be deleted in order to deactivate a remote monitoring agent.' if this SoftLayer_Monitoring_Agent has a SoftLayer_Monitoring_Agent_Status with a status code of 'ACTIVE', has a robot, the active user is an instance of SoftLayer_User_Customer, and this SoftLayer_Monitoring_Agent has 1 or more SoftLayer_Configuration_Template_Section_Profiles. 



