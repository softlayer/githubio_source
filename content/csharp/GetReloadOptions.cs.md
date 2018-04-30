---
title: "GetReloadOptions.cs"
description: "GetReloadOptions.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_Product_PackageInitParameters"
    - "SoftLayer_AccountObjectFilterValue"
    - "SoftLayer_Product_PackageInitParametersValue"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_AccountObjectFilter"
    - "SoftLayer_Product_PackageObjectFilterValue"
    - "SoftLayer_Product_PackageService"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_Product_Item_PriceObjectFilter"
    - "SoftLayer_Virtual_GuestObjectFilter"
    - "SoftLayer_Virtual_GuestService"
    - "SoftLayer_Product_Item_CategoryObjectFilter"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Product_PackageObjectFilter"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
tags:
    - "virtualguests"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetReloadOptions.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace VirtualGuests
{
    using System;
    class GetReloadOptions
    {
        /// <summary>
        ///  Get Reload Options
        ///  This script retrieves all options available for reload from a Virtual Guest. It is only necessary 
        ///  to declare the hostname from the vsi that you wish to reload operating system and the type of operating system.
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Product_Package/getItemPrices
        /// http://sldn.softlayer.com/article/Object-Masks
        /// http://sldn.softlayer.com/article/Object-Filters
        /// </manualPages>
        static void Main(string[] ards)
        {
            // You SoftLayer username
            string username = "set me";
            // Your SoftLayer API key.            
            string apiKey = "set me";
            // Define the hostname from vsi that you wish to retrieve the os reload options
            string hostname = "rcv-test1public";
            // Define type of software e.g. Microsoft
            // There exist the following options: "CentOS", "CloudLinux", "CoreOS", "Debian", "Microsoft", "Redhat", "Ubuntu", "Vyatta".
            string osType = "Microsoft";
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

            // Define objectMask to get Package id
            string objectMask = "mask[billingItem[package]]";
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = objectMask;

            // Declare an objectFilter to get the id from hostname specified.
            SoftLayer_AccountObjectFilter filter = new SoftLayer_AccountObjectFilter();
            filter.virtualGuests = new SoftLayer_Virtual_GuestObjectFilter();
            filter.virtualGuests.hostname = new SoftLayer_Utility_ObjectFilter_Operation();
            filter.virtualGuests.hostname.operation = "*=" + hostname;
            accountService.SoftLayer_AccountObjectFilterValue = filter;
            try
            {
                // Get the virtual guest with the hostname specified
                SoftLayer_Virtual_Guest[] virtualGuests = accountService.getVirtualGuests();

                // Set init parameters for SoftLayer_Product_Package, to get item prices
                packageService.SoftLayer_Product_PackageInitParametersValue = new SoftLayer_Product_PackageInitParameters();
                packageService.SoftLayer_Product_PackageInitParametersValue.id = (int)virtualGuests[0].billingItem.package.id;

                // Declare an objectMask for SoftLayer_Product_Package, to get software description and category information from each item
                String objectMaskPackage = "mask[item[softwareDescription], categories[categoryCode]]";
                packageService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
                packageService.SoftLayer_ObjectMaskValue.mask = objectMaskPackage;

                // Declare an objectFilter for SoftLayer_Product_Package, to get only the items with category type "os" (Operating System)
                SoftLayer_Product_PackageObjectFilter filterPackage = new SoftLayer_Product_PackageObjectFilter();
                filterPackage.itemPrices = new SoftLayer_Product_Item_PriceObjectFilter();
                filterPackage.itemPrices.categories = new SoftLayer_Product_Item_CategoryObjectFilter();
                filterPackage.itemPrices.categories.categoryCode = new SoftLayer_Utility_ObjectFilter_Operation();
                filterPackage.itemPrices.categories.categoryCode.operation = "_=os";
                packageService.SoftLayer_Product_PackageObjectFilterValue = filterPackage;

                // Retrieve the item prices 
                SoftLayer_Product_Item_Price[] items = packageService.getItemPrices();

                // Filter all item prices according the os type declared before (osType variable)
                foreach (var item in items)
                {
                    if (item.item.softwareDescription.manufacturer == osType)
                    {
                        Console.WriteLine("Id: " + item.id);
                        Console.WriteLine("Description: " + item.item.description);
                        Console.WriteLine("Key Name: " + item.item.keyName);
                        Console.WriteLine("Manufacturer: " + item.item.softwareDescription.manufacturer);
                        Console.WriteLine("---------------------------------------------------------------");
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get reload options: " + e.Message);
            }
            Console.ReadKey();          
        }
    }
}
```
