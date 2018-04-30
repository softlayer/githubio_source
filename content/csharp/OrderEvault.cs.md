---
title: "OrderEvault.cs"
description: "OrderEvault.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware"
    - "SoftLayer_Product_OrderService"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault"
    - "SoftLayer_Product_Order"
tags:
    - "evault"
---


```
//-----------------------------------------------------------------------
// <copyright file="OrderEvault.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace OrderEvaultNamespace
{
    using System;
    using System.Collections.Generic;

    class OrderEvault
    {
        /// <summary>
        /// Example to order a Evault
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username and API username.           
            string username = "set me";          
            string apiKey = "set me";

            int quantity = 1;

            // The location for the Evault
            string location = "DALLAS06";

            // The id of the SoftLayer_Product_Package you wish to order.
            int packageId = 0;

            // Building a skeleton SoftLayer_Virtual_Guest object.
            // The object contains the virtual guest Id of the
            // VSI wich will contain the Evault
            SoftLayer_Virtual_Guest virtualGuest = new SoftLayer_Virtual_Guest();
            virtualGuest.id = 4241550;
            virtualGuest.idSpecified = true;

            List<SoftLayer_Virtual_Guest> virtualGuestList = new List<SoftLayer_Virtual_Guest>();
            virtualGuestList.Add(virtualGuest);

            // Building a skeleton SoftLayer_Product_Item_Price object.
            // The object contains the price Id of the Evaul device
            // you wish order.
            int[] prices = 
            {
                1045  
            };

            List<SoftLayer_Product_Item_Price> pricesList = new List<SoftLayer_Product_Item_Price>();

            foreach (var item in prices)
            {
                SoftLayer_Product_Item_Price price = new SoftLayer_Product_Item_Price();
                price.id = item;
                price.idSpecified = true;
                pricesList.Add(price);
            }

            // Building a skeleton SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault object
            // containing the order you wish to place.
            SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault orderTemplate = new SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault();
            orderTemplate.quantity = quantity;
            orderTemplate.quantitySpecified = true;
            orderTemplate.location = location;
            orderTemplate.packageId = packageId;
            orderTemplate.packageIdSpecified = true;
            orderTemplate.prices = pricesList.ToArray();
            orderTemplate.virtualGuests = virtualGuestList.ToArray();

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
