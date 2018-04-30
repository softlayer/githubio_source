---
title: "CancelNotificationUpdate.cs"
description: "CancelNotificationUpdate.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_TicketInitParametersValue"
    - "SoftLayer_TicketInitParameters"
    - "SoftLayer_TicketService"
    - "SoftLayer_Container_Utility_File_Attachment"
    - "SoftLayer_Ticket"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="CancelNotificationUpdate.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Tickets
{
    using System;
    class CancelNotificationUpdate
    {
        /// <summary>
        /// Cancel Notification Update
        /// This script cancels the notifications when the ticke tis updated
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/edit
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username 
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Declare the ticket which you wish to cancel the notifications
            int ticketId = 21698750;
            // Declare the contents of the update
            string contents = "Disable the notifications";
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
            // Build a skeleton SoftLayer_Ticket object containing the data of the ticket you wish to edit
            SoftLayer_Ticket templateObject = new SoftLayer_Ticket();
            templateObject.notifyUserOnUpdateFlag = false;
            templateObject.notifyUserOnUpdateFlagSpecified = true;
            // Declare the attachedFiles array
            SoftLayer_Container_Utility_File_Attachment[] attachedFiles = new SoftLayer_Container_Utility_File_Attachment[0];
            try
            {
                SoftLayer_Ticket result = ticketService.edit(templateObject, contents, attachedFiles);
                Console.WriteLine("Notifications canceled");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to cancel notifications: " + e.Message);
            }
        }
    }
}

```
