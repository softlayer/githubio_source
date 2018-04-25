---
title: "GetQuotes.cs"
description: "GetQuotes.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Billing_Order_Quote"
    - "SoftLayer_ObjectMask"
tags:
    - "quotes"
---


```
﻿﻿//-----------------------------------------------------------------------
// <copyright file="GetQuotes.cs" company="Softlayer">
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
    class GetQuotes
    {
        /// <summary>
        /// Get Quotes
        /// This script retrieves an account's quotes
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getQuotes
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Order_Quote
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            // Define an object mask, to get amount property
            string objectMask = "mask[order]";
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = objectMask;
            try {
                SoftLayer_Billing_Order_Quote[] quotes = accountService.getQuotes();
                foreach (var quote in quotes)
                {
                    Console.WriteLine("Id: " + quote.id + " Name: " + quote.name + " Amount: "+ quote.order.orderTotalAmount + 
                        " Status: " + quote.status + " Note: "+ quote.publicNote + " Create Date: " + quote.createDate + " Expiration Date: " + quote.expirationDate);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get quotes: " + e.Message);
            }
        }
    }
}

```
