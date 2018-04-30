---
title: "OrderDedicatedFirewall.cs"
description: "OrderDedicatedFirewall.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_OrderService"
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Network_Protection_Firewall"
tags:
    - "firewall"
---


```
//-----------------------------------------------------------------------
// <copyright file="OrderDedicatedFirewall.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace OrderDedicatedFirewallNamespace
{
    using System;
    using System.Collections.Generic;

    class OrderDedicatedFirewall
    {
        /// <summary>
        /// Order dedicated Firewalls.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your username
            string username = "set me";

            // Your SoftLayer API key.            
            string apiKey = "set me";

            // The location for the firewall
            string location = "AMSTERDAM";

            // The package id to order firewalls
            int packageId = 0;

            int quantity = 1;

            // Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
            // much more than ids, but SoftLayer's ordering system only needs the price's id
            // to know what you want to order.
            // to get the list of valid prices for the package
            // use the SoftLayer_Product_Package:getItems method
            int[] prices = 
            {
                // Price to 10Mbps Hardware Firewall
                410,
            };

            List<SoftLayer_Product_Item_Price> pricesList = new List<SoftLayer_Product_Item_Price>();
            foreach (var item in prices)
            {
                SoftLayer_Product_Item_Price price = new SoftLayer_Product_Item_Price();
                price.id = item;
                price.idSpecified = true;
                pricesList.Add(price);
            }

            List<SoftLayer_Virtual_Guest> virtualGuests = new List<SoftLayer_Virtual_Guest>();
            SoftLayer_Virtual_Guest virtualGuest = new SoftLayer_Virtual_Guest();

            // The virtual Guest Id where you wish add a firewall.
            virtualGuest.id = 6674100;
            virtualGuest.idSpecified = true;
            virtualGuests.Add(virtualGuest);

            // Building a skeleton SoftLayer_Container_Product_Order_Network_Protection_Firewall object
            // containing the order you wish to place.
            SoftLayer_Container_Product_Order_Network_Protection_Firewall orderTemplate = new SoftLayer_Container_Product_Order_Network_Protection_Firewall();
            orderTemplate.location = location;
            orderTemplate.quantity = quantity;
            orderTemplate.quantitySpecified = true;
            orderTemplate.packageId = packageId;
            orderTemplate.packageIdSpecified = true;
            orderTemplate.prices = pricesList.ToArray();
            orderTemplate.virtualGuests = virtualGuests.ToArray();

            // Creating a connection to the SoftLayer_Product_OrderService API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            SoftLayer_Product_OrderService orderService = new SoftLayer_Product_OrderService();
            orderService.authenticateValue = authenticate;

            // verifyOrder() will check your order for errors. Replace this             
            // with a call to placeOrder() when you're ready to order. Both             
            // calls return a receipt object that you can use for your records.                       
            // Once your order is placed it'll go through SoftLayer's approval             
            // and provisioning process.       
            try
            {
                SoftLayer_Container_Product_Order verifiedOrder = (SoftLayer_Container_Product_Order)orderService.verifyOrder(orderTemplate);
                Console.WriteLine("Order verified!");
            }
            catch (Exception e)
            {
                Console.WriteLine("Invalid order: " + e.Message);
            }
        }
    }
}

```
