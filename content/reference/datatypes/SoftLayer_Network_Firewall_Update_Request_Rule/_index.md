---
title: "SoftLayer_Network_Firewall_Update_Request_Rule"
description: "The SoftLayer_Network_Firewall_Update_Request_Rule type contains information relating to a SoftLayer network firewall up... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request_Rule"
---

# SoftLayer_Network_Firewall_Update_Request_Rule
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Firewall_Update_Request_Rule' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request_Rule' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Firewall_Update_Request_Rule type contains information relating to a SoftLayer network firewall update request rule. This rule is a member of a [[SoftLayer Network Firewall Update Request]]. Use the [[SoftLayer Network Component Firewall]] service to view current rules. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates. 

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
The action that this update request rule is to take [permit or deny].  
<span class="type-label">Type: </span>**string**

-----
[destinationIpAddress]: #destinationipaddress
#### [destinationIpAddress]
The destination IP address considered for determining rule application.  
<span class="type-label">Type: </span>**string**

-----
[destinationIpCidr]: #destinationipcidr
#### [destinationIpCidr]
The CIDR is used for determining rule application. This value will  
<span class="type-label">Type: </span>**integer**

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
[firewallUpdateRequestId]: #firewallupdaterequestid
#### [firewallUpdateRequestId]
The unique identifier of the firewall update request that a firewall update request rule is associated with.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A Firewall update request rule's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[notes]: #notes
#### [notes]
The notes field for the firewall update request rule.  
<span class="type-label">Type: </span>**string**

-----
[orderValue]: #ordervalue
#### [orderValue]
The numeric value describing the order in which the rule should be applied.  
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
[sourceIpCidr]: #sourceipcidr
#### [sourceIpCidr]
The CIDR is used for determining rule application. This value will  
<span class="type-label">Type: </span>**integer**

-----
[sourceIpSubnetMask]: #sourceipsubnetmask
#### [sourceIpSubnetMask]
The source IP subnet mask considered for determining rule application.  
<span class="type-label">Type: </span>**string**

-----
[version]: #version
#### [version]
Whether this rule is an IPv4 rule or an IPv6 rule. If  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[firewallUpdateRequest]: #firewallupdaterequest
#### [firewallUpdateRequest]
The update request that this rule belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Firewall_Update_Request'>SoftLayer_Network_Firewall_Update_Request </a>**


## Count
</div>


