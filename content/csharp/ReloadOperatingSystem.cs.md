---
title: "ReloadOperatingSystem.cs"
description: "ReloadOperatingSystem.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_GuestInitParametersValue"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_AccountObjectFilter"
    - "SoftLayer_Virtual_GuestObjectFilter"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_AccountObjectFilterValue"
    - "SoftLayer_AccountService"
    - "SoftLayer_Product_Item_PriceObjectFilter"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_PackageInitParameters"
    - "SoftLayer_Product_PackageService"
    - "SoftLayer_Product_PackageObjectFilter"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_ItemObjectFilter"
    - "SoftLayer_Account"
    - "SoftLayer_Product_PackageInitParametersValue"
    - "SoftLayer_Virtual_GuestInitParameters"
    - "SoftLayer_Product_PackageObjectFilterValue"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_Virtual_GuestService"
    - "SoftLayer_Container_Hardware_Server_Configuration"
tags:
    - "virtualguests"
---


```
//-----------------------------------------------------------------------
// <copyright file="ReloadOperatingSystem.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace VirtualGuests
{
    using System;
    using System.Collections.Generic;
    class ReloadOperatingSystem
    {
        /// <summary>
        ///  Reload Operating System
        ///  This script reloads current system configuration.
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/reloadOperatingSystem
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration
        /// http://sldn.softlayer.com/article/Object-Filters
        /// </manualPages>
        public ReloadOperatingSystem()
        {
            // You SoftLayer username
            string username = "set me";
            // Your SoftLayer API key.            
            string apiKey = "set me";
            // Define the hostname from the vsi that you wish to reload the operating system
            string hostname = "rcv-test1public";
            // Declare token - This service has a confirmation protocol for proceeding with the reload. To proceed with the reload 
            // without confirmation, simply pass in 'FORCE' as the token parameter. 
            string token = "FORCE";
			// Declare the osKeyName from OS that you wish to reload
            string osKeyName = "OS_WINDOWS_2003_STD_64_BIT_SP2_WR2";
            // Creating a connection to the SoftLayer_Account, SoftLayer_Virtual_Guest and SoftLayer_Product_Package API services and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            // SoftLayer_Account
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            // SoftLayer_Virtual_Guest
            SoftLayer_Virtual_GuestService guestService = new SoftLayer_Virtual_GuestService();
            guestService.authenticateValue = authenticate;
            // SoftLayer_Product_Package
            SoftLayer_Product_PackageService packageService = new SoftLayer_Product_PackageService();
            packageService.authenticateValue = authenticate;

            // Define an objectMask for SoftLayer_Account, to get the packageId from the Vsi
            string objectMask = "mask[billingItem[package]]";
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = objectMask;
            // Declare an objectFilter for SoftLayer_Account, to get the id from hostname specified
            SoftLayer_AccountObjectFilter filter = new SoftLayer_AccountObjectFilter();
            filter.virtualGuests = new SoftLayer_Virtual_GuestObjectFilter();
            filter.virtualGuests.hostname = new SoftLayer_Utility_ObjectFilter_Operation();
            filter.virtualGuests.hostname.operation = "*=" + hostname;
            accountService.SoftLayer_AccountObjectFilterValue = filter;

            // Define an objectMask for SoftLayer_Product_Package, in order to have access for "keyName" property, to filter by it
            String objectMaskPackage = "mask[item[keyName]]";
            packageService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            packageService.SoftLayer_ObjectMaskValue.mask = objectMaskPackage;
            // Declare an objectFilter for SoftLayer_Product_Package, to get the id from os key name that you specified
            SoftLayer_Product_PackageObjectFilter filterPackage = new SoftLayer_Product_PackageObjectFilter();
            filterPackage.itemPrices = new SoftLayer_Product_Item_PriceObjectFilter();
            filterPackage.itemPrices.item = new SoftLayer_Product_ItemObjectFilter();
            filterPackage.itemPrices.item.keyName = new SoftLayer_Utility_ObjectFilter_Operation();
            filterPackage.itemPrices.item.keyName.operation = "_=" + osKeyName;
            packageService.SoftLayer_Product_PackageObjectFilterValue = filterPackage;
            try
            {
                // Get the virtual guest
                SoftLayer_Virtual_Guest[] virtualGuests = accountService.getVirtualGuests();

                // Set the init parameters for SofLayer_Product_Package, with the packageId from vsi
                packageService.SoftLayer_Product_PackageInitParametersValue = new SoftLayer_Product_PackageInitParameters();
                packageService.SoftLayer_Product_PackageInitParametersValue.id = (int)virtualGuests[0].billingItem.package.id;

                // Get the item price
                SoftLayer_Product_Item_Price[] priceOs = packageService.getItemPrices();

                // Build a SofLayer_Product_Item_Price object with the id gotten by the filters
                List<SoftLayer_Product_Item_Price> price = new List<SoftLayer_Product_Item_Price>();
                price[0].id = (int)priceOs[0].id;

                // Build a SoftLayer_Container_Hardware_Server_Configuration object with the configuration for the reload
                SoftLayer_Container_Hardware_Server_Configuration config = new SoftLayer_Container_Hardware_Server_Configuration();
                config.itemPrices = price.ToArray();

                // Set init parameters for SoftLayer_Virtual_Guest with the Id from the vsi
                guestService.SoftLayer_Virtual_GuestInitParametersValue = new SoftLayer_Virtual_GuestInitParameters();
                guestService.SoftLayer_Virtual_GuestInitParametersValue.id = (int)virtualGuests[0].id;
                
                // Reload Operating System
                String result = guestService.reloadOperatingSystem(token, config);
                Console.WriteLine("Result: " + result);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable reload Operating System: " + e.Message);
            }
        }
    }
}

```
