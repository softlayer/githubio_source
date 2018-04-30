---
title: "AddBulkDevicesAccess.cs"
description: "AddBulkDevicesAccess.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_User_CustomerInitParameters"
    - "SoftLayer_Account"
    - "SoftLayer_Utility_ObjectFilter_Operation_Option"
    - "SoftLayer_User_CustomerObjectFilter"
    - "SoftLayer_AccountObjectFilter"
    - "SoftLayer_User_CustomerInitParametersValue"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_User_Customer"
    - "SoftLayer_Hardware"
    - "SoftLayer_AccountObjectFilterValue"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_User_CustomerService"
tags:
    - "users"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="AddBulkDevicesAccess.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Users
{
    using System;
    using System.Collections.Generic;
    class AddBulkDevicesAccess
    {
        /// <summary>
        /// This script adds multiple devices (Virtual Servers or Hardware objects) to a portal users's access list.
        /// It is only necessary to specify the ip addresses from devices and the usernames from users that you wish to allow access to the devices.
        /// For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware
        /// http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/addBulkVirtualGuestAccess
        /// http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/addBulkHardwareAccess
        /// http://sldn.softlayer.com/article/Object-Filters
        /// </manualPages>
        static void Main(string[] args)
        {
            //Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey
            string apiKey = "set me";
            // Define the ip addresses from the devices that you wish to allow access to users
            string[] devices = new string[] { "169.57.129.196", "169.50.64.58", "10.143.219.168", "10.81.14.205"};
            // Declare the usernames that you wish to add the permissions
            List<string> usernameList = new List<string>();
            usernameList.Add("username1");
            usernameList.Add("username2");
            // Creating a connection to the SoftLayer_User_Customer and SoftLayer_Account API services and bind our API username and key to it.
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_User_CustomerService customerService = new SoftLayer_User_CustomerService();
            customerService.authenticateValue = authenticate;
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            // Declare an object filter, to get the user ids from usernames
            SoftLayer_AccountObjectFilter objectFilter = new SoftLayer_AccountObjectFilter();
            objectFilter.users = new SoftLayer_User_CustomerObjectFilter();
            objectFilter.users.username = new SoftLayer_Utility_ObjectFilter_Operation();
            objectFilter.users.username.operation = "in";
            objectFilter.users.username.options = new SoftLayer_Utility_ObjectFilter_Operation_Option[1];
            objectFilter.users.username.options[0] = new SoftLayer_Utility_ObjectFilter_Operation_Option();
            objectFilter.users.username.options[0].name = "data";
            objectFilter.users.username.options[0].value = usernameList.ToArray();
            try
            {
                // Declare arrays to store ids from hardware objects and virtual guests
                List<int> hardwareIds = new List<int>();
                List<int> guestIds = new List<int>();
                // Get Hardware objects
                SoftLayer_Hardware[] hardwareList = accountService.getHardware();
                // Get Virtual Guests
                SoftLayer_Virtual_Guest[] guestList = accountService.getVirtualGuests();
                // Get hardware ids and virtual guests ids from the ip addresses
                foreach (var device in devices)
                {
                    foreach (var hardware in hardwareList)
                    {
                        if (device == hardware.primaryIpAddress || device == hardware.primaryBackendIpAddress)
                        {
                            hardwareIds.Add((int)hardware.id);
                        }
                    }
                    foreach (var guest in guestList)
                    {
                        if (device == guest.primaryIpAddress || device == guest.primaryBackendIpAddress)
                        {
                            guestIds.Add((int)guest.id);
                        }
                    }
                }
                // Setting object filter
                accountService.SoftLayer_AccountObjectFilterValue = objectFilter;
                SoftLayer_User_Customer[] users = accountService.getUsers();
                Console.WriteLine("***** PERMISSIONS ALLOWED *****");
                foreach (var user in users)
                {
                    // Setting init parameter
                    customerService.SoftLayer_User_CustomerInitParametersValue = new SoftLayer_User_CustomerInitParameters();
                    customerService.SoftLayer_User_CustomerInitParametersValue.id = (int)user.id;
                    // Allow access for hardware devices
                    bool resultHarware = customerService.addBulkHardwareAccess(hardwareIds.ToArray());
                    // Allow access for virtual guest 
                    bool resultGuests = customerService.addBulkVirtualGuestAccess(guestIds.ToArray());
                    Console.WriteLine("User: " + user.username + "    Hardware devices: " + resultHarware + "     Virtual Servers: " + resultGuests);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to allow access to devices: " + e.Message);
            }
        }
    }
}

```
