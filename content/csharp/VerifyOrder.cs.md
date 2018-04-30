---
title: "VerifyOrder.cs"
description: "VerifyOrder.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
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
﻿﻿//-----------------------------------------------------------------------
// <copyright file="VerifyOrder.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Quotes
{
    using System;
    using System.Collections.Generic;
    class VerifyOrder
    {
        /// <summary>
        /// Verify Order
        /// This is script verifies a quote
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/verifyOrder
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Define the quote identifier that you wish to verify
            int quoteId = 1326046;
            // Creating a connection to the SoftLayer_Account API service and             
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
                Console.WriteLine(order.id);
                // Setting init parameters
                orderService.SoftLayer_Billing_OrderInitParametersValue = new SoftLayer_Billing_OrderInitParameters();
                orderService.SoftLayer_Billing_OrderInitParametersValue.id = (int)order.id;
                string message = "this is for test";
                bool ignoreDiscountsFlag = false;
                SoftLayer_Container_Product_Order result = orderService.getRecalculatedOrderContainer(message, ignoreDiscountsFlag);
                SoftLayer_Container_Product_Order verifyOrder = quoteService.verifyOrder(result);
                Console.WriteLine("Order verified");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to delete quote: " + e.Message);
            }
        }
    }
}

```
