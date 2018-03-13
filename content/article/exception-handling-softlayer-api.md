---
title: "Exception Handling in the SoftLayer API"
description: "How to handle Exceptions provided by the SoftLayer API"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
    - "debugging"
author: "sldn"
---



Like any programming interface the SoftLayer API at times needs to return error messages to its users. The SoftLayer API brings these exceptions forward to the user so their application can handle the unexpected result. Exceptions are returned as SOAP or XML-RPC faults depending on the RPC method used to execute your API method call. Programming and scripting languages with SOAP and XML-RPC support usually have built-in methods for handling faults.

If you are manually processing your API response a SOAP Fault is akin to this:
<xml>
<SOAP-ENV:Fault>
    <faultcode>MY_FAULT_CODE</faultcode>
    <faultstring>MY_EXCEPTION</faultstring>
</SOAP-ENV:Fault>
</xml>

Its XML-RPC counterpart resembles this:

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

The REST responses vary based on the requested output type.  An example REST response that you might find looks like this:

XML:
<xml>
<root>
    <error>faultString</error>
</root>
</xml>

JSON:
<javascript>
{
    error: "faultString"
}
</javascript>

Method calls are halted if exceptions are encountered during their execution.  The specialized exceptions that a method can throw are listed on that method's manual page.

## Common Exceptions ##
Though the exceptions that each method can throw are listed on that method's manual page, the SoftLayer API throws a number of more common exceptions in the case of a general failure. These exceptions include:
<ul>
<li>'''<code>An error has occurred while processing your request.  Please try again later.</code>'''
A generic message for an internal error.  Upon encountering this error, please open a Support Ticket in the SoftLayer Customer Portal with the following information:
<ul>
<li>Note that error was received through the API</li>
<li>API call that is generating the error</li>
</ul>
</li>
<li>'''<code>No valid authentication found</code>'''
[[Authenticate]] header was not passed to the method call</li>
<li>'''<code>Invalid API token</code>'''
Username of API key passed to the  method call are incorrect</li>
<li>'''<code>SOAP-ERROR: Encoding: Violation of encoding rules</code>'''
SOAP API call is passing an incorrect data type in its request
'''Example:''' A string where an integer is expected.</li>

<li>'''<code>This feature is managed by SoftLayer support.</code>'''
The resource you are trying to access is a managed service of your SoftLayer account and can only be changed by SoftLayer support.</li>
<li>'''<code>Unable to find object with id of ‘<id>’</code>'''
A resource could not be found for the provided identifier.</li>
</ul>
## External Links ##

* [http://www.w3schools.com/soap/soap_fault.asp SOAP Fault Element] at [http://www.w3schools.com/ w3schools.com]
* [http://www.xmlrpc.com/spec XML-RPC Specification] at [http://www.xmlrpc.com/ xmlrpc.com]
