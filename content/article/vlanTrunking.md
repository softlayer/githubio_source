---
title: "VLAN Trunking"
description: "An explanation of how to trunk vlans with the CLI so servers can have access to more than their native VLANs"
date: "2023-12-18"
tags:
    - "article"
    - "sldn"
    - "vlan"
---


# Basics of VLAN Trunking

Trunking VLANs allows you to enable bare metal servers that are in the same POD, but on different primary VLANs, to be able to communicate as if they were on the same VLAN. So if you have `Server1` on `VLAN1`, and `Server2` on `VLAN2` (in the same POD), you could trunk `VLAN2` to `Server1`'s switch port allowing `Server1` to communicate on `VLAN2`.

This article will explain how to do that with the CLI and API tools. See [Configuring VLAN trunks](https://cloud.ibm.com/docs/vlans?topic=vlans-configuring-vlan-trunks&interface=ui) for how to use the UI to do this.
[VLAN Trunks](https://cloud.ibm.com/docs/bare-metal?topic=bare-metal-network-options#bare-metal-vlan-trunks) has some additional information on this topic as well.

The CLI commands were added in [ibmcloud sl v1.5.0](https://github.com/softlayer/softlayer-cli/releases/tag/v1.5.0) and [slcli v6.1.11](https://github.com/softlayer/softlayer-python/releases/tag/v6.1.11)

# View Available VLANs

The first thing to do is figure out which VLANs a server is able to have trunked to it. For this we will use the `hardware vlan-trunkable <hardware-id>` command. It will list all the VLANs available to be trunked to this specific server. In this case we can trunk the Private vlan `1632` or the Public vlan `1163` to server `1907356`

```bash
$> ibmcloud sl hardware vlan-trunkable 1907356
Id        Fully qualified name   Name                 Network
1404269   dal10.bcr01.1632       iSCSI DAL10          PRIVATE
2282899   dal10.fcr01.1163       fmirPublic           PUBLIC
```

To get this information from the API, it can be found in the [Hardware_Server](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server/)->[networkComponents](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Component/)->[networkVLansTrunkable](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Component/#networkVlansTrunkable) property.

```bash
curl -u $SL_USER:$SL_APIKEY https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/1907356.json?objectMask=mask[networkComponents[id,name,port,macAddress,primaryIpAddress,networkVlansTrunkable[id,name,vlanNumber,fullyQualifiedName,networkSpace]]]
```

## Vlans on a server

To see which VLANs a server has access to, use the `hardware detail` command.

```bash
$> ibmcloud.exe  sl hardware detail 1907356
Name               Value
ID                 1907356
GUID               ec3a60fc-fb36-46a7-8d25-76751d504cca
Hostname           testibm
Vlans              Network   Number   ID        Name               Type
                   PRIVATE   777      3029822   dal10.bcr01.777    Primary
                   PUBLIC    2188     3029824   dal10.fcr01.2188   Primary
                   PUBLIC    1455     1404267   dal10.fcr01.1455   Trunked
                   PUBLIC    974      3249384   dal10.fcr01.974    Trunked
```

The Primary VLANs are avilable from the [Hardware_Server](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server)->[networkVlans](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server/#networkVlans) property. The Trunked VLANs are associated with the server's switch port's networkComponent, so you need to request the [Hardware_Server](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server)->[uplinkComponent](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Component/#uplinkComponent)->[networkVlanTrunks](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Component/#networkVlanTrunks)->[networkVlan](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan/) property in your object mask when making API requests.

```bash
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/1907356/getNetworkComponents.json?objectMask=mask[id,uplinkComponent[networkVlanTrunks[networkVlan[networkSpace]]]]'
```

## Servers on a VLAN

If you want to see which servers are on a VLAN, the `vlan detail` command will show that information.

```bash
$> ibmcloud sl  vlan  detail 1404267
Name              Value
id                1404267
number            1455
datacenter        Dallas 10
primary_router    fcr01a.dal10.softlayer.com
hardware          Hostname       domain           public_ip       private_ip
                  testibm        sldn.testcloud   52.118.38.246   10.221.68.227
```

For servers that have `VLAN 1455` as thir primary VLAN, they will show up on the [Network_Vlan](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan)->[hardware](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan/#hardware) property. Finding servers that are trunked into the vlan is slightly convoluted.

[Network_Vlan](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan)->[networkComponentTrunks](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan/#networkComponentTrunks)->[networkComponent](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Component_Network_Vlan_Trunk/#networkComponent)->[downlinkComponent](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Component/#downlinkComponent)->[hardware](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Component/#hardware)
To explain the logic here, a Network_Vlan will have network components trunked to it. These networkComponentTrunks link to a networkComponent, which is the actual switch port the server is connected to. The downlinkComponent from there is the physical network card on the server, which is what the hardware property links to.

An example API call to get all that information:
```bash
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Vlan/1404267/getObject.json?objectMask=mask[primaryRouter[id,fullyQualifiedDomainName,datacenter],hardware,virtualGuests,networkComponentTrunks[networkComponent[downlinkComponent[networkComponentGroup[membersDescription],hardware[tagReferences]]]]]'
```

# Adding and Removing a VLAN

To add or remove a vlan from a server, you can use the `hardware vlan-add <SERVER_ID> <VLAN_ID>...`  and  `hardware vlan-remove <SERVER_ID> <VLAN_ID>...` commands.

```bash
$> ibmcloud sl hardware vlan-add     1907356 1404267
$> ibmcloud sl hardware vlan-remove  1907356 1404267
```

The API this command uses is [SoftLayer_Network_Component::addNetworkVlanTrunks()](https://sldn.softlayer.com/reference/services/SoftLayer_Network_Component/addNetworkVlanTrunks/) or [SoftLayer_Network_Component::removeNetworkVlanTrunks()](https://sldn.softlayer.com/reference/services/SoftLayer_Network_Component/removeNetworkVlanTrunks/). 
That API takes an [init parameter](https://sldn.softlayer.com/article/using-initialization-parameters-softlayer-api/) which is the ID of the appropriate network component attached to the server (the network card's component, not the switch port component which is what you would use when getting the vlan trunks). 
If you are trunking a public vlan, use [SoftLayer_Hardware_Server::getFrontendNetworkComponents(id=1907356, mask='mask[id, name, port, macAddress, primaryIpAddress]')](https://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getFrontendNetworkComponents/) and for private vlans, use [SoftLayer_Hardware_Server::getBackendNetworkComponents(id=1907356, mask='mask[id, name, port, macAddress, primaryIpAddress]')](https://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getBackendNetworkComponents/). Servers will usually have 2 network components for public and private, so make sure to use the ID of the component that has a primaryIpAddress defined.

Once you have the component id, you just need to call the removeNetworkVlanTrunks API and pass in the id of the vlans you want to remove. If you need to remove multiple vlans at once, make sure to pass them all in a single API call. Otherwise you will need to wait for the removal transaction to finish before removing another VLAN.

```bash
curl -u $SL_USER:$SL_APIKEY -X POST '{"parameters": [[{"id": 1404267}]]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Component/13765658/addNetworkVlanTrunks.json'

curl -u $SL_USER:$SL_APIKEY -X POST '{"parameters": [[{"id": 1404267}]]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Component/13765658/removeNetworkVlanTrunks.json'
```
