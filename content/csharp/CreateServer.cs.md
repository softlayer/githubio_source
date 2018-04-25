---
title: "CreateServer.cs"
description: "CreateServer.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Hardware"
    - "SoftLayer_Product_OrderService"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
tags:
    - "baremetalservers"
---


```
//-----------------------------------------------------------------------
// <copyright file="CreateServer.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace CreateServerNamespace
{
    using System;
    using System.Collections.Generic;

    class CreateServer
    {
        /// <summary>
        /// Order a new server.
        /// Building a SoftLayer_Container_Product_Order object for a new
        /// server order and pass it to the SoftLayer_Product_Order API service to order
        /// it. In this care we'll order a Xeon 3460 server with 2G RAM, 100mbit NICs,
        /// 2000GB bandwidth, a 500G SATA drive, CentOS 5 32-bit, and default server
        /// order options. See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
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

            // The number of servers you wish to order in this configuration.
            int quantity = 1;

            // Where you'd like your new server provisioned.
            // This can either be the id of the datacenter you wish your new server to be
            // provisioned in or the string 'FIRST_AVAILABLE' if you have no preference
            // where your server is provisioned.
            // Location id 3     = Dallas
            // Location id 18171 = Seattle
            // Location id 37473 = Washington, D.C.
            string location = "FIRST_AVAILABLE";

            // The id of the SoftLayer_Product_Package you wish to order.
            // In this case the Intel Xeon 3460's package id is 145.
            int packageId = 145;

            // Building a skeleton SoftLayer_Hardware_Server object to model the hostname and
            // domain we want for our server. If you set quantity greater than 1 then you
            // need to define/ one hostname/domain pair per server you wish to order.
            SoftLayer_Hardware hardware = new SoftLayer_Hardware();
            hardware.hostname = "test"; // The hostname of the server you wish to order.
            hardware.domain = "example.org";

            List<SoftLayer_Hardware> hardwareList = new List<SoftLayer_Hardware>();
            hardwareList.Add(hardware);

            // Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
            // much more than ids, but SoftLayer's ordering system only needs the price's id
            // to know what you want to order.
            // Every item in SoftLayer's product catalog is assigned an id. Use these ids
            // to tell the SoftLayer API which options you want in your new server. Use
            // the getActivePackages() method in the SoftLayer_Account API service to get
            // a list of available item and price options per available package.
            int[] prices = 
            {
                17231, // Single Processor Quad Core Xeon 3460 - 2.80GHz (Lynnfield) - 1 x 8MB cache w/HT
                637,   // 2 GB DDR2 667
                682,   // CentOS 5.x (32 bit)
                876,   // 2 GB DDR2 667
                19087, // 500GB SATA II
                342,   // 20000 GB Bandwidth
                273,   // 100 Mbps Public & Private Network Uplinks
                55,    // Host Ping
                58,    // Automated Notification
                420,   // Unlimited SSL VPN Users & 1 PPTP VPN User per account
                418,   // Nessus Vulnerability Assessment & Reporting
                21,    // 1 IP Address
                57,    // Email and Ticket
                906  // Reboot / KVM over IP
            };

            List<SoftLayer_Product_Item_Price> pricesList = new List<SoftLayer_Product_Item_Price>();
            foreach (var item in prices)
            {
                SoftLayer_Product_Item_Price price = new SoftLayer_Product_Item_Price();
                price.id = item;
                price.idSpecified = true;
                pricesList.Add(price);
            }

            // Building a skeleton SoftLayer_Container_Product_Order object
            // containing the order you wish to place.
            SoftLayer_Container_Product_Order orderTemplate = new SoftLayer_Container_Product_Order();
            orderTemplate.quantity = quantity;
            orderTemplate.quantitySpecified = true;
            orderTemplate.location = location;
            orderTemplate.packageId = packageId;
            orderTemplate.packageIdSpecified = true;
            orderTemplate.prices = pricesList.ToArray();
            orderTemplate.hardware = hardwareList.ToArray();

            // Creating a connection to the SoftLayer_Account API service and             
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
