---
title: "AddBulkPortalPermission.cs"
description: "AddBulkPortalPermission.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_User_CustomerInitParameters"
    - "SoftLayer_Account"
    - "SoftLayer_Utility_ObjectFilter_Operation_Option"
    - "SoftLayer_User_Customer_CustomerPermissions_Permissions"
    - "SoftLayer_User_CustomerObjectFilter"
    - "SoftLayer_AccountObjectFilter"
    - "SoftLayer_User"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_User_Customer"
    - "SoftLayer_User_CustomerInitParametersValue"
    - "SoftLayer_AccountObjectFilterValue"
    - "SoftLayer_User_CustomerService"
    - "SoftLayer_User_Customer_CustomerPermission_Permission"
tags:
    - "users"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="AddBulkPortalPermission.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Users
{
    using System;
    using System.Collections.Generic;
    class AddBulkPortalPermission
    {
        /// <summary>
        ///  This script adds multiple permissions to a portal user's permissions set.
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
        /// http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/addBulkPortalPermission
        /// http://sldn.softlayer.com/article/Object-Filters
        /// </manualPages>
        static void Main(string[] args)
        {
            //Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey
            string apiKey = "set me";
            /*
             * Declare a string array containing the keyNames from the permissions that you wish to add for users
             * The following method helps you yo get all of them: SoftLayer_User_Customer_CustomerPermissions_Permissions::getAllObjects
             * http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/getAllObjects
             */
            string[] permissions = new string[] {"ACCOUNT_SUMMARY_VIEW","COMPANY_EDIT","SERVICE_ADD", "DNS_MANAGE", "HARDWARE_VIEW"};
            // Declare the usernames that you wish to add the permissions
            List<string> usernameList = new List<string>();
            usernameList.Add("username1");
            usernameList.Add("username2");
            usernameList.Add("username3");
            // Creating a connection to the SoftLayer_User_Customer and SoftLayer_Account API services and bind our API username and key to it.
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_User_CustomerService customerService = new SoftLayer_User_CustomerService();
            customerService.authenticateValue = authenticate;
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            // Declare an object filter, to get the user ids from usernames
            SoftLayer_AccountObjectFilter objectFilter = new SoftLayer_AccountObjectFilter();
            objectFilter.users = new SoftLayer_User_CustomerObjectFilter();
            objectFilter.users.username = new SoftLayer_Utility_ObjectFilter_Operation();
            objectFilter.users.username.operation = "in";
            objectFilter.users.username.options = new SoftLayer_Utility_ObjectFilter_Operation_Option[1];
            objectFilter.users.username.options[0] = new SoftLayer_Utility_ObjectFilter_Operation_Option();
            objectFilter.users.username.options[0].name = "data";
            objectFilter.users.username.options[0].value = usernameList.ToArray();
            accountService.SoftLayer_AccountObjectFilterValue = objectFilter;
            // Build a SoftLayer_User-Customer_CustomerPermission_Permission object with the collection of permissions to assign to users
            List<SoftLayer_User_Customer_CustomerPermission_Permission> permissionList = new List<SoftLayer_User_Customer_CustomerPermission_Permission>();
            foreach (var permission in permissions)
            {
                // Define Permission
                SoftLayer_User_Customer_CustomerPermission_Permission permission1 = new SoftLayer_User_Customer_CustomerPermission_Permission();
                permission1.keyName = permission;
                permissionList.Add(permission1);
            }

            try
            {
                SoftLayer_User_Customer[] users = accountService.getUsers();
                foreach (var user in users)
                {
                    // Setting init parameter
                    customerService.SoftLayer_User_CustomerInitParametersValue = new SoftLayer_User_CustomerInitParameters();
                    customerService.SoftLayer_User_CustomerInitParametersValue.id = (int)user.id;
                    // Adding the permissions
                    bool result = customerService.addBulkPortalPermission(permissionList.ToArray());
                    Console.WriteLine("Has been added the permissions for user: " + user.username  + "?: " + result);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to add permissions: " + e.Message);
            }
        }
    }
}

```
