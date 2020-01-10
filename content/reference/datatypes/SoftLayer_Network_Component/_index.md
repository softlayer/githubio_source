---
title: "SoftLayer_Network_Component"
description: "Every piece of hardware running in SoftLayer's datacenters connected to the public, private, or management networks (whe... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Component"
---

# SoftLayer_Network_Component
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Component' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Component' >Datatype</a></li>
    </ul>
</div>

## Description 
Every piece of hardware running in SoftLayer's datacenters connected to the public, private, or management networks (where applicable) have a corresponding network component. These network components are modeled by the SoftLayer_Network_Component data type. These data types reflect the servers' local ethernet and remote management interfaces. 

### External Links


* [IP address at Wikipedia](http://en.wikipedia.org/wiki/IP_address)


* [MAC address at Wikipedia](http://en.wikipedia.org/wiki/MAC_address)


* [Virtual LAN at Wikipedia](http://en.wikipedia.org/wiki/Virtual_LAN)



### associatedMethods

*  [SoftLayer_Hardware::getNetworkComponents](/reference/services/SoftLayer_Hardware/getNetworkComponents )
*  [SoftLayer_Hardware::getPrimaryIpAddress](/reference/services/SoftLayer_Hardware/getPrimaryIpAddress )
*  [SoftLayer_Hardware_Server::getPublicNetworkComponent](/reference/services/SoftLayer_Hardware_Server/getPublicNetworkComponent )
*  [SoftLayer_Hardware_Server::getPrivateNetworkComponent](/reference/services/SoftLayer_Hardware_Server/getPrivateNetworkComponent )
*  [SoftLayer_Hardware_Server::getManagementNetworkComponent](/reference/services/SoftLayer_Hardware_Server/getManagementNetworkComponent )
*  [SoftLayer_Hardware_Server::getPrimaryIpAddress](/reference/services/SoftLayer_Hardware_Server/getPrimaryIpAddress )
*  [SoftLayer_Hardware_Server::getPrivateIpAddress](/reference/services/SoftLayer_Hardware_Server/getPrivateIpAddress )
*  [SoftLayer_Hardware_Server::setPublicPortSpeed](/reference/services/SoftLayer_Hardware_Server/setPublicPortSpeed )
*  [SoftLayer_Hardware_Server::setPrivatePortSpeed](/reference/services/SoftLayer_Hardware_Server/setPrivatePortSpeed )
*  [SoftLayer_Network_Vlan::getNetworkComponents](/reference/services/SoftLayer_Network_Vlan/getNetworkComponents )





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
[duplexModeId]: #duplexmodeid
#### [duplexModeId]
A network component's Duplex mode.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The internal identifier of the hardware that a network component belongs to.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A network component's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[ipmiIpAddress]: #ipmiipaddress
#### [ipmiIpAddress]
The IP address of an IPMI-based management network component.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[ipmiMacAddress]: #ipmimacaddress
#### [ipmiMacAddress]
The MAC address of an IPMI-based management network component.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[macAddress]: #macaddress
#### [macAddress]
A network component's unique MAC address. IPMI-based management network interfaces may not have a MAC address.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[maxSpeed]: #maxspeed
#### [maxSpeed]
A network component's maximum allowed speed, measured in Mbit per second. ''maxSpeed'' is determined by the capabilities of the network interface and the port speed purchased on your SoftLayer server.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a network component was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A network component's short name. For most servers this is the string "eth" for ethernet ports or "mgmt" for remote management ports. Use this in conjunction with the ''port'' property to identify a network component. For instance, the "eth0" interface on a server has the network component name "eth" and port 0.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[networkVlanId]: #networkvlanid
#### [networkVlanId]
The unique internal id of the network VLAN that the port belongs to.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[port]: #port
#### [port]
A network component's port number. Most hardware has more than one network interface. The port property separates these interfaces. Use this in conjunction with the ''name'' property to identify a network component. For instance, the "eth0" interface on a server has the network component name "eth" and port 0.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[primaryIpAddress]: #primaryipaddress
#### [primaryIpAddress]
A network component's primary IP address. IPMI-based management network interfaces may not have an IP address.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[speed]: #speed
#### [speed]
A network component's speed, measured in Mbit per second.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
A network component's status. This can take one of four possible values: "ACTIVE", "DISABLE", "USER_OFF", or "MACWAIT". "ACTIVE" network components are enabled and in use on a servers. "DISABLE" status components have been administratively disabled by SoftLayer accounting or abuse. "USER_OFF" components have been administratively disabled by you, the user. "MACWAIT" components only exist on network components that have not been provisioned. You should never see a network interface in MACWAIT state. If you happen to see one please contact SoftLayer support.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[activeCommand]: #activecommand
#### [activeCommand]
Reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) command currently executing by the server's remote management card.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request </a>**


</div>
<div class="prop-row">

-----
[downlinkComponent]: #downlinkcomponent
#### [downlinkComponent]
The network component linking this object to a child device  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**


</div>
<div class="prop-row">

-----
[duplexMode]: #duplexmode
#### [duplexMode]
The duplex mode of a network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Duplex_Mode'>SoftLayer_Network_Component_Duplex_Mode </a>**


</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware that a network component resides in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[highAvailabilityFirewallFlag]: #highavailabilityfirewallflag
#### [highAvailabilityFirewallFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[interface]: #interface
#### [interface]
A hardware switch's interface to the bandwidth pod.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Interface'>SoftLayer_Network_Bandwidth_Version1_Interface </a>**


</div>
<div class="prop-row">

-----
[ipAddressBindings]: #ipaddressbindings
#### [ipAddressBindings]
The records of all IP addresses bound to a network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_IpAddress'>SoftLayer_Network_Component_IpAddress[] </a>**


</div>
<div class="prop-row">

-----
[ipAddresses]: #ipaddresses
#### [ipAddresses]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress[] </a>**


</div>
<div class="prop-row">

-----
[lastCommand]: #lastcommand
#### [lastCommand]
Last reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) command issued to the server's remote management card.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request </a>**


</div>
<div class="prop-row">

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
The metric tracking object for this network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a>**


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
[networkComponentGroup]: #networkcomponentgroup
#### [networkComponentGroup]
A network component's associated group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Group'>SoftLayer_Network_Component_Group </a>**


</div>
<div class="prop-row">

-----
[networkHardware]: #networkhardware
#### [networkHardware]
All network devices in SoftLayer's network hierarchy that this device is connected to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[networkVlan]: #networkvlan
#### [networkVlan]
The VLAN that a network component's subnet is associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**


</div>
<div class="prop-row">

-----
[networkVlanTrunks]: #networkvlantrunks
#### [networkVlanTrunks]
The VLANs that are trunked to this network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Network_Vlan_Trunk'>SoftLayer_Network_Component_Network_Vlan_Trunk[] </a>**


</div>
<div class="prop-row">

-----
[primaryIpAddressRecord]: #primaryipaddressrecord
#### [primaryIpAddressRecord]
The primary IPv4 Address record for a network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[primarySubnet]: #primarysubnet
#### [primarySubnet]
The subnet of the primary IP address assigned to this network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**


</div>
<div class="prop-row">

-----
[primaryVersion6IpAddressRecord]: #primaryversion6ipaddressrecord
#### [primaryVersion6IpAddressRecord]
The primary IPv6 Address record for a network component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress'>SoftLayer_Network_Subnet_IpAddress </a>**


</div>
<div class="prop-row">

-----
[recentCommands]: #recentcommands
#### [recentCommands]
The last five reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) commands issued to the server's remote management card.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_Command_Request'>SoftLayer_Hardware_Component_RemoteManagement_Command_Request[] </a>**


</div>
<div class="prop-row">

-----
[redundancyCapableFlag]: #redundancycapableflag
#### [redundancyCapableFlag]
Indicates whether the network component is participating in a group of two or more components capable of being operationally redundant, if enabled.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[redundancyEnabledFlag]: #redundancyenabledflag
#### [redundancyEnabledFlag]
Indicates whether the network component is participating in a group of two or more components which is actively providing link redundancy.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[remoteManagementUsers]: #remotemanagementusers
#### [remoteManagementUsers]
User(s) credentials to issue commands and/or interact with the server's remote management card.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_RemoteManagement_User'>SoftLayer_Hardware_Component_RemoteManagement_User[] </a>**


</div>
<div class="prop-row">

-----
[router]: #router
#### [router]
A network component's routers.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[storageNetworkFlag]: #storagenetworkflag
#### [storageNetworkFlag]
Whether a network component's primary ip address is from a storage network subnet or not.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[subnets]: #subnets
#### [subnets]
A network component's subnets. A subnet is a group of IP addresses  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[uplinkComponent]: #uplinkcomponent
#### [uplinkComponent]
The network component linking this object to parent  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**


</div>
<div class="prop-row">

-----
[uplinkDuplexMode]: #uplinkduplexmode
#### [uplinkDuplexMode]
The duplex mode of the uplink network component linking to this object  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component_Duplex_Mode'>SoftLayer_Network_Component_Duplex_Mode </a>**


</div>

## Count
<div class="prop-row">

-----
[ipAddressBindingCount]: #ipaddressbindingcount
#### [ipAddressBindingCount]
A count of the records of all IP addresses bound to a network component.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ipAddressCount]: #ipaddresscount
#### [ipAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkHardwareCount]: #networkhardwarecount
#### [networkHardwareCount]
A count of all network devices in SoftLayer's network hierarchy that this device is connected to.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[networkVlanTrunkCount]: #networkvlantrunkcount
#### [networkVlanTrunkCount]
A count of the VLANs that are trunked to this network component.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[recentCommandCount]: #recentcommandcount
#### [recentCommandCount]
A count of the last five reboot/power (rebootDefault, rebootSoft, rebootHard, powerOn, powerOff and powerCycle) commands issued to the server's remote management card.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[remoteManagementUserCount]: #remotemanagementusercount
#### [remoteManagementUserCount]
A count of user(s) credentials to issue commands and/or interact with the server's remote management card.   
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


