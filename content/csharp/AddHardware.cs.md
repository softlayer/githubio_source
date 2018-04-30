---
title: "AddHardware.cs"
description: "AddHardware.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_TicketInitParametersValue"
    - "SoftLayer_Hardware_ServerService"
    - "SoftLayer_Ticket_Attachment_Hardware"
    - "SoftLayer_TicketService"
    - "SoftLayer_Ticket"
    - "SoftLayer_TicketInitParameters"
    - "SoftLayer_Hardware_Server"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="AddHardware.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Tickets
{
    using System;
    class AddHardware
    {
        /// <summary>
        /// Add Hardware
        /// This script adds a hardware to the ticket through Ip Address from the server(Public or Private)
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/addAttachedHardware
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket_Attachment_Hardware
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Declare the ticket id to which you wish to add the hardware
            int ticketId = 21720750;
            // Declare the hardware's hostname
            string hardwareIpAddress = "158.85.130.98";
            // Creating a connection to the SoftLayer_Ticket and SoftLayer_Hardware_Server API services and             
            // bind our API username and key to it.
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_TicketService ticketService = new SoftLayer_TicketService();
            ticketService.authenticateValue = authenticate;
            SoftLayer_Hardware_ServerService hardwareService = new SoftLayer_Hardware_ServerService();
            hardwareService.authenticateValue = authenticate;
            // Set init parameters for SoftLayer Ticket
            ticketService.SoftLayer_TicketInitParametersValue = new SoftLayer_TicketInitParameters();
            ticketService.SoftLayer_TicketInitParametersValue.id = ticketId;
            try
            {
                // Get hardware's identifier through its ip address
                SoftLayer_Hardware_Server server = hardwareService.findByIpAddress(hardwareIpAddress);
                // Adding the hardware
                SoftLayer_Ticket_Attachment_Hardware result = ticketService.addAttachedHardware((int)server.id);
                Console.WriteLine("Hardware added, Ticket Id: " + result.ticketId + " Hardware Id: " + result.hardwareId);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to add Hardware: " + e.Message);
            }
        }
    }
}

```
