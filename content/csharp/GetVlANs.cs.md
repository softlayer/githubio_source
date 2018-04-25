---
title: "GetVlANs.cs"
description: "GetVlANs.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Network_Subnet_IpAddress"
tags:
    - "vlan"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetVlANs.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace GetVlansNamespace
{
    using System;
    
    class GetVlANs
    {
        /// <summary>
        /// Retrieve account VLANs and subnet information.
        /// The script retrieves a list of all VLANs associated with a SoftLayer customer account 
        /// and prints a simple report detailing these VLANs and the subnets assigned to 
        /// them. We do this with a call to the getNetworkVlans() method in the 
        /// SoftLayer_Account API service using an object mask to retrieve the VLANs' 
        /// associated subnets and primary router records. See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkVlans
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username and key.            
            string username = "set me"; 
            string apiKey = "set me";

            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring the API client
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;

            // Declaring an object mask to get more information about the VLANs
            // such as the primaryRouter and the subnets
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = "mask[primaryRouter, subnets[ipAddresses]]";

            try
            {
                // Sending the request to get the VLANs
                SoftLayer_Network_Vlan[] result = accountService.getNetworkVlans();
                Console.WriteLine("The VLANs have been retrieved successfully. ");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve the VLANs. " + e.Message);
            }
        }
    }
}

```
