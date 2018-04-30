---
title: "OrderViyatta.cs"
description: "OrderViyatta.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance"
    - "SoftLayer_Account"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Hardware"
    - "SoftLayer_Product_OrderService"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Hardware_Server"
tags:
    - "viyatta"
---


```
//-----------------------------------------------------------------------
// <copyright file="OrderVyatta.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace OrderVyattaNamespace
{
    using System;
    using System.Collections.Generic;

    class OrderVyatta
    {
        /// <summary>
        /// Example to order a Network Gateway Appliance (Vyatta)
        /// The examples orders a (Vyatta) high availability pair.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server_Gateway_Appliance
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username and key.
            string username = "set me";
            string apiKey = "set me";

            // The number of servers you wish to order.
            // If you wish a high availability pair you must specify 2 as quantity.
            int quantity = 2;

            // Building a skeleton SoftLayer_Hardware_Server object to model the hostname and
            // domain we want for our server. If you set quantity greater than 1 then you
            // need to define one hostname/domain pair per server you wish to order.
            SoftLayer_Hardware hardwareNode1 = new SoftLayer_Hardware();
            hardwareNode1.hostname = "vyattagw"; 
            hardwareNode1.domain = "test.com";

            SoftLayer_Hardware hardwareNode2 = new SoftLayer_Hardware();
            hardwareNode2.hostname = "vyattagw2"; 
            hardwareNode2.domain = "test.com";

            List<SoftLayer_Hardware> hardwareList = new List<SoftLayer_Hardware>();
            hardwareList.Add(hardwareNode1);
            hardwareList.Add(hardwareNode2);

            // Where you'd like your new server provisioned.
            // This can either be the id of the datacenter
            // you wish your new server to be provisioned in
            string location = "AMSTERDAM";

            // The id of the SoftLayer_Product_Package you wish to order.
            // In this case the Network Gateway Appliance (Vyatta) package id is 174.
            int packageId = 174;

            // Building a skeleton SoftLayer_Product_Item_Price objects. These objects contain
            // much more than ids, but SoftLayer's ordering system only needs the price's id
            // to know what you want to order.
            // Every item in SoftLayer's product catalog is assigned an id. Use these ids
            // to tell the SoftLayer API which options you want in your new server. Use
            // the getActivePackages() method in the SoftLayer_Account API service to get
            // a list of available item and price options per available package.
            int[] prices = 
            {
                420,
                73935,
                74865,
                21,
                57,
                1267,
                17129,
                69623,
                906,
                74995,
                36044,
                342,
                52595,
                55,
                58,
                418
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
            SoftLayer_Container_Product_Order orderContainer = new SoftLayer_Container_Product_Order();
            orderContainer.quantity = quantity;
            orderContainer.quantitySpecified = true;
            orderContainer.location = location;
            orderContainer.packageId = packageId;
            orderContainer.packageIdSpecified = true;
            orderContainer.prices = pricesList.ToArray();
            orderContainer.hardware = hardwareList.ToArray();

            SoftLayer_Container_Product_Order orderTemplate = new SoftLayer_Container_Product_Order();
            orderTemplate.orderContainers = new SoftLayer_Container_Product_Order[1];
            orderTemplate.orderContainers[0] = orderContainer;

            // Creating the authentication
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring a new API service objects for:
            // SoftLayer_Product_Order
            SoftLayer_Product_OrderService productOrderService = new SoftLayer_Product_OrderService();
            productOrderService.authenticateValue = authenticate;

            // verifyOrder() will check your order for errors. Replace this             
            // with a call to placeOrder() when you're ready to order. Both             
            // calls return a receipt object that you can use for your records.            
            // Once your order is placed it'll go through SoftLayer's approval             
            // and provisioning process.       
            try 
            {
                SoftLayer_Container_Product_Order verifiedOrder = (SoftLayer_Container_Product_Order)productOrderService.verifyOrder(orderTemplate); 
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
