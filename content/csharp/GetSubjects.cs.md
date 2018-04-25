---
title: "GetSubjects.cs"
description: "GetSubjects.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Ticket_SubjectService"
    - "SoftLayer_Ticket_Subject"
tags:
    - "tickets"
---


```
﻿//-----------------------------------------------------------------------
// <copyright file="GetSubjects.cs" company="Softlayer">
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
    class GetSubjects
    {
        /// <summary>
        /// Get Subjects
        /// This script retrieves all ticket subjects
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Ticket_Subject/getAllObjects
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket_Subject
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            String username = "set me";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            String apiKey = "set me";
            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.   
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Ticket_SubjectService subjectService = new SoftLayer_Ticket_SubjectService();
            subjectService.authenticateValue = authenticate;
            try
            {
                // Get all ticket subjects
                foreach (SoftLayer_Ticket_Subject subject in subjectService.getAllObjects())
                {
                    Console.WriteLine("Id: " + subject.id + " Subject Name: " + subject.name);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to get subjects: " + e.Message);
            }
        }
    }
}

```
