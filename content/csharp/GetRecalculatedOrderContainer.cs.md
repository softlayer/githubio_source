---
title: "GetRecalculatedOrderContainer.cs"
description: "GetRecalculatedOrderContainer.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Product_Order"
    - "SoftLayer_Billing_OrderInitParametersValue"
    - "SoftLayer_Billing_OrderInitParameters"
    - "SoftLayer_Billing_Order_QuoteService"
    - "SoftLayer_Billing_Order_QuoteInitParameters"
    - "SoftLayer_Billing_OrderService"
    - "SoftLayer_Billing_Order"
    - "SoftLayer_Billing_Order_QuoteInitParametersValue"
    - "SoftLayer_Billing_Order_Quote"
tags:
    - "quotes"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="GetRecalculatedOrderContainer.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Quotes
{
    using System;
    class GetRecalculatedOrderContainer
    {
        /// <summary>
        /// Get Order
        /// This script gets a SoftLayer_Container_Product_Order with all the recalculated total with considerations
        /// for promotions, resellear status and taxes.
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/getRecalculatedOrderContainer
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Define the quote identifier that you wish to recalculate the order
            int quoteId = 1326046;
            // Define if the order is actually being placed 
            bool orderBeingPlacedFlag = false;
            // Define the message to return with the verified order
            string message = "this is for test";
            // Define if you want to ignore the promo code if any for this order
            bool ignoreDiscountsFlag = false;
            // Creating a connection to the SoftLayer_Billing_Order_Quote API service and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Billing_Order_QuoteService quoteService = new SoftLayer_Billing_Order_QuoteService();
            quoteService.authenticateValue = authenticate;
            SoftLayer_Billing_OrderService orderService = new SoftLayer_Billing_OrderService();
            orderService.authenticateValue = authenticate;
            // Setting init parameters
            quoteService.SoftLayer_Billing_Order_QuoteInitParametersValue = new SoftLayer_Billing_Order_QuoteInitParameters();
            quoteService.SoftLayer_Billing_Order_QuoteInitParametersValue.id = quoteId;
            try
            {
                SoftLayer_Billing_Order order = quoteService.getOrder();
                // Setting init parameters
                orderService.SoftLayer_Billing_OrderInitParametersValue = new SoftLayer_Billing_OrderInitParameters();
                orderService.SoftLayer_Billing_OrderInitParametersValue.id = (int)order.id;
                // Get the Container Product Order from the order 
                SoftLayer_Container_Product_Order orderData = orderService.getRecalculatedOrderContainer(message, ignoreDiscountsFlag);
                SoftLayer_Container_Product_Order resultQuote = quoteService.getRecalculatedOrderContainer(orderData, orderBeingPlacedFlag);
                Console.WriteLine("The order was recalculated");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get orders from quote: " + e.Message);
            }
        }
    }
}

```
