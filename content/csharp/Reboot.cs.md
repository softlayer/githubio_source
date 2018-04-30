---
title: "Reboot.cs"
description: "Reboot.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_ServerInitParameters"
    - "SoftLayer_Hardware_ServerInitParametersValue"
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Hardware_ServerService"
tags:
    - "baremetalservers"
---


```
//-----------------------------------------------------------------------
// <copyright file="Reboot.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace RebootNamespace
{
    using System;
    using System.Collections.Generic;

    class Reboot
    {
        /// <summary>
        /// Reboot a SoftLayer server
        /// Given a server id call the rebootDefault() method in the
        /// SoftLayer_Hardware_Server service to attempt to reboot the server via IPMI or
        /// its power strip if remote management is unavailable.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/rebootDefault
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username.           
            string username = "set me";

            // Your SoftLayer API key.                      
            string apiKey = "set me";

            // If you don't know your server id you can call getHardware() in the
            // SoftLayer_Account API service to get a list of hardware or call
            // findByIpAddress() in the SoftLayer_Hardware_Server service if you already
            // know your server's primary IP address.
            int serverId = 320902;

            // Creating a connection to the SoftLayer_Hardware_Server API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Hardware_ServerService hardwareServerService = new SoftLayer_Hardware_ServerService();
            hardwareServerService.authenticateValue = authenticate;

            // Setting the init parameter
            hardwareServerService.SoftLayer_Hardware_ServerInitParametersValue = new SoftLayer_Hardware_ServerInitParameters();
            hardwareServerService.SoftLayer_Hardware_ServerInitParametersValue.id = serverId;

            try
            {
                hardwareServerService.rebootDefault();
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to  reboot the server: " + e.Message);
            }
        }
    }
}

```
