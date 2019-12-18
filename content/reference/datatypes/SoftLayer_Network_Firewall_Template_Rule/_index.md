---
title: "SoftLayer_Network_Firewall_Template_Rule"
description: "The SoftLayer_Network_Component_Firewall_Rule type contains general information relating to a single SoftLayer firewall... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Template_Rule"
---

# SoftLayer_Network_Firewall_Template_Rule
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Firewall_Template_Rule' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Component_Firewall_Rule type contains general information relating to a single SoftLayer firewall template rule. Use the [[SoftLayer Network Component Firewall]] service to view current rules. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. 

### External Links


* [Firewall at Wikipedia](http://en.wikipedia.org/wiki/Firewall_(networking))






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
[action]: #action
#### [action]
The action that this template rule is to take [permit or deny].  
<span class="type-label">Type: </span>**string**

-----
[destinationIpAddress]: #destinationipaddress
#### [destinationIpAddress]
The destination IP address considered for determining rule application.  
<span class="type-label">Type: </span>**string**

-----
[destinationIpSubnetMask]: #destinationipsubnetmask
#### [destinationIpSubnetMask]
The destination IP subnet mask considered for determining rule application.  
<span class="type-label">Type: </span>**string**

-----
[destinationPortRangeEnd]: #destinationportrangeend
#### [destinationPortRangeEnd]
The ending (upper end of range) destination port considered for determining rule application.  
<span class="type-label">Type: </span>**integer**

-----
[destinationPortRangeStart]: #destinationportrangestart
#### [destinationPortRangeStart]
The starting (lower end of range) destination port considered for determining rule application.  
<span class="type-label">Type: </span>**integer**

-----
[firewallTemplateId]: #firewalltemplateid
#### [firewallTemplateId]
The unique identifier of the firewall template that a firewall template rule is associated with.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A Firewall template rule's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[notes]: #notes
#### [notes]
The notes field for the firewall template rule.  
<span class="type-label">Type: </span>**string**

-----
[orderValue]: #ordervalue
#### [orderValue]
The numeric value describing the order in which the rule set should be applied.  
<span class="type-label">Type: </span>**integer**

-----
[protocol]: #protocol
#### [protocol]
The protocol considered for determining rule application.  
<span class="type-label">Type: </span>**string**

-----
[sourceIpAddress]: #sourceipaddress
#### [sourceIpAddress]
The source IP address considered for determining rule application.  
<span class="type-label">Type: </span>**string**

-----
[sourceIpSubnetMask]: #sourceipsubnetmask
#### [sourceIpSubnetMask]
The source IP subnet mask considered for determining rule application.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[firewallTemplate]: #firewalltemplate
#### [firewallTemplate]
The firewall template that this rule is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Firewall_Template'>SoftLayer_Network_Firewall_Template </a>**


## Count
</div>


