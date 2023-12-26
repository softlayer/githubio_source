---
title: "route"
description: "This interface allows you to change the route of your secondary subnets. It accommodates a number of ways to identify your desired routing destination through the use of a 'type' and 'identifier'. Subnets may be routed as either Static or Portable, and that designation is dictated by the routing destination specified. 

Static subnets have an ultimate routing destination of a single IP address but may not be routed to an existing subnet's IP address whose subnet is routed as a Static. Portable subnets have an ultimate routing destination of a VLAN. 

A subnet can be routed to any resource within the same 'routing region' as the subnet itself. A subnet's routing region can be diverse but is usually limited to a single data center. 

The following identifier 'type' values will result in Static routing: <ul> <li>SoftLayer_Network_Subnet_IpAddress</li> <li>SoftLayer_Hardware_Server</li> <li>SoftLayer_Virtual_Guest</li> </ul> 

The following identifier 'type' values will result in Portable routing: <ul> <li>SoftLayer_Network_Vlan</li> </ul> 

For each identifier type, one or more 'identifier' formats are possible. 

''SoftLayer_Network_Subnet_IpAddress'' will accept the following identifier formats: <ul> <li>An entirely numeric value will be treated as a SoftLayer_Network_Subnet_IpAddress.id value of the desired IP address object.</li> <li>A dotted-quad IPv4 address.</li> <li>A full or compressed IPv6 address.</li> </ul> 

''SoftLayer_Network_Vlan'' will accept the following identifier formats: <ul> <li>An entirely numeric value will be treated as a SoftLayer_Network_Vlan.id value of the desired VLAN object.</li> <li>A semantic VLAN identifier of the form &lt;data center short name&gt;.&lt;router&gt;.&lt;vlan number&gt;, where &lt; and &gt; are literal, eg. dal13.fcr01.1234 - the router name may optionally contain the 'a' or 'b' redundancy qualifier (which has no meaning in this context).</li> </ul> 

''SoftLayer_Hardware_Server'' will accept the following identifier formats: <ul> <li>An entirely numeric value will be treated as a SoftLayer_Hardware_Server.id value of the desired server.</li> <li>A UUID corresponding to a server's SoftLayer_Hardware_Server.globalIdentifier.</li> <li>A value corresponding to a unique SoftLayer_Hardware_Server.hostname.</li> <li>A value corresponding to a unique fully-qualified domain name in the format 'hostname&lt;domain&gt;' where &lt; and &gt; are literal, e.g. myhost&lt;mydomain.com&gt;, hostname refers to SoftLayer_Hardware_Server.hostname and domain to SoftLayer_Hardware_Server.domain, respectively.</li> </ul> 

''SoftLayer_Virtual_Guest'' will accept the following identifier formats: <ul> <li>An entirely numeric value will be treated as a SoftLayer_Virtual_Guest.id value of the desired server.</li> <li>A UUID corresponding to a server's SoftLayer_Virtual_Guest.globalIdentifier.</li> <li>A value corresponding to a unique SoftLayer_Virtual_Guest.hostname.</li> <li>A value corresponding to a unique fully-qualified domain name in the format 'hostname&lt;domain&gt;' where &lt; and &gt; are literal, e.g. myhost&lt;mydomain.com&gt;, hostname refers to SoftLayer_Virtual_Guest.hostname and domain to SoftLayer_Virtual_Guest.domain, respectively.</li> </ul> 

The routing destination result of specifying a SoftLayer_Hardware_Server or SoftLayer_Virtual_Guest type will be the primary IP address of the server for the same network segment the subnet is on. Thus, a public subnet will be routed to the server's public, primary IP address. Additionally, this IP address resolution will match the subnet's IP version; routing a IPv6 subnet to a server will result in selection of the primary IPv6 address of the respective network segment, if available. 

Subnets may only be routed to the IP version they themselves represent. That means an IPv4 subnet can only be routed to IPv4 addresses. Any type/identifier combination that resolves to an IP address must be able to locate an IP address of the same version as the subnet being routed. 

When routing to an IP address on a Primary subnet, only those addresses actively assigned to resources may be targeted. Additionally, the network, gateway, or broadcast address of any Portable subnet may not be a routing destination. For some VLANs utilizing the HSRP redundancy strategy, there are additional addresses which cannot be a route destination. 

When routing a subnet that is already routed, note that the subnet first has its route removed; this procedure is the same as what will occur when using SoftLayer_Network_Subnet::clearRoute. Special consideration should be made for subnets routed as Portable. Please refer to the documentation for SoftLayer_Network_Subnet::clearRoute for details. 

The behavior of this interface is such that either true or false is returned. A response of false indicates the route request would not result in the route of the subnet changing; attempts to route the subnet to the same destination, even if identified by differing means, will result in no changes. A result of false can be interpreted as the route request having already been completed. In contrast, a result of true means the requested destination is different from the current destination and the subnet's routing will be transitioned. This route change is asynchronous to the request. A response of true does not mean the subnet's route has changed, but simply that it will change. In order to monitor for the completion of the change, you may either attempt a route change again until the result is false, or monitor one or more SoftLayer_Network_Subnet properties: subnetType, networkVlanId, and or endPointIpAddress to determine if routing of the subnet has become the desired route destination. 

Use of this operation is limited to a single active request per subnet. If a previous route request is not yet complete, a 'not ready' message will be returned upon subsequent requests. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet/{SoftLayer_Network_SubnetID}/route'
```
