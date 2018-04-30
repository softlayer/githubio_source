---
title: "UpdatePassword.cs"
description: "UpdatePassword.cs"
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
// <copyright file="UpdatePassword.cs" company="Softlayer">
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
    class UpdatePassword
    {
        /// <summary>
        /// This script updates the passwords from users. 
        /// It's necessary to run the script with master user's credentials
        /// For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
        /// http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/updatePassword
        /// http://sldn.softlayer.com/article/Object-Filters
        /// </manualPages>
        static void Main(string[] args)
        {
            //Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey
            string apiKey = "set me";
            // Declare the new portal password for users
            string newPassword = "NewPassword123*-";
            // Declare the usernames from users that you wish to update the password
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
            try
            {
                SoftLayer_User_Customer[] users = accountService.getUsers();
                foreach (var user in users)
                {
                    // Setting init parameters
                    customerService.SoftLayer_User_CustomerInitParametersValue = new SoftLayer_User_CustomerInitParameters();
                    customerService.SoftLayer_User_CustomerInitParametersValue.id = (int)user.id;
                    // Update the password
                    bool result = customerService.updatePassword(newPassword);
                    Console.WriteLine("The password has been updated for user: " + user.username + " :? " + result);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to update password: " + e.Message);
            }
        }
    }
}

```
