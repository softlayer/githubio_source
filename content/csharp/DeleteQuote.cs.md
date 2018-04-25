---
title: "DeleteQuote.cs"
description: "DeleteQuote.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Order_QuoteInitParametersValue"
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Order_QuoteService"
    - "SoftLayer_Billing_Order_QuoteInitParameters"
    - "SoftLayer_Billing_Order_Quote"
tags:
    - "quotes"
---


```
﻿﻿//-----------------------------------------------------------------------
// <copyright file="DeleteQuote.cs" company="Softlayer">
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
    class DeleteQuote
    {
        /// <summary>
        /// Delete Quote
        /// This script deletes the quote of an order
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/deleteQuote
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Order_Quote
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Define the quote identifier that you wish to delete
            int quoteId = 1556821;
            // Creating a connection to the SoftLayer_Account API service and             
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
                SoftLayer_Billing_Order_Quote result = quoteService.deleteQuote();
                Console.WriteLine("The quoteId: " + result.id + " was: " + result.status);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to delete quote: " + e.Message);
            }
        }
    }
}

```
