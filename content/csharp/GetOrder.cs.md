---
title: "GetOrder.cs"
description: "GetOrder.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Order"
    - "SoftLayer_Billing_Order_QuoteService"
    - "SoftLayer_Billing_Order_QuoteInitParameters"
    - "SoftLayer_Billing_Order_Quote"
    - "SoftLayer_Billing_Order_QuoteInitParametersValue"
tags:
    - "quotes"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="GetOrder.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Quotes
{
    using System;
    class GetOrder
    {
        /// <summary>
        /// Get Order
        /// This script retrieves a quite's corresponding order
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/getOrder
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Order
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Define the quote identifier that you wish to get the order
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
                // Getting the order
                SoftLayer_Billing_Order order = quoteService.getOrder();
                Console.WriteLine(order.id);
                Console.WriteLine(order.orderQuoteId);
                Console.WriteLine(order.createDate);
                Console.WriteLine(order.userRecordId);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get orders from quote: " + e.Message);
            }
        }
    }
}

```
