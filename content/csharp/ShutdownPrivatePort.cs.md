---
title: "ShutdownPrivatePort.cs"
description: "ShutdownPrivatePort.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_GuestInitParametersValue"
    - "SoftLayer_Virtual_GuestInitParameters"
    - "SoftLayer_AccountObjectFilter"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_Virtual_GuestObjectFilter"
    - "SoftLayer_Virtual_GuestService"
    - "SoftLayer_AccountObjectFilterValue"
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualguests"
---


```
//-----------------------------------------------------------------------
// <copyright file="ShutdownPrivatePort.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace VirtualGuests
{
    using System;
    class ShutdownPrivatePort
    {
        /// <summary>
        ///  Shut Down Private Port
        ///  This script shuts down the private network port
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/shutdownPrivatePort
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
        /// http://sldn.softlayer.com/article/Object-Filters
        /// </manualPages>
        static void Main(String [] args)
        {
            // You SoftLayer username
            string username = "set me";
            // Your SoftLayer API key.            
            string apiKey = "set me";
            // Creating a connection to the SoftLayer_Account and SoftLayer_Virtual_Guest API services and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            // SoftLayer_Account
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            // SoftLayer_Virtual_Guest
            SoftLayer_Virtual_GuestService guestService = new SoftLayer_Virtual_GuestService();
            guestService.authenticateValue = authenticate;
            // Define the hostname from vsi that you wish to shut down private port
            string hostname = "rcv-test1public";
            // Declare an objectFilter to get the id from hostname specified.
            SoftLayer_AccountObjectFilter filter = new SoftLayer_AccountObjectFilter();
            filter.virtualGuests = new SoftLayer_Virtual_GuestObjectFilter();
            filter.virtualGuests.hostname = new SoftLayer_Utility_ObjectFilter_Operation();
            filter.virtualGuests.hostname.operation = "*="+hostname;
            accountService.SoftLayer_AccountObjectFilterValue = filter;
            try
            {
                // Get the virtual guest with the hostname specified
                SoftLayer_Virtual_Guest[] virtualGuests = accountService.getVirtualGuests();
                // Set init parameters
                guestService.SoftLayer_Virtual_GuestInitParametersValue = new SoftLayer_Virtual_GuestInitParameters();
                guestService.SoftLayer_Virtual_GuestInitParametersValue.id = (int)virtualGuests[0].id;
                // Shut down private port from the vsi
                bool result = guestService.shutdownPrivatePort();
                Console.WriteLine("Was the private port shut down?: " + result);
                // The following lines will help if you want to active the private port from the vsi
                // bool result = guestService.activatePrivatePort();
                // Console.WriteLine("Was the private port activated?: " + result);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to shut down the private port: " + e.Message);
            }
        }
    }
}

```
