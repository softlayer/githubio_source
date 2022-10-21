---
title: "Basic and Advanced Ordering"
description: "A breakdown of Classic Infrastructure Ordering."
date: "2020-08-24"
author: "Christopher Gallo"
tags:
    - "article"
    - "ordering"
    - "quotes"
---

## The Catalog
Before we can order anything, we need a list of the valid price IDs that represent our order. This article on [The Catalog](/article/catalog/) will explain how to retrieve those. Always remember that the price ID that represents a specific item can change at any time, without notice, but the item's KeyName will not. So it is always important before submitting an order to lookup the item keynames to fine the current price ID. While price IDs don't change often, not using a current one will cause your order to fail with the exception `SoftLayer_Exception_Public: Price # 454616 does not exist.`


## [A Simple Order](#simple_order) {#simple_order .anchor-link}
In these examples, we will be using [SoftLayer_Product_Order::verifyOrder()](/reference/services/SoftLayer_Product_Order/verifyOrder/), which will let us know if our order would have worked, without actually placing an order. [SoftLayer_Product_Order::placeOrder()](/reference/services/SoftLayer_Product_Order/placeOrder/) is what you would need to use to actually order something, it takes the exact same options as verifyOrder, so the only thing you need to change is the word `verify` to `place`.

To start off with, this method takes in one parameters, called `orderData`, which is a [SoftLayer_Container_Product_Order](/reference/datatypes/SoftLayer_Container_Product_Order/) type. This is the generic container, you will likely want to refer to the container that matches the product you are ordering. While the containers are mostly the same, some offer different fields that you might need to set when ordering different products. These containers will all start with `SoftLayer_Container_Product_Order_`

#### Most common containers
- [SoftLayer_Container_Product_Order_Hardware_Server](/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server/)
- [SoftLayer_Container_Product_Order_Hardware_Server_Upgrade](/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server_Upgrade)
- [SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance](/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance)
- [SoftLayer_Container_Product_Order_Network_LoadBalancer_AsAService](/reference/datatypes/SoftLayer_Container_Product_Order_Network_LoadBalancer_AsAService)
- [SoftLayer_Container_Product_Order_Network_Storage_AsAService](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_AsAService)
- [SoftLayer_Container_Product_Order_Network_Subnet](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Subnet)
- [SoftLayer_Container_Product_Order_Network_Vlan](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Vlan)
- [SoftLayer_Container_Product_Order_Virtual_Guest](/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Guest)
- [SoftLayer_Container_Product_Order_Virtual_DedicatedHost](/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_DedicatedHost)
- [SoftLayer_Container_Product_Order_Virtual_ReservedCapacity](/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_ReservedCapacity)


#### Base POST Datastructure

Below is what a basic order structure would look like. The container is defined by adding `complexType` to the order container.

```json
{
  "parameters": [
    {
      "location": "449600",
      "packageId": 1035,
      "presetId": 559,
      "prices": [
        {
          "id": 241898,
          "item": {
            "description": "Debian GNU/Linux 10.x Buster/Stable - Minimal Install (64 bit)"
          }
        },
        {
          "id": 1639,
          "item": {
            "description": "100 GB (SAN)"
          }
        },
        {
          "id": 905,
          "item": {
            "description": "Reboot / Remote Console"
          }
        },
        {
          "id": 210301,
          "item": {
            "description": "100 Mbps Public & Private Network Uplinks"
          }
        },
        {
          "id": 1800,
          "item": {
            "description": "0 GB Bandwidth Allotment"
          }
        },
        {
          "id": 21,
          "item": {
            "description": "1 IP Address"
          }
        },
        {
          "id": 210349,
          "item": {
            "description": "Host Ping and TCP Service Monitoring"
          }
        },
        {
          "id": 57,
          "item": {
            "description": "Email and Ticket"
          }
        }, 
        {
          "id": 210353,
          "item": {
            "description": "Automated Reboot from Monitoring"
          }
        },
        {
          "id": 420,
          "item": {
            "description": "Unlimited SSL VPN Users"
          }
        },
        {
          "id": 17129,
          "item": {
            "description": "1 IPv6 Address"
          }
        }
      ],
      "quantity": 1,
      "useHourlyPricing": true,
      "virtualGuests": [{"domain": "ibm.com","hostname": "test-order"}],
      "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest"
    }
  ]
}
```

#### The container
- location: The SoftLayer_Location Id of where you want this order to be provisioned in.
- packageId: Package from which the price Ids can be found in.
- presetId: Virtual Guests use presets, or flavors, to define the CPU/RAM/First Disk size, this field lets you define that.
- prices: An array of price objects. You only need to specify the ID property of each price object. Included in this example is the item->description property to help you understand which price Id goes to which item.
- quantity: How many of these to order. If you want more than 1, the virtualGuests or hardware property needs to have the same number of objects in it.
- userHourlyPricing: Use hourly pricing.
- virtualGuests / hardware: An array containing the detail for each server to be ordered. The number of objects in this array should match `quantity`. 
- complexType: Defines the specific container to use.



## [Complex Orders](#comple_order) {#complex_order .anchor_link}

While the above example lets you order multiple products that have the exact same configuration, ordering different products in the same API call is a little more complicated.

First, take note of the [`orderContainers`](/reference/datatypes/SoftLayer_Container_Product_Order/#ordercontainers) property. This property is an array of containers. The structure of the API call would look something like this:

```json
{
  "parameters":[
    {
      "orderContainers": [
        {  
               "complexType":"SoftLayer_Container_Product_Order_Virtual_Guest",
               "containerIdentifier": "OptionalId",
               "prices":[]
        },
        {  
               "complexType":"SoftLayer_Container_Product_Order_Virtual_Guest",
               "containerIdentifier": "VirtualGuest2",
               "prices":[]
        }
    ]}
]}
```

The `orderContainers` property can be a mix of complexTypes as well. When ordering this way, the "top level" container will only have the `orderContainers` property defined.


#### A Full Example
Below is an example that will order serveral Virtual Guests of differing configurations, with different options.

```
curl -u $SL_USER:$SL_APIKEY  -X POST -d  @testOrder.json 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/verifyOrder'
```

`testOrder.json`
```json
{
  "parameters":[
    {
      "orderContainers": [
        {  
            "complexType":"SoftLayer_Container_Product_Order_Virtual_Guest",
            "containerIdentifier": "Container1",
            "virtualGuests": [
                {
                    "hostname": "test", "domain": "ibm.com",
                    "primaryNetworkComponent": {
                            "networkVlan": {
                                    "id": 123, 
                                    "primarySubnet": {"id": 12345}
                                }
                        }
                }
            ],
            "location":"DALLAS13",
            "packageId":835,
            "presetId": 405,
            "prices":[
                {"id":45466},{"id":2202},{"id":1800},{"id":273},{"id":55},
                {"id":58},{"id":420},{"id":21},{"id":57},{"id":905}
            ],
            "sshKeys":[{"id":9999}],
            "quantity":1
        },
        {
            "complexType":"SoftLayer_Container_Product_Order_Virtual_Guest",
            "containerIdentifier": "Container2",
            "hardware": [{"hostname": "hostname2", "domain": "ibm.com"}],
            "location":449600,
            "quantity":1,
            "packageId":835,
            "reservedCapacityId":6701,
            "useHourlyPricing":false,
            "presetId":337,
            "prices":[
                {"id":905, "item":{"keyName":"REBOOT_REMOTE_CONSOLE"}},
                {"id":1800, "item":{"keyName":"BANDWIDTH_0_GB_2"}},
                {"id":274, "item":{"keyName":"1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS"}},
                {"id":21,"item":{"keyName":"1_IP_ADDRESS"}},
                {"id":55,"item":{"keyName":"MONITORING_HOST_PING"}},
                {"id":216951, "item":{ "keyName":"OS_WINDOWS_2016_FULL_DC_64_BIT_VIRTUAL"}},
                {"id":57, "item":{"keyName":"NOTIFICATION_EMAIL_AND_TICKET"}},
                {"id":58, "item":{"keyName":"AUTOMATED_NOTIFICATION"}},
                {"id":36490, "item":{"keyName":"DATABASE_MYSQL_5_7_WINDOWS"}},
                {"id":420, "item":{"keyName":"UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT"}}
            ]
        },
        {
            "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest",
            "containerIdentifier": "Container3",
            "quantity": 1,
            "useHourlyPricing": true,
            "hardware": [{"hostname": "hostname0", "domain": "ibm.com"}],
            "packageId": 46,
            "prices": [
                {"id": 200313}, {"id": 200353}, {"id": 45466}, {"id": 200397},
                {"id": 200425}, {"id": 1800}, {"id": 203857}, {"id": 55},
                {"id": 58}, {"id": 420}, {"id": 21}, {"id": 57},
                {"id": 905}
            ],
            "hostId": 542454
        }]
    }]
}
```

You can also use the SLCLI and IBMCLOUD SL tools to place orders.
[slcli order place](https://softlayer-python.readthedocs.io/en/latest/cli/ordering/#order-place)

## [Quotes](#quotes) {#quotes .anchor_link}

The [SoftLayer_Billing_Order_Quote](https://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/) is very similar to the Billing_Order service, but with quotes you can save an order for later use. Quote features exist in the SLCLI and IBMCLOUD SL tools. 
[Python example for working with quotes](https://sldn.softlayer.com/python/quotes/)

### Creating a Quote

Use the same process for creating a normal order, but use [SoftLayer_Billing_Order_Quote::placeQuote](https://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/placeQuote/) instead of SoftLayer_Billing_Order::placeOrder. 

#### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST  -d '{"parameters": [{"orderContainers": [{"packageId": 46, "quantity": 1, "location": 1854895, "useHourlyPricing": false,
"complexType": "SoftLayer_Container_Product_Order_Virtual_Guest", "prices": [{"id": 1642}, {"id": 1927}, {"id": 905}, {"id": 274}, {"id": 1800}, {"id": 21}, {"id": 1639}, {"id": 211481}, {"id": 55}, {"id": 57}, {"id":
58}, {"id": 420}]}], "quoteName": "test1", "sendQuoteEmailFlag": false}]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/placeQuote.json'
````

### Listing Quotes

Use [SoftLayer_Account::getQuotes](https://sldn.softlayer.com/reference/services/SoftLayer_Account/getQuotes/) to list the quotes on your account. You will need the quote ID for placing the actual order.

[slcli order  quote-list](https://softlayer-python.readthedocs.io/en/latest/cli/ordering/#order-quote-list)

### Ordering from a Quote

To actually order from a quote, you need to use [SoftLayer_Billing_Order_Quote::placeOrder](https://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/placeOrder/), and *NOT* SoftLayer_Billing_Order::placeOrder. 

You will also need to order container, which you can get with [SoftLayer_Billing_Order_Quote::getRecalculatedOrderContainer](https://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/getRecalculatedOrderContainer/), this will return an object you will then send in as your order. The only real change you need to make is fille out the `hardware` or `virtualGuests` property with the hostname/domain for each server in the order.

#### Curl Example
This will be a little complicated, because you need to modify the results of SoftLayer_Billing_Order_Quote::getRecalculatedOrderContainer() a little bit before sending it in.

```bash
# All parameters you send into the API need to start with this bit
echo '{"parameters":[' > my_quote.json
# Get the order container and append it to the my_quote.json file
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Quote/2998225/getRecalculatedOrderContainer.json' >> my_quote.json
# Close out the parameters bit
echo ']}' >> my_quote.json
```
Now you need to edit `my_quote.json` and add the `virtualGuests` or `hardware` property, there should be 1 entry for each server you are ordering. It will look something like this. Make sure to edit `quantity` and set the `complexType`

```json
{
  "parameters":[{
    // Lots of stuff removed for brevity.....
    "quantity": 1,
    "hostId": null,
    "reservedCapacityId": null,
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest",
    "virtualGuests":[{"hostname": "testing","domain": "ibm.com"}]
}]}
```

Then just verify or place the order (with the `SoftLayer_Billing_Order_Quote` service)
```bash
curl -u  $SL_USER:$SL_APIKEY -X POST -d @my_quote.json  'https://api.softlayer.com/rest/v3.1/SoftLayer_Billing_Order_Quote/2998225/verifyOrder.json'
```
#### CLI Example

```bash
slcli -vvv  order  quote  2998225 --verify --quantity 1 --complex-type SoftLayer_Container_Product_Order_Virtual_Guest --fqdn testing.ibm.com
```


