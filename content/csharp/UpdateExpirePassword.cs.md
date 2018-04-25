---
title: "UpdateExpirePassword.cs"
description: "UpdateExpirePassword.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_User_CustomerInitParameters"
    - "SoftLayer_Account"
    - "SoftLayer_Utility_ObjectFilter_Operation_Option"
    - "SoftLayer_User_Customer_ApiAuthentication"
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
// <copyright file="UpdateExpirePassword.cs" company="Softlayer">
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
    class UpdateExpirePassword
    {
        /// <summary>
        /// This script updates the Expire Password days for users.
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
            // Declare the usernames that you wish to update the expire password days
            List<string> usernameList = new List<string>();
            usernameList.Add("username1");
            usernameList.Add("username2");
            usernameList.Add("username3");
            // Declare the expiration password days. It should be: 0, 30, 45, 60, 90, 120. (0 means never)
            int expirationPasswordDays = 120;
            // Creating a connection to the SoftLayer_Account and SoftLayer_User_Customer API services and bind our API username and key to it.
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            SoftLayer_User_CustomerService customerService = new SoftLayer_User_CustomerService();
            customerService.authenticateValue = authenticate;
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
            // Build a SoftLayer_User_Customer object with the properties that you wish to change.
            SoftLayer_User_Customer templateObject = new SoftLayer_User_Customer();
            templateObject.secondaryPasswordTimeoutDays = expirationPasswordDays;
            templateObject.secondaryPasswordTimeoutDaysSpecified = true;
            try
            {
                SoftLayer_User_Customer[] users = accountService.getUsers();
                foreach (var user in users)
                {
                    // Setting init parameters
                    customerService.SoftLayer_User_CustomerInitParametersValue = new SoftLayer_User_CustomerInitParameters();
                    customerService.SoftLayer_User_CustomerInitParametersValue.id = (int)user.id;
                    SoftLayer_User_Customer_ApiAuthentication[] apiKeys = customerService.getApiAuthenticationKeys();
                    // Update expire password
                    bool result = customerService.editObject(templateObject);
                    Console.WriteLine("Has been updated the number of expiration password days to: " + expirationPasswordDays + " for user " + user.username + " ?: " + result);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to update the number of expiration password days: " + e.Message);
            }
        }
    }
}

```
