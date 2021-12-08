---
title: "SoftLayer_Network_Subnet_IpAddress"
description: "Every SoftLayer IP address is defined in the SoftLayer_Network_Subnet_IpAddress service. SoftLayer IP addresses are assi... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress"
---
# SoftLayer_Network_Subnet_IpAddress
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Subnet_IpAddress' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress' >Datatype</a></li>
    </ul>
</div>

## Description


Every SoftLayer IP address is defined in the SoftLayer_Network_Subnet_IpAddress service. SoftLayer IP addresses are assigned to a SoftLayer_Network_Subnet.  The SoftLayer_Network_Subnet_IpAddress service gives you information about an IP address such if it is reserved, a network address, or a gateway.  Use the data returned by these methods with other API services to get more detailed information about your services. 

SoftLayer customers can order and manage IP addresses through the customer portal. If you need to cancel a subnet please open a sales ticket in our customer portal and our account management staff will assist you. 

### External Links


* [Ip address at Wikipedia](http://en.wikipedia.org/wiki/Ip_address)


* [RFC791: Internet Protocol Specification at ietf.org](http://tools.ietf.org/html/rfc791)




### seeAlso

* [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan )


* [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet )


* [SoftLayer_Network_Subnet_IpAddress_Version6](/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Version6 )


        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [allowAccessToNetworkStorage](/reference/services/SoftLayer_Network_Subnet_IpAddress/allowAccessToNetworkStorage)
Allow access to a SoftLayer_Network_Storage volume from this device. 

</div>

<div class="method-row">

#### [allowAccessToNetworkStorageList](/reference/services/SoftLayer_Network_Subnet_IpAddress/allowAccessToNetworkStorageList)
Allow access to multiple SoftLayer_Network_Storage volumes from this device. 

</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_Subnet_IpAddress/editObject)
Edit the object by passing in a modified instance of the object

</div>

<div class="method-row">

#### [editObjects](/reference/services/SoftLayer_Network_Subnet_IpAddress/editObjects)
Edit multiple objects by passing in modified instances of the object.

</div>

<div class="method-row">

#### [findByIpv4Address](/reference/services/SoftLayer_Network_Subnet_IpAddress/findByIpv4Address)
Search for an IP address record by IPv4 address.

</div>

<div class="method-row">

#### [getAllowedHost](/reference/services/SoftLayer_Network_Subnet_IpAddress/getAllowedHost)
Retrieve the SoftLayer_Network_Storage_Allowed_Host information to connect this IP Address to Network Storage supporting access control lists.

</div>

<div class="method-row">

#### [getAllowedNetworkStorage](/reference/services/SoftLayer_Network_Subnet_IpAddress/getAllowedNetworkStorage)
Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.

</div>

<div class="method-row">

#### [getAllowedNetworkStorageReplicas](/reference/services/SoftLayer_Network_Subnet_IpAddress/getAllowedNetworkStorageReplicas)
Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.

</div>

<div class="method-row">

#### [getApplicationDeliveryController](/reference/services/SoftLayer_Network_Subnet_IpAddress/getApplicationDeliveryController)
Retrieve the application delivery controller using this address.

</div>

<div class="method-row">

#### [getAttachedNetworkStorages](/reference/services/SoftLayer_Network_Subnet_IpAddress/getAttachedNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes authorized to this device. 

</div>

<div class="method-row">

#### [getAvailableNetworkStorages](/reference/services/SoftLayer_Network_Subnet_IpAddress/getAvailableNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. 

</div>

<div class="method-row">

#### [getByIpAddress](/reference/services/SoftLayer_Network_Subnet_IpAddress/getByIpAddress)
Search for an IP address record.

</div>

<div class="method-row">

#### [getContextTunnelTranslations](/reference/services/SoftLayer_Network_Subnet_IpAddress/getContextTunnelTranslations)
Retrieve an IPSec network tunnel's address translations. These translations use a SoftLayer ip address from an assigned static NAT subnet to deliver the packets to the remote (customer) destination.

</div>

<div class="method-row">

#### [getEndpointSubnets](/reference/services/SoftLayer_Network_Subnet_IpAddress/getEndpointSubnets)
Retrieve all the subnets routed to an IP address.

</div>

<div class="method-row">

#### [getGuestNetworkComponent](/reference/services/SoftLayer_Network_Subnet_IpAddress/getGuestNetworkComponent)
Retrieve a network component that is statically routed to an IP address.

</div>

<div class="method-row">

#### [getGuestNetworkComponentBinding](/reference/services/SoftLayer_Network_Subnet_IpAddress/getGuestNetworkComponentBinding)
Retrieve a network component that is statically routed to an IP address.

</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Network_Subnet_IpAddress/getHardware)
Retrieve a server that this IP address is routed to.

</div>

<div class="method-row">

#### [getNetworkComponent](/reference/services/SoftLayer_Network_Subnet_IpAddress/getNetworkComponent)
Retrieve a network component that is statically routed to an IP address.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Subnet_IpAddress/getObject)
Retrieve a SoftLayer_Network_Subnet_IpAddress record.

</div>

<div class="method-row">

#### [getPrivateNetworkGateway](/reference/services/SoftLayer_Network_Subnet_IpAddress/getPrivateNetworkGateway)
Retrieve the network gateway appliance using this address as the private IP address.

</div>

<div class="method-row">

#### [getProtectionAddress](/reference/services/SoftLayer_Network_Subnet_IpAddress/getProtectionAddress)


</div>

<div class="method-row">

#### [getPublicNetworkGateway](/reference/services/SoftLayer_Network_Subnet_IpAddress/getPublicNetworkGateway)
Retrieve the network gateway appliance using this address as the public IP address.

</div>

<div class="method-row">

#### [getRemoteManagementNetworkComponent](/reference/services/SoftLayer_Network_Subnet_IpAddress/getRemoteManagementNetworkComponent)
Retrieve an IPMI-based management network component of the IP address.

</div>

<div class="method-row">

#### [getSubnet](/reference/services/SoftLayer_Network_Subnet_IpAddress/getSubnet)
Retrieve an IP address' associated subnet.

</div>

<div class="method-row">

#### [getSyslogEventsOneDay](/reference/services/SoftLayer_Network_Subnet_IpAddress/getSyslogEventsOneDay)
Retrieve all events for this IP address stored in the datacenter syslogs from the last 24 hours

</div>

<div class="method-row">

#### [getSyslogEventsSevenDays](/reference/services/SoftLayer_Network_Subnet_IpAddress/getSyslogEventsSevenDays)
Retrieve all events for this IP address stored in the datacenter syslogs from the last 7 days

</div>

<div class="method-row">

#### [getTopTenSyslogEventsByDestinationPortOneDay](/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsByDestinationPortOneDay)
Retrieve top Ten network datacenter syslog events, grouped by destination port, for the last 24 hours

</div>

<div class="method-row">

#### [getTopTenSyslogEventsByDestinationPortSevenDays](/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsByDestinationPortSevenDays)
Retrieve top Ten network datacenter syslog events, grouped by destination port, for the last 7 days

</div>

<div class="method-row">

#### [getTopTenSyslogEventsByProtocolsOneDay](/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsByProtocolsOneDay)
Retrieve top Ten network datacenter syslog events, grouped by source port, for the last 24 hours

</div>

<div class="method-row">

#### [getTopTenSyslogEventsByProtocolsSevenDays](/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsByProtocolsSevenDays)
Retrieve top Ten network datacenter syslog events, grouped by source port, for the last 7 days

</div>

<div class="method-row">

#### [getTopTenSyslogEventsBySourceIpOneDay](/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsBySourceIpOneDay)
Retrieve top Ten network datacenter syslog events, grouped by source ip address, for the last 24 hours

</div>

<div class="method-row">

#### [getTopTenSyslogEventsBySourceIpSevenDays](/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsBySourceIpSevenDays)
Retrieve top Ten network datacenter syslog events, grouped by source ip address, for the last 7 days

</div>

<div class="method-row">

#### [getTopTenSyslogEventsBySourcePortOneDay](/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsBySourcePortOneDay)
Retrieve top Ten network datacenter syslog events, grouped by source port, for the last 24 hours

</div>

<div class="method-row">

#### [getTopTenSyslogEventsBySourcePortSevenDays](/reference/services/SoftLayer_Network_Subnet_IpAddress/getTopTenSyslogEventsBySourcePortSevenDays)
Retrieve top Ten network datacenter syslog events, grouped by source port, for the last 7 days

</div>

<div class="method-row">

#### [getVirtualGuest](/reference/services/SoftLayer_Network_Subnet_IpAddress/getVirtualGuest)
Retrieve a virtual guest that this IP address is routed to.

</div>

<div class="method-row">

#### [getVirtualLicenses](/reference/services/SoftLayer_Network_Subnet_IpAddress/getVirtualLicenses)
Retrieve virtual licenses allocated for an IP Address.

</div>

<div class="method-row">

#### [removeAccessToNetworkStorageList](/reference/services/SoftLayer_Network_Subnet_IpAddress/removeAccessToNetworkStorageList)
Remove access to multiple SoftLayer_Network_Storage volumes from this device. 

</div>
</div>

</div>

