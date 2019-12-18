---
title: "SoftLayer_Network_Firewall_Update_Request_Customer"
description: "A SoftLayer_Ticket_Update_Customer is a single update made by a customer to a ticket."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request_Customer"
---

# SoftLayer_Network_Firewall_Update_Request_Customer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request_Customer' >Datatype</a></li>
    </ul>
</div>

## Description 
A SoftLayer_Ticket_Update_Customer is a single update made by a customer to a ticket. 





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
[applyDate]: #applydate
#### [applyDate]
Timestamp of when the rules from the update request were applied to the firewall.  
<span class="type-label">Type: </span>**dateTime**

-----
[authorizingUserId]: #authorizinguserid
#### [authorizingUserId]
The unique identifier of the user that authorized the update request.  
<span class="type-label">Type: </span>**integer**

-----
[authorizingUserType]: #authorizingusertype
#### [authorizingUserType]
The type of user that authorized the update request [EMP or USR].  
<span class="type-label">Type: </span>**string**

-----
[bypassFlag]: #bypassflag
#### [bypassFlag]
Flag indicating whether the request is for a rule bypass configuration [0 or 1].  
<span class="type-label">Type: </span>**boolean**

-----
[createDate]: #createdate
#### [createDate]
Timestamp of the creation of the record.  
<span class="type-label">Type: </span>**dateTime**

-----
[firewallContextAccessControlListId]: #firewallcontextaccesscontrollistid
#### [firewallContextAccessControlListId]
The unique identifier of the firewall access control list that the rule set is destined for.  
<span class="type-label">Type: </span>**integer**

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The unique identifier of the server that the rule set is destined to protect.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
The unique identifier of the firewall update request.  
<span class="type-label">Type: </span>**integer**

-----
[networkComponentFirewallId]: #networkcomponentfirewallid
#### [networkComponentFirewallId]
The unique identifier of the network component firewall that the rule set is destined for.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[authorizingUser]: #authorizinguser
#### [authorizingUser]
A user object for the customer user who created the firewall update request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[guest]: #guest
#### [guest]
The downstream virtual server that the rule set will be applied to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**

-----
[hardware]: #hardware
#### [hardware]
The downstream server that the rule set will be applied to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[networkComponentFirewall]: #networkcomponentfirewall
#### [networkComponentFirewall]
The network component firewall that the rule set will be applied to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall </a>**

-----
[rules]: #rules
#### [rules]
The group of rules contained within the update request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request_Rule'>SoftLayer_Network_Firewall_Update_Request_Rule[] </a>**


## Count

-----
[ruleCount]: #rulecount
#### [ruleCount]
A count of the group of rules contained within the update request.   
<span class="type-label">Type: </span>**unsigned long**

</div>


