---
title: "PlaceOrder.cs"
description: "PlaceOrder.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware"
    - "SoftLayer_Product_OrderService"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "virtualguests"
---


```
//-----------------------------------------------------------------------
// <copyright file="PlaceOrder.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace VirtualGuests
{
    using System;
    using System.Collections.Generic;
    class PlaceOrder
    {
        /// <summary>
        ///  Place Order
        ///  This script orders a Virtual Guest using SoftLayer_Product_Order::placeOrder method
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Item_Price/
        /// </manualPages>
        static void Main(string[] args)
        {
            // You SoftLayer username
            string username = "set me";
            // Your SoftLayer API key.            
            string apiKey = "set me";
            // Define the number of servers you wish to order
            int quantity = 1;
            // Define the location where you wish your server would be provisioned
            String location = "SINGAPORE";
            // Define the package Id you wish to order
            int packageId = 46;
            // Build a SoftLayer_Hardware object to specify the hostname and domain, that you wish for your server
            SoftLayer_Hardware hardware = new SoftLayer_Hardware();
            hardware.hostname = "rcvtest";
            hardware.domain = "softlayer.com";
            List<SoftLayer_Hardware> hardwareList = new List<SoftLayer_Hardware>();
            hardwareList.Add(hardware);
            // Build a SoftLayer_Product_Item_Price objects with the ids from prices that you want to order. 
            // You can retrieve them with SoftLayer_Product_Package::getItemPrices method
            int[] prices = {
                               1640,  // 1 x 2.0 GHz Core
                               1644,  // 1 GB RAM
                               13940,  // CentOS 6.x - LAMP Install (32 bit)
                               2202,  // 25 GB (SAN)
                               50241,  // 5000 GB Bandwidth
                               273,  // 100 Mbps Public & Private Network Uplinks
                               2302,  // Monitoring Package - Basic
                               55,  // Host Ping
                               58,  // Automated Notification
                               420,  // Unlimited SSL VPN Users & 1 PPTP VPN User per account
                               418,  // Nessus Vulnerability Assessment & Reporting
                               21,  // 1 IP Address
                               57,  // Email and Ticket
                               905,  // Reboot / Remote Console
                               14022  // International Services
                           };

            List<SoftLayer_Product_Item_Price> pricesList = new List<SoftLayer_Product_Item_Price>();
            foreach (var price in prices)
            {
                SoftLayer_Product_Item_Price newPrice = new SoftLayer_Product_Item_Price();
                newPrice.id = price;
                newPrice.idSpecified = true;
                pricesList.Add(newPrice);
            }
            // Build a SoftLayer_COntainer_Product_Order object containing the order you wish to place
            SoftLayer_Container_Product_Order orderTemplate = new SoftLayer_Container_Product_Order();
            orderTemplate.quantity = quantity;
            orderTemplate.quantitySpecified = true;
            orderTemplate.location = location;
            orderTemplate.packageId = packageId;
            orderTemplate.packageIdSpecified = true;
            orderTemplate.prices = pricesList.ToArray();
            orderTemplate.hardware = hardwareList.ToArray();
            // Creating a connection to the SoftLayer_Product_Order API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Product_OrderService orderService = new SoftLayer_Product_OrderService();
            orderService.authenticateValue = authenticate;
            try
            {
                // We will check the template for errors, we will use the verifyOrder() method for this. 
                // Replace it with placeOrder() method when you are ready to order.
                SoftLayer_Container_Product_Order verifiedOrder = orderService.verifyOrder(orderTemplate);
                Console.WriteLine("Order Verified!");
            }
            catch (Exception e)
            {
                Console.WriteLine("Invalid order: " + e.Message);
            }
        }
    }
}

```
