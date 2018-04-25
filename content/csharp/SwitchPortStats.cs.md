---
title: "SwitchPortStats.cs"
description: "SwitchPortStats.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Hardware_ServerService"
    - "SoftLayer_Network_ComponentService"
    - "SoftLayer_NetworkComponent"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Network_ComponentInitParameters"
    - "SoftLayer_Container_Network_Port_Statistic"
    - "SoftLayer_Hardware_ServerInitParametersValue"
    - "SoftLayer_Network_ComponentInitParametersValue"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Hardware_ServerInitParameters"
    - "SoftLayer_Network_Component"
tags:
    - "vlan"
---


```
//-----------------------------------------------------------------------
// <copyright file="SwitchPortStats.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace SwitchPortStatsNamespace
{
    using System;

    class SwitchPortStats
    {
        /// <summary>
        /// Retrieve a list of switchport statistics for a server's network interfaces.
        /// This script makes a single call to the getPortStatistics() method in the
        /// SoftLayer_Network_Component API service
        /// for each of a server's network components to query port statistics for that
        /// interface from SoftLayer's switches. Port statistics are modeled by the
        /// SoftLayer__Container_Network_Port_Statistic data type
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_NetworkComponent/getPortStatistics
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Network_Port_Statistic
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API key and username.            
            string username = "set me";
            string apiKey = "set me";

            // Your server's id. Call the getHardware() method in the SoftLayer_Account API
            // service (http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware)
            // to get a list of your account's hardware records.
            int serverId = 87165;

            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring the API client
            SoftLayer_Hardware_ServerService hardwareServerService = new SoftLayer_Hardware_ServerService();
            hardwareServerService.authenticateValue = authenticate;
            SoftLayer_Network_ComponentService networkComponentService = new SoftLayer_Network_ComponentService();
            networkComponentService.authenticateValue = authenticate;

            // Switchport statistics are measured off the server's network components. Use
            // an object mask to network component records along with our server record.
            hardwareServerService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            hardwareServerService.SoftLayer_ObjectMaskValue.mask = "mask[networkComponents]";

            // Setting the init parameter 
            hardwareServerService.SoftLayer_Hardware_ServerInitParametersValue = new SoftLayer_Hardware_ServerInitParameters();
            hardwareServerService.SoftLayer_Hardware_ServerInitParametersValue.id = serverId;
            networkComponentService.SoftLayer_Network_ComponentInitParametersValue = new SoftLayer_Network_ComponentInitParameters();

            try
            {
                // Making the call to retrieve our hardware record. Once we have that we can query
                // the server's network components.
                SoftLayer_Hardware_Server server = hardwareServerService.getObject();

                // Separating our network components for easier processing later.
                SoftLayer_Network_Component[] networkComponents = server.networkComponents;

                // Looping through our server's network components. For each NIC make a call to the
                // SoftLayer_Network_Component API service method getPortStatics() to get a list
                // of switchport statistics retrieved from the switch on the other side of your
                // NIC. Print a simple report per NIC.
                foreach (SoftLayer_Network_Component networkComponent in networkComponents)
                {
                    // Skipping the management network component.
                    if (!networkComponent.name.Equals("mgmt"))
                    {
                        networkComponentService.SoftLayer_Network_ComponentInitParametersValue.id = networkComponent.id.Value;

                        // Retrieving switchport statistics for the NIC.
                        SoftLayer_Container_Network_Port_Statistic stats = networkComponentService.getPortStatistics();
                        Console.WriteLine("The stats have been retrieved successfully. ");
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve server record. " + e.Message);
            }
        }
    }
}

```
