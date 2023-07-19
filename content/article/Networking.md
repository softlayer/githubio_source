---
title: "Classic Infrastructure Networking"
description: "An overview of how networking is connected on Classic Infrastructure, and the APIs used to control it. "
date: "2020-05-29"
tags:
    - "article"
    - "sldn"
    - "network"
---



# POPs and PODs
A Point Of Presence (POP) refers to the networking equipment responsible for handling traffic from The Internet and customer Direct Links. Each POP is connected to at least two others on our backend network

A Point of Delivery (POD) is a segmentation of our physical datacenters. Each POP will service several POD, although some POPs are standalone. These PODs are generally recognizable by their router in the datacenter.


## Listing Datacenters and PODs
[SoftLayer_Location_Datacenter::getDatacenters](https://sldn.softlayer.com/reference/services/SoftLayer_Location_Datacenter/getDatacenters/) will return a list of all Datacenters and with an objectMask, can return each datacenter's routers.

Here, we have to force the API to use the SoftlLayer_Location_Datacenter objectMask instead of the default return type of SoftLayer_Location. That is why the objectMask is like `mask(SoftLayer_Location_Datacenter)[`.

#### SLCLI
```
slcli -vvv  call-api SoftLayer_Location_Datacenter getDatacenters  --mask="mask(SoftLayer_Location_Datacenter)[backendHardwareRouters[id,hostname]]"
```

#### REST
```
curl -u $SL_USER:$SL_APIKEY   'https://api.softlayer.com/rest/v3.1/SoftLayer_Location_Datacenter/getDatacenters.json?objectMask=mask%28SoftLayer_Location_Datacenter%29%5BbackendHardwareRouters%5Bid%2Chostname%5D%5D'
```


#### Result

```
:............................:.........:..............:.......:..........:
:   backendHardwareRouters   :    id   :   longName   :  name : statusId :
:............................:.........:..............:.......:..........:
: :..............:........:  :  265592 : Amsterdam 1  : ams01 :    2     :
: :   hostname   :   id   :  :         :              :       :          :
: :..............:........:  :         :              :       :          :
: : bcr01a.ams01 : 117917 :  :         :              :       :          :
: : bcr02a.ams01 : 190854 :  :         :              :       :          :
: :..............:........:  :         :              :       :          :
:............................:.........:..............:.......:..........:
```


bcr01a is Backend Customer Router 01a, so POD 1.
bcr02a is Backend Customer Router 02a, so Pod 2.

Each router will also have a `b` pair, but usually the API will only return the `a` of the pair, which is what we need for ordering purposes.


Selecting the correct POD at order time is important if you need all of your servers in the same datacenter to be on the same vlan or IP subnet.  


# VLANs
[VLANs](https://cloud.ibm.com/docs/vlans?topic=vlans-getting-started) are a way to isolate network traffic between servers. Each network capable resource provisioned will have at least one VLAN per network (Public/Private). This is done automatically and in general, doesn't need to be changed by the end user. 


## [Vlan Spanning](https://cloud.ibm.com/docs/vlans?topic=vlans-vlan-spanning)
By default this feature is disabled, preventing servers in your account from communicating with each other over the private network if they are on different VLANs. However this can be enabled quite easily either in the portal, or with [SoftLayer_Account::setVlanSpan](reference/services/SoftLayer_Account/setVlanSpan/)

## Vlan Trunking/Tagging
VLan Trunking (or tagging) allows a server's network component to exist on multiple VLANs at the same time. This can only be done through the API.

- [Vlan Trunking Example](/python/vlanTagging/)
- [SoftLayer_Network_Component::addNetworkVlanTrunks](/reference/services/SoftLayer_Network_Component/addNetworkVlanTrunks/) Adds a VLAN trunk to a Network Component
- [SoftLayer_Network_Component::removeNetworkVlanTrunks](/reference/services/SoftLayer_Network_Component/removeNetworkVlanTrunks/) Removes a VLAN trunk to a Network Component
- [SoftLayer_Network_Component::getNetworkVlanTrunks](/reference/services/SoftLayer_Network_Component/getNetworkVlanTrunks/) Lists all VLAN trunks on a Network Component


## Useful VLAN APIs
+ [SoftLayer_Network_Component::getVlan](reference/services/SoftLayer_Network_Component/getNetworkVlan/) Gets the primary VLAN associated with a specific network component
+ [SoftLayer_Network_Vlan](/reference/services/SoftLayer_Network_Vlan/) most vlans will be of this Class
+ [SoftLayer_Network_Gateway_Vlan](/reference/services/SoftLayer_Network_Gateway_Vlan/) Vlans that belong to a gateway device.

# [Subnets](https://cloud.ibm.com/docs/subnets?topic=subnets-getting-started)
Subnets exist on VLANs, and provide compute resources IP addresses to access the network.  There are several different types of subnets to be concerned about.

#### Primary
These are used by our provisoining system to automatically give an IP address to a compute resource. __NEVER__ manually distribute IP space from these subnets, it disrupt provisioning on your account since our system will not know if you are using an IP out of this subnet.

#### Secondary Static
These subnets are routed to a specific IP address, and allow the server associated with the static IP to use all the ips in this subnet.

#### Secondary Portable
These subnets are routed to a VLAN, and allows any server on that vlan access to IP space here. You lose 3 IPs for the Network IP, Gateway Ip, and Broadcast Ip.

## Useful Subnet APIs
+ [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet/) Service used for interacting with subnets
    * [createReverseDomainRecords](https://sldn.softlayer.com/reference/services/SoftLayer_Network_Subnet/createReverseDomainRecords/) Create the default PTR records for this subnet
    * [editNote](/reference/services/SoftLayer_Network_Subnet/editNote/) Allows editing a subnet's note.
+ [SoftLayer_Network_Subnet_IpAddress](/reference/services/SoftLayer_Network_Subnet_IpAddress/) Service used for interacting with IP addresses
    * [findByIpv4Address](/reference/services/SoftLayer_Network_Subnet_IpAddress/findByIpv4Address/) Looks up an IP address record by its ipv4 address
    * [getVirtualGuest](/reference/services/SoftLayer_Network_Subnet_IpAddress/getVirtualGuest/) and [getHardware](/reference/services/SoftLayer_Network_Subnet_IpAddress/getHardware/) let you look up the VirtualGuest or Hardware object associated with a Primary IP
+ [SoftLayer_Network_Subnet_Rwhois_Data](/reference/services/SoftLayer_Network_Subnet_Rwhois_Data/) Service for interacting with Rwhois data.

