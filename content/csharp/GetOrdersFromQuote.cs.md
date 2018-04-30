---
title: "GetOrdersFromQuote.cs"
description: "GetOrdersFromQuote.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Order_QuoteInitParametersValue"
    - "SoftLayer_Billing_Order_QuoteService"
    - "SoftLayer_Billing_Order_QuoteInitParameters"
    - "SoftLayer_Billing_Order_Quote"
    - "SoftLayer_Billing_Order"
tags:
    - "quotes"
---


```
﻿﻿//-----------------------------------------------------------------------
// <copyright file="GetOrdersFromQuote.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Quotes
{
    using System;
    class GetOrdersFromQuote
    {
        /// <summary>
        /// Get Orders from quote
        /// This script retrieves a quote's corresponding order
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/getOrdersFromQuote
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Define the quote identifier that you wish to get the orders
            int quoteId = 1326046;
            // Creating a connection to the SoftLayer_Billing_Order_Quote API service and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Billing_Order_QuoteService quoteService = new SoftLayer_Billing_Order_QuoteService();
            quoteService.authenticateValue = authenticate;
            // Setting init parameters
            quoteService.SoftLayer_Billing_Order_QuoteInitParametersValue = new SoftLayer_Billing_Order_QuoteInitParameters();
            quoteService.SoftLayer_Billing_Order_QuoteInitParametersValue.id = quoteId;

            try
            {
                // Getting the orders
                SoftLayer_Billing_Order[] orders = quoteService.getOrdersFromQuote();
                foreach (var order in orders)
                {
                    Console.WriteLine(order.id);
                    Console.WriteLine(order.createDate);
                    Console.WriteLine(order.orderTypeId);
                    Console.WriteLine(order.status);
                    Console.WriteLine(order.userRecordId);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get orders from quote: " + e.Message);
            }
        }
    }
}

```
