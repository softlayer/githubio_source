---
title: "SoftLayer_Network_Subnet_IpAddress_UsageDetail"
description: "Describes an IP address assigned to a resource on your network. 

Details on the associated resource are also provided, described below. Details include the resource's type, unique identifier, name, fully qualified name, and context, the contents of which depends on the resource's type. If the fully qualified name is not included for a resource type below, the resource's name will apply. 

The following resource types and associated dependent properties are supported: 


* <b>HARDWARE</b>: A [Bare Metal Server](/reference/datatypes/SoftLayer_Hardware_Server)


-- <i>resourceName</i>: The hostname of the server. 

-- <i>resourceFullyQualifiedName</i>: The fully qualified domain name of the server. 

-- <i>resourceContext</i>: The name of the network component or network component group assigned to the IP address, <i>e.g. eth0/2</i>. 


* <b>GUEST</b>: A [Virtual Server Instance](/reference/datatypes/SoftLayer_Virtual_Guest)


-- <i>resourceName</i>: The hostname of the guest. 

-- <i>resourceFullyQualifiedName</i>: The fully qualified domain name of the guest. 

-- <i>resourceContext</i>: The name of the virtual network component assigned to the IP address, <i>e.g. eth0</i>. 


* <b>GATEWAY</b>: A [Network Gateway](/reference/datatypes/SoftLayer_Network_Gateway)


-- <i>resourceName</i>: The name of the gateway. 

-- <i>resourceContext</i>: Either the term 'virtual' to indicate a gateway IP address, or the name of the network component or network component group assigned to the IP address followed by the id-value of the [Bare Metal Server](/reference/datatypes/SoftLayer_Hardware_Server) gateway member surrounded by '<', '>', <i>e.g. eth1/3<123456></i>. 

- <b>FIREWALL_MULTIVLAN</b>: A [Multi-VLAN Firewall](/reference/datatypes/SoftLayer_Network_Vlan_Firewall) 

-- <i>resourceName</i>: The name of the firewall. 

-- <i>resourceContext</i>: The term 'virtual' to indicate a firewall IP address. 

- <b>LBAAS</b>: A [Cloud Load Balancer](/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer) 

-- <i>resourceName</i>: The name of the load balancer. 

-- <i>resourceFullyQualifiedName</i>: The full DNS address of the load balancer. 

-- <i>resourceContext</i>: The term 'ephemeral' to indicate a currently assigned IP address, subject to change. Users are strongly encouraged to access the service by the fully qualified DNS name and not the underlying IP addresses. The UUID of the load balancer is also provided, surrounded by '<' and '>', e.g. ephemeral<84f0affb-0d5e-40f1-ad87-a92d6544936a> 

- <b>NETSCALER_VPX</b>: A [Netscaler VPX Load Balancer](/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller) 

-- <i>resourceName</i>: The hostname of the load balancer. 

-- <i>resourceFullyQualifiedName</i>: The fully qualified domain name of the load balancer. 

-- <i>resourceContext</i>: Either the term 'nsip' to indicate the management IP address, or the name of the network component assigned to the IP address followed by the id-value of the [Virtual Server Instance](/reference/datatypes/SoftLayer_Virtual_Guest) load balancer host surrounded by '<', '>', <i>e.g. eth1<123456></i>. 

- <b>NETSCALER_MPX</b>: A [Netscaler MPX Load Balancer](/reference/datatypes/SoftLayer_Hardware_LoadBalancer) 

-- <i>resourceName</i>: The hostname of the load balancer. 

-- <i>resourceFullyQualifiedName</i>: The fully qualified domain name of the load balancer. 

-- <i>resourceContext</i>: The name of the network component or network component group assigned to the IP address, <i>e.g. eth0/2</i>. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress_UsageDetail"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Network_Subnet_IpAddress_UsageDetail"
---
