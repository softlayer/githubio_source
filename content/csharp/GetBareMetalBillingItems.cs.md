---
title: "GetBareMetalBillingItems.cs"
description: "GetBareMetalBillingItems.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Hardware"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_ObjectMask"
tags:
    - "billings"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetBareMetalBillingItems.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace GetBareMetalBillingItemsNamespace
{
    using System;
    
    class GetBareMetalBillingItems
    {
        /// <summary>
        /// Retrieve the billing info for the Bare Metals in the account.
        /// This script makes a single call to the getHardware() method in the
        /// SoftLayer_Account API service and uses a object mask to get the
        /// billing items and items for each Bare Metal server in the account.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item
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

            // Declaring the object mask to get information about the billing items.
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = "mask[id, hostname, domain, datacenter[longName], billingItem[item]]";

            try
            {
                // Retrieving the bare metal servers billing items for the account.
                SoftLayer_Hardware[] result = (SoftLayer_Hardware[])accountService.getHardware();
                Console.WriteLine("The billing items list has been retrieved. ");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve the billing items list. " + e.Message);
            }
        }
    }
}

```
