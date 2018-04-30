---
title: "GetAllAttachedResources.cs"
description: "GetAllAttachedResources.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_TicketInitParametersValue"
    - "SoftLayer_Ticket"
    - "SoftLayer_User_Customer_AdditionalEmail"
    - "SoftLayer_Ticket_Attachment_File"
    - "SoftLayer_TicketService"
    - "SoftLayer_Container_Utility_File_Attachment"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Hardware"
    - "SoftLayer_TicketInitParameters"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="GetAllAttachedResources.cs" company="Softlayer">
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
    class GetAllAttachedResources
    {
        /// <summary>
        /// Get All Attached Resources
        /// This script retrieves the emails, files, hardware objects and virtual guests from a ticket
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
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "set me";
            // Declare the ticket id to which you wish to get all resources
            int ticketId = 21720750;
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
            try
            {
                // Getting files, emails, hardware objects and virtual guests attached to the ticket
                SoftLayer_Ticket_Attachment_File[] files = ticketService.getAttachedFiles();
                SoftLayer_User_Customer_AdditionalEmail[] emails = ticketService.getAttachedAdditionalEmails();
                SoftLayer_Hardware[] hardwareList = ticketService.getAttachedHardware();
                SoftLayer_Virtual_Guest[] virtualGuests = ticketService.getAttachedVirtualGuests();
                Console.WriteLine(" *** FILES ***");
                foreach (var file in files)
                {
                    Console.WriteLine("File Id: " + file.id + " Filename: " + file.fileName + " File size: " + file.fileSize + " File created: " + file.createDate);
                }
                Console.WriteLine("\n *** EMAILS ***");
                foreach (var email in emails)
                {
                    Console.WriteLine("Email: " + email.email);
                }
                Console.WriteLine("\n *** HARDWARE ***");
                foreach (var hardware in hardwareList)
                {
                    Console.WriteLine("Hardware Id: " + hardware.id + " FQDN: " + hardware.fullyQualifiedDomainName);
                }
                Console.WriteLine("\n *** VIRTUAL GUESTS ***");
                foreach (var vsi in virtualGuests)
                {
                    Console.WriteLine("Virtual Guest Id: " + vsi.id + " FQDN: " + vsi.fullyQualifiedDomainName);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve all resources: " + e.Message);
            }
        }
    }
}

```
