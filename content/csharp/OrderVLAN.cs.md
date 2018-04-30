---
title: "OrderVLAN.cs"
description: "OrderVLAN.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_OrderService"
    - "SoftLayer_Container_Product_Order_Network_Vlan"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "vlan"
---


```
//-----------------------------------------------------------------------
// <copyright file="OrderVLAN.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace OrderVLANNamespace
{
    using System;
    using System.Collections.Generic;

    class OrderVLAN
    {
        /// <summary>
        /// Example to create a new VLAN
        /// the script uses the placeOrder method to order
        /// a new VLAN with 32 static IP address
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Vlan
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price        
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API and username key.
            string username = "set me";
            string apiKey = "set me";

            string location = "AMSTERDAM";

            // The package id for order monitoring packages is 0
            int packageId = 0;

            int quantity = 1;

            string name = "myVLANnew";

            bool sendQuoteEmailFlag = true;

            int routerID = 117960;

            // Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
            // much more than ids, but SoftLayer's ordering system only needs the price's id
            // to know what you want to order.
            // to get the list of valid prices for the package
            // use the SoftLayer_Product_Package:getItems method
            int[] prices = 
            {
                2018,
                1092 
            };

            List<SoftLayer_Product_Item_Price> pricesList = new List<SoftLayer_Product_Item_Price>();

            foreach (var item in prices)
            {
                SoftLayer_Product_Item_Price price = new SoftLayer_Product_Item_Price();
                price.id = item;
                price.idSpecified = true;
                pricesList.Add(price);
            }

            // Building a skeleton SoftLayer_Container_Product_Order_Network_Vlan object
            // containing the order you wish to place.
            SoftLayer_Container_Product_Order_Network_Vlan orderTemplate = new SoftLayer_Container_Product_Order_Network_Vlan();
            orderTemplate.location = location;
            orderTemplate.name = name;
            orderTemplate.routerId = routerID;
            orderTemplate.routerIdSpecified = true;
            orderTemplate.quantity = quantity;
            orderTemplate.quantitySpecified = true;
            orderTemplate.packageId = packageId;
            orderTemplate.packageIdSpecified = true;
            orderTemplate.prices = pricesList.ToArray();
            orderTemplate.sendQuoteEmailFlag = sendQuoteEmailFlag;
            orderTemplate.sendQuoteEmailFlagSpecified = true;

            // Creating a connection to the SoftLayer_Product_Order API service and             
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
            // and provisioning process. When it's done you'll have a new            
            // SoftLayer_Network_Subnet object ready to use.            
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
