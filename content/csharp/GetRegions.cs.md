---
title: "GetRegions.cs"
description: "GetRegions.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Location_Group_TypeObjectFilter"
    - "SoftLayer_Location_GroupObjectFilterValue"
    - "SoftLayer_Location_GroupObjectFilter"
    - "SoftLayer_Location_GroupService"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Location_Group"
tags:
    - "bandwidthpools"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="GetRegions.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace BandwidthPools
{
    using System;
    class GetRegions
    {
        /// <summary>
        ///  Get Regions
        ///  This script retrieves the regions which are required to create the bandwidth pool (locationGroupId)
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Location_Group/getAllObjects
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Location_Group
        /// http://sldn.softlayer.com/article/object-masks
        /// http://sldn.softlayer.com/article/Object-Filters
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            string username = "set me"; 
            // You SoftLayer apiKey
            string apiKey = "set me";
            // Creating a connection to the SoftLayer_Location_Group API service and             
            // bind our API username and key to it.   
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Location_GroupService groupService = new SoftLayer_Location_GroupService();
            groupService.authenticateValue = authenticate;
            // Define an object mask, to get the locationGroupType property
            string objectMask = "mask[locationGroupType]";
            groupService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            groupService.SoftLayer_ObjectMaskValue.mask = objectMask;
            // Declare an object filter, to filter by VDR regions
            SoftLayer_Location_GroupObjectFilter objectFilter = new SoftLayer_Location_GroupObjectFilter();
            objectFilter.locationGroupType = new SoftLayer_Location_Group_TypeObjectFilter();
            objectFilter.locationGroupType.name = new SoftLayer_Utility_ObjectFilter_Operation();
            objectFilter.locationGroupType.name.operation = "_=VDR";
            groupService.SoftLayer_Location_GroupObjectFilterValue = objectFilter;

            try
            {
                SoftLayer_Location_Group[] regions = groupService.getAllObjects();
                foreach (var region in regions)
                {
                    Console.WriteLine("Id: " + region.id + " Name: " + region.name);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve regions: " + e.Message);
            }
        }
    }
}

```
