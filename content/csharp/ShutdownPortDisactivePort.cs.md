---
title: "ShutdownPortDisactivePort.cs"
description: "ShutdownPortDisactivePort.cs"
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
// <copyright file="ShutdownPortDisactivePort.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace ShutdownPortdisactivePortNamespace
{
    using System;
    using System.Collections.Generic;

    class ShutdownPortdisactivePort
    {
        /// <summary>
        /// Sets the networks speed for a hardware device
        /// This script makes a single call to the setPublicNetworkInterfaceSpeed() method
        /// to change the speed to public network or call the setPrivateNetworkInterfaceSpeed method
        /// to change the speed to private network.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/setPrivateNetworkInterfaceSpeed
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

            SoftLayer_Hardware_ServerService hardwareServerService = new SoftLayer_Hardware_ServerService();
            hardwareServerService.authenticateValue = authenticate;

            // The Id of the hardware you wish to modify the networks.
            int hardwareId = 167407;

            // The speed you wish configure if you want to disconnect the network you should set the value to '0'
            int newSpeedPublicNetwork = 10;
            int newSpeedPrivateNetwork = 100;

            // Setting the init parameter in our hardwareServerService
            hardwareServerService.SoftLayer_Hardware_ServerInitParametersValue = new SoftLayer_Hardware_ServerInitParameters();
            hardwareServerService.SoftLayer_Hardware_ServerInitParametersValue.id = hardwareId;

            try
            {
                // It is not possible to update the two networks at same time, you need to update one and wait until
                // the transaction is completed to update the second one.
                var result = hardwareServerService.setPublicNetworkInterfaceSpeed(newSpeedPublicNetwork);
                Console.WriteLine("The public network speed has been modified? " + result);
                result = hardwareServerService.setPrivateNetworkInterfaceSpeed(newSpeedPrivateNetwork);
                Console.WriteLine("The private network speed has been modified? " + result);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Unable to set the network speed: " + ex.Message);
            }
        }
    }
}

```
