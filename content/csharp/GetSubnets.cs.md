---
title: "GetSubnets.cs"
description: "GetSubnets.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_VlanInitParametersValue"
    - "SoftLayer_Network_VlanService"
    - "SoftLayer_Network_VlanInitParameters"
    - "SoftLayer_Network_Subnet"
    - "SoftLayer_Network_Vlan"
tags:
    - "vlan"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetSubnets.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace GetSubnetsNamespace
{
    using System;

    class GetSubnets
    {
        /// <summary>
        /// Retrieve the subnets for a VLAN 
        /// The example retrieves all the subnets for a determinate VLAN
        /// associated with a SoftLayer customer account 
        /// We do this with a call to the getSubnets() method in the 
        /// SoftLayer_Network_Vlan API service. See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getSubnets
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API key and username.            
            string username = "set me";
            string apiKey = "set me";

            // The VLAN id you wish to see its subnets
            int vlanId = 557984;

            // Creating a connection to the SoftLayer_Network_VlanService API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring the API client
            SoftLayer_Network_VlanService networkService = new SoftLayer_Network_VlanService();
            networkService.authenticateValue = authenticate;

            networkService.SoftLayer_Network_VlanInitParametersValue = new SoftLayer_Network_VlanInitParameters();
            networkService.SoftLayer_Network_VlanInitParametersValue.id = vlanId;

            try
            {
                // Sending the request to get the subnets
                SoftLayer_Network_Subnet[] result = networkService.getSubnets();
                Console.WriteLine("The subnet was retrieved successfully. ");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve the subnets. " + e.Message);
            }
        }
    }
}

```
