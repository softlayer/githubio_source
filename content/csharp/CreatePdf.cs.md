---
title: "CreatePdf.cs"
description: "CreatePdf.cs"
date: "2018-04-25"
classes: 
    - "SoftLayer_Billing_Order_QuoteInitParametersValue"
    - "SoftLayer_Billing_Order_QuoteService"
    - "SoftLayer_Billing_Order_QuoteInitParameters"
    - "SoftLayer_Billing_Order_Quote"
tags:
    - "quotes"
---


```
﻿﻿//-----------------------------------------------------------------------
// <copyright file="CreatePdf.cs" company="Softlayer">
//     SoftLayer Technologies, Inc.
// </copyright>
// <license>
// http://sldn.softlayer.com/article/License
// </license>
//-----------------------------------------------------------------------
namespace Quotes
{
    using System;
    using System.IO;
    using System.Collections.Generic;
    class CreatePdf
    {
        /// <summary>
        /// Create Pdf
        /// This script creates a PDF record of a SoftLayer quoted order.
        /// The Pdf is stored in the path specified in "path" string
        /// See below for more details.
        /// </summary>
        /// <manualPages>
        /// http://sldn.softlayer.com/reference/services/SoftLayer_Billing_Order_Quote/getPdf
        /// </manualPages>
        static void Main(string[] args)
        {
            // Your SoftLayer username
            string username = "";
            // Your SoftLayer apiKey, you can generate it on: https://control.softlayer.com/account/users
            string apiKey = "apikey_goes_here";
            // Define the quote identifier that you wish to save
            int quoteId = 1528487;
            // Define the path that you wish to create the PDF from quote
            string path = @"C:\Reports\testpdf.pdf";
            // Creating a connection to the SoftLayer_Billing_Order_Quote API service and             
            // bind our API username and key to it. 
            authenticate authenticate = new authenticate();
            authenticate.username = username;
            authenticate.apiKey = apiKey;
            SoftLayer_Billing_Order_QuoteService quoteService = new SoftLayer_Billing_Order_QuoteService();
            quoteService.authenticateValue = authenticate;
            // Setting init parameters
            quoteService.SoftLayer_Billing_Order_QuoteInitParametersValue = new SoftLayer_Billing_Order_QuoteInitParameters();
            quoteService.SoftLayer_Billing_Order_QuoteInitParametersValue.id = quoteId;
            try
            {
                byte[] result = quoteService.getPdf();
                File.WriteAllBytes(path, result);
                Console.WriteLine("The PDF was created");
            }
            catch (Exception e)
            {
                Console.WriteLine("Unable to create PDF: " + e.Message);
            }
        }
    }
}

```
