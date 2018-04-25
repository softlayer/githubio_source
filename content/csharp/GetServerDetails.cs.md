---
title: "GetServerDetails.cs"
description: "GetServerDetails.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountService"
    - "SoftLayer_Account"
    - "SoftLayer_AccountObjectMask"
    - "SoftLayer_AccountObjectMaskValue"
    - "SoftLayer_Software_Component_Password"
    - "SoftLayer_Hardware"
    - "SoftLayer_Software_Component_OperatingSystem"
    - "SoftLayer_Hardware_Component"
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Network_Component"
tags:
    - "baremetalservers"
---


```
//-----------------------------------------------------------------------
// <copyright file="GetServerDetails.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace GetServerDetailsNamespace
{
    using System;
    using System.Collections.Generic;

    class GetServerDetails
    {
        /// <summary>
        /// Retrieve a list of hardware and print a report with server hostname, domain,
        /// login info, network, CPU, and RAM details.
        /// This script makes a single call to the getHardware() method in the
        /// SoftLayer_Account API service
        /// (http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware)
        /// and uses an object mask to retrieve related information. 
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
        /// http://sldn.softlayer.com/reference/datatype/SoftLayer_Hardware_Server/
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer API username.           
            string username = "set me";

            // Your SoftLayer API key.                       
            string apiKey = "set me";

            // Creating a connection to the SoftLayer_Account API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            // Declaring a new API service object for the SoftLayer_Account API service.
            SoftLayer_AccountService accountService = new SoftLayer_AccountService();
            accountService.authenticateValue = authenticate;

            // Adding an object mask to retrieve our hardwares' related items such as its
            // operating system, hardware components, and network components. Object masks
            // can retrieve any information related to your object. See
            // http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
            // for a list of the relational properties you can retrieve along with hardware.
            SoftLayer_AccountObjectMask objectMask = new SoftLayer_AccountObjectMask();
            objectMask.mask = new SoftLayer_Account();

            objectMask.mask.hardware = new SoftLayer_Hardware[1];
            objectMask.mask.hardware[0] = new SoftLayer_Hardware();
            objectMask.mask.hardware[0].processors = new SoftLayer_Hardware_Component[1];
            objectMask.mask.hardware[0].processorCount = new uint();
            objectMask.mask.hardware[0].processorCountSpecified = true;
            objectMask.mask.hardware[0].memory = new SoftLayer_Hardware_Component[1];
            objectMask.mask.hardware[0].memoryCount = new uint();
            objectMask.mask.hardware[0].memoryCountSpecified = true;
            objectMask.mask.hardware[0].networkComponents = new SoftLayer_Network_Component[1];
            objectMask.mask.hardware[0].networkComponents[0] = new SoftLayer_Network_Component();
            objectMask.mask.hardware[0].operatingSystem = new SoftLayer_Software_Component_OperatingSystem();
            objectMask.mask.hardware[0].operatingSystem.passwords = new SoftLayer_Software_Component_Password[1];
            objectMask.mask.hardware[0].operatingSystem.passwords[0] = new SoftLayer_Software_Component_Password();

            accountService.SoftLayer_AccountObjectMaskValue = objectMask;

            SoftLayer_Hardware[] hardwares = null;
            try
            {
                // Making the call to retrieve our hardware records.
                hardwares = (SoftLayer_Hardware[])accountService.getHardware();
            }
            catch (Exception e)
            {
                // If there was an error returned from the SoftLayer API then bomb out with the
                // error message.
                Console.WriteLine("Unable to retrieve hardware. " + e.Message);
            }

            foreach (var hardware in hardwares)
            {
                var passwords = hardware.operatingSystem.passwords[0];
                var networks = hardware.networkComponents;

                // Go through the hardware's network components to get it's public and
                // private network ports. Save MAC addresses.
                string publicMacAddress = "not found";
                string privateMacAddress = "not found";
                foreach (var network in networks)
                {
                    // SoftLayer uses eth0 on the private network and eth1 on the public
                    // network.
                    if (network.name.Equals("eth") && network.port == 0)
                    {
                        privateMacAddress = network.macAddress;
                    }
                    else
                    {
                        if (network.name.Equals("eth") && network.port == 1)
                        {
                            publicMacAddress = network.macAddress;
                        }
                    }
                }

                // Hardware can only have like processors in them, so use the first item in
                // the processors array to get the type of processor in the server.
                string processorType = hardware.processors[0].hardwareComponentModel.hardwareGenericComponentModel.capacity +
                                        hardware.processors[0].hardwareComponentModel.hardwareGenericComponentModel.units + " " +
                                        hardware.processors[0].hardwareComponentModel.hardwareGenericComponentModel.description;

                // Treat memory the same way we did processors.  
                string memoryType = hardware.memory[0].hardwareComponentModel.hardwareGenericComponentModel.capacity +
                                    hardware.memory[0].hardwareComponentModel.hardwareGenericComponentModel.units + " " +
                                    hardware.memory[0].hardwareComponentModel.hardwareGenericComponentModel.description;

                // All done! Print hardware info.
                Console.WriteLine("Hostname: " + hardware.hostname);
                Console.WriteLine("Domain: " + hardware.domain);
                Console.WriteLine("Login: " + passwords.username + "/" + passwords.password);
                Console.WriteLine("Public IP Address: " + hardware.primaryIpAddress);
                Console.WriteLine("Public MAC Address: " + publicMacAddress);
                Console.WriteLine("Private MAC Address: " + privateMacAddress);
                Console.WriteLine("CPUs: " + hardware.processorCount + "x " + processorType);
                Console.WriteLine("RAM: " + hardware.memoryCount + "x " + processorType);
                Console.WriteLine(" ");
            }
        }

        /// <summary>
        /// Convert an object to a json to print it beautiful.
        /// </summary>
        /// <param name="obj"></param>
        /// <returns>a json string</returns>
        public static string objectToJson(Object obj)
        {
            string json = Newtonsoft.Json.JsonConvert.SerializeObject(obj, Newtonsoft.Json.Formatting.Indented);
            JsonPrettyPrinterPlus.JsonPrettyPrinter jsonPP = new JsonPrettyPrinterPlus.JsonPrettyPrinter(new JsonPrettyPrinterPlus.JsonPrettyPrinterInternals.JsonPPStrategyContext());

            string jsonx = jsonPP.PrettyPrint(json);

            return jsonx;
        }
    }
}

```
