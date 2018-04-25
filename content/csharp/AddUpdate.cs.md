---
title: "AddUpdate.cs"
description: "AddUpdate.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Ticket"
    - "SoftLayer_TicketInitParametersValue"
    - "SoftLayer_Ticket_Update"
    - "SoftLayer_TicketService"
    - "SoftLayer_Container_Utility_File_Attachment"
    - "SoftLayer_TicketInitParameters"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="AddUpdate.cs" company="Softlayer">
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
    class AddUpdate
    {
        /// <summary>
        /// Add Update
        /// This script adds an update to a ticket. A ticket update's entry has a maximum length of 4000
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/addUpdate
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket_Update
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Utility_File_Attachment
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Declare the ticket id to which you wish to add the update
            int ticketId = 23206059;
            // Declare the source path from the file that you wish to attach to the ticket
            string filePath = @"C:\Users\Public\Pictures\Example.jpg";
            // Define the name of a file that is uploaded to the SoftLayer API.
            string filename = "example.jpg";
            // Define the contents of a ticket update.
            string entry = "This is for test - C#";
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
            // Build a SoftLayer_Ticket_Update object containing the update for the ticket
            SoftLayer_Ticket_Update templateObject = new SoftLayer_Ticket_Update();
            templateObject.entry = entry;
            // Declare a list of SoftLayer_Container_Utility_File_Attachment to add the files which will be attached to the ticket
            List<SoftLayer_Container_Utility_File_Attachment> attachedFiles = new List<SoftLayer_Container_Utility_File_Attachment>();
            // Create a SoftLayer_Container_Utility_File_Attachment object containing the file that you wish to attach to the ticket
            SoftLayer_Container_Utility_File_Attachment fileOne = new SoftLayer_Container_Utility_File_Attachment();
            fileOne.filename = filename;
            // Read the file's content
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
            byte[] data = new byte[fs.Length];
            fs.Read(data, 0, System.Convert.ToInt32(fs.Length));
            fs.Close();
            fileOne.data = data;
            // Add the file read to attachedFiles list
            attachedFiles.Add(fileOne);
            try
            {
                SoftLayer_Ticket_Update[] updates = ticketService.addUpdate(templateObject, attachedFiles.ToArray());
                foreach (SoftLayer_Ticket_Update update in updates)
                {
                    Console.WriteLine("Update Id: " + update.id);
                    Console.WriteLine("Ticket Id: " + update.ticketId);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to add the update: " + e.Message);
            }
        }
    }
}

```
