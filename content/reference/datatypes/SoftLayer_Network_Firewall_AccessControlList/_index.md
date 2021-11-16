---
title: "SoftLayer_Network_Firewall_AccessControlList"
description: "The SoftLayer_Network_Firewall_AccessControlList data type contains general information relating to a single SoftLayer f... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_AccessControlList"
---

# SoftLayer_Network_Firewall_AccessControlList
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Firewall_AccessControlList' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Firewall_AccessControlList' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Firewall_AccessControlList data type contains general information relating to a single SoftLayer firewall access to controll list. This is the object which ties the running rules to a specific context. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. 

### External Links


* [Firewall at Wikipedia](http://en.wikipedia.org/wiki/Firewall_(networking))




### seeAlso

* [SoftLayer_Network_Firewall_Template](/reference/services/SoftLayer_Network_Firewall_Template )


* [SoftLayer_Network_Firewall_Update_Request](/reference/services/SoftLayer_Network_Firewall_Update_Request )




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
[direction]: #direction
#### [direction]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[firewallContextInterfaceId]: #firewallcontextinterfaceid
#### [firewallContextInterfaceId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[networkFirewallUpdateRequests]: #networkfirewallupdaterequests
#### [networkFirewallUpdateRequests]
The update requests made for this firewall.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request'>SoftLayer_Network_Firewall_Update_Request[] </a>**  



</div>
<div class="prop-row">

-----
[networkVlan]: #networkvlan
#### [networkVlan]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**  



</div>
<div class="prop-row">

-----
[rules]: #rules
#### [rules]
The currently running rule set of this context access control list firewall.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan_Firewall_Rule'>SoftLayer_Network_Vlan_Firewall_Rule[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[networkFirewallUpdateRequestCount]: #networkfirewallupdaterequestcount
#### [networkFirewallUpdateRequestCount]
A count of the update requests made for this firewall.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[ruleCount]: #rulecount
#### [ruleCount]
A count of the currently running rule set of this context access control list firewall.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


