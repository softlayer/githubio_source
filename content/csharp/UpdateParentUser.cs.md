---
title: "UpdateParentUser.cs"
description: "UpdateParentUser.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_User_CustomerInitParameters"
    - "SoftLayer_Account"
    - "SoftLayer_Utility_ObjectFilter_Operation_Option"
    - "SoftLayer_User_CustomerObjectFilter"
    - "SoftLayer_AccountObjectFilter"
    - "SoftLayer_User_CustomerInitParametersValue"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_User_Customer"
    - "SoftLayer_AccountObjectFilterValue"
    - "SoftLayer_User_CustomerService"
tags:
    - "users"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="UpdateParentUser.cs" company="Softlayer">
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
    class UpdateParentUser
    {
        /// <summary>
        /// This script updates the "parent user" for users
        /// For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
        /// http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/editObject
        /// http://sldn.softlayer.com/article/Object-Filters
        /// </manualPages>
        static void Main(string[] args)
        {
            //Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey
            string apiKey = "set me";
            // Declare the usernames that you wish to change the parent user
            List<string> usernameList = new List<string>();
            usernameList.Add("username1");
            usernameList.Add("username2");
            usernameList.Add("username3");
            // Declare the username that you wish to assign as parent user
            string parentUsername = "parentUsername";
            usernameList.Add(parentUsername);
            // Creating a connection to the SoftLayer_User_Customer and SoftLayer_Account API services and bind our API username and key to it.
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_User_CustomerService customerService = new SoftLayer_User_CustomerService();
            customerService.authenticateValue = authenticate;
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            // Declare an object filter, to get the user id from usernames
            SoftLayer_AccountObjectFilter objectFilter = new SoftLayer_AccountObjectFilter();
            objectFilter.users = new SoftLayer_User_CustomerObjectFilter();
            objectFilter.users.username = new SoftLayer_Utility_ObjectFilter_Operation();
            objectFilter.users.username.operation = "in";
            objectFilter.users.username.options = new SoftLayer_Utility_ObjectFilter_Operation_Option[1];
            objectFilter.users.username.options[0] = new SoftLayer_Utility_ObjectFilter_Operation_Option();
            objectFilter.users.username.options[0].name = "data";
            objectFilter.users.username.options[0].value = usernameList.ToArray();
            accountService.SoftLayer_AccountObjectFilterValue = objectFilter;
            // Build a SoftLayer_User_Customer object with the properties that you wish to change
            SoftLayer_User_Customer templateObject = new SoftLayer_User_Customer();
            try
            {
                SoftLayer_User_Customer[] users = accountService.getUsers();
                foreach (var user in users)
                {
                    if (user.username == parentUsername)
                    {
                        templateObject.parentId = (int)user.id;
                        templateObject.parentIdSpecified = true;
                    }
                }
                foreach (var user in users)
                {
                    if (user.username != parentUsername)
                    {
                        // Setting Init parameter
                        customerService.SoftLayer_User_CustomerInitParametersValue = new SoftLayer_User_CustomerInitParameters();
                        customerService.SoftLayer_User_CustomerInitParametersValue.id = (int)user.id;
                        // Updating the parent user
                        bool result = customerService.editObject(templateObject);
                        Console.WriteLine("The parent user (" + parentUsername + ") has been updated for user " + user.username + "?: " + result);
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to update parent user: " + e.Message);
            }
        }
    }
}

```
