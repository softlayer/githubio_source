---
title: "CreateSecurityScanRequest.cs"
description: "CreateSecurityScanRequest.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_ObjectMaskValue"
    - "SoftLayer_Network_Security_Scanner_RequestService"
    - "SoftLayer_Hardware"
    - "SoftLayer_Network_Security_Scanner_Request"
    - "SoftLayer_ObjectMask"
    - "SoftLayer_Virtual_Guest"
tags:
    - "vulnerabilityscanrequests"
---


```
//-----------------------------------------------------------------------
// <copyright file="CreateSecurityScanRequest.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace VulnerabilityScans
{
    using System;
    class CreateSecurityScanRequest
    {
        /// <summary>
        ///  Create Vulnerability Scan Request
        ///  This script creates a new vulnerability scan request. It is only necessary to specify the public ip from hardware/virtual server.
        ///  For more information, review the following links:
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Network_Security_Scanner_Request/createObject
        /// http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Security_Scanner_Request
        /// </manualPages>
        static void Main(string[] args)
        { 
            // Your SoftLayer username
            string username = "set me";
            // You SoftLayer ApiKey
            string apiKey = "set me";
            string ipAddress = "169.45.129.188";

            // Creating a connection to the SoftLayer_Account and SoftLayer_Network_Security_Scanner_Request API services and             
            // bind our API username and key to it.   
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;
            SoftLayer_Network_Security_Scanner_RequestService securityService = new SoftLayer_Network_Security_Scanner_RequestService();
            securityService.authenticateValue = authenticate;
            // Declare an objectMask, to get public ip from bare metal/virtual servers
            String objectMask = "mask[primaryIpAddress]";
            accountService.SoftLayer_ObjectMaskValue = new SoftLayer_ObjectMask();
            accountService.SoftLayer_ObjectMaskValue.mask = objectMask;
            // Build SoftLayer_Network_Security_Scanner_Request object that you wish to create
            SoftLayer_Network_Security_Scanner_Request templateObject = new SoftLayer_Network_Security_Scanner_Request();
            templateObject.accountIdSpecified = true;
            try
            {
                // Get Virtual Guests and Hardware object, to get the Server to which belongs the Ip Address.
                SoftLayer_Virtual_Guest[] virtualGuests = accountService.getVirtualGuests();
                SoftLayer_Hardware[] hardwareList = accountService.getHardware();
                // Verify if the Ip Address belongs to a Virtual Server
                foreach (var vsi in virtualGuests)
                {
                    if (vsi.primaryIpAddress == ipAddress)
                    {
                        templateObject.accountId = vsi.accountId;
                        templateObject.guestId = vsi.id;
                        templateObject.guestIdSpecified = true;
                    }
                }
                // Verify if the Ip Address belongs to a Hardware Object
                foreach(var hardware in hardwareList)
                {
                    if(hardware.primaryIpAddress == ipAddress)
                    {
                        templateObject.accountId = hardware.accountId;
                        templateObject.hardwareId = hardware.id;
                        templateObject.hardwareIdSpecified = true;
                    }
                }
                SoftLayer_Network_Security_Scanner_Request request = securityService.createObject(templateObject);
                Console.WriteLine("Vulnerability Scan Request created: " + request.id);
                Console.WriteLine("Create Date: " + request.createDate);
                Console.WriteLine("Ip Address: " + request.ipAddress);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to create security scan request: " + e.Message);
            }
        }
    }
}

```
