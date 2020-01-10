---
title: "SoftLayer_Network_SecurityGroup_Rule"
description: "The SoftLayer_Network_SecurityGroup_Rule data type contains general information for a single rule that belongs to a [Sof... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup_Rule"
---

# SoftLayer_Network_SecurityGroup_Rule
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_Rule' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_SecurityGroup_Rule data type contains general information for a single rule that belongs to a [SoftLayer_Network_SecurityGroup]({{<ref "reference/datatypes/SoftLayer_Network_SecurityGroup">}}). By default, all traffic (both inbound and  outbound) to a virtual server instance is blocked. Security group rules are permissive, and define the allowed incoming (ingress) and outgoing (egress) traffic to both the public and private interfaces of a  virtual server instance. The order of rules within a security group does not matter and priority always falls to the least restrictive rule. 





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
[createDate]: #createdate
#### [createDate]
The createDate field for a rule. It is essentially the date and time that the security group rule was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[direction]: #direction
#### [direction]
The direction of traffic (ingress or egress).  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[ethertype]: #ethertype
#### [ethertype]
IPv4 or IPv6. If the remoteIp or ethertype properties are not specified, the default is IPv4. Otherwise ethertype will default based on the format of the specified remoteIp.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique ID for a rule.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The modifyDate field for a rule. It is essentially the date and time that the security group rule was last changed.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[portRangeMax]: #portrangemax
#### [portRangeMax]
The end of the port range for allowed traffic.  When the protocol is icmp, this value specifies the icmp code to permit.  When icmp code is specified, icmp type is required. When the protocol is vrrp, ports cannot be specified.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[portRangeMin]: #portrangemin
#### [portRangeMin]
The start of the port range for allowed traffic.  When the protocol is icmp, this value specifies the icmp type to permit.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[protocol]: #protocol
#### [protocol]
The protocol of packets (icmp, tcp, udp, or vrrp).  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[remoteGroupId]: #remotegroupid
#### [remoteGroupId]
The ID of the remote security group allowed as part of the rule. This property is mutually exclusive with the remoteIp property.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[remoteIp]: #remoteip
#### [remoteIp]
CIDR or IP address for allowed connections. This property is mutually exclusive with the remoteGroupId property. When the protocol is vrrp, ports cannot be specified.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[securityGroupId]: #securitygroupid
#### [securityGroupId]
The ID of the security group that owns the rule.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[remoteGroup]: #remotegroup
#### [remoteGroup]
The remote security group allowed as part of this rule.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup'>SoftLayer_Network_SecurityGroup </a>**


</div>
<div class="prop-row">

-----
[securityGroup]: #securitygroup
#### [securityGroup]
The security group of this rule.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup'>SoftLayer_Network_SecurityGroup </a>**


</div>

## Count
</div>


