---
title: "Using Initialization Parameters in the SoftLayer API"
description: "How Initialization parameters work"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
---

Table of contents 

1. [Structure](#structure) 
2. [Creating an Initialization Parameter](#creating-an-initialization-parameter)
    1. [SOAP](#soap)
    2. [XML-RPC](#xml-rpc)
    3. [REST](#rest)
3. [Exceptions to the Rule](#exceptions-to-the-rule)
4. [Parameters](#Parameters)
5. [Optional Headers](#Optional-Headers)

Prior to calling methods on some objects represented in the [SoftLayer API](/reference/services/), a unique identifier must be used during instantiation of the service.  SoftLayer provides a way to instantiate your service objects by passing the service's initialization parameter in the header of your API calls.  Once this action is complete, all methods following this header will be directed to the method containing the initialization parameter.  
Nearly all data represented in the SoftLayer API is identified by a unique integer value. For instance, your SoftLayer customer account number is one of these unique identifiers and, consequently, is the value of the initialization parameter in your calls to the [SoftLayer_Account](/reference/services/SoftLayer_Account/) service.


## Structure
An initialization parameter is an object of the type `<SoftLayer_Service>InitParameters` where `<SoftLayer_Service>` is the name of the service you're accessing. Each initialization parameter has a single integer property called `id`, representing the unique identifier of the object you're trying to retrieve or edit. For instance, The [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server/getObject/) method's initialization parameter is stored in the `SoftLayer_Hardware_ServerInitParameters` data type with the single integer property `id`.

If a method requires a `SoftLayer_ServiceInitParameter` you will find that documented under the `Required Headers` section of each method.

## Creating an Initialization Parameter
### SOAP
Languages that support SOAP usually have built-in mechanisms to add headers to a SOAP call (the [SoapHeader](https://www.php.net/manual/en/class.soapheader.php) PHP class, for instance). If building manual SOAP calls, then format your request XML akin to the following (assuming you're working with the SoftLayer_Network_Backbone service):
```xml
<xml>
<SoftLayer_Network_BackboneInitParameters xsi:type="v3:SoftLayer_Network_BackboneInitParameters">
    <id xsi:type="xsd:int">115</id>
</SoftLayer_Network_BackboneInitParameters>
</xml>
```

### XML-RPC
Since XML-RPC treats data as array keys and values, its initialization parameter structure is quite different:
```xml
<xml>
<struct>
  <member>
    <name>SoftLayer_Network_BackboneInitParameters</name>
    <value>
      <struct>
        <member>
          <name>id</name>
          <value>
            <int>115</int>
          </value>
        </member>
      </struct>
    </value>
  </member>
</struct>
</xml>
```

Most programming and scripting languages with SOAP and XML-RPC support have built-in methods to create request headers, but if formatting a call manually then place XML like the values above into the headers of your requests.

### REST
With REST, the init parameter goes directly into the URL, between the `SoftLayer_Server` and method call (`getObject` in the below example). 

```rest
https://<username>:<apiKey>@api.softlayer.com/rest/v3/SoftLayer_Network_Backbone/115/getObject.json
```


## Exceptions to the Rule
Some methods do not require initialization parameters. These kinds of methods usually create objects or retrieve groups of objects. For instance, the [SoftLayer_Ticket::addUpdate](/reference/services/SoftLayer_Ticket/addUpdate/) method requires an initialization parameter set since it relates to updating a specific ticket, but the [SoftLayer_Ticket::createAdministrativeTicket](/reference/services/SoftLayer_Ticket/createAdministrativeTicket) method does not since there is no existing ticket to reference. If a method does not require an initialization parameter, its service's initialization parameter data type is absent from its manual page.

On most methods, you will also see the `authenticate` header, however the [SoftLayer_Resource_Metadata](reference/services/SoftLayer_Resource_Metadata/) service doesn't require this because it uses information about the server making the API call itself to return useful data. Since that service is meant to only be used by infrastructure on the SoftLayer network, it is only available on the private network endpoint itself. 

## Parameters
On each method's documentation page, you will see a section called `Parameters`. If this is just an empty table, that means the method requires no parameters to be passed in. However if the method accepts parameters, they will be documented like this:

#### [Hardware_Server::editObject() Parameters](/reference/services/SoftLayer_Hardware_Server/editObject/)
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Hardware_Server'>SoftLayer_Hardware_Server </a>| A skeleton SoftLayer_Hardware_Server object with only the properties defined that you wish to change. Unchanged properties are left alone.|

This indicates that this method takes in 1 parameter, of type SoftLayer_Hardware_Server. 

>*IMPORTANT*:

>The order of the parameters is critical. The order you pass them in needs to match the order listed in the documentation. Parameters are NOT named, so don't pass in the parameter name when calling the specific method.


#### XML-RPC
The XML-RPC payload would look something like this:

```xml
<?xml version='1.0'?>
<methodCall>
    <methodName>editObject</methodName>
    <params>
        <param>
            <value>
                <struct>
                    <member>
                        <name>headers</name>
                        <value>
                            <struct>
                                <member>
                                    <name>SoftLayer_Virtual_GuestInitParameters</name>
                                    <value>
                                        <struct>
                                            <member>
                                                <name>id</name>
                                                <value><int>92888528</int></value>
                                            </member>
                                        </struct>
                                    </value>
                                </member>
                            </struct>
                        </value>
                    </member> 
                </struct>
            </value> 
        </param>
        <param> 
            <value>
                <struct>
                    <member>
                        <name>domain</name>
                        <value><string>testing02.com</string></value>
                    </member>
                </struct>
            </value>
        </param>
    </params>
</methodCall>
```

#### REST
When making REST api calls that require parameters, they need to be specified as a POST request. For API calls with multiple parameters, this is the format  `-d '{"parameters": [PARAM1, PARAM2, PARAM3]}'`

```
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [{"domain": "testing02.com"}]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/123456789/editObject.json'
```


