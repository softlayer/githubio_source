---
title: "SoftLayer_Network_Subnet"
description: "Every SoftLayer ip address is associated with a subnet which is defined in the SoftLayer_Network_Subnet service. SoftLay... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
---
# SoftLayer_Network_Subnet
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Subnet' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet' >Datatype</a></li>
    </ul>
</div>

## Description
Every SoftLayer ip address is associated with a subnet which is defined in the SoftLayer_Network_Subnet service. SoftLayer subnets define a group of ip addresses and are assigned to a SoftLayer_Network_Vlan.  The SoftLayer_Network_Subnet service gives you information about your subnet such as your network address, broadcast address, the subnet gateway address, and the total number of IP addresses within the subnet. Use the data returned by these methods with other API services to get more detailed information about your services. 

Along with VLANs, subnets are an integral part of the SoftLayer network. Each server ordered by SoftLayer comes with at least one public and one private subnet, with more available for order in the customer portal. Subnets exist in the SoftLayer network as either interfaces on a VLAN or as route destination from an IP address or VLAN. 

SoftLayer customers can order and manage subnets through the customer portal. If you need to cancel a subnet please open a sales ticket in our customer portal and our account management staff will assist you. 

### External Links


* [Subnetwork at Wikipedia](http://en.wikipedia.org/wiki/Subnetwork)


* [RFC950:Internet Standard Subnetting Procedure at ietf.org](http://tools.ietf.org/html/rfc950)




### seeAlso

* [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan )


* [SoftLayer_Network_IpAddress](/reference/datatypes/SoftLayer_Network_IpAddress )


        
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

#### [allowAccessToNetworkStorage](/reference/services/SoftLayer_Network_Subnet/allowAccessToNetworkStorage)
Allow access to a SoftLayer_Network_Storage volume from this device. 
</div>

<div class="method-row">

#### [allowAccessToNetworkStorageList](/reference/services/SoftLayer_Network_Subnet/allowAccessToNetworkStorageList)
Allow access to multiple SoftLayer_Network_Storage volumes from this device. 
</div>

<div class="method-row">

#### [clearRoute](/reference/services/SoftLayer_Network_Subnet/clearRoute)

</div>

<div class="method-row">

#### [createReverseDomainRecords](/reference/services/SoftLayer_Network_Subnet/createReverseDomainRecords)
Create the default PTR records for this subnet
</div>

<div class="method-row">

#### [createSubnetRouteUpdateTransaction](/reference/services/SoftLayer_Network_Subnet/createSubnetRouteUpdateTransaction)
create a new transaction to modify a subnet route.
</div>

<div class="method-row">

#### [createSwipTransaction](/reference/services/SoftLayer_Network_Subnet/createSwipTransaction)
create a SWIP transaction for a subnet
</div>

<div class="method-row">

#### [editNote](/reference/services/SoftLayer_Network_Subnet/editNote)
Edit the note for this subnet.
</div>

<div class="method-row">

#### [findAllSubnetsAndActiveSwipTransactionStatus](/reference/services/SoftLayer_Network_Subnet/findAllSubnetsAndActiveSwipTransactionStatus)
Retrieve a list of subnets along with their SWIP transaction statuses.
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Subnet/getAccount)

</div>

<div class="method-row">

#### [getActiveRegistration](/reference/services/SoftLayer_Network_Subnet/getActiveRegistration)
Retrieve if present, the active registration for this subnet.
</div>

<div class="method-row">

#### [getActiveSwipTransaction](/reference/services/SoftLayer_Network_Subnet/getActiveSwipTransaction)
Retrieval: DEPRECATED
</div>

<div class="method-row">

#### [getActiveTransaction](/reference/services/SoftLayer_Network_Subnet/getActiveTransaction)
Retrieve the billing item for a subnet.
</div>

<div class="method-row">

#### [getAddressSpace](/reference/services/SoftLayer_Network_Subnet/getAddressSpace)
Retrieve identifier which distinguishes what classification of addresses the subnet represents.
</div>

<div class="method-row">

#### [getAllowedHost](/reference/services/SoftLayer_Network_Subnet/getAllowedHost)
Retrieve the SoftLayer_Network_Storage_Allowed_Host information to connect this Subnet to Network Storage supporting access control lists.
</div>

<div class="method-row">

#### [getAllowedNetworkStorage](/reference/services/SoftLayer_Network_Subnet/getAllowedNetworkStorage)
Retrieve the SoftLayer_Network_Storage objects that this SoftLayer_Hardware has access to.
</div>

<div class="method-row">

#### [getAllowedNetworkStorageReplicas](/reference/services/SoftLayer_Network_Subnet/getAllowedNetworkStorageReplicas)
Retrieve the SoftLayer_Network_Storage objects whose Replica that this SoftLayer_Hardware has access to.
</div>

<div class="method-row">

#### [getAttachedNetworkStorages](/reference/services/SoftLayer_Network_Subnet/getAttachedNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes authorized to this device. 
</div>

<div class="method-row">

#### [getAvailableNetworkStorages](/reference/services/SoftLayer_Network_Subnet/getAvailableNetworkStorages)
Return a list of SoftLayer_Network_Storage volumes that can be authorized to this device. 
</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Network_Subnet/getBillingItem)
Retrieve the billing item for a subnet.
</div>

<div class="method-row">

#### [getBoundDescendants](/reference/services/SoftLayer_Network_Subnet/getBoundDescendants)

</div>

<div class="method-row">

#### [getBoundRouterFlag](/reference/services/SoftLayer_Network_Subnet/getBoundRouterFlag)
Retrieve whether or not this subnet is associated with a router. Subnets that are not associated with a router cannot be routed.
</div>

<div class="method-row">

#### [getBoundRouters](/reference/services/SoftLayer_Network_Subnet/getBoundRouters)

</div>

<div class="method-row">

#### [getChildren](/reference/services/SoftLayer_Network_Subnet/getChildren)

</div>

<div class="method-row">

#### [getDatacenter](/reference/services/SoftLayer_Network_Subnet/getDatacenter)
Retrieve the data center this subnet may be routed within.
</div>

<div class="method-row">

#### [getDescendants](/reference/services/SoftLayer_Network_Subnet/getDescendants)

</div>

<div class="method-row">

#### [getDisplayLabel](/reference/services/SoftLayer_Network_Subnet/getDisplayLabel)

</div>

<div class="method-row">

#### [getEndPointIpAddress](/reference/services/SoftLayer_Network_Subnet/getEndPointIpAddress)
Retrieve a static routed ip address
</div>

<div class="method-row">

#### [getGlobalIpRecord](/reference/services/SoftLayer_Network_Subnet/getGlobalIpRecord)

</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Network_Subnet/getHardware)
Retrieve the hardware using IP addresses on this subnet.
</div>

<div class="method-row">

#### [getIpAddresses](/reference/services/SoftLayer_Network_Subnet/getIpAddresses)
Retrieve all the ip addresses associated with a subnet.
</div>

<div class="method-row">

#### [getNetworkComponentFirewall](/reference/services/SoftLayer_Network_Subnet/getNetworkComponentFirewall)
Retrieve the upstream network component firewall.
</div>

<div class="method-row">

#### [getNetworkProtectionAddresses](/reference/services/SoftLayer_Network_Subnet/getNetworkProtectionAddresses)

</div>

<div class="method-row">

#### [getNetworkTunnelContexts](/reference/services/SoftLayer_Network_Subnet/getNetworkTunnelContexts)
Retrieve iPSec network tunnels that have access to a private subnet.
</div>

<div class="method-row">

#### [getNetworkVlan](/reference/services/SoftLayer_Network_Subnet/getNetworkVlan)
Retrieve the VLAN object that a subnet is associated with.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Subnet/getObject)
Retrieve a SoftLayer_Network_Subnet record.
</div>

<div class="method-row">

#### [getPodName](/reference/services/SoftLayer_Network_Subnet/getPodName)
Retrieve the pod in which this subnet resides.
</div>

<div class="method-row">

#### [getProtectedIpAddresses](/reference/services/SoftLayer_Network_Subnet/getProtectedIpAddresses)

</div>

<div class="method-row">

#### [getRegionalInternetRegistry](/reference/services/SoftLayer_Network_Subnet/getRegionalInternetRegistry)

</div>

<div class="method-row">

#### [getRegistrations](/reference/services/SoftLayer_Network_Subnet/getRegistrations)
Retrieve all registrations that have been created for this subnet.
</div>

<div class="method-row">

#### [getReverseDomain](/reference/services/SoftLayer_Network_Subnet/getReverseDomain)
Retrieve the reverse DNS domain associated with this subnet.
</div>

<div class="method-row">

#### [getReverseDomainRecords](/reference/services/SoftLayer_Network_Subnet/getReverseDomainRecords)
Retrieve all reverse DNS records associated with a subnet.
</div>

<div class="method-row">

#### [getRoleKeyName](/reference/services/SoftLayer_Network_Subnet/getRoleKeyName)
Retrieve an identifier of the role the subnet is within. Roles dictate how a subnet may be used.
</div>

<div class="method-row">

#### [getRoleName](/reference/services/SoftLayer_Network_Subnet/getRoleName)
Retrieve the name of the role the subnet is within. Roles dictate how a subnet may be used.
</div>

<div class="method-row">

#### [getRoutableEndpointIpAddresses](/reference/services/SoftLayer_Network_Subnet/getRoutableEndpointIpAddresses)
Retrieve IP addresses which may be used as a routing endpoint from a subnet.
</div>

<div class="method-row">

#### [getRoutingTypeKeyName](/reference/services/SoftLayer_Network_Subnet/getRoutingTypeKeyName)
Retrieve the identifier for the type of route then subnet is currently configured for.
</div>

<div class="method-row">

#### [getRoutingTypeName](/reference/services/SoftLayer_Network_Subnet/getRoutingTypeName)
Retrieve the name for the type of route then subnet is currently configured for.
</div>

<div class="method-row">

#### [getSubnetForIpAddress](/reference/services/SoftLayer_Network_Subnet/getSubnetForIpAddress)
Retrieve an IP addresses's associated subnet.
</div>

<div class="method-row">

#### [getSwipTransaction](/reference/services/SoftLayer_Network_Subnet/getSwipTransaction)
Retrieval: DEPRECATED
</div>

<div class="method-row">

#### [getTagReferences](/reference/services/SoftLayer_Network_Subnet/getTagReferences)
Retrieve references to all tags for this subnet.
</div>

<div class="method-row">

#### [getUnboundDescendants](/reference/services/SoftLayer_Network_Subnet/getUnboundDescendants)

</div>

<div class="method-row">

#### [getUtilizedIpAddressCount](/reference/services/SoftLayer_Network_Subnet/getUtilizedIpAddressCount)
Retrieve provides the total number of utilized IP addresses on this subnet. The primary consumer of IP addresses are compute resources, which can consume more than one address. This value is only supported for primary subnet types.
</div>

<div class="method-row">

#### [getVirtualGuests](/reference/services/SoftLayer_Network_Subnet/getVirtualGuests)
Retrieve the Virtual Servers using IP addresses on this subnet.
</div>

<div class="method-row">

#### [removeAccessToNetworkStorageList](/reference/services/SoftLayer_Network_Subnet/removeAccessToNetworkStorageList)
Remove access to multiple SoftLayer_Network_Storage volumes from this device. 
</div>

<div class="method-row">

#### [route](/reference/services/SoftLayer_Network_Subnet/route)

</div>

<div class="method-row">

#### [setTags](/reference/services/SoftLayer_Network_Subnet/setTags)

</div>
</div>

</div>

