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
[action]: #action
#### [action]
The action that this template rule is to take [permit or deny].  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[destinationIpAddress]: #destinationipaddress
#### [destinationIpAddress]
The destination IP address considered for determining rule application.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[destinationIpSubnetMask]: #destinationipsubnetmask
#### [destinationIpSubnetMask]
The destination IP subnet mask considered for determining rule application.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[destinationPortRangeEnd]: #destinationportrangeend
#### [destinationPortRangeEnd]
The ending (upper end of range) destination port considered for determining rule application.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[destinationPortRangeStart]: #destinationportrangestart
#### [destinationPortRangeStart]
The starting (lower end of range) destination port considered for determining rule application.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[firewallTemplateId]: #firewalltemplateid
#### [firewallTemplateId]
The unique identifier of the firewall template that a firewall template rule is associated with.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A Firewall template rule's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
The notes field for the firewall template rule.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[orderValue]: #ordervalue
#### [orderValue]
The numeric value describing the order in which the rule set should be applied.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[protocol]: #protocol
#### [protocol]
The protocol considered for determining rule application.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[sourceIpAddress]: #sourceipaddress
#### [sourceIpAddress]
The source IP address considered for determining rule application.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[sourceIpSubnetMask]: #sourceipsubnetmask
#### [sourceIpSubnetMask]
The source IP subnet mask considered for determining rule application.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[firewallTemplate]: #firewalltemplate
#### [firewallTemplate]
The firewall template that this rule is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Firewall_Template'>SoftLayer_Network_Firewall_Template </a>**  



</div>

## Count
</div>


