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
[id]: #id
#### [id]
An IP's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[ipAddress]: #ipaddress
#### [ipAddress]
An IP address expressed in dotted quad format.  
<span class="type-label">Type: </span>**string**

-----
[isBroadcast]: #isbroadcast
#### [isBroadcast]
Indicates if an IP address is reserved to be used as the network broadcast address and cannot be assigned to a network interface   
<span class="type-label">Type: </span>**boolean**

-----
[isGateway]: #isgateway
#### [isGateway]
Indicates if an IP address is reserved to a gateway and cannot be assigned to a network interface   
<span class="type-label">Type: </span>**boolean**

-----
[isNetwork]: #isnetwork
#### [isNetwork]
Indicates if an IP address is reserved to a network address and cannot be assigned to a network interface   
<span class="type-label">Type: </span>**boolean**

-----
[isReserved]: #isreserved
#### [isReserved]
Indicates if an IP address is reserved and cannot be assigned to a network interface   
<span class="type-label">Type: </span>**boolean**

-----
[note]: #note
#### [note]
An IP address' user defined note.   
<span class="type-label">Type: </span>**string**

-----
[subnetId]: #subnetid
#### [subnetId]
An IP address' subnet id.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[allowedHost]: #allowedhost
#### [allowedHost]
The SoftLayer_Network_Storage_Allowed_Host information to connect this IP Address to Network Storage supporting access control lists.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host </a>**

-----
[allowedNetworkStorage]: #allowednetworkstorage
#### [allowedNetworkStorage]
The SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[allowedNetworkStorageReplicas]: #allowednetworkstoragereplicas
#### [allowedNetworkStorageReplicas]
The SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[applicationDeliveryController]: #applicationdeliverycontroller
#### [applicationDeliveryController]
The application delivery controller using this address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller </a>**

-----
[contextTunnelTranslations]: #contexttunneltranslations
#### [contextTunnelTranslations]
An IPSec network tunnel's address translations. These translations use a SoftLayer ip address from an assigned static NAT subnet to deliver the packets to the remote (customer) destination.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation[] </a>**

-----
[endpointSubnets]: #endpointsubnets
#### [endpointSubnets]
All the subnets routed to an IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**

-----
[guestNetworkComponent]: #guestnetworkcomponent
#### [guestNetworkComponent]
A network component that is statically routed to an IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component'>SoftLayer_Virtual_Guest_Network_Component </a>**

-----
[guestNetworkComponentBinding]: #guestnetworkcomponentbinding
#### [guestNetworkComponentBinding]
A network component that is statically routed to an IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Network_Component_IpAddress'>SoftLayer_Virtual_Guest_Network_Component_IpAddress </a>**

-----
[hardware]: #hardware
#### [hardware]
The hardware that this IP address is routed to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[networkComponent]: #networkcomponent
#### [networkComponent]
A network component that is statically routed to an IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**

-----
[privateNetworkGateway]: #privatenetworkgateway
#### [privateNetworkGateway]
The network gateway appliance using this address as the private IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>**

-----
[protectionAddress]: #protectionaddress
#### [protectionAddress]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Protection_Address'>SoftLayer_Network_Protection_Address[] </a>**

-----
[publicNetworkGateway]: #publicnetworkgateway
#### [publicNetworkGateway]
The network gateway appliance using this address as the public IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>**

-----
[publicVersion6NetworkGateway]: #publicversion6networkgateway
#### [publicVersion6NetworkGateway]
The network gateway appliance using this address as the public IPv6 address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway'>SoftLayer_Network_Gateway </a>**

-----
[remoteManagementNetworkComponent]: #remotemanagementnetworkcomponent
#### [remoteManagementNetworkComponent]
An IPMI-based management network component of the IP address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component </a>**

-----
[subnet]: #subnet
#### [subnet]
An IP address' associated subnet.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet </a>**

-----
[syslogEventsOneDay]: #syslogeventsoneday
#### [syslogEventsOneDay]
All events for this IP address stored in the datacenter syslogs from the last 24 hours  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**

-----
[syslogEventsSevenDays]: #syslogeventssevendays
#### [syslogEventsSevenDays]
All events for this IP address stored in the datacenter syslogs from the last 7 days  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**

-----
[topTenSyslogEventsByDestinationPortOneDay]: #toptensyslogeventsbydestinationportoneday
#### [topTenSyslogEventsByDestinationPortOneDay]
Top Ten network datacenter syslog events, grouped by destination port, for the last 24 hours  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**

-----
[topTenSyslogEventsByDestinationPortSevenDays]: #toptensyslogeventsbydestinationportsevendays
#### [topTenSyslogEventsByDestinationPortSevenDays]
Top Ten network datacenter syslog events, grouped by destination port, for the last 7 days  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**

-----
[topTenSyslogEventsByProtocolsOneDay]: #toptensyslogeventsbyprotocolsoneday
#### [topTenSyslogEventsByProtocolsOneDay]
Top Ten network datacenter syslog events, grouped by source port, for the last 24 hours  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**

-----
[topTenSyslogEventsByProtocolsSevenDays]: #toptensyslogeventsbyprotocolssevendays
#### [topTenSyslogEventsByProtocolsSevenDays]
Top Ten network datacenter syslog events, grouped by source port, for the last 7 days  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**

-----
[topTenSyslogEventsBySourceIpOneDay]: #toptensyslogeventsbysourceiponeday
#### [topTenSyslogEventsBySourceIpOneDay]
Top Ten network datacenter syslog events, grouped by source ip address, for the last 24 hours  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**

-----
[topTenSyslogEventsBySourceIpSevenDays]: #toptensyslogeventsbysourceipsevendays
#### [topTenSyslogEventsBySourceIpSevenDays]
Top Ten network datacenter syslog events, grouped by source ip address, for the last 7 days  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**

-----
[topTenSyslogEventsBySourcePortOneDay]: #toptensyslogeventsbysourceportoneday
#### [topTenSyslogEventsBySourcePortOneDay]
Top Ten network datacenter syslog events, grouped by source port, for the last 24 hours  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**

-----
[topTenSyslogEventsBySourcePortSevenDays]: #toptensyslogeventsbysourceportsevendays
#### [topTenSyslogEventsBySourcePortSevenDays]
Top Ten network datacenter syslog events, grouped by source port, for the last 7 days  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog'>SoftLayer_Network_Logging_Syslog[] </a>**

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
A virtual guest that this IP address is routed to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**

-----
[virtualLicenses]: #virtuallicenses
#### [virtualLicenses]
Virtual licenses allocated for an IP Address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_VirtualLicense'>SoftLayer_Software_VirtualLicense[] </a>**


## Count

-----
[allowedNetworkStorageCount]: #allowednetworkstoragecount
#### [allowedNetworkStorageCount]
A count of the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[allowedNetworkStorageReplicaCount]: #allowednetworkstoragereplicacount
#### [allowedNetworkStorageReplicaCount]
A count of the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.   
<span class="type-label">Type: </span>**unsigned long**


-----
[contextTunnelTranslationCount]: #contexttunneltranslationcount
#### [contextTunnelTranslationCount]
A count of an IPSec network tunnel's address translations. These translations use a SoftLayer ip address from an assigned static NAT subnet to deliver the packets to the remote (customer) destination.   
<span class="type-label">Type: </span>**unsigned long**


-----
[endpointSubnetCount]: #endpointsubnetcount
#### [endpointSubnetCount]
A count of all the subnets routed to an IP address.   
<span class="type-label">Type: </span>**unsigned long**


-----
[protectionAddressCount]: #protectionaddresscount
#### [protectionAddressCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[syslogEventsOneDayCount]: #syslogeventsonedaycount
#### [syslogEventsOneDayCount]
A count of all events for this IP address stored in the datacenter syslogs from the last 24 hours   
<span class="type-label">Type: </span>**unsigned long**


-----
[syslogEventsSevenDayCount]: #syslogeventssevendaycount
#### [syslogEventsSevenDayCount]
A count of all events for this IP address stored in the datacenter syslogs from the last 7 days   
<span class="type-label">Type: </span>**unsigned long**


-----
[topTenSyslogEventsByDestinationPortOneDayCount]: #toptensyslogeventsbydestinationportonedaycount
#### [topTenSyslogEventsByDestinationPortOneDayCount]
A count of top Ten network datacenter syslog events, grouped by destination port, for the last 24 hours   
<span class="type-label">Type: </span>**unsigned long**


-----
[topTenSyslogEventsByDestinationPortSevenDayCount]: #toptensyslogeventsbydestinationportsevendaycount
#### [topTenSyslogEventsByDestinationPortSevenDayCount]
A count of top Ten network datacenter syslog events, grouped by destination port, for the last 7 days   
<span class="type-label">Type: </span>**unsigned long**


-----
[topTenSyslogEventsByProtocolsOneDayCount]: #toptensyslogeventsbyprotocolsonedaycount
#### [topTenSyslogEventsByProtocolsOneDayCount]
A count of top Ten network datacenter syslog events, grouped by source port, for the last 24 hours   
<span class="type-label">Type: </span>**unsigned long**


-----
[topTenSyslogEventsByProtocolsSevenDayCount]: #toptensyslogeventsbyprotocolssevendaycount
#### [topTenSyslogEventsByProtocolsSevenDayCount]
A count of top Ten network datacenter syslog events, grouped by source port, for the last 7 days   
<span class="type-label">Type: </span>**unsigned long**


-----
[topTenSyslogEventsBySourceIpOneDayCount]: #toptensyslogeventsbysourceiponedaycount
#### [topTenSyslogEventsBySourceIpOneDayCount]
A count of top Ten network datacenter syslog events, grouped by source ip address, for the last 24 hours   
<span class="type-label">Type: </span>**unsigned long**


-----
[topTenSyslogEventsBySourceIpSevenDayCount]: #toptensyslogeventsbysourceipsevendaycount
#### [topTenSyslogEventsBySourceIpSevenDayCount]
A count of top Ten network datacenter syslog events, grouped by source ip address, for the last 7 days   
<span class="type-label">Type: </span>**unsigned long**


-----
[topTenSyslogEventsBySourcePortOneDayCount]: #toptensyslogeventsbysourceportonedaycount
#### [topTenSyslogEventsBySourcePortOneDayCount]
A count of top Ten network datacenter syslog events, grouped by source port, for the last 24 hours   
<span class="type-label">Type: </span>**unsigned long**


-----
[topTenSyslogEventsBySourcePortSevenDayCount]: #toptensyslogeventsbysourceportsevendaycount
#### [topTenSyslogEventsBySourcePortSevenDayCount]
A count of top Ten network datacenter syslog events, grouped by source port, for the last 7 days   
<span class="type-label">Type: </span>**unsigned long**


-----
[virtualLicenseCount]: #virtuallicensecount
#### [virtualLicenseCount]
A count of virtual licenses allocated for an IP Address.   
<span class="type-label">Type: </span>**unsigned long**

</div>


