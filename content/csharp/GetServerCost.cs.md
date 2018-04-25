---
title: "GetServerCost.cs"
description: "GetServerCost.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Hardware"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Hardware_Server"
tags:
    - "billings"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetServerCost.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace GetServerCostNamespace
{
    using System;
    using System.Linq;

    class GetServerCost
    {
        /// <summary>
        /// Get the recurring cost of all servers on your account.
        /// Get a list of servers on a SoftLayer account along with their recurring
        /// monthly costs. We can get that by calling getHardware() in the
        /// SoftLayer_Account API service with an object mask to retrieve cost.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getCost
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

            // Declaring an object mask to get more information about the server cost
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = "mask(SoftLayer_Hardware_Server).cost";

            try
            {
                // Retrieving the bare metal servers for the account.
                SoftLayer_Hardware[] result = (SoftLayer_Hardware[])accountService.getHardware();
                SoftLayer_Hardware_Server[] resultHardwareServer = result.Cast<SoftLayer_Hardware_Server>().ToArray();
                foreach (SoftLayer_Hardware_Server item in resultHardwareServer)
                {
                    Console.WriteLine("Server: " + item.fullyQualifiedDomainName + " cost: " + item.cost);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve the cost. " + e.Message);
            }
        }
    }
}

```
