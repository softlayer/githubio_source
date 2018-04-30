---
title: "RemoveEmails.cs"
description: "RemoveEmails.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_TicketInitParametersValue"
    - "SoftLayer_TicketInitParameters"
    - "SoftLayer_TicketService"
    - "SoftLayer_Ticket"
    - "SoftLayer_User_Customer_AdditionalEmail"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="RemoveEmails.cs" company="Softlayer">
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
    class RemoveEmails
    {
        /// <summary>
        /// Remove Emails
        /// This script removes all the emails attached
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/getAttachedAdditionalEmails
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/removeAttachedAdditionalEmails
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Declare the ticket id that you wish to delete the additional emails
            int ticketId = 21698750;
            // Creating a connection to the SoftLayer_Ticket API service and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_TicketService ticketService = new SoftLayer_TicketService();
            ticketService.authenticateValue = authenticate;
            // Setting init parameters
            ticketService.SoftLayer_TicketInitParametersValue = new SoftLayer_TicketInitParameters();
            ticketService.SoftLayer_TicketInitParametersValue.id = ticketId;
            // Declare string array to add the emails that will be deleted
            List<string> emailList = new List<string>();
            try
            {
                // Retrieving additional emails attached
                SoftLayer_User_Customer_AdditionalEmail[] additionalEmails = ticketService.getAttachedAdditionalEmails();
                foreach (var email in additionalEmails)
                {
                    emailList.Add(email.email);
                }
                // Delete emails
                bool result = ticketService.removeAttachedAdditionalEmails(emailList.ToArray());
                Console.WriteLine("Result:" + result);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to remove additional emails: " + e.Message);
            }
        }
    }
}

```
