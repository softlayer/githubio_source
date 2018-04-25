---
title: "GetDetailVLAN.cs"
description: "GetDetailVLAN.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_VlanInitParametersValue"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Network_VlanInitParameters"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Network_Subnet_IpAddress"
    - "SoftLayer_Network_VlanService"
tags:
    - "vlan"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetDetailVLAN.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace GetDetailVLANNamespace
{
    using System;

    /// <summary>
    /// Retrieve VLAN details such as primary router and subnet.
    /// The script retrieves the primary router and subnet for a determinate VLAN
    /// associated with a SoftLayer customer account 
    /// We do this with a call to the getObject() method in the 
    /// SoftLayer_Network_Vlan API service using an object mask to retrieve  
    /// associated subnets and primary router records. See below for more details.
    /// </summary>
    /// <manualPages>
    /// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
    /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
    /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet_IpAddress
    /// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject
    /// </manualPages>
    class GetDetailVLAN
    {
        static void Main(string[] args)
        {
            // Your SoftLayer API key.            
            string username = "set me";

            // Your SoftLayer API username.            
            string apiKey = "set me";

            // the VLAN id you wish to see its details
            int vlanId = 557984;

            // Creating a connection to the SoftLayer_Network_VlanService API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring the API client
            SoftLayer_Network_VlanService networkService = new SoftLayer_Network_VlanService();
            networkService.authenticateValue = authenticate;

            // Declaring an object mask to get more information about the VLANs
            // such as the primaryRouter and the subnets
            networkService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            networkService.SoftLayer_ObjectMaskValue.mask = "mask[primaryRouter, subnets[ipAddresses]]";

            // Setting the init parameter 
            networkService.SoftLayer_Network_VlanInitParametersValue = new SoftLayer_Network_VlanInitParameters();
            networkService.SoftLayer_Network_VlanInitParametersValue.id = vlanId;

            try
            {
                // Sending the request to get the VLAN
                SoftLayer_Network_Vlan result = networkService.getObject();
                Console.WriteLine("The VLAN have been retrieved successfully. ");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve the VLAN. " + e.Message);
            }
        }
    }
}

```
