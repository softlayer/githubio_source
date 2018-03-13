---
title: "Using Initialization Parameters in the SoftLayer API"
description: "How Initialization parameters work"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
---



<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc4">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#Structure">Structure</a></li>
<li class="toc-level-1"><a href="#Creating_an_Initialization_Parameter">Creating an Initialization Parameter</a>
<ol>
<li class="toc-level-2"><a href="#SOAP">SOAP</a></li>
<li class="toc-level-2"><a href="#XML-RPC">XML-RPC</a></li>
<li class="toc-level-2"><a href="#REST">REST</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Exceptions_to_the_Rule">Exceptions to the Rule</a></li>
</ol>
</div>
</div>
Prior to calling methods on some objects represented in the [[SoftLayer API]], a unique identifier must be used during instantiation of the service.  SoftLayer provides a way to instantiate your service objects by passing the service's initialization parameter in the header of your API calls.  Once this action is complete, all methods following this header will be directed to the method containing the initialization parameter.  
Nearly all data represented in the SoftLayer API is identified by a unique integer value. For instance, your SoftLayer customer account number is one of these unique identifiers and, consequently, is the value of the initialization parameter in your calls to the [[SoftLayer_Account]] service.
##Structure
An initialization parameter is an object of the type <SoftLayer_Service>''InitParameters'' where <SoftLayer_Service> is the name of the service you're accessing. Each initialization parameter has a single integer property called id, representing the unique identifier of the object you're trying to retrieve or edit. For instance, The [[SoftLayer_Network_Backbone]] service's initialization parameter is stored in the ''SoftLayer_Network_BackboneInitParameters'' data type with the single integer property id.

##Creating an Initialization Parameter
###SOAP
Languages that support SOAP usually have built-in mechanisms to add headers to a SOAP call (the [http://www.php.net/manual/en/function.soap-soapheader-construct.php SoapHeader] PHP class, for instance). If building manual SOAP calls, then format your request XML akin to the following (assuming you're working with the SoftLayer_Network_Backbone service):
<xml>
<SoftLayer_Network_BackboneInitParameters xsi:type="v3:SoftLayer_Network_BackboneInitParameters">
    <id xsi:type="xsd:int"115</id>
</SoftLayer_Network_BackboneInitParameters>
</xml>
===XML-RPC===
Since XML-RPC treats data as array keys and values, its initialization parameter structure is quite different:
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
Most programming and scripting languages with SOAP and XML-RPC support have built-in methods to create request headers, but if formatting a call manually then place XML like the values above into the headers of your requests.
###REST
<code>
https://<username>:<apiKey>@api.softlayer.com/rest/v3/SoftLayer_Network_Backbone/115.xml
</code>
##Exceptions to the Rule
Some methods do not require initialization parameters. These kinds of methods usually create objects or retrieve groups of objects. For instance, the [[SoftLayer_Ticket::addUpdate]] method requires an initialization parameter set since it relates to updating a specific ticket, but the [[SoftLayer_Ticket::createAdministrativeTicket|createAdministrativeTicket]] method does not since there is no existing ticket to reference. If a method does not require an initialization parameter, its service's initialization parameter data type is absent from its manual page.