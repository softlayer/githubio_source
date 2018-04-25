---
title: "GetTags.cs"
description: "GetTags.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_Tag"
tags:
    - "metadata"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetTags.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace GetTagsNamespace
{
    using System;

    class GetTags
    {
        /// <summary>
        /// Get all the tags in the account.
        /// The script gets all the tags in the account we make a simple
        /// call the getTags() in the SoftLayer_Account API service.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getTags
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

            try
            {
                // Getting the tags in the account.
                SoftLayer_Tag[] result = accountService.getTags();
                Console.WriteLine("The list of tags has been retrieved successfull.");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve the tag lists. " + e.Message);
            }
        }
    }
}

```
