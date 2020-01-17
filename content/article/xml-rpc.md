---
title: "XML-RPC"
description: "How to interact with the XML-RPC endpoint"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
    - "resultlimit"
    - "objectmask"
---




SoftLayer provides an XML-RPC interface in addition to [SOAP](/article/soap) and [REST](/article/rest). The XML-RPC API is built to mimic the SOAP interface. We recommend using the XML-RPC API when your chosen language doesn't have proper SOAP support.

## Endpoint URLs
The SoftLayer XML-RPC API has one endpoint per available API service. Each endpoint has a unique URL containing the service name of the API services that it calls.  For example:
`https://api.softlayer.com/xmlrpc/v3/<serviceName>`
or
`http://api.service.softlayer.com/xmlrpc/v3/<serviceName>`

In these examples, `"<serviceName>"` would be replaced with the name of the API service you wish to call. Use the second URL to access the XML-RPC API over SoftLayer's private network. It's a faster, more secure way to communicate with SoftLayer, but the system making API calls must be on SoftLayer's private network. All SoftLayer servers come with access to our private network, including CCIs.  Additional private IP addresses are available for purchase should they be needed.   

## Data Types
The XML-RPC API's data types mimic the same data types found in the SOAP API. Complex types are modeled as XML-RPC <code>struct</code>s. Declare and receive these <code>struct</code>s when working with method parameters and return types. A [[SoftLayer_Hardware_Server]] is rendered as a collection of simple types:
```xml
<xml>
<struct>
    <member>
        <name>id</name>
        <value>
            <int>1234</int>
        </value>
    </member>
    <member>
        <name>hostname</name>
        <value>
            <string>test</string>
        </value>
    </member>
    <member>
        <name>domain</name>
        <value>
            <string>example.org</string>
        </value>
    </member>
    <member>
        <name>fullyQualifiedDomainName</name>
        <value>
            <string>test.example.org</string>
        </value>
    </member>
    <member>
        <name>hardwareStatusid</name>
        <value>
            <int>2</int>
        </value>
    </member>
    <member>
        <name>accountId</name>
        <value>
            <int>12345</int>
        </value>
    </member>
    <member>
        <name>bareMetalInstanceFlag</name>
        <value>
            <boolean>0</boolean>
        </value>
    </member>
</struct>
</xml>
```
## Sending API Call Headers
The first parameter in every XML-RPC call is a <code><struct></code> named "headers". Your headers parameter contains the headers required for your API call to work, such as authentication and initialization parameters. Like their SOAP complex type equivalent, these headers are modeled as <code><struct></code> objects in your call's XML. This sample header parameter contains authentication information and an initialization parameter for the [[SoftLayer_Hardware_Server]] API service:
```xml
<xml>
<struct>
    <member>
        <name>headers</name>
        <value>
            <struct>
                <member>
                    <name>authenticate</name>
                    <value>
                        <struct>
                            <member>
                                <name>username</name>
                                <value>
                                    <string>set me</string>
                                </value>
                            </member>
                            <member>
                                <name>apiKey</name>
                                <value>
                                    <string>set me!</string>
                                </value>
                            </member>
                        </struct>
                    </value>
                </member>
                <member>
                    <name>SoftLayer_Hardware_ServerInitParameters</name>
                    <value>
                        <struct>
                            <member>
                                <name>id</name>
                                <value>
                                    <string>1234</string>
                                </value>
                            </member>
                        </struct>
                    </value>
                </member>
            </struct>
        </value>
    </member>
</struct>
</xml>
```
## Using Object Masks
Add an [[object mask]] to your API call by adding a <code><struct></code> to your headers parameter with the name "<serviceName>ObjectMask", where <code><serviceName></code> corresponds to the name of the API service you are calling. For instance, an object mask for the SoftLayer_Account API service has the name <code>SoftLayer_AccountObjectMask</code> and the SoftLayer_Hardware_Server service's corresponding object mask class name is <code>SoftLayer_Hardware_ServerObjectMask</code>.

Declare a <code><struct></code> inside your object with the name "mask" containing the relational and count properties you wish to retrieve along with your API call result. Each item in your object mask is a <code><struct></code> with the name of the property you wish to retrieve and an empty array value.
This example retrieves the following information:

* An account's physical hardware records 
* That hardware's operating system record
* Operating system passwords 
* Network components 
* Datacenter in which the hardware is located  
* Number of processors in each hardware

```xml
<xml>
<struct>
    <member>
        <name>SoftLayer_Hardware_ServerObjectMask</name>
        <value>
             <struct>
                <member>
                    <name>mask</name>
                    <value>
                        <struct>
                            <member>
                                <name>operatingSystem</name>
                                <value>
                                    <struct>
                                        <member>
                                            <name>passwords</name>
                                            <value>
                                                <array>
                                                    <data/>
                                                </array>
                                            </value>
                                        </member>
                                    </struct>
                                </value>
                            </member>
                            <member>
                                <name>networkComponents</name>
                                <value>
                                    <array>
                                        <data/>
                                    </array>
                                </value>
                            </member>
                            <member>
                                <name>datacenter</name>
                                <value>
                                    <array>
                                        <data/>
                                    </array>
                                </value>
                            </member>
                            <member>
                                <name>processorCount</name>
                                <value>
                                    <array>
                                        <data/>
                                    </array>
                                </value>
                            </member>
                        </struct>
                    </value>
                </member>
            </struct>
        </value>
    </member>
</struct>
</xml>
```
## Using Result Limits
Place a result limit in your API call by adding a <code><struct></code> to your headers parameter with the name "resultLimit" containing two members:

* "limit", an integer representing the number of results to limit your call.
* "offset", an integer offset to begin your result set.
This resultLimit <strict> represents a result with a limit of 2, starting at offset 0.

```xml
<xml>
<struct>
    <member>
        <name>resultLimit</name>
        <value>
            <struct>
                <member>
                    <name>limit</name>
                    <value>
                        <int>2</int>
                    </value>
                </member>
                <member>
                    <name>offset</name>
                    <value>
                        <int>0</int>
                    </value>
                </member>
            </struct>
        </value>
    </member>
</struct>
</xml>
```
## Error Handling
The XML-RPC API returns XML-RPC faults if your call encounters an error. You may receive different <code>faultCodes</code> and <code>faultStrings</code> depending on your error.  The table below lists the most common faultCode and faultString returns you may receive.

faultCode   faultString Reason
-32601  "server error. requested method not found"  The API service youare querying doesn't contain the method youare calling or your call is missing a <methodName> entity.
-32602  "server error. invalid method init parameters"  One or more required API call headers are missing from your call.
-32700  "'parse error. not well formed" Your request contained invalid XML.
Various, usually the name of the API service you're requesting. Various Your API call encountered an error not represented by the errors above. Most faults belong to this category and result form an error encountered by SoftLayer while executing your method.

## Caveats
### Specifying Complex Types
As with REST, the XML-RPC API cannot determine extended complex types in certain parameters. In these cases you should define a <code>complexType</code> property in your complex parameters set to the type of object you're sending to your method.
## Referenced API Components
### Services

* [SoftLayer_Account](/reference/services/SoftLayer_Account)
* [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain)
* [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server)

### Data Types

* [SoftLayer_Hardware_Server](/reference/datatypes/SoftLayer_Hardware_Server)

## External Links
*  [The XML-RPC Home Page](http://www.xmlrpc.com/)
*  [XML-RPC](http://en.wikipedia.org/wiki/XML-RPC) at http://wikipedia.org/
