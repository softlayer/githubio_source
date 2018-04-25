---
title: "OrderMonitoring.cs"
description: "OrderMonitoring.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group"
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Container_Product_Order_Monitoring_Package"
    - "SoftLayer_Product_OrderService"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Order"
tags:
    - "monitoring"
---


```
//-----------------------------------------------------------------------
// <copyright file="OrderMonitoring.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace OrderMonitoringNamespace
{
    using System;
    using System.Collections.Generic;

    class OrderMonitoring
    {
        /// <summary>
        /// Example to order a Monitoring Package
        /// Build a SoftLayer_Container_Product_Order_Monitoring_Package object for a new
        /// monitoring order and pass it to the SoftLayer_Product_Order API service to order it
        /// In this care we'll order a Basic (Hardware and OS) package with Basic Monitoring Package - Linux
        /// configuration for more details see below
        /// </summary>
        /// <manualPages>
        /// https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Monitoring_Package
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Product_Item_Price
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username.           
            string username = "set me";

            // Your SoftLayer API key.            
            string apiKey = "set me";

            // The quantity for order a service (in this case monitoring package) must be 0
            int quantity = 0;

            // The package id for order monitoring packages is 0
            int packageId = 0;

            bool sendQuoteEmailFlag = true;
            bool useHourlyPricing = true;

            // Building a skeleton SoftLayer_Virtual_Guest object.
            SoftLayer_Virtual_Guest virtualGuest = new SoftLayer_Virtual_Guest();

            // The virtual guest id where you wish to add the monitoring package 
            virtualGuest.id = 4906034;
            virtualGuest.idSpecified = true;

            List<SoftLayer_Virtual_Guest> virtualGuestList = new List<SoftLayer_Virtual_Guest>();
            virtualGuestList.Add(virtualGuest);

            List<SoftLayer_Monitoring_Agent_Configuration_Template_Group> configurationTemplateGroupList = new List<SoftLayer_Monitoring_Agent_Configuration_Template_Group>();

            // The templateidD for the monitoring group (in this case Basic Monitoring package for Unix/Linux operating system.
            SoftLayer_Monitoring_Agent_Configuration_Template_Group configurationTemplateGroup = new SoftLayer_Monitoring_Agent_Configuration_Template_Group();
            configurationTemplateGroup.id = 3;
            configurationTemplateGroup.idSpecified = true;
            configurationTemplateGroupList.Add(configurationTemplateGroup);

            // Building a skeleton SoftLayer_Product_Item_Price object.
            // The object contains the price id of the Evaul device
            // you wish to order.
            int[] prices = 
            {
                // This is the price for Monitoring Package - Basic ((Hardware and OS))
                2302  
            };

            List<SoftLayer_Product_Item_Price> pricesList = new List<SoftLayer_Product_Item_Price>();

            foreach (var item in prices)
            {
                SoftLayer_Product_Item_Price price = new SoftLayer_Product_Item_Price();
                price.id = item;
                price.idSpecified = true;
                pricesList.Add(price);
            }

            // Building a skeleton SoftLayer_Container_Product_Order_Monitoring_Package object
            // containing the order you wish to place.
            SoftLayer_Container_Product_Order_Monitoring_Package orderTemplate = new SoftLayer_Container_Product_Order_Monitoring_Package();
            orderTemplate.quantity = quantity;
            orderTemplate.quantitySpecified = true;
            orderTemplate.packageId = packageId;
            orderTemplate.packageIdSpecified = true;
            orderTemplate.prices = pricesList.ToArray();
            orderTemplate.virtualGuests = virtualGuestList.ToArray();
            orderTemplate.configurationTemplateGroups = configurationTemplateGroupList.ToArray();
            orderTemplate.sendQuoteEmailFlag = sendQuoteEmailFlag;
            orderTemplate.sendQuoteEmailFlagSpecified = true;
            orderTemplate.useHourlyPricing = useHourlyPricing;
            orderTemplate.useHourlyPricingSpecified = true;

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
            // and provisioning process. When it's done you'll have a new            
            // SoftLayer_Container_Product_Order_Monitoring_Package object ready to use.            
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
