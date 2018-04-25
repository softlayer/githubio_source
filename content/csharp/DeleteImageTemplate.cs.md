---
title: "DeleteImageTemplate.cs"
description: "DeleteImageTemplate.cs"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest_Block_Device_Template_GroupService"
    - "SoftLayer_Provisioning_Version"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParameters"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
    - "SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParametersValue"
tags:
    - "imagetemplate"
---


```
//-----------------------------------------------------------------------
// <copyright file="DeleteImageTemplate.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------

namespace DeleteImageTemplateNamespace
{
    using System;

    class DeleteImageTemplate
    {
        /// <summary>
        /// Delete an image template
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username. 
            string username = "set me";

            // Your SoftLayer API key.            
            string apiKey = "set me";

            // The image template which you wish to delete
            // To get the list of images templates in your account call the Softlayer_Account::getPrivateBlockDeviceTemplateGroups method
            int imageTemplateId = 315894;

            // Creating a connection to the SoftLayer_Virtual_Guest_Block_Device_Template_GroupService API service and             
            // bind our API username and key to it.           
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;

            SoftLayer_Virtual_Guest_Block_Device_Template_GroupService imageTemplateService = new SoftLayer_Virtual_Guest_Block_Device_Template_GroupService();
            imageTemplateService.authenticateValue = authenticate;

            // Setting the init parameter
            imageTemplateService.SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParametersValue = new SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParameters();
            imageTemplateService.SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParametersValue.id = imageTemplateId;

            try
            {
                SoftLayer_Provisioning_Version1_Transaction result = imageTemplateService.deleteObject();
                Console.WriteLine("The image template has been deleted successfully ");
            }
            catch (Exception e)
            {
                Console.WriteLine("There was an error deleting the image template " + e);
            }
        }
    }
}

```
