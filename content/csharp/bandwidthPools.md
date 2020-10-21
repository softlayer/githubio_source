---
title: "Bandwidth Pools"
description: "Managing Bandwidth pools in C#"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Bandwidth_Version"
tags:
    - "bandwidthpools"
    - "bandwidth"
---

## Create Bandwidth Pool

```csharp
﻿namespace BandwidthPools
{
    using System;
    class CreateBandwidthPool
    {
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

## Get Bandwidth Pools

```csharp
namespace BandwidthPools
{
    using System;
    using System.Reflection;
    class GetBandwidthPools
    {
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

## Edit Bandwidth Pool
```csharp
﻿namespace BandwidthPools
{
    using System;
    class EditBandwidthPool
    {
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


## Cancel Bandwith Pool

```csharp
﻿namespace BandwidthPools
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