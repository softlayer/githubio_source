---
title: "RetrieveMetadata.cs"
description: "RetrieveMetadata.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_ObjectMask"
tags:
    - "metadata"
---


```
//-----------------------------------------------------------------------
// <copyright file="RetrieveMetadata.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace RetrieveMetadataNamespace
{
    using System;

    class RetrieveMetadata
    {
        /// <summary>
        /// Retrieves the user data for the VSIs in the account
        /// The script gets the user metadata for a VSI in the account we make a simple
        /// call the getVirtualGuests() in the SoftLayer_Virtual_Guest API service
        /// and we set an object mask to get the information about the user data
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username.            
            string username = "set me";

            // Your SoftLayer API key.            
            string apiKey = "set me";

            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring the API client
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;

            // Adding the object mask to the call to get the information about the user data.
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = "mask[userData]";

            try
            {
                // Retrieve our account's VSI records.
                SoftLayer_Virtual_Guest[] result = accountService.getVirtualGuests();
                Console.WriteLine("The list of VSIs has been retrieved successfully.");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve the list of VSIs " + e.Message);
            }
        }
    }
}

```
