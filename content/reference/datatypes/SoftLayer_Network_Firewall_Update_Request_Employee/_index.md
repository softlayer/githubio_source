---
title: "SoftLayer_Network_Firewall_Update_Request_Employee"
description: "The SoftLayer_Network_Firewall_Update_Request_Employee data type returns a user object for the SoftLayer employee that c... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request_Employee"
---

# SoftLayer_Network_Firewall_Update_Request_Employee
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request_Employee' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Firewall_Update_Request_Employee data type returns a user object for the SoftLayer employee that created the request. 





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
[applyDate]: #applydate
#### [applyDate]
Timestamp of when the rules from the update request were applied to the firewall.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[authorizingUserId]: #authorizinguserid
#### [authorizingUserId]
The unique identifier of the user that authorized the update request.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[authorizingUserType]: #authorizingusertype
#### [authorizingUserType]
The type of user that authorized the update request [EMP or USR].  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[bypassFlag]: #bypassflag
#### [bypassFlag]
Flag indicating whether the request is for a rule bypass configuration [0 or 1].  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
Timestamp of the creation of the record.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[firewallContextAccessControlListId]: #firewallcontextaccesscontrollistid
#### [firewallContextAccessControlListId]
The unique identifier of the firewall access control list that the rule set is destined for.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The unique identifier of the server that the rule set is destined to protect.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique identifier of the firewall update request.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[networkComponentFirewallId]: #networkcomponentfirewallid
#### [networkComponentFirewallId]
The unique identifier of the network component firewall that the rule set is destined for.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[authorizingUser]: #authorizinguser
#### [authorizingUser]
A user object for the SoftLayer employee who created the firewall update request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**


</div>
<div class="prop-row">

-----
[guest]: #guest
#### [guest]
The downstream virtual server that the rule set will be applied to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**


</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The downstream server that the rule set will be applied to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[networkComponentFirewall]: #networkcomponentfirewall
#### [networkComponentFirewall]
The network component firewall that the rule set will be applied to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall </a>**


</div>
<div class="prop-row">

-----
[rules]: #rules
#### [rules]
The group of rules contained within the update request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request_Rule'>SoftLayer_Network_Firewall_Update_Request_Rule[] </a>**


</div>

## Count
<div class="prop-row">

-----
[ruleCount]: #rulecount
#### [ruleCount]
A count of the group of rules contained within the update request.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


