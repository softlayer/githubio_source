---
title: "Exception Handling in the SoftLayer API"
description: "How to handle Exceptions provided by the SoftLayer API"
date: "2018-08-23"
tags:
    - "article"
    - "sldn"
    - "debugging"
author: "sldn"
---

Like any programming interface the SoftLayer API at times needs to return error messages to its users. The SoftLayer API brings these exceptions forward to the user so their application can handle the unexpected result. Exceptions are returned as SOAP, REST, or XML-RPC faults depending on the RPC method used to execute your API method call. Programming and scripting languages with SOAP and XML-RPC support usually have built-in methods for handling faults.

## Exceptions by Endpoint

#### SOAP Style Exceptions

```xml
<xml>
<SOAP-ENV:Fault>
    <faultcode>MY_FAULT_CODE</faultcode>
    <faultstring>MY_EXCEPTION</faultstring>
</SOAP-ENV:Fault>
</xml>
```

#### XML-RPC Style Exceptions

```xml
<xml>
<?xml version="1.0"?>
<methodResponse>
    <fault>
        <value>
            <struct>
                <member>
                    <name>faultCode</name>
                    <value>
                        <int>1</int>
                     </value>
                 </member>
                 <member>
                     <name>faultString</name>
                     <value>
                         <string>MY_EXCEPTION</string>
                     </value>
                 </member>
             </struct>
         </value>
     </fault>
</methodResponse>
</xml>
```
#### REST Style Exceptions

Rest API calls can have the results returned as XML, or JSON, depending on how you end your api call.

https://api.softlayer.com/rest/v3.1/SoftLayer_Account/BlockDeviceTemplateGroups1.xml:
```xml
<root>
    <error>Function (&quot;BlockDeviceTemplateGroups1&quot;) is not a valid method for this service.</error>
    <code>SoftLayer_Exception_Public</code>
</root>
```

https://api.softlayer.com/rest/v3.1/SoftLayer_Account/BlockDeviceTemplateGroups1.json:
```
<json>
{
    "code": "SoftLayer_Exception_Public",
    "error": "Function (\"BlockDeviceTemplateGroups1\") is not a valid method for this service."
}
</json>
```
Method calls are halted if exceptions are encountered during their execution.  The specialized exceptions that a method can throw are listed on that method's manual page.

## Common Exceptions 

- SoftLayer_Exception_Public
This is the base exception class, and most exceptions will fall into this code. Generally you will need to read the error code to understand what exactly went wrong.

`{"error":"Access Denied. ","code":"SoftLayer_Exception_Public"}`
Check your username and API key to make sure they are still valid. 

`{"error":"Internal Error","code":"SoftLayer_Exception_Public"}`

Generally this indicates you are requesting too much data. Try limiting your objectMask to only the local and relational properties you need, or use a resultLimit. 

- SoftLayer_Exception_InvalidValue

`{"error": The character @ must appear once and only once in an email address.","code":"SoftLayer_Exception_InvalidValue"}`

Check the methods manual page to make sure the data you are sending matches the type expected.

- SoftLayer_Exception_ObjectNotFound

`{"error":"Unable to find object with id of '1'.","code":"SoftLayer_Exception_ObjectNotFound"}`

Either the ID you are looking for doesn't exist, or you don't have access to it.

- SoftLayer_Exception_WebService_BadRequest

`{"error":"Bad request","code":"SoftLayer_Exception_WebService_BadRequest"}`

The API endpoint wasn't able to figure out your request. Could be the result of trying to POST to a method that only accepts GET requests, or some other badly formed data.

- SoftLayer_Exception_NotImplemented

Generally not an error you should encounter, but can be seen when trying to do some actions on resources that have not fully provisioned. If you get this exception on a resource that is fully provisioned, opening a ticket is recommended. 


