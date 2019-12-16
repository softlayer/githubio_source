---
title: "Getting Started"
description: "Basics for the SoftLayer API"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
---


## Before You Start
### Choosing a Protocol
SoftLayer's API can be accessed by [SOAP](/article/soap/), [XML-RPC](/article/xml-rpc), or [REST](/article/rest/) means. Choose the best protocol for your preferred language and situation. We generally recommend using our SOAP interface, as it's the most comprehensive and most easily models the API's services and data types.

|Protocol |Advantages |Disadvantages | Recommended For | Recommended Languages|
| ---       |   ---        |       ---       |  ----     |----     |
|[SOAP](/article/soap/)| It's the fastest of the three protocols and allows you to make direct calls against SoftLayer's API services and data types. | Initial WSDL consumption may take some time. | Calling SoftLayer API services as code local to your project. | [C-Sharp](/csharp/), [Perl](/perl), [PHP](/php)|
|[XML-RPC](/article/xml-rpc) | Wide support amongst programming languages. | Lack of complex type specifications may require extra work when working with specific data types. |  Making API calls in languages without proper SOAP support. | [PHP](/php), [Python](/python) |
| [REST](/article/rest/) | Most programming languages support standard HTTP protocol operations if they don't have explicit support for SOAP or XML-RPC. |  REST URLs can become complex, especially when working with complex data structures. | Quickly calling get*() methods and retrieving data with a minimum amount of hierarchy. | [Ruby](/ruby), [Go](/go), [Java](/java), Any language that supports standard HTTP protocol operations, JSON parsing, and XML parsing

### Getting Your API Key
API calls are authenticated by the username you use to authenticate to the SoftLayer portal and a special [API Key](article/authenticating-softlayer-api/). You'll have the most access by using your account's master user to make API calls, but your code may be more secure if you use a sub-account with a more limited permission set.

### Using The Private Network
SoftLayer has API endpoints listening on the private network. Private network calls can only be made from systems on the private network, either from servers or computing instances purchased from SoftLayer or from systems VPN'd into the private network. On the other hand private network calls aren't made over the public Internet. They're more secure and take less time to execute.

To use the private network in your API call replace `https://api.softlayer.com` with `https://api.service.softlayer.com`. 

## Your First API Call

The [SoftLayer_Account/getObject|getObject()](/reference/services/SoftLayer_Account/getObject/) method in the [SoftLayer_Account](/reference/services/SoftLayer_Account/) service is a simple call that only requires an authentication header. It returns basic, top-level information about your SoftLayer account and is a great way to test your first API call. Here are a few ways to get it going:

### Raw SOAP
```xml
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="https://api.softlayer.com/soap/v3/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <SOAP-ENV:Header>
        <ns1:authenticate>
            <username>set me</username>
            <apiKey>set me too</apiKey>
        </ns1:authenticate>
    </SOAP-ENV:Header>
    <SOAP-ENV:Body>
        <ns1:getObject/>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```
### Raw XML-RPC

```xml
<?xml version="1.0" encoding="iso-8859-1"?>
<methodCall>
    <methodName>getObject</methodName>
    <params>
        <param>
            <value>
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
                                                    <string>set me too</string>
                                                </value>
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
    </params>
</methodCall>
```
### REST URL
`https://<username>:<apiKey>@api.service.softlayer.com/rest/v3/SoftLayer_Account`

### C\#
```csharp

String username = "set me";
String apiKey = "set me";
 
authenticate authenticate = new authenticate();
authenticate.username = username;
authenticate.apiKey = apiKey;
 
SoftLayer_AccountService accountService = new SoftLayer_AccountService();
accountService.authenticateValue = authenticate;

SoftLayer_Account account = accountService.getObject();
```

### Perl 

```perl

use SoftLayer::API::SOAP;
use strict;
 
my $api_username = 'set me';
my $api_key = 'set me';
 
my $account = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $api_username, $api_key)->getObject();

```
### PHP
```php
<?php
 
require_once('/path/to/SoftLayer/SoapClient.class.php');
 
$apiUsername = 'set me';
$apiKey = 'set me';
 
$client = SoftLayer_SoapClient::getClient('SoftLayer_Account', null, $apiUsername, $apiKey);
$account = $client->getObject();
```

### Python
```python
import SoftLayer
 
api_username = 'set me'
api_key = 'set me'
 
client = SoftLayer.Client(username=api_username, username=api_key)
account = client['Account'].getObject()
```
### Visual Basic .NET
```
Dim username As String = "set me"
Dim apiKey As String = "set me"
 
Dim authenticate As authenticate = New authenticate()
authenticate.username = username
authenticate.apiKey = apiKey
 
Dim accountService As SoftLayer_AccountService = New SoftLayer_AccountService()
accountService.authenticateValue = authenticate
 
Dim account as SoftLayer_Account = accountService.getObject()
```

## Where To Go From Here

The [SoftLayer_Account](/reference/services/SoftLayer_Account) service is an umbrella service. Everything relates back to your account record, your inventory, accounting records, domains, support tickets, and everything else. Where you go from here depends solely on what you're trying to accomplish. Make a few more queries to the SoftLayer_Account service to see what data types are returned. Try out a few [object mask](/article/object-masks/) to see how our data types relate to each other. If you need to work with another service then head to its manual page to see what you can do with it. Here are a few of the more common services used:

*   [SoftLayer_Hardware_Server](/reference/services/SoftLayer_Hardware_Server): Access information related to hardware purchased from SoftLayer.
*   [SoftLayer_Virtual_Guest](/reference/services/SoftLayer_Virtual_Guest): Access and automate CloudLayer Computing Instances.
*   [SoftLayer_Dns_Domain](/reference/services/SoftLayer_Dns_Domain): Create and manage domains in SoftLayer's DNS infrastructure.
*   [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket): Create and update support tickets.
*   [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer): Manage your account's portal, forum, VPN, and API users.
*   [SoftLayer_Billing_Item](/reference/services/SoftLayer_Billing_Item): Find out more information about what will show up on your next invoice.
*   [SoftLayer_Billing_Invoice](/reference/services/SoftLayer_Billing_Invoice): Access your previous invoices and audit what you've been paying for since you opened your account.
*   [SoftLayer_Product_Order](/reference/services/SoftLayer_Product_Order): Place orders for new or upgrade your existing SoftLayer services.