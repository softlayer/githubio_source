---
title: "CreateArchiveTransaction.cs"
description: "CreateArchiveTransaction.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_AccountObjectFilterValue"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_AccountObjectFilter"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_Virtual_GuestObjectFilter"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualguests"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetVirtualGuests.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace VirtualGuests
{
    using System;
    class GetVirtualGuests
    {
        /// <summary>
        ///  Get Virtual Guests
        ///  This script retrieves an account's associated virtual guest objects. Also it uses an objectMask and objectFilter.
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
        /// </manualPages>
        static void Main(string[] args)
        {
            // You SoftLayer username
            string username = "set me";
            // Your SoftLayer API key.            
            string apiKey = "set me";

            // Creating a connection to the SoftLayer_AccountService API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;

            // Declare an Object Mask
            String objectMask = "mask[primaryIpAddress, primaryBackendIpAddress, operatingSystemReferenceCode]";
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = objectMask;
            

            // Declare an object filter
            SoftLayer_AccountObjectFilter filter = new SoftLayer_AccountObjectFilter();
            filter.virtualGuests = new SoftLayer_Virtual_GuestObjectFilter();
            filter.virtualGuests.hostname = new SoftLayer_Utility_ObjectFilter_Operation();
            filter.virtualGuests.hostname.operation = "*=rcv";
            accountService.SoftLayer_AccountObjectFilterValue = filter;

            try
            {
                SoftLayer_Virtual_Guest[] result = accountService.getVirtualGuests();
                foreach (var vsi in result)
                {
                    Console.WriteLine("Id: " + vsi.id);
                    Console.WriteLine("FQDN: " + vsi.fullyQualifiedDomainName);
                    Console.WriteLine("Public IP: " + vsi.primaryIpAddress);
                    Console.WriteLine("Private IP: " +  vsi.primaryBackendIpAddress);
                    Console.WriteLine("Operating System Reference Code: " + vsi.operatingSystemReferenceCode);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve the Virtual Guests. " + e);
            }
        }
    }
}

```
