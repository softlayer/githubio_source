---
title: "Legacy Object Masks"
description: "(DEPRECIATED) Dealing with Legacy Object Masks"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
    - "debugging"
    - "deprecated"
author: "sldn"
---

<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc10">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#Structure">Structure</a></li>
<li class="toc-level-1"><a href="#Creating_an_Object_Mask">Creating an Object Mask</a></li>
<li class="toc-level-1"><a href="#Referenced_API_Components">Referenced API Components</a>
<ol>
<li class="toc-level-2"><a href="#Services">Services</a></li>
<li class="toc-level-2"><a href="#Data_Types">Data Types</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Internal_Links">Internal Links</a></li>
</ol>
</div>
</div>
Most of the data types modeled in the SoftLayer API contain relational properties that tie one data type to another. For instance, a SoftLayer_Account has links to its domains, support tickets, hardware, users, and much more. By default, calling the [[SoftLayer_Account]] service's <code>getObject</code> method won't retrieve relational and count properties. In order to retrieve this information, you would have to call getUsers, getTickets, and other methods. Making multiple API calls can significantly slow down an API-based application's response time, especially if the application retrieves a large amount of information at once. An alternative to making multiple method calls is to define an object mask in your method's header to retrieve all the information you need with a single call.  Defining an object mask can result in a very noticeable increase in overall API responsiveness. While object masks are optional, they are the only way to retrieve a data type's count properties.

## Structure

An object mask is an object of the type <prefix>ObjectMask where <prefix> is the name of the service you are accessing, “SoftLayer_AccountObjectMask” in this example. The structure within an object mask is determined by the one making the API method call. No values are defined in an object mask - only the relational data you wish to retrieve. To retrieve a relational or count property, simply add an empty property to your request's object mask with the name of the properties you are trying to receive. 

In the example below we are retrieving multiple sets of information, some of which is part of a hierarchy and some stands alone.  We are first retrieving all domains and the resource records associated to those domains.  The next information queried is all open tickets.  As a part of the open tickets, we will be looking for assigned users, attached hardware and all updates to be returned.  Finally, we will query a count of all users associated with this account. The following Object Mask structure will help us retrieve all of that information.
```
*Domains
**resourceRecords
*openTickets
**assignedUser
**attachedHardware
**updates
*userCount
```
In this level of the object mask, the ''domains'', ''openTickets'', and ''userCount'' (all first level properties) are directly related to the SoftLayer_Account data type.  The ''resourceRecords'', ''assignedUser'', ''attachedHardware'' and ''updates'' properties are considered second level properties, which are related to the first level properties they are nested under. Domains have resource records, and tickets have users, hardware, and updates. Create an object mask with this structure and send it in the header to a call to getObject in the SoftLayer_Account service to retrieve all of this data.

## Creating an Object Mask
Languages that support SOAP usually have built-in mechanisms to add headers to a SOAP call (i.e. the [http://php.net/manual/en/class.soapheader.php SoapHeader] PHP class).  When building manual SOAP calls, format your request XML similar to the following (assuming you're retrieving the structure above from the SoftLayer_Account service):

```xml
<xml>
<SoftLayer_AccountObjectMask xsi:type="v3:SoftLayer_AccountObjectMask">
    <mask xsi:type="slt:SoftLayer_Account" xmlns:slt="http://api.service.softlayer.com/soap/v3/SLTypes/">
        <domains>
            <resourceRecords />
        </domains>
        <openTickets>
            <assignedUser />
            <attachedHardware />
            <updates />
        </openTickets>
        <userCount />
    </mask>
</SoftLayer_AccountObjectMask>
</xml>
```
Again, note that we're not setting any values, just empty records for the data we wish to retrieve. Since XML-RPC treats data as array keys and values, its structure is quite different:
```xml
<xml>
<struct>
    <member>
        <name>SoftLayer_AccountObjectMask</name>
        <value>
             <struct>
                <member>
                    <name>mask</name>
                    <value>
                        <struct>
                            <member>
                                <name>domains</name>
                                <value>
                                    <struct>
                                        <member>
                                            <name>resourceRecords</name>
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
                                <name>openTickets</name>
                                <value>
                                    <struct>
                                        <member>
                                            <name>assignedUser</name>
                                            <value>
                                                <array>
                                                    <data/>
                                                </array>
                                            </value>
                                        </member>
                                        <member>
                                            <name>attachedHardware</name>
                                            <value>
                                                <array>
                                                    <data/>
                                                </array>
                                            </value>
                                        </member>
                                        <member>
                                            <name>updates</name>
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
                                <name>userCount</name>
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

Most programming and scripting languages with SOAP and XML-RPC support have built-in methods to create request headers, but if formatting a call manually then place XML like the values above into the headers of your requests.

##Referenced API Components
###Services
[[SoftLayer_Account]]
###Data Types
[[SoftLayer_Account]]
##Internal Links
[[Implementing SOAP in Perl]]
[[Object Masks and Filters in C Sharp]]