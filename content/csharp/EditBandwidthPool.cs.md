---
title: "EditBandwidthPool.cs"
description: "EditBandwidthPool.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Bandwidth_Version"
tags:
    - "bandwidthpools"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="EditBandwidthPool.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace BandwidthPools
{
    using System;
    class EditBandwidthPool
    {
        /// <summary>
        ///  Edit Bandwidth Pool
        ///  This script edits the properties of a bandwidth pool. Currently you may only change the name-
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/softlayer_network_bandwidth_version1_allotment/editObject
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey
            string apiKey = "set me";
            // Declare the Bandwidh Pool Id that you wish to edit
            int allotmentId = 234419;
			// Define the bandwidth pool's name which will be edited
			string name = "new NameTest";
            // Creating a connection to the SoftLayer_Network_Bandwidth_Version1_Allotment API service and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Network_Bandwidth_Version1_AllotmentService allotmentService = new SoftLayer_Network_Bandwidth_Version1_AllotmentService();
            allotmentService.authenticateValue = authenticate;
            // Build a SoftLayer_Network_Bandwidth_Version1_Allotment object, containing the properties to edit. (In this case only the name can be edited)
            SoftLayer_Network_Bandwidth_Version1_Allotment templateObject = new SoftLayer_Network_Bandwidth_Version1_Allotment();
            templateObject.name = name;
            // Setting init parameters
            allotmentService.SoftLayer_Network_Bandwidth_Version1_AllotmentInitParametersValue = new SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters();
            allotmentService.SoftLayer_Network_Bandwidth_Version1_AllotmentInitParametersValue.id = allotmentId;
            try {
                bool result = allotmentService.editObject(templateObject);
                Console.WriteLine(result);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to edit bandwidth pool: " + e.Message);
            }
        }
    }
}

```
