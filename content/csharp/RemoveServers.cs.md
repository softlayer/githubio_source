---
title: "RemoveServers.cs"
description: "RemoveServers.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Application_Delivery_Controller"
    - "SoftLayer_Hardware"
    - "SoftLayer_Network_Bandwidth_Version"
    - "SoftLayer_Virtual_Guest"
tags:
    - "bandwidthpools"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="RemoveServers.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace BandwidthPools
{
    using System;
    using System.Collections.Generic;
    class RemoveServers
    {
        /// <summary>
        ///  Remove servers from a bandwidth pool
        ///  This script removes servers from a bandwidth pool
        /// </summary>
        /// <manualPages>
		/// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Bandwidth_Version1_Allotment/requestVdrContentUpdates
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            string username = "set me";
            // You SoftLayer apiKey
            string apiKey = "set me";
            // Declare the Bandwidth pool id 
            int bandwidthPoolId = 236297;

            // Declare a collection of servers to be assigned to a bandwidth pool
            SoftLayer_Hardware[] hardwareToAdd  = new SoftLayer_Hardware[]{};
            // Declare a collection of servers to be unassigned from a allotment and assigned to the virtual private rack
            SoftLayer_Hardware[] hardwareToRemove  = new SoftLayer_Hardware[]{};
            // Declare a collection of VSI to be assigned to a bandwidth pool
            SoftLayer_Virtual_Guest[] cloudsToAdd = new SoftLayer_Virtual_Guest[] {};
            // Declare a collection of VSI ids to be unassigned from an allotment and assigned to the virtual private rack
            int[] cloudsToRemoveArray = { 13115425, 18223423 };
            // Declare the bandwidth pool to move the servers to provided only for backwards compatibility
            int optionalAllotmentId = 0;
            // Declare a collection of application delivery controllers to be assigned to a bandwidth pool
            SoftLayer_Network_Application_Delivery_Controller[] adcToAdd = new SoftLayer_Network_Application_Delivery_Controller[]{};
            // Declare a collection of application delivery controllers to be unassigned from an allotment and assigned to the virtual private rack
            SoftLayer_Network_Application_Delivery_Controller[] adcToRemove = new SoftLayer_Network_Application_Delivery_Controller[]{};
            // Creating a connection to the SoftLayer_Network_Bandwidth_Version1_Allotment API service and             
            // bind our API username and key to it.   
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Network_Bandwidth_Version1_AllotmentService allotmentService = new SoftLayer_Network_Bandwidth_Version1_AllotmentService();
            allotmentService.authenticateValue = authenticate;
            allotmentService.SoftLayer_Network_Bandwidth_Version1_AllotmentInitParametersValue = new SoftLayer_Network_Bandwidth_Version1_AllotmentInitParameters();
            allotmentService.SoftLayer_Network_Bandwidth_Version1_AllotmentInitParametersValue.id = bandwidthPoolId;

            // Add Virtual Servers to the cloudsToRemove list, in order that they can be removed
            List<SoftLayer_Virtual_Guest> cloudsToRemove = new List<SoftLayer_Virtual_Guest>();
            foreach (var vsi in cloudsToRemoveArray)
            {
                SoftLayer_Virtual_Guest virtualGuest = new SoftLayer_Virtual_Guest();
                virtualGuest.id = vsi;
                virtualGuest.idSpecified = true;
                cloudsToRemove.Add(virtualGuest);
            }
            try
            {
				// Remove the servers
                bool result = allotmentService.requestVdrContentUpdates(hardwareToAdd, hardwareToRemove, cloudsToAdd, cloudsToRemove.ToArray(), optionalAllotmentId, adcToAdd, adcToRemove);
                Console.WriteLine(result);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to remove servers: " + e.Message);
            }
        }
    }
}

```
