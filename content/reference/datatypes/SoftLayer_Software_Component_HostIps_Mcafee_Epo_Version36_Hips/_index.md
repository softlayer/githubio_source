---
title: "SoftLayer_Software_Component_HostIps_Mcafee_Epo_Version36_Hips"
description: "The SoftLayer_Software_Component_HostIps_Mcafee_Epo_Version36_Hips data type represents a single McAfee Secure Host IPS... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_HostIps_Mcafee_Epo_Version36_Hips"
---

# SoftLayer_Software_Component_HostIps_Mcafee_Epo_Version36_Hips
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_Component_HostIps_Mcafee_Epo_Version36_Hips' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Software_Component_HostIps_Mcafee_Epo_Version36_Hips data type represents a single McAfee Secure Host IPS software component that uses the ePolicy Orchestrator version 3.6 backend. 





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
[epoVersion]: #epoversion
#### [epoVersion]
The version of ePolicy Orchestrator that the host IPS client communicates with.  
<span class="type-label">Type: </span>**string**

-----
[hardwareId]: #hardwareid
#### [hardwareId]
Hardware Identification Number for the server this Software Component is installed upon.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
An ID number identifying this Software Component (Software Installation)  
<span class="type-label">Type: </span>**integer**

-----
[manufacturerActivationCode]: #manufactureractivationcode
#### [manufacturerActivationCode]
The manufacturer code that is needed to activate a license.  
<span class="type-label">Type: </span>**string**

-----
[manufacturerLicenseInstance]: #manufacturerlicenseinstance
#### [manufacturerLicenseInstance]
A license key for this specific installation of software, if it is needed.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[agentDetails]: #agentdetails
#### [agentDetails]
The host IPS agent details.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Agent_Details**

-----
[applicationModePolicyNames]: #applicationmodepolicynames
#### [applicationModePolicyNames]
The names of the possible policy options for the application mode setting.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Policy_Object[]**

-----
[applicationRuleSetPolicyNames]: #applicationrulesetpolicynames
#### [applicationRuleSetPolicyNames]
The names of the possible policy options for the application rule set setting.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Policy_Object[]**

-----
[averageInstallationDuration]: #averageinstallationduration
#### [averageInstallationDuration]
The average amount of time that a software component takes to install.  
<span class="type-label">Type: </span>**unsigned long**

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a software component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[enforcementPolicyNames]: #enforcementpolicynames
#### [enforcementPolicyNames]
The names of the possible options for the enforcement policy setting.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Policy_Object[]**

-----
[firewallModePolicyNames]: #firewallmodepolicynames
#### [firewallModePolicyNames]
The names of the possible policy options for the firewall mode setting.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Policy_Object[]**

-----
[firewallRuleSetPolicyNames]: #firewallrulesetpolicynames
#### [firewallRuleSetPolicyNames]
The names of the possible policy options for the firewall rule set setting.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Policy_Object[]**

-----
[hardware]: #hardware
#### [hardware]
The hardware this Software Component is installed upon.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[ipsModePolicyNames]: #ipsmodepolicynames
#### [ipsModePolicyNames]
The names of the possible policy options for the host IPS mode setting.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Policy_Object[]**

-----
[ipsProtectionPolicyNames]: #ipsprotectionpolicynames
#### [ipsProtectionPolicyNames]
The names of the possible policy options for the host IPS protection setting.  
<span class="type-label">Type: </span>**McAfee_Epolicy_Orchestrator_Version36_Policy_Object[]**

-----
[passwordHistory]: #passwordhistory
#### [passwordHistory]
History Records for Software Passwords.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_Password_History'>SoftLayer_Software_Component_Password_History[] </a>**

-----
[passwords]: #passwords
#### [passwords]
Username/Password pairs used for access to this Software Installation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_Password'>SoftLayer_Software_Component_Password[] </a>**

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
The Software Description of this Software Component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**

-----
[softwareLicense]: #softwarelicense
#### [softwareLicense]
The License this Software Component uses.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_License'>SoftLayer_Software_License </a>**

-----
[transactionStatus]: #transactionstatus
#### [transactionStatus]
The current transaction status of a server.  
<span class="type-label">Type: </span>**string**

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
The virtual guest this software component is installed upon.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**


## Count

-----
[applicationModePolicyNameCount]: #applicationmodepolicynamecount
#### [applicationModePolicyNameCount]
A count of the names of the possible policy options for the application mode setting.   
<span class="type-label">Type: </span>**unsigned long**


-----
[applicationRuleSetPolicyNameCount]: #applicationrulesetpolicynamecount
#### [applicationRuleSetPolicyNameCount]
A count of the names of the possible policy options for the application rule set setting.   
<span class="type-label">Type: </span>**unsigned long**


-----
[enforcementPolicyNameCount]: #enforcementpolicynamecount
#### [enforcementPolicyNameCount]
A count of the names of the possible options for the enforcement policy setting.   
<span class="type-label">Type: </span>**unsigned long**


-----
[firewallModePolicyNameCount]: #firewallmodepolicynamecount
#### [firewallModePolicyNameCount]
A count of the names of the possible policy options for the firewall mode setting.   
<span class="type-label">Type: </span>**unsigned long**


-----
[firewallRuleSetPolicyNameCount]: #firewallrulesetpolicynamecount
#### [firewallRuleSetPolicyNameCount]
A count of the names of the possible policy options for the firewall rule set setting.   
<span class="type-label">Type: </span>**unsigned long**


-----
[ipsModePolicyNameCount]: #ipsmodepolicynamecount
#### [ipsModePolicyNameCount]
A count of the names of the possible policy options for the host IPS mode setting.   
<span class="type-label">Type: </span>**unsigned long**


-----
[ipsProtectionPolicyNameCount]: #ipsprotectionpolicynamecount
#### [ipsProtectionPolicyNameCount]
A count of the names of the possible policy options for the host IPS protection setting.   
<span class="type-label">Type: </span>**unsigned long**


-----
[passwordCount]: #passwordcount
#### [passwordCount]
A count of username/Password pairs used for access to this Software Installation.   
<span class="type-label">Type: </span>**unsigned long**


-----
[passwordHistoryCount]: #passwordhistorycount
#### [passwordHistoryCount]
A count of history Records for Software Passwords.   
<span class="type-label">Type: </span>**unsigned long**

</div>


