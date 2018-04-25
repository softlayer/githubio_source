---
title: "CreateAdministrativeTicket.cs"
description: "CreateAdministrativeTicket.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_Ticket"
    - "SoftLayer_User_CustomerObjectFilter"
    - "SoftLayer_AccountObjectFilter"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_User_Customer"
    - "SoftLayer_TicketService"
    - "SoftLayer_Container_Utility_File_Attachment"
    - "SoftLayer_AccountObjectFilterValue"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="CreateAdministrativeTicket.cs" company="Softlayer">
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
    class CreateAdministrativeTicket
    {
        /// <summary>
        /// Create Administrative Ticket
        /// This script creates an administrative support ticket. Use an adminisrative ticket if you require SoftLayer's 
        /// assistance managing your server or content. 
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/createAdministrativeTicket
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Utility_File_Attachment
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Define the ticket's assigned username
            string assignedUsername = "usertest";
            // Define the ticket's title
            string title = "title for test";
            // Define the contents of the first update of the ticket. (Ticket's problem description)
            string contents = "This content is for test";
            // Define an optional internal identifier of a piece of hardware or CloudLayer Computing Instance you wish to attach to this ticket
            int attachmentId = 0;
            // Define the root password of the hardware you wish to attach to this ticket
            string rootPassword = "";
            // Define an optional administrative password to a hosting control panel running on your server
            string controlPanelPassword = "";
            // Define the TCP port on your server that SoftLayer must use to access your OS
            string accessPort = "";
            // Creating a connection to the SoftLayer_Ticket and SoftLayer_Account API services and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_TicketService ticketService = new SoftLayer_TicketService();
            ticketService.authenticateValue = authenticate;
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            // Define a list of files to attach to a ticket upon creation
            List<SoftLayer_Container_Utility_File_Attachment> attachedFiles = new List<SoftLayer_Container_Utility_File_Attachment>();
            // Define the attachment type e.g. HARDWARE or VIRTUAL_GUEST
            createAdministrativeTicket_attachmentType attachmentType = new createAdministrativeTicket_attachmentType();
            // Build a skeleton SoftLayer_Ticket object containing the data of the ticket you wish to submit
            SoftLayer_Ticket templateObject = new SoftLayer_Ticket();
            templateObject.title = title;
            // Declare an objectfilter, to get the user id whose the ticket will be assigned
            SoftLayer_AccountObjectFilter filter = new SoftLayer_AccountObjectFilter();
            filter.users = new SoftLayer_User_CustomerObjectFilter();
            filter.users.username = new SoftLayer_Utility_ObjectFilter_Operation();
            filter.users.username.operation = "_=" + assignedUsername;
            accountService.SoftLayer_AccountObjectFilterValue = filter;
            try
            {
                SoftLayer_User_Customer[] users = accountService.getUsers();
                templateObject.assignedUserId = users[0].id;
                templateObject.assignedUserIdSpecified = true;
                // Create Administrative Ticket
                SoftLayer_Ticket result = ticketService.createAdministrativeTicket(templateObject, contents, attachmentId, rootPassword, controlPanelPassword, accessPort, attachedFiles.ToArray(), attachmentType);
                Console.WriteLine(result.id);
                Console.WriteLine(result.title);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to create administrative ticket: " + e.Message);
            }       
        }
    }
}

```
