---
title: "GetAllTicketGroups.cs"
description: "GetAllTicketGroups.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_TicketService"
    - "SoftLayer_Ticket_Group"
    - "SoftLayer_Ticket"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="GetAllTicketGroups.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Tickets
{
    using System;
    using System.Collections.Generic;
    class GetAllTicketGroups
    {
        /// <summary>
        /// Get All Ticket Groups
        /// This script retrieves a list of all groups that a ticket may be assigned to.
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/getAllTicketGroups
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket_Group
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            String username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            String apiKey = "set me";
            // Creating a connection to the SoftLayer_Ticket API service and             
            // bind our API username and key to it.   
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_TicketService ticketService = new SoftLayer_TicketService();
            ticketService.authenticateValue = authenticate;
            try
            {
                // Get all ticket groups
                foreach (SoftLayer_Ticket_Group ticketGroup in ticketService.getAllTicketGroups())
                {
                    Console.WriteLine("Ticket Group Id: " + ticketGroup.id + " Name: " + ticketGroup.name);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get ticket groups: " + e.Message);
            }
        }
    }
}

```
