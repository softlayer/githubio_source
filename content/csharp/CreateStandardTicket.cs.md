---
title: "CreateStandardTicket.cs"
description: "CreateStandardTicket.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Ticket"
    - "SoftLayer_User_CustomerObjectFilter"
    - "SoftLayer_AccountObjectFilter"
    - "SoftLayer_Utility_ObjectFilter_Operation"
    - "SoftLayer_User_Customer"
    - "SoftLayer_TicketService"
    - "SoftLayer_Container_Utility_File_Attachment"
    - "SoftLayer_AccountObjectFilterValue"
    - "SoftLayer_Ticket_Subject"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="CreateStandardTicket.cs" company="Softlayer">
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
    using System.IO;
    class CreateStandardTicket
    {
        /// <summary>
        /// Create Standart Ticket
        /// This script creates a standard ticket. Use a standard support ticket if you need to work out a problem related to SoftLayer's 
        /// hardware, network, or services. If you require SoftLayer's assistance managing your server or content then please open an administrative ticket.
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/createStandardTicket
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Utility_File_Attachment
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            String username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            String apiKey = "set me";
            // Define the ticket's assigned username
            string assignedUsername = "usertest";
            // Declare the 
            // Creating a connection to the SoftLayer_Ticket API service and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_TicketService ticketService = new SoftLayer_TicketService();
            ticketService.authenticateValue = authenticate;
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            // Define the subjectId that the ticket is associated with. To get the identifiers: http://sldn.softlayer.com/reference/services/SoftLayer_Ticket_Subject/getAllObjects
            int subjectId = 1522; // API Question
            // Define a ticket's title
            string title = "This is for test";
            // Declare the contents of the first update of the ticket (Ticket's problem description)
            string contents = "This is for test - Content";
            // Declare identifier of hardware or cloudlayer computing instance you wish to attach to this ticket
            int attachmentId = 0;
            // Declare the root password of the hardware you wish to attach to this ticket
            string rootPassword = "rootPasswordTest";
            // Declare an optional administrative password to a hosting control panel running on your servers, if your server
            // has one installed
            string controlPanelPassword = "ControlPanelPasswordTest";
            // Declare the TCP port on your servers that SoftLayer must use to access your Operating System
            string accessPort = "";
            // Declare the source path from the file that you wish to attach to the ticket
            string filePath = @"C:\Users\Ruber Cuellar\Pictures\allow.jpg";
            // Define the name of a file that is uploaded to the SoftLayer API.
            string filename = "example.org";
            // Declare the attachment type e.g. HARDWARE or VIRTUAL_GUEST
            createStandardTicket_attachmentType attach = new createStandardTicket_attachmentType();
            // Build a skeleton SoftLayer_Ticket object containing the data of the ticket you wish to submit
            SoftLayer_Ticket templateObject = new SoftLayer_Ticket();
            templateObject.subjectId = subjectId;
            templateObject.subjectIdSpecified = true;
            templateObject.title = title;
            // Declare an object filter, to get the user id to whom will be assigned the ticket
            SoftLayer_AccountObjectFilter filter = new SoftLayer_AccountObjectFilter();
            filter.users = new SoftLayer_User_CustomerObjectFilter();
            filter.users.username = new SoftLayer_Utility_ObjectFilter_Operation();
            filter.users.username.operation = "_=" + assignedUsername;
            accountService.SoftLayer_AccountObjectFilterValue = filter;
            // Declare an array of files to attach to a ticket upon creation
            List<SoftLayer_Container_Utility_File_Attachment> attachedFiles = new List<SoftLayer_Container_Utility_File_Attachment>();
            // Create a SoftLayer_Container_Utility_File_Attachment object containing the file that you wish to attach to the ticket
            SoftLayer_Container_Utility_File_Attachment fileOne = new SoftLayer_Container_Utility_File_Attachment();
            // Seting the name for the file
            fileOne.filename = filename;
            // Read the file's content
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
            byte[] data = new byte[fs.Length];
            fs.Read(data, 0, System.Convert.ToInt32(fs.Length));
            fs.Close();
            fileOne.data = data;
            // Add the file read to attachedFiles list
            attachedFiles.Add(fileOne);
            try {
                // Get the user's identifier
                SoftLayer_User_Customer[] users = accountService.getUsers();
                templateObject.assignedUserId = users[0].id;
                templateObject.assignedUserIdSpecified = true;
                // Create Standard Ticket
                SoftLayer_Ticket result = ticketService.createStandardTicket(templateObject, contents, attachmentId, rootPassword, controlPanelPassword, accessPort, attachedFiles.ToArray(), attach);
                Console.WriteLine(result.id);
                Console.WriteLine(result.title);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to create standard ticket: " + e.Message);
            }
        }
    }
}

```
