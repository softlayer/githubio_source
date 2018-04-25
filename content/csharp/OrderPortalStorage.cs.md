---
title: "OrderPortalStorage.cs"
description: "OrderPortalStorage.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_OrderService"
    - "SoftLayer_Container_Product_Order_Virtual_Disk_Image"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "portablestorage"
---


```
//-----------------------------------------------------------------------
// <copyright file="OrderPortalStorage.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace OrderPortalStorageNamespace
{
    using System;
    using System.Collections.Generic;

    class OrderPortalStorage
    {
        /// <summary>
        /// Example to order a portal storage.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Disk_Image
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
        /// </manualPages
        static void Main(string[] args)
        {
            // Your SoftLayer API username.           
            string username = "set me";

            // Your SoftLayer API key.            
            string apiKey = "set me";

            string location = "SANJOSE";

            string diskDescription = "test portable storage";

            // The package for order portable storage 
            int packageId = 198;

            // The prices for the portable storage
            // to see the list of prices available for the package
            // use the Softlayer_Product_Package::getItems method (http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItems)
            int[] prices = 
            {
                21861 
            };

            List<SoftLayer_Product_Item_Price> pricesList = new List<SoftLayer_Product_Item_Price>();

            foreach (int item in prices)
            {
                SoftLayer_Product_Item_Price price = new SoftLayer_Product_Item_Price();
                price.id = item;
                price.idSpecified = true;
                pricesList.Add(price);
            }

            // Building a skeleton SoftLayer_Container_Product_Order_Virtual_Disk_Image object
            // containing the order you wish to place.
            SoftLayer_Container_Product_Order_Virtual_Disk_Image orderTemplate = new SoftLayer_Container_Product_Order_Virtual_Disk_Image();
            orderTemplate.packageId = packageId;
            orderTemplate.packageIdSpecified = true;
            orderTemplate.prices = pricesList.ToArray();
            orderTemplate.location = location;
            orderTemplate.diskDescription = diskDescription;

            // Create a connection to the SoftLayer_Product_OrderService API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            SoftLayer_Product_OrderService orderService = new SoftLayer_Product_OrderService();
            orderService.authenticateValue = authenticate;

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
