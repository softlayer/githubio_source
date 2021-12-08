---
title: "SoftLayer_Network_Subnet_IpAddress_Version6"
description: "The SoftLayer_Network_Subnet_IpAddress data type contains general information relating to a single SoftLayer IPv6 addres... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress_Version6"
---

# SoftLayer_Network_Subnet_IpAddress_Version6
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_IpAddress_Version6' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Subnet_IpAddress data type contains general information relating to a single SoftLayer IPv6 address. 

### External Links


* [IPv6 at Wikipedia](http://en.wikipedia.org/wiki/IPv6)


* [RFC2460: Internet Protocol, Version 6 (IPv6) Specification at ietf.org](http://tools.ietf.org/html/rfc2460)



### associatedMethods

*  [SoftLayer_Network_Subnet_IpAddress::getObject](/reference/services/SoftLayer_Network_Subnet_IpAddress/getObject )
*  [SoftLayer_Network_Subnet_IpAddress::editObject](/reference/services/SoftLayer_Network_Subnet_IpAddress/editObject )



### seeAlso

* [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan )


* [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet )


* [SoftLayer_Network_Subnet_IpAddress](/reference/services/SoftLayer_Network_Subnet_IpAddress )




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
[id]: #id
#### [id]
An IP's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[ipAddress]: #ipaddress
#### [ipAddress]
An IP address expressed in dotted quad format.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[isBroadcast]: #isbroadcast
#### [isBroadcast]
Indicates if an IP address is reserved to be used as the network broadcast address and cannot be assigned to a network interface   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[isGateway]: #isgateway
#### [isGateway]
Indicates if an IP address is reserved to a gateway and cannot be assigned to a network interface   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[isNetwork]: #isnetwork
#### [isNetwork]
Indicates if an IP address is reserved to a network address and cannot be assigned to a network interface   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[isReserved]: #isreserved
#### [isReserved]
Indicates if an IP address is reserved and cannot be assigned to a network interface   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[note]: #note
#### [note]
An IP address' user defined note.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[subnetId]: #subnetid
#### [subnetId]
An IP address' subnet id.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[allowedHost]: #allowedhost
#### [allowedHost]
The SoftLayer_Network_Storage_Allowed_Host information to connect this IP Address to Network Storage supporting access control lists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host </a>**  



</div>
<div class="prop-row">

-----
[allowedNetworkStorage]: #allowednetworkstorage
#### [allowedNetworkStorage]
The SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**  



</div>
<div class="prop-row">

-----
[allowedNetworkStorageReplicas]: #allowednetworkstoragereplicas
#### [allowedNetworkStorageReplicas]
The SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**  



</div>
<div class="prop-row">

-----
[applicationDeliveryController]: #applicationdeliverycontroller
#### [applicationDeliveryController]
The application delivery controller using this address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller </a>**  



</div>
<div class="prop-row">

-----
[contextTunnelTranslations]: #contexttunneltranslations
#### [contextTunnelTranslations]
An IPSec network tunnel's address translations. These translations use a SoftLayer ip address from an assigned static NAT subnet to deliver the packets to the remote (customer) destination.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation[] </a>**  



</div>
<div class="prop-row">

-----
[endpointSubnets]: #endpointsubnets
#### [endpointSubnets]
All the subnets routed to an IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**  



</div>
<div class="prop-row">

-----
[guestNetworkComponent]: #guestnetworkcomponent
#### [guestNetworkComponent]
A network component that is statically routed to an IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component </a>**  



</div>
<div class="prop-row">

-----
[guestNetworkComponentBinding]: #guestnetworkcomponentbinding
#### [guestNetworkComponentBinding]
A network component that is statically routed to an IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component_IpAddress'>SoftLayer_Virtual_Guest_Network_Component_IpAddress </a>**  



</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware that this IP address is routed to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[networkComponent]: #networkcomponent
#### [networkComponent]
A network component that is statically routed to an IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**  



</div>
<div class="prop-row">

-----
[privateNetworkGateway]: #privatenetworkgateway
#### [privateNetworkGateway]
The network gateway appliance using this address as the private IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>**  



</div>
<div class="prop-row">

-----
[protectionAddress]: #protectionaddress
#### [protectionAddress]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Protection_Address'>SoftLayer_Network_Protection_Address[] </a>**  



</div>
<div class="prop-row">

-----
[publicNetworkGateway]: #publicnetworkgateway
#### [publicNetworkGateway]
The network gateway appliance using this address as the public IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>**  



</div>
<div class="prop-row">

-----
[publicVersion6NetworkGateway]: #publicversion6networkgateway
#### [publicVersion6NetworkGateway]
The network gateway appliance using this address as the public IPv6 address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>**  



</div>
<div class="prop-row">

-----
[remoteManagementNetworkComponent]: #remotemanagementnetworkcomponent
#### [remoteManagementNetworkComponent]
An IPMI-based management network component of the IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**  



</div>
<div class="prop-row">

-----
[subnet]: #subnet
#### [subnet]
An IP address' associated subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**  



</div>
<div class="prop-row">

-----
[syslogEventsOneDay]: #syslogeventsoneday
#### [syslogEventsOneDay]
All events for this IP address stored in the datacenter syslogs from the last 24 hours  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**  



</div>
<div class="prop-row">

-----
[syslogEventsSevenDays]: #syslogeventssevendays
#### [syslogEventsSevenDays]
All events for this IP address stored in the datacenter syslogs from the last 7 days  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsByDestinationPortOneDay]: #toptensyslogeventsbydestinationportoneday
#### [topTenSyslogEventsByDestinationPortOneDay]
Top Ten network datacenter syslog events, grouped by destination port, for the last 24 hours  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsByDestinationPortSevenDays]: #toptensyslogeventsbydestinationportsevendays
#### [topTenSyslogEventsByDestinationPortSevenDays]
Top Ten network datacenter syslog events, grouped by destination port, for the last 7 days  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsByProtocolsOneDay]: #toptensyslogeventsbyprotocolsoneday
#### [topTenSyslogEventsByProtocolsOneDay]
Top Ten network datacenter syslog events, grouped by source port, for the last 24 hours  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsByProtocolsSevenDays]: #toptensyslogeventsbyprotocolssevendays
#### [topTenSyslogEventsByProtocolsSevenDays]
Top Ten network datacenter syslog events, grouped by source port, for the last 7 days  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsBySourceIpOneDay]: #toptensyslogeventsbysourceiponeday
#### [topTenSyslogEventsBySourceIpOneDay]
Top Ten network datacenter syslog events, grouped by source ip address, for the last 24 hours  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsBySourceIpSevenDays]: #toptensyslogeventsbysourceipsevendays
#### [topTenSyslogEventsBySourceIpSevenDays]
Top Ten network datacenter syslog events, grouped by source ip address, for the last 7 days  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsBySourcePortOneDay]: #toptensyslogeventsbysourceportoneday
#### [topTenSyslogEventsBySourcePortOneDay]
Top Ten network datacenter syslog events, grouped by source port, for the last 24 hours  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsBySourcePortSevenDays]: #toptensyslogeventsbysourceportsevendays
#### [topTenSyslogEventsBySourcePortSevenDays]
Top Ten network datacenter syslog events, grouped by source port, for the last 7 days  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**  



</div>
<div class="prop-row">

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
A virtual guest that this IP address is routed to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**  



</div>
<div class="prop-row">

-----
[virtualLicenses]: #virtuallicenses
#### [virtualLicenses]
Virtual licenses allocated for an IP Address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_VirtualLicense'>SoftLayer_Software_VirtualLicense[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[allowedNetworkStorageCount]: #allowednetworkstoragecount
#### [allowedNetworkStorageCount]
A count of the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[allowedNetworkStorageReplicaCount]: #allowednetworkstoragereplicacount
#### [allowedNetworkStorageReplicaCount]
A count of the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[contextTunnelTranslationCount]: #contexttunneltranslationcount
#### [contextTunnelTranslationCount]
A count of an IPSec network tunnel's address translations. These translations use a SoftLayer ip address from an assigned static NAT subnet to deliver the packets to the remote (customer) destination.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[endpointSubnetCount]: #endpointsubnetcount
#### [endpointSubnetCount]
A count of all the subnets routed to an IP address.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[protectionAddressCount]: #protectionaddresscount
#### [protectionAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[syslogEventsOneDayCount]: #syslogeventsonedaycount
#### [syslogEventsOneDayCount]
A count of all events for this IP address stored in the datacenter syslogs from the last 24 hours   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[syslogEventsSevenDayCount]: #syslogeventssevendaycount
#### [syslogEventsSevenDayCount]
A count of all events for this IP address stored in the datacenter syslogs from the last 7 days   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsByDestinationPortOneDayCount]: #toptensyslogeventsbydestinationportonedaycount
#### [topTenSyslogEventsByDestinationPortOneDayCount]
A count of top Ten network datacenter syslog events, grouped by destination port, for the last 24 hours   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsByDestinationPortSevenDayCount]: #toptensyslogeventsbydestinationportsevendaycount
#### [topTenSyslogEventsByDestinationPortSevenDayCount]
A count of top Ten network datacenter syslog events, grouped by destination port, for the last 7 days   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsByProtocolsOneDayCount]: #toptensyslogeventsbyprotocolsonedaycount
#### [topTenSyslogEventsByProtocolsOneDayCount]
A count of top Ten network datacenter syslog events, grouped by source port, for the last 24 hours   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsByProtocolsSevenDayCount]: #toptensyslogeventsbyprotocolssevendaycount
#### [topTenSyslogEventsByProtocolsSevenDayCount]
A count of top Ten network datacenter syslog events, grouped by source port, for the last 7 days   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsBySourceIpOneDayCount]: #toptensyslogeventsbysourceiponedaycount
#### [topTenSyslogEventsBySourceIpOneDayCount]
A count of top Ten network datacenter syslog events, grouped by source ip address, for the last 24 hours   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsBySourceIpSevenDayCount]: #toptensyslogeventsbysourceipsevendaycount
#### [topTenSyslogEventsBySourceIpSevenDayCount]
A count of top Ten network datacenter syslog events, grouped by source ip address, for the last 7 days   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsBySourcePortOneDayCount]: #toptensyslogeventsbysourceportonedaycount
#### [topTenSyslogEventsBySourcePortOneDayCount]
A count of top Ten network datacenter syslog events, grouped by source port, for the last 24 hours   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[topTenSyslogEventsBySourcePortSevenDayCount]: #toptensyslogeventsbysourceportsevendaycount
#### [topTenSyslogEventsBySourcePortSevenDayCount]
A count of top Ten network datacenter syslog events, grouped by source port, for the last 7 days   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[virtualLicenseCount]: #virtuallicensecount
#### [virtualLicenseCount]
A count of virtual licenses allocated for an IP Address.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


