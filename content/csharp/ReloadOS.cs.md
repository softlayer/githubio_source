---
title: "ReloadOS.cs"
description: "ReloadOS.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware_ServerService"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Hardware_ServerInitParameters"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Hardware_ServerInitParametersValue"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Container_Hardware_Server_Configuration"
tags:
    - "baremetalservers"
---


```
//-----------------------------------------------------------------------
// <copyright file="ReloadOS.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace ReloadOSNamespace
{
    using System;
    using System.Collections.Generic;

    class ReloadOS
    {
        /// <summary>
        /// Reload servers from a list of IPs
        /// This script looks for a server with a determinate IP address and reloads
        /// the Operative System with another one.
        /// It makes a single call to the reloadOperatingSystem() method in the
        /// SoftLayer_Hardware_Server API service
        /// </summary>
        /// <manualPages>
        /// Some referential web pages
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/reloadOperatingSystem
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username.           
            string username = "set me";

            // Your SoftLayer API key.            
            string apiKey = "set me";

            // The IP addresses you wish to reload
            string[] ipsToReload = { "50.97.205.198", "50.97.205.196" };

            // The new OS you wish to load
            string newOSToLoad = "CentOS 5.x - Minimal Install (64 bit)";

            // Add an object mask to retrieve our prices related to the servers
            // http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
            // for a list of the relational properties you can retrieve along with hardware.
            string objectMask = "mask[billingItem[package[items[prices]]]]";

            // Create a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            SoftLayer_Hardware_ServerService hardwareService = new SoftLayer_Hardware_ServerService();
            hardwareService.authenticateValue = authenticate;

            // Setting the object mask to our hardwareService
            hardwareService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            hardwareService.SoftLayer_ObjectMaskValue.mask = objectMask;

            Dictionary<string, Dictionary<string, int>> serversToReload = new Dictionary<string, Dictionary<string, int>>();
            foreach (var ipToReload in ipsToReload)
            {
                var server = hardwareService.findByIpAddress(ipToReload);
                Dictionary<string, int> serverID = new Dictionary<string, int>();
                serverID.Add("id", server.id.GetValueOrDefault());

                if (server.billingItem != null)
                {
                    foreach (var item in server.billingItem.package.items)
                    {
                        if (item.description == newOSToLoad)
                        {
                            serverID.Add("priceId", item.prices[0].id.GetValueOrDefault());
                            serversToReload.Add(ipToReload, serverID);
                        }
                    }
                }
            }

            hardwareService.SoftLayer_Hardware_ServerInitParametersValue = new SoftLayer_Hardware_ServerInitParameters();
            SoftLayer_Container_Hardware_Server_Configuration config = new SoftLayer_Container_Hardware_Server_Configuration();
            SoftLayer_Product_Item_Price[] itemPrices = new SoftLayer_Product_Item_Price[1];
            config.itemPrices = itemPrices;
            config.itemPrices[0] = new SoftLayer_Product_Item_Price();
            foreach (var ipToReload in ipsToReload)
            {
                try
                {
                    hardwareService.SoftLayer_Hardware_ServerInitParametersValue.id = serversToReload[ipToReload]["id"];
                    config.itemPrices[0].id = serversToReload[ipToReload]["priceId"];
                    string reload = hardwareService.reloadOperatingSystem("FORCE", config);
                    Console.WriteLine(reload);
                }
                catch (Exception e)
                {
                    Console.WriteLine("unable to reload the server : " + e.Message);
                }
            }
        }
    }
}

```
