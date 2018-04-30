---
title: "CreateBandwidthPool.cs"
description: "CreateBandwidthPool.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Bandwidth_Version"
tags:
    - "bandwidthpools"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="CreateBandwidthPool.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace BandwidthPools
{
    using System;
    class CreateBandwidthPool
    {
        /// <summary>
        ///  Create Bandwidth Pool
        ///  This script creates a Bandwidth Pool.
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/softlayer_network_bandwidth_version1_allotment/createobject
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey
            string apiKey = "set me";
			// Define the bandwidth pool's name
			string name = "TestBandwidthPool";
			// Define the bandwidth pool's locationGroupId
			int locationGroupId = 1;
			// Define the accountId associated with this bandwidth pool
			int accountId = 207819;

            // Creating a connection to the SoftLayer_Network_Bandwidth_Version1_Allotment API service and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Network_Bandwidth_Version1_AllotmentService allotmentService = new SoftLayer_Network_Bandwidth_Version1_AllotmentService();
            allotmentService.authenticateValue = authenticate;

            // Build SoftLayer_Network_Bandwidth_Version1_Allotment object that you wish to create
            SoftLayer_Network_Bandwidth_Version1_Allotment templateObject = new SoftLayer_Network_Bandwidth_Version1_Allotment();
            templateObject.name = name;
            templateObject.locationGroupId = locationGroupId;
            templateObject.locationGroupIdSpecified = true;
            templateObject.bandwidthAllotmentTypeId = 2;
            templateObject.bandwidthAllotmentTypeIdSpecified = true;
            templateObject.serviceProviderId = 1;
            templateObject.serviceProviderIdSpecified = true;
            templateObject.accountId = accountId;
            templateObject.accountIdSpecified = true;
            try {
                bool result = allotmentService.createObject(templateObject);
                Console.WriteLine(result);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to create Bandwidth Pool: " + e.Message);
            }
        }
    }
}

```
