---
title: "OrderNAS.cs"
description: "OrderNAS.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_OrderService"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Network_Storage_Nas"
tags:
    - "nas"
---


```
//-----------------------------------------------------------------------
// <copyright file="OrderNAS.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace OrderNASNamespace
{
    using System;
    using System.Collections.Generic;

    class OrderNAS
    {
        /// <summary>
        /// Order a NAS
        /// Build a SoftLayer_Container_Product_Order_Network_Storage_Nas
        /// object for a new CDN account order and pass it to the SoftLayer_Product_Order
        /// API service to order it. In this script we'll order a NAS. See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Nas
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username.            
            string username = "set me";

            // Your SoftLayer API key.            
            string apiKey = "set me";

            // Creating a connection to the SoftLayer_Product_OrderService API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            SoftLayer_Product_OrderService orderService = new SoftLayer_Product_OrderService();
            orderService.authenticateValue = authenticate;

            string location = "AMSTERDAM";

            // The package id to order NAS
            int packageId = 216;

            int quantity = 1;

            bool privateCloudOrderFlag = false;

            // Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
            // much more than ids, but SoftLayer's ordering system only needs the price's id
            // to know what you want to order.
            // to get the list of valid prices for the package
            // use the SoftLayer_Product_Package:getItems method
            int[] prices = 
            {
                508, // 20 GB NAS 
            };

            List<SoftLayer_Product_Item_Price> pricesList = new List<SoftLayer_Product_Item_Price>();

            foreach (var item in prices)
            {
                SoftLayer_Product_Item_Price price = new SoftLayer_Product_Item_Price();
                price.id = item;
                price.idSpecified = true;
                pricesList.Add(price);
            }

            // Building a skeleton SoftLayer_Container_Product_Order_Network_Storage_Nas object
            // containing the order you wish to place.
            SoftLayer_Container_Product_Order_Network_Storage_Nas orderTemplate = new SoftLayer_Container_Product_Order_Network_Storage_Nas();
            orderTemplate.location = location;
            orderTemplate.quantity = quantity;
            orderTemplate.quantitySpecified = true;
            orderTemplate.packageId = packageId;
            orderTemplate.packageIdSpecified = true;
            orderTemplate.prices = pricesList.ToArray();
            orderTemplate.privateCloudOrderFlag = privateCloudOrderFlag;
            orderTemplate.privateCloudOrderFlagSpecified = true;

            // verifyOrder() will check your order for errors. Replace this             
            // with a call to placeOrder() when you're ready to order. Both             
            // calls return a receipt object that you can use for your records.            
            //            
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
