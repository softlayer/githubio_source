---
title: "AddAdditionalEmails.cs"
description: "AddAdditionalEmails.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_TicketInitParametersValue"
    - "SoftLayer_Account"
    - "SoftLayer_TicketService"
    - "SoftLayer_TicketInitParameters"
    - "SoftLayer_Ticket"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="AddAdditionalEmails.cs" company="Softlayer">
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
    class AddAdditionalEmails
    {
        /// <summary>
        /// Add New Additional Emails
        /// This script creates new additional emails for the ticket
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/addAttachedAdditionalEmails
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            string username = "set me";
            // You SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // The ticket id that you wish to add the emails
            int ticketId = 21698750;
            // Define a List to add the email addresses to notify when a ticket is updated
            List<string> emails = new List<string>();
            emails.Add("noreply4@softlayer.com");
            emails.Add("noreply5@softlayer.com");
            emails.Add("noreply6@softlayer.com");
            // Creating a connection to the SoftLayer_Ticket and SoftLayer_Account API services and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_TicketService ticketService = new SoftLayer_TicketService();
            ticketService.authenticateValue = authenticate;
            // Setting init parameters
            ticketService.SoftLayer_TicketInitParametersValue = new SoftLayer_TicketInitParameters();
            ticketService.SoftLayer_TicketInitParametersValue.id = ticketId;
            try {
                // Change to removeAttachedAdditionalEmails method, if you want to remove the emails
                bool result = ticketService.addAttachedAdditionalEmails(emails.ToArray());
                Console.WriteLine("Result: " + result);               
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable add emails to the ticket: " + e.Message);
            }
        }
    }
}

```
