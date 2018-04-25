---
title: "AddVirtualGuest.cs"
description: "AddVirtualGuest.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_TicketInitParametersValue"
    - "SoftLayer_TicketService"
    - "SoftLayer_Virtual_GuestService"
    - "SoftLayer_Ticket"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Ticket_Attachment_Virtual_Guest"
    - "SoftLayer_TicketInitParameters"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="AddVirtualGuest.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Tickets
{
    using System;
    class AddVirtualGuest
    {
        /// <summary>
        /// Add Virtual Guest
        /// This script adds a Virtual Guest Server to the ticket through Ip Address from the server(Public or Private)
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/addAttachedVirtualGuest
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket_Attachment_Virtual_Guest
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/findByIpAddress
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Declare the ticket id to which you wish to add the Virtual Guest
            int ticketId = 21720750;
            // Declare the Virtual Guest's hostname
            string vsiIpAddress = "10.104.73.202";
            // Creating a connection to the SoftLayer_Ticket and SoftLayer_Virtual_Guest API services and             
            // bind our API username and key to it.
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_TicketService ticketService = new SoftLayer_TicketService();
            ticketService.authenticateValue = authenticate;
            SoftLayer_Virtual_GuestService guestService = new SoftLayer_Virtual_GuestService();
            guestService.authenticateValue = authenticate;
            // Set init parameters for SoftLayer Ticket
            ticketService.SoftLayer_TicketInitParametersValue = new SoftLayer_TicketInitParameters();
            ticketService.SoftLayer_TicketInitParametersValue.id = ticketId;
            try
            {
                // Get Virtual Guest's identifier through its ip address
                SoftLayer_Virtual_Guest server = guestService.findByIpAddress(vsiIpAddress);
                // Adding the Virtual Guest
                SoftLayer_Ticket_Attachment_Virtual_Guest result = ticketService.addAttachedVirtualGuest((int)server.id);
                Console.WriteLine("Virtual Guest added, Ticket Id: " + result.ticketId + " Virtual Guest Id: " + result.virtualGuestId);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to add Virtual Guest: " + e.Message);
            }
        }
    }
}

```
