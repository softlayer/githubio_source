---
title: "CancelServer.cs"
description: "CancelServer.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Billing_ItemInitParameters"
    - "SoftLayer_Account"
    - "SoftLayer_Billing_ItemInitParametersValue"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Billing_Item_Hardware"
    - "SoftLayer_Hardware"
    - "SoftLayer_Billing_ItemService"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Billing_Item"
tags:
    - "baremetalservers"
---


```
//-----------------------------------------------------------------------
// <copyright file="CancelServer.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace CancelServerNamespace
{
    using System;
    using System.Collections.Generic;

    class CancelServer
    {
        /// <summary>
        /// Cancel servers from a list of IPs
        /// This script looks for a server with a determinate IP address and delete it.
        /// It makes a single call to the cancelService() method in the
        /// SoftLayer_Billing_Item API service
        /// </summary>
        /// <manualPages>
        /// Some referential web pages
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item_Hardware
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username and key.
            string username = "set me";
            string apiKey = "set me";

            // Creating the authentication
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring a new API service objects for:
            // SoftLayer_Account
            // SoftLayer_Billing_Item
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            SoftLayer_Billing_ItemService billingItemService = new SoftLayer_Billing_ItemService();
            billingItemService.authenticateValue = authenticate;

            // Adding an object mask to retrieve our billing items related to the servers
            // http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
            // for a list of the relational properties you can retrieve along with hardware.
            SoftLayer_ObjectMask mask = new SoftLayer_ObjectMask();
            mask.mask = "mask[billingItem]";
            accountService.SoftLayer_ObjectMaskValue = mask;

            // Making the call to retrieve our hardware records along with their billing item.
            SoftLayer_Hardware[] servers = accountService.getHardware();

            // The list of IPs from the servers you wish to cancel
            string[] ipsToCancel = { "1.1.1.1", "2.2.2.2" };

            // We are looking for the server which has the desired IP to delete it.
            foreach (string ipToCancel in ipsToCancel)
            {
                foreach (SoftLayer_Hardware server in servers)
                {
                    if (server.primaryIpAddress != null)
                    {
                        if (server.primaryIpAddress.Equals(ipToCancel))
                        {
                            if (server.billingItem != null)
                            {
                                SoftLayer_Billing_ItemInitParameters billingId = new SoftLayer_Billing_ItemInitParameters();
                                billingId.id = server.billingItem.id.GetValueOrDefault();
                                billingItemService.SoftLayer_Billing_ItemInitParametersValue = billingId;
                                bool ressult = billingItemService.cancelService();
                                Console.WriteLine(ressult);
                            }
                        }
                    }
                }
            }
        }
    }
}

```
