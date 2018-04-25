---
title: "GetBandwidthPools.cs"
description: "GetBandwidthPools.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Network_Bandwidth_Version"
    - "SoftLayer_ObjectMask"
tags:
    - "bandwidthpools"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="GetBandwidthPools.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace BandwidthPools
{
    using System;
    using System.Reflection;
    class GetBandwidthPools
    {
        /// <summary>
        ///  Get Bandwidth Pools
        ///  This script retrieves the bandwidth pools for an account
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getBandwidthAllotments
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Bandwidth_Version1_Allotment
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            string username = "set me";
            // You SoftLayer apiKey
            string apiKey = "set me";
            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.   
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            // Define an object mask to retrieve the same properties than: https://control.softlayer.com/network/bandwidth/vdr
            string objectMask = "mask[locationGroup, totalBandwidthAllocated, currentBandwidthSummary, projectedPublicBandwidthUsage, detailCount]";
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = objectMask;
            try {
                SoftLayer_Network_Bandwidth_Version1_Allotment[] bandwidthList = accountService.getBandwidthAllotments();
                foreach (var bandwidth in bandwidthList)
                {
                    Console.WriteLine("Pool Name: " + bandwidth.name);
                    Console.WriteLine("Region: " + bandwidth.locationGroup.name);
                    Console.WriteLine("Servers: " + bandwidth.detailCount);
                    Console.WriteLine("Allocation: " + bandwidth.totalBandwidthAllocated);
                    // Verify if the currentBandwidthSummary is not null
                    if(bandwidth.currentBandwidthSummary != null)
                    {
                        Console.WriteLine("Current usage: " + bandwidth.currentBandwidthSummary.outboundBandwidthAmount);
                        Console.WriteLine("Projected Usage: " + bandwidth.projectedPublicBandwidthUsage);
                    }
                    else{
                        Console.WriteLine("Current usage: 0");
                        Console.WriteLine("Projected Usage: 0");
                    }
                    Console.WriteLine("======================================================");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get bandwidth pools: " + e.Message);
            }
        }
    }
}

```
