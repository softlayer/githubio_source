---
title: "Using Result Limits in the SoftLayer API"
description: "How to paginate results from the SoftLayer API using ResultLimits"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
    - "resultlimit"
---

Many of the methods in the SoftLayer API return arrays of data types. In these cases it may be useful to limit the number of results that the API retrieves from your method call. Fortunately SoftLayer provides an easy way to accomplish this via a method analogous to the SQL <tt>LIMIT</tt> statement that you can apply in the header of your method calls. Result limits are optional for  all method calls, and a method's manual page states whether or not it can use a result limit. Methods that retrieve only one item cannot use result limits.

## Structure
A result limit is an object of the type `resultLimit` with two integer properties, `limit` and `offset`. The result limit's `limit` defines how many items you wish your limit result set to while its `offset` defines the starting point in your result set list to begin your limit. For instance, if you want to only retrieve 10 items in an API call starting with item 5 then your `limit` is 10 and `offset` is 5.

## Creating a Result Limit
Languages that support SOAP usually have built-in mechanisms to add headers to a SOAP call (the [SoapHeader](http://www.php.net/manual/en/function.soap-soapheader-construct.php ) PHP class, for instance). If building manual SOAP calls, then format your request XML akin to the following (assuming you're setting a 10 item limit starting at item 5 in your result set):

###  SOAP

```xml
<xml>
<resultLimit xsi:type="slt:resultLimit" xmlns:slt="http://api.service.softlayer.com/soap/v3/SLTypes/">
    <limit xsi:type="xsd:int">10</limit>
    <offset xsi:type="xsd:int">5</offset>
</resultLimit>
</xml>
```

Replace the value of the `limit` and `offset` fields with the data limits and offsets that you wish to limit your result set with. Since XML-RPC treats data as array keys and values, its structure is quite different:

### XML-RPC

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
                        <int>10</int>
                    </value>
                </member>
                <member>
                    <name>offset</name>
                    <value>
                        <int>5</int>
                    </value>
                </member>
            </struct>
        </value>
    </member>
</struct>
</xml>
```

Again, most programming and scripting languages with SOAP and XML-RPC support have built-in methods to create request headers, but if formatting a call manually then place XML like the values above into the headers of your requests.


### REST

For REST API users, simply add `resultLimit=Offset,Limit` as a url argument.

```
curl -u $SL_USER:$SL_APIKEY \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getHardware.json?resultLimit=0%2C2'
```