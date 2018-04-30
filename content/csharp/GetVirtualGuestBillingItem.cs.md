---
title: "GetVirtualGuestBillingItem.cs"
description: "GetVirtualGuestBillingItem.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Virtual_Guest"
tags:
    - "billings"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetVirtualGuestBillingItem.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace GetVirtualGuestBillingItemNamespace
{
    using System;

    class GetVirtualGuestBillingItem
    {
        /// <summary>
        /// Retrieve the billing items  for the VSI in the account.
        /// This script makes a single call to the getVirtualGuests() method in the
        /// SoftLayer_Account API service and uses a object mask to get the
        /// billing items and items for each VSI server in the account.
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

            // Create a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring the API client
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;

            // Declaring the object mask to get information about the items.
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = "mask[id, hostname, domain, datacenter[longName], billingItem[item]]";

            try
            {
                // Retrieving the VSIs billing items for the account.
                SoftLayer_Virtual_Guest[] result = accountService.getVirtualGuests();
                Console.WriteLine("The billing items list have been retrieved successfully. ");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve the billing items list. " + e.Message);
            }
        }
    }
}

```
