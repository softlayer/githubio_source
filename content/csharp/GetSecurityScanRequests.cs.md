---
title: "GetSecurityScanRequests.cs"
description: "GetSecurityScanRequests.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Network_Security_Scanner_Request"
    - "SoftLayer_ObjectMask"
tags:
    - "vulnerabilityscanrequests"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetSecurityScanRequests.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace VulnerabilityScans
{
    using System;
    class GetSecurityScanRequests
    {
        /// <summary>
        ///  Get Security Scan Requests
        ///  This script retrieves an account's vulnerability scan requests
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Account/getSecurityScanRequests
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Security_Scanner_Request
        /// </manualPages>
        static void Main(string [] args)
        { 
            // Your SoftLayer username
            string username = "set me";
            // Your SoftLayer Api Key
            string apiKey = "set me";

            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.   
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            // Declare an objectMask, to get status, hardware and guest information from scan requests
            string objectMask = "mask[status, hardware, guest]";
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = objectMask;
            try {
                SoftLayer_Network_Security_Scanner_Request[] scans = accountService.getSecurityScanRequests();
                foreach (var scan in scans)
                {
                    Console.Write("Scan Date: " + scan.createDate);
                    if (scan.hardwareId != null)
                    {
                        Console.WriteLine(" Device Name: " + scan.hardware.fullyQualifiedDomainName + " Public Ip: " + scan.hardware.primaryIpAddress + " Private Ip: " + scan.hardware.primaryBackendIpAddress + " Status: " + scan.status.name);
                    }
                    else {
                        Console.WriteLine(" Device Name: " + scan.guest.fullyQualifiedDomainName + " Public Ip: " + scan.guest.primaryIpAddress + " Private Ip: " + scan.guest.primaryBackendIpAddress + " Status: " + scan.status.name);
                    }
                    Console.WriteLine(scan.status.name);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to retrieve security scan requests: " + e.Message);
            }
        }
    }
}

```
