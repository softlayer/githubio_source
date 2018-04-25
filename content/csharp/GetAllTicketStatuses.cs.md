---
title: "GetAllTicketStatuses.cs"
description: "GetAllTicketStatuses.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_TicketService"
    - "SoftLayer_Ticket_Status"
    - "SoftLayer_Ticket"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="GetAllTicketStatuses.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Tickets
{
    using System;
    class GetAllTicketStatuses
    {
        /// <summary>
        /// Get All Ticket Statuses
        /// This script retrieves all available ticket statuses
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/getAllTicketStatuses
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket_Status
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
                // Get all available ticket statuses
                foreach (SoftLayer_Ticket_Status ticketStatus in ticketService.getAllTicketStatuses())
                {
                    Console.WriteLine("Id: " + ticketStatus.id + " Status name: " + ticketStatus.name);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get ticket statuses: " + e.Message);
            }
        }
    }
}

```
