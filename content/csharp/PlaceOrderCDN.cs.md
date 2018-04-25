---
title: "PlaceOrderCDN.cs"
description: "PlaceOrderCDN.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Network_ContentDelivery_Account"
    - "SoftLayer_Product_OrderService"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Container_Product_Order_Network_ContentDelivery_Account"
tags:
    - "cdn"
---


```
//-----------------------------------------------------------------------
// <copyright file="PlaceOrderCDN.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace PlaceOrderCDNNamespace
{
    using System;
    using System.Collections.Generic;

    class PlaceOrderCDN
    {
        /// <summary>
        /// Order a new CDN account
        /// Build a SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
        /// object for a new CDN account order and pass it to the SoftLayer_Product_Order
        /// API service to order it. In this script we'll order a pay as you go bandwidth
        /// and storage CDN account. See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_ContentDelivery_Account
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_ContentDelivery_Account
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/verifyOrder
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Order/placeOrder
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username and API key.               
            string username = "set me";
            string apiKey = "set me";

            // The package id to order Content Delivery Network
            int packageId = 208;

            int quantity = 1;

            // Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
            // much more than ids, but SoftLayer's ordering system only needs the price's id
            // to know what you want to order.
            // to get the list of valid prices for the package
            // use the SoftLayer_Product_Package:getItems method
            // the example uses the prices:
            // 1661 = "CDN Pay as You Go Bandwidth"
            // 1670 = "CDN No storage (origin pull)"
            int[] prices = { 1661, 1670 };

            // Creating a connection to the SoftLayer_Product_OrderService API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            SoftLayer_Product_OrderService orderService = new SoftLayer_Product_OrderService();
            orderService.authenticateValue = authenticate;

            List<SoftLayer_Product_Item_Price> pricesList = new List<SoftLayer_Product_Item_Price>();

            foreach (int item in prices)
            {
                SoftLayer_Product_Item_Price price = new SoftLayer_Product_Item_Price();
                price.id = item;
                price.idSpecified = true;
                pricesList.Add(price);
            }

            // Building a skeleton SoftLayer_Container_Product_Order_Network_ContentDelivery_Account object
            // containing the order you wish to place.
            SoftLayer_Container_Product_Order_Network_ContentDelivery_Account orderTemplate = new SoftLayer_Container_Product_Order_Network_ContentDelivery_Account();
            orderTemplate.quantity = quantity;
            orderTemplate.quantitySpecified = true;
            orderTemplate.packageId = packageId;
            orderTemplate.packageIdSpecified = true;
            orderTemplate.prices = pricesList.ToArray();

            // verifyOrder() will check your order for errors. Replace this             
            // with a call to placeOrder() when you're ready to order. Both             
            // calls return a receipt object that you can use for your records.            
            //            
            // Once your order is placed it'll go through SoftLayer's approval             
            // and provisioning process. When it's done you'll have a new            
            // SoftLayer_Network_ContentDelivery_Account object ready to use.            
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
