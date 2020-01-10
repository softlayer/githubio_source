---
title: "SoftLayer_Virtual_Guest_Network_Component"
description: "The virtual guest network component data type presents the structure in which all computing instance network components... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Network_Component"
---

# SoftLayer_Virtual_Guest_Network_Component
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_Guest_Network_Component' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component' >Datatype</a></li>
    </ul>
</div>

## Description 
The virtual guest network component data type presents the structure in which all computing instance network components are presented. Internally, the structure supports various virtualization platforms with no change to external interaction. 

A guest, also known as a virtual server, represents an allocation of resources on a virtual host. 





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
The date a computing instance's network component was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[guestId]: #guestid
#### [guestId]
The unique ID of the [SoftLayer_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest">}}) that this network component belongs to.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A computing instance's network component's unique ID.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[macAddress]: #macaddress
#### [macAddress]
A computing instance network component's unique MAC address.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[maxSpeed]: #maxspeed
#### [maxSpeed]
A computing instance network component's maximum allowed speed, measured in Mbit per second. ''maxSpeed'' is determined by the capabilities of the network interface and the port speed purchased on your SoftLayer computing instance.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a computing instance's network component was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A computing instance network component's short name. This is usually ''eth''. Use this in conjunction with the ''port'' property to identify a network component. For instance, the "eth0" interface on a server has the network component name "eth" and port 0.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[networkId]: #networkid
#### [networkId]
A computing instance's network component's [SoftLayer_Virtual_Network]({{<ref "reference/datatypes/SoftLayer_Virtual_Network">}}) ID   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[port]: #port
#### [port]
A computing instance network component's port number. Most computing instances have more than one network interface. The port property separates these interfaces. Use this in conjunction with the ''name'' property to identify a network component. For instance, the "eth0" interface on a server has the network component name "eth" and port 0.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[speed]: #speed
#### [speed]
A computing instance network component's speed, measured in Mbit per second.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
A computing instance network component's status. This can be one of four possible values: "ACTIVE", "DISABLED", "INACTIVE", or "ABUSE_DISCONNECT". "ACTIVE" network components are enabled and in use on a cloud instance. "ABUSE_DISCONNECT" status components have been administratively disabled by SoftLayer accounting or abuse. "DISABLED" components have been administratively disabled by you, the user. You should never see a network interface in MACWAIT state. If you happen to see one please contact SoftLayer support.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[uuid]: #uuid
#### [uuid]
A computing instance's network component's unique ID on a virtualization platform.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[guest]: #guest
#### [guest]
The computing instance that this network component exists on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**


</div>
<div class="prop-row">

-----
[highAvailabilityFirewallFlag]: #highavailabilityfirewallflag
#### [highAvailabilityFirewallFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[icpBinding]: #icpbinding
#### [icpBinding]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component_IcpBinding'>SoftLayer_Virtual_Guest_Network_Component_IcpBinding </a>**


</div>
<div class="prop-row">

-----
[ipAddressBindings]: #ipaddressbindings
#### [ipAddressBindings]
The records of all IP addresses bound to a computing instance's network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component_IpAddress'>SoftLayer_Virtual_Guest_Network_Component_IpAddress[] </a>**


</div>
<div class="prop-row">

-----
[networkComponentFirewall]: #networkcomponentfirewall
#### [networkComponentFirewall]
The upstream network component firewall.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Firewall'>SoftLayer_Network_Component_Firewall </a>**


</div>
<div class="prop-row">

-----
[networkVlan]: #networkvlan
#### [networkVlan]
The VLAN that a computing instance network component's subnet is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**


</div>
<div class="prop-row">

-----
[primaryIpAddress]: #primaryipaddress
#### [primaryIpAddress]
A computing instance network component's primary IP address.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[primaryIpAddressRecord]: #primaryipaddressrecord
#### [primaryIpAddressRecord]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[primarySubnet]: #primarysubnet
#### [primarySubnet]
A network component's subnet for its primary IP address  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**


</div>
<div class="prop-row">

-----
[primaryVersion6IpAddressRecord]: #primaryversion6ipaddressrecord
#### [primaryVersion6IpAddressRecord]
A network component's primary IPv6 IP address record.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[router]: #router
#### [router]
A network component's routers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Router'>SoftLayer_Hardware_Router </a>**


</div>
<div class="prop-row">

-----
[securityGroupBindings]: #securitygroupbindings
#### [securityGroupBindings]
The bindings associating security groups to this network component  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding'>SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding[] </a>**


</div>
<div class="prop-row">

-----
[subnets]: #subnets
#### [subnets]
A network component's subnets. A subnet is a group of IP addresses  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>

## Count
<div class="prop-row">

-----
[ipAddressBindingCount]: #ipaddressbindingcount
#### [ipAddressBindingCount]
A count of the records of all IP addresses bound to a computing instance's network component.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[securityGroupBindingCount]: #securitygroupbindingcount
#### [securityGroupBindingCount]
A count of the bindings associating security groups to this network component   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[subnetCount]: #subnetcount
#### [subnetCount]
A count of a network component's subnets. A subnet is a group of IP addresses   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


