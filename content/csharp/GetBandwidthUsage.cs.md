---
title: "GetBandwidthUsage.cs"
description: "GetBandwidthUsage.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_HardwareInitParametersValue"
    - "SoftLayer_HardwareInitParameters"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_HardwareService"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetBandwidthUsage.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace GetBandwidthUsageNamespace
{
    using System;
    using System.Collections.Generic;

    class GetBandwidthUsage
    {
        /// <summary>
        /// Retrieve a bandwidth usage for a list of  servers.
        /// The scripts returns the bandwidth usage from an arbitrary
        /// list of servers, the script makes a simple call to the
        /// Softlayer_Hardware_Server::getObject method using a object mask
        /// in order to get the bandwidth information.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
        /// http://sldn.softlayer.com/reference/datatype/SoftLayer_Hardware_Server/
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username.           
            string username = "set me";

            // Your SoftLayer API key.            
            string apiKey = "set me";

            // The list of server that wish to see the bandwidth usage
            int[] servers = { 153851, 166391 };

            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            SoftLayer_HardwareService hardwareService = new SoftLayer_HardwareService();
            hardwareService.authenticateValue = authenticate;

            // Add an object mask to retrieve our hardware' related items such as its
            // host name and currentBillableBandwidthUsage. Object masks
            // can retrieve any information related to your object. See
            // http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
            // for a list of the relational properties you can retrieve along with hardware.
            string objectMask = "mask[hostname,currentBillableBandwidthUsage]";

            hardwareService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            hardwareService.SoftLayer_ObjectMaskValue.mask = objectMask;

            hardwareService.SoftLayer_HardwareInitParametersValue = new SoftLayer_HardwareInitParameters();

            try
            {
                decimal total = 0;
                foreach (var server in servers)
                {
                    hardwareService.SoftLayer_HardwareInitParametersValue.id = server;
                    var bandwidth_data = hardwareService.getObject();
                    Console.WriteLine(bandwidth_data.hostname + ":" + bandwidth_data.currentBillableBandwidthUsage + "GB");
                    total = total + bandwidth_data.currentBillableBandwidthUsage;
                }

                Console.WriteLine("Total :" + total + "GB");
            }
            catch (Exception e)
            {
                Console.WriteLine("unable to bandwidth usage : " + e.Message);
            }
        }
    }
}

```
