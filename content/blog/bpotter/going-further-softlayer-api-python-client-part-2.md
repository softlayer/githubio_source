---
title: "Going Further with the SoftLayer API Python Client - Part 2"
description: "<p>In my previous <a href=http://sldn.softlayer.com/blog/bpotter/Going-Further-SoftLayer-API-Python-Client-Part-1>blog"
date: "2015-02-13"
author: "bpotter"
tags:
    - "blog"
---

<p>In my previous <a href="http://sldn.softlayer.com/blog/bpotter/Going-Further-SoftLayer-API-Python-Client-Part-1">blog post</a>, I covered how to navigate the <a href="http://sldn.softlayer.com/reference/services/SoftLayer_Account">SoftLayer Services</a> website, and how to query the SoftLayer API efficiently. In this post, I'll cover additional aspects of using the SoftLayer API with the python client. 
</p>

<h2>List of Services to Start Navigating From</h2>

  <p>If you read <a href="http://sldn.softlayer.com/blog/bpotter/Going-Further-SoftLayer-API-Python-Client-Part-1">part 1</a> of the series, you have a lot of good techniques for querying the data of resources in SoftLayer such that from any service you can efficiently follow the data trail to other services to get to all of the information you want. The last big thing you need to know about querying the SoftLayer API is: Where are the best places in the enormous SoftLayer Services website to begin these trails? The Account service is a good place to start for many data types, but always starting there will not get you to everything. Even if you can eventually get to the data you want by starting with the Account service, there are often shortcuts to be found by starting somewhere else. I've put together a list of useful trail heads and what data types can be found down each trail. This is by no means an exhaustive list, but will hopefully get you started. 
  </p>

  <ul>
  <li><a href="http://sldn.softlayer.com/reference/services/SoftLayer_Account">Account</a>
    <ul>
    <li>getNetworkVlans(): returns the network VLANs in the account, which can also get you to the subnets and primaryRouters 
    <li>getHardware(): returns hardware, which gets you to datacenter, hardDrives, processors, memory, networkCards, operatingSystem which gets you to
passwords
    <li>getVirtualGuests(): returns Virtual_Guest, which gets you to maxCpu, maxMemory, datacenter, operatingSystem 
    <li>getCurrentUser(): returns User_Customer, which gets you to childUsers and permissions 
    <li>getUsers(): returns all of the users in this account
    <li>getNetworkGateways(): returns the gateways (Vyattas), which gets you to the networkVlans associated to (routed by) the gateway, and then the subnets and primaryRouters 
    <li>getTickets(): returns the tickets associated with an account
    <li>getOrders(): returns the orders for this account
    </ul>
  <li><a href="http://sldn.softlayer.com/reference/services/SoftLayer_Location">Location</a>
    <ul>
    <li>getDatacenters(): returns datacenters, which can get you to routers, etc. 
    </ul>
  <li><a href="http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package">Product_Package</a>
    <ul>
    <li>getAllObjects(): returns the products that can be ordered
    <li>getConfiguration(): returns the categories of items (parts) of a product that can be specified when ordering it 
    <li>getItemPrices(): returns the various parts of a product that can be specified when ordering it
    </ul>
  <li><a href="http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order">Billing_Order</a>
    <ul>
    <li>getOrderStatuses(): returns the status for all orders of this account
    </ul>
  <li><a href="http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer">User_Customer</a>
    <ul>
    <li>getChildUsers(): returns the users that are children of (i.e., created by) the current user 
    </ul>
  </ul>

<h2>Services That Modify SoftLayer Resources</h2>

  <p>Now that you are an expert at <strong>querying</strong> the SoftLayer API, let's move on to SoftLayer API calls that <strong>modify</strong> SoftLayer resources. The basics are similar: Find the right service and method within that service, fill out a data structure similar to what it would be like if you queried it, and if this is an existing resource, use the id to identify it. There are <strong>many</strong> SoftLayer API methods that modify resources, but to give you a feel for what they are like, I'll list a few and then give you a detailed example of one. 
  </p>

  <ul>
  <li><a href="http://sldn.softlayer.com/reference/services/SoftLayer_Hardware">Hardware</a>
    <ul>
    <li>editSoftwareComponentPasswords(): notifies SoftLayer that you changed the password of a CCI or bare metal server so it will display correctly in the SoftLayer portal and so SoftLayer support can access the CCI when you have a problem
    </ul>
  <li><a href="http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway">Network_Gateway</a>
    <ul>
    <li>bypassVlans(): change a VLAN that is associated to a gateway from routed state to bypassed state 
    <li>unbypassVlans(): change a VLAN that is associated to a gateway from bypassed state to routed state 
    </ul>
  <li><a href="http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway_Vlan">Network_Gateway_Vlan</a>
    <ul>
    <li>createObjects(): associate VLANs to this gateway (i.e., have the gateway be the router for them) 
    <li>deleteObjects(): disassociate VLANs from this gateway
    </ul>
  <li><a href="http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order">Product_Order</a>
    <ul>
    <li>placeOrder(): order a resource from SoftLayer
    <li>verifyOrder(): verify that your order data structure is valid, but don't actually order the resource 
    </ul>
  <li><a href="http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item">Billing_Item</a>
    <ul>
    <li>cancelItem(): give a resource back to SoftLayer (for monthly items, they are still usable until the end of the month)
    </ul>
  </ul>

  <p>For our detailed example, we will associate VLANs to a network gateway. On the SoftLayer Services website, we find that the <a href="http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway_Vlan">Network_Gateway_Vlan</a> service has a method called <a href="http://sldn.softlayer.com/reference/services/SoftLayer_Network_Gateway_Vlan/createObjects">createObjects</a> that will associate VLANs to a gateway. We see that the argument the method takes is an array of <a href="http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Gateway_Vlan">Network_Gateway_Vlan</a> data type objects.
  So this example will:
  </p>

  <ul>
  <li>Get the id of the gateway we want to associate the VLANs to 
  <li>Get id values of the VLANs to be associated with the gateway
  <li>Build an array of Network_Gateway_Vlan objects; filling in the local properties of that data type 
  <li>Call Network_Gateway_Vlan.createObjects(); giving it that array 
  </ul>

  <code>
import SoftLayer
import pprint

# Get the SoftLayer API client object
client = SoftLayer.Client(username=myuser, api_key=mykey, endpoint_url=SoftLayer.API_PUBLIC_ENDPOINT)

# Get the id of the gateway you want to associate the VLANs to
gateways = client['Account'].getNetworkGateways(mask='id, name', filter={'networkGateways': {'name': {'operation': 'v1'}}})
gatewayid = gateways[0]['id']

# Get all of the VLANs that are allowed to be associated with this gateway.
# For this example, we assume we want to associate all of them.
vlans = client['Network_Gateway'].getPossibleInsideVlans(id=gatewayid, mask='id, vlanNumber')

# Build the array of Network_Gateway_Vlan objects.
# It's local properties are: bypassFlag, id, networkGatewayId, networkVlanId.
objs = []
for v in vlans:
    # Fill in the object properties. We set id to None, because SoftLayer will fill that in when the
    # objects are created.
    objs.append({'bypassFlag':True, 'id':None, 'networkGatewayId':gatewayid, 'networkVlanId':v['id']})

# Use the Network_Gateway_Vlan service to associate them
assocVlans = client['Network_Gateway_Vlan'].createObjects(objs)
# the output is the created Network_Gateway_Vlan objects
pprint.pprint(assocVlans)</code>

<h2>SoftLayer Exceptions</h2>

<p>You probably noticed that none of the example code had error checking. That's because I was waiting to cover SoftLayer exceptions here. The main SoftLayer API exception class is SoftLayer.exceptions.SoftLayerAPIError, and it has two members: faultCode and faultString. You can catch API errors like this:</p>

  <code>import SoftLayer

# Get the SoftLayer API client object
client = SoftLayer.Client(username=myuser, api_key=mykey, endpoint_url=SoftLayer.API_PUBLIC_ENDPOINT)

try:
    # A sample API call
    gatewayid = 1      # an id that does not exist
    gw = client['Network_Gateway'].getObject(id=gatewayid, mask='id')
except SoftLayer.exceptions.SoftLayerAPIError as e:
    print 'SoftLayer exception occurred: ' + str(e.faultCode) + ': ' + e.faultString</code>

  <p>You can see some of the common faultStrings at the bottom of <a href="http://sldn.softlayer.com/article/Exception-Handling-SoftLayer-API">http://sldn.softlayer.com/article/Exception-Handling-SoftLayer-API</a> in case you want to handle some of them individually in the "except" section of your code.
  </p>

<p>In my next blog post I'll cover in detail how to order SoftLayer resources using the API.</p>

