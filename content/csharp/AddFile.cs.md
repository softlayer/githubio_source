---
title: "AddFile.cs"
description: "AddFile.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_TicketInitParametersValue"
    - "SoftLayer_Ticket"
    - "SoftLayer_Ticket_Attachment_File"
    - "SoftLayer_TicketService"
    - "SoftLayer_Container_Utility_File_Attachment"
    - "SoftLayer_TicketInitParameters"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="AddFile.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Tickets
{
    using System;
    using System.IO;
    class AddFile
    {
        /// <summary>
        /// Add File
        /// This script adds a file to the ticket
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket/addAttachedFile
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket_Attachment_File
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Utility_File_Attachment
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            string username = "set me";
            // You SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Define the ticket id to which you wish to add the file
            int ticketId = 21720750;
            // Define the name of a file that is uploaded to the SoftLayer API
            string filename = "exa.jpg";
            // Define  the source path from the file that you wish to attach to the ticket
            string filePath = @"C:\Users\Public\Pictures\Example.jpg";
            // Creating a connection to the SoftLayer_Ticket API service and             
            // bind our API username and key to it.
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_TicketService ticketService = new SoftLayer_TicketService();
            ticketService.authenticateValue = authenticate;
            // Set init parameters for SoftLayer Ticket
            ticketService.SoftLayer_TicketInitParametersValue = new SoftLayer_TicketInitParameters();
            ticketService.SoftLayer_TicketInitParametersValue.id = ticketId;
            // Create a SoftLayer_Container_Utility_File_Attachment object containing the file that you wish to attach to the ticket
            SoftLayer_Container_Utility_File_Attachment file = new SoftLayer_Container_Utility_File_Attachment();
            // Seting the name for the file
            file.filename = filename;
            // Read the file's content
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
            byte[] data = new byte[fs.Length];
            fs.Read(data, 0, System.Convert.ToInt32(fs.Length));
            fs.Close();
            file.data = data;
            // Setting init parameters
            ticketService.SoftLayer_TicketInitParametersValue = new SoftLayer_TicketInitParameters();
            ticketService.SoftLayer_TicketInitParametersValue.id = ticketId;
            try
            {
                SoftLayer_Ticket_Attachment_File result = ticketService.addAttachedFile(file);
                Console.WriteLine("File Added - Ticket Id: " + result.ticketId + " File Name: " + result.fileName);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to add file: " + e.Message);
            }
        }
    }
}

```
