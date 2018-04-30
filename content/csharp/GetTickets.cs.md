---
title: "GetTickets.cs"
description: "GetTickets.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Ticket"
    - "SoftLayer_ObjectMask"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="GetTickets.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Tickets
{
    using System;
    class GetTickets
    {
        /// <summary>
        /// Get Tickets
        /// This script retrieves an account's associated tickets
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getTickets
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            String username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            String apiKey = "set me";
            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.   
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            // Define an objectMask, to get relational properties
            String objectMask = "mask[group, subject, assignedUser, lastUpdate]";
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = objectMask;
            try {
                // Retrieving the tickets
                SoftLayer_Ticket[] tickets = accountService.getTickets();
                foreach (var ticket in tickets)
                {
                    Console.WriteLine("Id: " + ticket.id + " Group: " + ticket.group.name + "Subject/Title: " + ticket.title + " Owner: " + ticket.assignedUser.username
                    + " Last Replied: " + ticket.lastUpdate.editorType + " Updated: " + ticket.lastUpdate.createDate);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get tickets: " + e.Message);
            }
        }
    }
}

```
