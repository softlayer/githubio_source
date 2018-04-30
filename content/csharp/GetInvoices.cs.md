---
title: "GetInvoices.cs"
description: "GetInvoices.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Billing_Invoice"
    - "SoftLayer_ObjectMask"
tags:
    - "billings"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetInvoices.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace GetInvoicesNamespace
{
    using System;

    class GetInvoices
    {
        /// <summary>
        /// Retrieve the billing info for the Bare Metals in the account.
        /// This script makes a single call to the getInvoices() method in the
        /// SoftLayer_Account API service and uses a object mask to get more
        /// information about the invoices.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getInvoices
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Invoice
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username and API key.            
            string username = "set me";
            string apiKey = "set me";

            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring the API client
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;

            // Declaring an object mask to get more information about the invoices
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = "mask[payment,amount,invoiceTotalOneTimeAmount,invoiceTotalRecurringAmount,invoiceTotalOneTimeTaxAmount,invoiceTotalRecurringTaxAmount]";

            try
            {
                // Retrieving the invoices
                SoftLayer_Billing_Invoice[] result = accountService.getInvoices();
                Console.WriteLine("The invoices has been retrieve successfully. ");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve the invoices. " + e.Message);
            }
        }
    }
}

```
