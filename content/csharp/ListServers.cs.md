---
title: "ListServers.cs"
description: "ListServers.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
tags:
    - "baremetalservers"
---


```
//-----------------------------------------------------------------------
// <copyright file="ListServers.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace ListServersNamespace
{
    using System;
    using System.Collections.Generic;

    class ListServers
    {
        /// <summary>
        /// List Bare Metal servers.
        /// The script retrieves a list of all bare metal servers in your
        /// account. it makes a single call to the Softlayer_Account::getHardware
        /// method for more information see below.
        /// </summary>
        /// <manualPages>
        /// https://sldn.softlayer.com/reference/services/SoftLayer_Account
        /// https://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
        /// https://sldn.softlayer.com/reference/datatype/SoftLayer_Hardware/
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

            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;

            try
            {
                // getHardware will get all bare metal servers that an account has
                List<SoftLayer_Hardware> hardawareList = accountService.getHardware().ToList();
                foreach (var item in hardawareList)
                {
                    Console.WriteLine("hostname : " + item.hostname);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("unable to list the servers: " + e.Message);
            }
        }
    }
}

```
