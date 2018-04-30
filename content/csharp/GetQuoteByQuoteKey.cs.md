---
title: "GetQuoteByQuoteKey.cs"
description: "GetQuoteByQuoteKey.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Billing_Order_QuoteService"
    - "SoftLayer_Billing_Order_Quote"
tags:
    - "quotes"
---


```
﻿﻿//-----------------------------------------------------------------------
// <copyright file="GetQuoteByQuoteKey.cs" company="Softlayer">
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
    class GetQuoteByQuoteKey
    {
        /// <summary>
        /// Get Quote By Quote Key
        /// This script retrieves a valid quote record of a SoftLayer order by quote key.
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/getQuoteByQuoteKey
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Order_Quote
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Define the quote key
            string quoteKey = "8f51025debc3fa0693a539cf32952fd1";
            // Creating a connection to the SoftLayer_Billing_Order_Quote API service and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Billing_Order_QuoteService quoteService = new SoftLayer_Billing_Order_QuoteService();
            quoteService.authenticateValue = authenticate;
            try
            {
                SoftLayer_Billing_Order_Quote quote = quoteService.getQuoteByQuoteKey(quoteKey);
                Console.WriteLine("Id: " + quote.id + " Name: " + quote.name + " Create Date: " + quote.createDate + " Expiration Date: " + quote.expirationDate);   
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get quote record: " + e.Message);
            }
        }
    }
}

```
