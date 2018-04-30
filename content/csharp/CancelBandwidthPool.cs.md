---
title: "CancelBandwidthPool.cs"
description: "CancelBandwidthPool.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Bandwidth_Version"
tags:
    - "bandwidthpools"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="CancelBandwidthPool.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace BandwidthPools
{
    using System;
    class CancelBandwidthPool
    {
        /// <summary>
        ///  Remove Bandwidth Pool
        ///  This script cancels a Bandwidth Pool
        ///  Note: New VDRs can be created dynamically, but deleting existing VDRs only happens 
        ///  at 12:01 on the bill date, just like deleting servers happens.
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/requestVdrCancellation
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey
            string apiKey = "set me";
            // Declare the bandwidth pool id that you wish to delete
            int allotmentId = 236221;
            // Creating a connection to the SoftLayer_Network_Bandwidth_Version1_Allotment API service and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Network_Bandwidth_Version1_AllotmentService allotmentService = new SoftLayer_Network_Bandwidth_Version1_AllotmentService();
            allotmentService.authenticateValue = authenticate;
            // Setting init parameters
            allotmentService.SoftLayer_Network_Bandwidth_Version1_AllotmentInitParametersValue = new SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters();
            allotmentService.SoftLayer_Network_Bandwidth_Version1_AllotmentInitParametersValue.id = allotmentId;
            try
            {
                bool result = allotmentService.requestVdrCancellation();
                Console.WriteLine(result);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to cancel Vdr: " + e.Message);
            }    
        }
    }
}

```
