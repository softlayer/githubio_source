---
title: "GetRamOptions.cs"
description: "GetRamOptions.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_AccountObjectFilterValue"
    - "SoftLayer_Virtual_GuestInitParametersValue"
    - "SoftLayer_Billing_Item_Virtual_Guest"
    - "SoftLayer_Product_Item_Price"
    - "SoftLayer_Virtual_GuestInitParameters"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_AccountObjectFilter"
    - "SoftLayer_Product_PackageService"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_Virtual_GuestObjectFilter"
    - "SoftLayer_Virtual_GuestService"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Billing_Item"
tags:
    - "virtualguests"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetRamOptions.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace VirtualGuests
{
    using System;
    class GetRamOptions
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
            // Declare a downgrade flag to include the downgrade item prices 
            bool downgradeFlag = true;
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
            // Declare an objectMask to get hourlyBillingFlag property
            String accountMask = "mask[hourlyBillingFlag]";
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = accountMask;
            // Declare an objectFilter to get the id from hostname specified.
            SoftLayer_AccountObjectFilter filter = new SoftLayer_AccountObjectFilter();
            filter.virtualGuests = new SoftLayer_Virtual_GuestObjectFilter();
            filter.virtualGuests.hostname = new SoftLayer_Utility_ObjectFilter_Operation();
            filter.virtualGuests.hostname.operation = "*=" + hostname;
            accountService.SoftLayer_AccountObjectFilterValue = filter;
            // Declare an objectMask to get the hour

            // Declare an objectMask to get the children items (Get the current ram configuration from vsi)
            String objectMask = "mask[children, hourlyFlag]";
            guestService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            guestService.SoftLayer_ObjectMaskValue.mask = objectMask;
            // Declare a string to get the current ram description
            String currentRam = "";
            try
            {
                // Get the Virtual Guest id
                SoftLayer_Virtual_Guest[] virtualGuest = accountService.getVirtualGuests();
                // Get Billing Item to get children items (Get the current ram configuration)
                guestService.SoftLayer_Virtual_GuestInitParametersValue = new SoftLayer_Virtual_GuestInitParameters();
                guestService.SoftLayer_Virtual_GuestInitParametersValue.id = (int)virtualGuest[0].id;
                SoftLayer_Billing_Item_Virtual_Guest resultBillingItem = guestService.getBillingItem();
                SoftLayer_Billing_Item[] billingItems = resultBillingItem.children;
                // Retriving the current ram configuration
                foreach (var billingItem in billingItems)
                {
                    if (billingItem.categoryCode == "ram")
                    {
                        currentRam = billingItem.description;
                    }
                }
                // Declare an objectMask, to get categoryCode and Description from each upgrade item
                String itemMask = "mask[categories, item]";
                guestService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
                guestService.SoftLayer_ObjectMaskValue.mask = itemMask;
                // Get Upgrade Item Prices
                SoftLayer_Product_Item_Price[] items = guestService.getUpgradeItemPrices(downgradeFlag);
                // Retrieving all RAM items and excluding the current ram configuration
                foreach (var item in items)
                {
                    if (item.categories[0].categoryCode == "ram" && item.item.description != currentRam)
                    {
                        Console.Write("Id: " + item.id + "   Description: " + item.item.description );
                        if (virtualGuest[0].hourlyBillingFlag == true)
                        {
                            Console.WriteLine(" Hourly Recurring Fee: " + item.hourlyRecurringFee);
                        }
                        else
                        {
                            Console.WriteLine("  Recurring Fee: " + item.recurringFee);
                        }
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get ram options: " + e.Message);
            }
        }
    }
}

```
