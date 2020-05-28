---
title: "Classic Infrastructure Networking"
description: "An overview of how networking is connected "
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
    - "permissions"
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

- [Vlan Trunking Example](python/vlanTagging/)
- [SoftLayer_Network_Component::addNetworkVlanTrunks](/reference/services/SoftLayer_Network_Component/addNetworkVlanTrunks/) Adds a VLAN trunk to a Network Component
- [SoftLayer_Network_Component::removeNetworkVlanTrunks](/reference/services/SoftLayer_Network_Component/removeNetworkVlanTrunks/) Removes a VLAN trunk to a Network Component
- [SoftLayer_Network_Component::getNetworkVlanTrunks](/reference/services/SoftLayer_Network_Component/getNetworkVlanTrunks/) Lists all VLAN trunks on a Network Component


## Types of network setups


https://cloud.ibm.com/docs/bare-metal?topic=bare-metal-about-bm#network-redundancy

- Automatic ?
- User managed


VLANS:
id, networkVlan, name
2797214 :  826   : networkTest

COMPONENTS

========
       {
            "id": 10626113,
            "name": "eth",
            "networkVlanTrunks": [],
            "port": 1,
            "primaryIpAddress": "10.152.17.213",
            "speed": 1000,
            "uplinkComponent": {
                "id": 5959217,
                "networkVlan": {
                    "accountId": 307608,
                    "id": 2797108,
                    "modifyDate": "2020-02-05T14:47:09-06:00",
                    "primarySubnetId": 2356598,
                    "vlanNumber": 797
                },
                "networkVlanTrunks": [
                    {
                        "networkComponentId": 5959217,
                        "networkVlanId": 2797214
                    }
                ]
            }
        },
        {
            "id": 10626117,
            "name": "eth",
            "networkVlanTrunks": [],
            "port": 3,
            "primaryIpAddress": null,
            "speed": 1000,
            "uplinkComponent": {
                "id": 5961549,
                "networkVlan": {
                    "accountId": 307608,
                    "id": 2797108,
                    "modifyDate": "2020-02-05T14:47:09-06:00",
                    "primarySubnetId": 2356598,
                    "vlanNumber": 797
                },
                "networkVlanTrunks": [
                    {
                        "networkComponentId": 5961549,
                        "networkVlanId": 2797214
                    }
                ]
            }
        },
=======

mask[id,hostname,networkComponents[port,speed,networkVlanTrunks,name,id,uplinkComponent[networkVlan,networkVlanTrunks[networkVlan],id],primaryIpAddress],networkVlans]

slcli --format=json call-api SoftLayer_Hardware_Server getObject --id=1398593 --mask="mask[id,hostname,networkComponents[port,speed,networkVlanTrunks,name,id,uplinkComponent[networkVlan,networkVlanTrunks[networkVlan],id],primaryIpAddress],networkVlans]"
{
    "hostname": "networktest",
    "id": 1398593,
    "networkComponents": [
        {
            "id": 10626113,
            "name": "eth",
            "networkVlanTrunks": [],
            "port": 1,
            "primaryIpAddress": "10.152.17.213",
            "speed": 1000,
            "uplinkComponent": {
                "id": 5959217,
                "networkVlan": {
                    "accountId": 307608,
                    "id": 2797108,
                    "modifyDate": "2020-02-05T14:47:09-06:00",
                    "primarySubnetId": 2356598,
                    "vlanNumber": 797
                },
                "networkVlanTrunks": [
                    {
                        "networkComponentId": 5959217,
                        "networkVlan": {
                            "accountId": 307608,
                            "id": 2797214,
                            "modifyDate": "2020-02-05T15:31:46-06:00",
                            "name": "networkTest",
                            "primarySubnetId": 1448573,
                            "vlanNumber": 826
                        },
                        "networkVlanId": 2797214
                    }
                ]
            }
        },
        {
            "id": 10626117,
            "name": "eth",
            "networkVlanTrunks": [],
            "port": 3,
            "primaryIpAddress": null,
            "speed": 1000,
            "uplinkComponent": {
                "id": 5961549,
                "networkVlan": {
                    "accountId": 307608,
                    "id": 2797108,
                    "modifyDate": "2020-02-05T14:47:09-06:00",
                    "primarySubnetId": 2356598,
                    "vlanNumber": 797
                },
                "networkVlanTrunks": [
                    {
                        "networkComponentId": 5961549,
                        "networkVlan": {
                            "accountId": 307608,
                            "id": 2797214,
                            "modifyDate": "2020-02-05T15:31:46-06:00",
                            "name": "networkTest",
                            "primarySubnetId": 1448573,
                            "vlanNumber": 826
                        },
                        "networkVlanId": 2797214
                    }
                ]
            }
        },
    ]
}