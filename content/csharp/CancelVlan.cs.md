---
title: "CancelVlan.cs"
description: "CancelVlan.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_VlanInitParametersValue"
    - "SoftLayer_Billing_ItemInitParameters"
    - "SoftLayer_Billing_ItemInitParametersValue"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Network_VlanInitParameters"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Network_Vlan"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Network_VlanService"
    - "SoftLayer_Billing_ItemService"
tags:
    - "vlan"
---


```
//-----------------------------------------------------------------------
// <copyright file="CancelVlan.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace CancelVlanNamespace
{
    using System;

    /// <summary>
    /// Example to cancel a VLAN
    /// The script will get the Billing_Item id of the VLAN service
    /// then it will cancel the VLAN service
    /// </summary>
    /// <manualPages>
    /// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan
    /// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Vlan/getObject
    /// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item
    /// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Item/cancelService
    /// </manualPages>
    class CancelVlan
    {
        static void Main(string[] args)
        {
            // Your SoftLayer API username and key.                      
            string username = "set me";
            string apiKey = "set me";

            // The VLAN id you wish to cancel
            int vlanId = 557984;

            // Creating a connection to the SoftLayer_Network_VlanService API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring the API client
            SoftLayer_Network_VlanService networkService = new SoftLayer_Network_VlanService();
            networkService.authenticateValue = authenticate;
            SoftLayer_Billing_ItemService billingItemService = new SoftLayer_Billing_ItemService();
            billingItemService.authenticateValue = authenticate;

            // Setting the init paramters
            networkService.SoftLayer_Network_VlanInitParametersValue = new SoftLayer_Network_VlanInitParameters();
            networkService.SoftLayer_Network_VlanInitParametersValue.id = vlanId;

            // Declaring an object mask to get the billing item information
            networkService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            networkService.SoftLayer_ObjectMaskValue.mask = "mask[billingItem]";

            try
            {
                // Getting the Billing Item to cancel the VLAN service.
                SoftLayer_Network_Vlan vlan = networkService.getObject();

                // Canceling the VLAN service.
                billingItemService.SoftLayer_Billing_ItemInitParametersValue = new SoftLayer_Billing_ItemInitParameters();
                billingItemService.SoftLayer_Billing_ItemInitParametersValue.id = vlan.billingItem.id.Value;
                bool canceled = billingItemService.cancelService();
                Console.WriteLine("The VLAN was canceled successfully. " + canceled);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to cancel the VLAN. " + e.Message);
            }
        }
    }
}

```
