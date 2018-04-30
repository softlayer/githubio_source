---
title: "Visual Basic .NET"
description: "Visual Basic .NET"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
---


<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#Consuming_SOAP_WSDLs">Consuming SOAP WSDLs</a>
<ol>
<li class="toc-level-2"><a href="#Creating_Web_References">Creating Web References</a></li>
<li class="toc-level-2"><a href="#Using_Wsdl.exe">Using Wsdl.exe</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Making_API_Calls">Making API Calls</a>
<ol>
<li class="toc-level-2"><a href="#Creating_Service_Objects">Creating Service Objects</a></li>
<li class="toc-level-2"><a href="#Binding_Authentication">Binding Authentication</a></li>
<li class="toc-level-2"><a href="#Setting_Initialization_Parameters">Setting Initialization Parameters</a></li>
<li class="toc-level-2"><a href="#Making_the_API_Call">Making the API Call</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Using_Object_Masks">Using Object Masks</a></li>
<li class="toc-level-1"><a href="#Using_Result_Limits">Using Result Limits</a></li>
<li class="toc-level-1"><a href="#Error_Handling">Error Handling</a></li>
<li class="toc-level-1"><a href="#Caveats">Caveats</a>
<ol>
<li class="toc-level-2"><a href="#Setting_Specified_Properties">Setting "Specified" Properties</a></li>
<li class="toc-level-2"><a href="#What_to_do_When_API_Services_Change">What to do When API Services Change</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Referenced_API_Components">Referenced API Components</a>
<ol>
<li class="toc-level-2"><a href="#Services">Services</a></li>
<li class="toc-level-2"><a href="#Data_Types">Data Types</a></li>
<li class="toc-level-2"><a href="#Methods">Methods</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#External_Links">External Links</a></li>
</ol>
</div>
</div>
<h2 id="Consuming_SOAP_WSDLs">Consuming SOAP WSDLs</h2>
<p>There are two ways to import SoftLayer's API WSDLs into your project. Visual Studio can consume a SOAP service into a web reference accessible by your project. Visual Studio also comes with a utility called <a href="http://msdn.microsoft.com/en-us/library/7h3ystb6(VS.80).aspx">wsdl.exe</a> that is executed from a command prompt to read one or more WSDL files and directly convert them into source code that you can add to your project. Web services are typically easier to use in Visual Studio, but can become cumbersome if your project uses many SoftLayer API services. <span class="geshifilter"><code class="text geshifilter-text">Wsdl.exe</code></span> is useful if your project requires many API services.</p>
<p>The code samples in this article reflect code generated from SoftLayer API services by <span class="geshifilter"><code class="text geshifilter-text">wsdl.exe</code></span>.</p>
<h3 id="Creating_Web_References">Creating Web References</h3>
<ol>
<li>Click the <b>Project</b> menu in Visual Studio.</li>
<li>Select <b>Add Service Reference</b> from the <b>Project</b> menu dropdown box.</li>
<li>Click the <b>Advanced</b> button in the <b>Add Service Reference</b> window.<br />
<b>Note:</b>  The Service Reference Settings window will appear.</li>
<li>Click the <b>Add Web Reference</b> button in the <b>Service Reference Settings</b> window.</li>
<li>Enter the <b>URL to the WSDL</b> of the SoftLayer API service you wish to use in the <b>URL</b> field.</li>
<li>Click the green arrow to the right of the <b>URL</b> field.<br />
<b>Note:</b>  Visual Studio will download the WSDL file and analyze the methods and data types it contains.     </li>
<li>Enter a name for your new web reference in the <b>Web reference name</b> field.<br />
<b>Note:</b> Any reference to the API service added to the project will be referenced by this name.</li>
<li>Click the <b>Add Reference</b> button to import your new web service.<br />
<b>Note:</b>  You will now be returned to your project and your new API service will be visible in Visual Studio’s <b>Solution Explorer</b>.</li>
</ol>
<h3 id="Using_Wsdl.exe">Using Wsdl.exe</h3>
<p><span class="geshifilter"><code class="text geshifilter-text">Wsdl.exe</code></span> is located in <span class="geshifilter"><code class="text geshifilter-text">C:\Program Files\Microsoft SDKs\Windows\v7.0A\bin\</code></span> and should be executed with the following switches to convert SoftLayer's API WSDLs into Visual Basic code:</p>
<ul>
<li><span class="geshifilter"><code class="text geshifilter-text">/language:VB</code></span> - Tell wsdl.exe to export Visual Basic .NET code.</li>
<li><span class="geshifilter"><code class="text geshifilter-text">/sharetypes</code></span> - SoftLayer's WSDL files share a number of similar data types. The /sharetypes switch compiles these data types into single class files, making for a smaller source footprint and more efficiency when working in Visual Studio.</li>
<li><span class="geshifilter"><code class="text geshifilter-text">/out:C:\path\to\project\SoftLayer_API.vb</code></span> - Export generated code to a path within your project hierarchy. In this case we'll save code to the fileSoftLayer_API.vb.</li>
</ul>
<p>End the command with a space-separated list of the URLs of the API WSDLS you wish to import.  You can import as many WSDL files as you like.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">wsdl.exe /language:VB /out:"C:\Path\to\Project\SoftLayer_API.vb" /sharetypes 
https://api.softlayer.com/soap/v3/SoftLayer_Account?wsdl 
https://api.softlayer.com/soap/v3/SoftLayer_Hardware_Server?wsdl 
https://api.softlayer.com/soap/v3/SoftLayer_Dns_Domain?wsdl</pre></div>
<p><b>Note:</b>  To make private API calls, replace <span class="geshifilter"><code class="text geshifilter-text">https://api.softlayer.com</code></span><br />
    with <span class="geshifilter"><code class="text geshifilter-text">http://api.service.softlayer.com</code></span>.  Refer to our <a href="/article/Getting Started">Getting Started</a> article for more information on making private API calls.</p>
<p>Re-run this command if you wish to import more API services into your project.</p>
<p>Once your code file is created you must add it to your project.</p>
<ol>
<li>Right click the name of your project in the <b>Visual Studio Solution Explorer</b>.</li>
<li>Scroll over the <b>Add</b> option in the expanded menu.</li>
<li>Click the <b>Existing Item</b> button in the <b>Add</b> menu.</li>
<li>Locate your generated code file in the <b>Add Existing Item</b> dialog window.</li>
<li>Click to highlight your <b>generated code file</b>.</li>
<li>Click the <b>OK</b> button to continue.</li>
</ol>
<p>Finally, your project must include the <span class="geshifilter"><code class="text geshifilter-text">System.Web.Services</code></span> service reference to make SOAP calls from your imported code.</p>
<ol>
<li>Click to expand the <b>Project</b> menu in Visual Studio.</li>
<li>Select <b>Add Reference</b>.</li>
<li>Click the <b>.NET</b> tab.</li>
<li>Select <b>System.Web.Services</b></li>
<li>Click the <b>OK</b> button to add the reference to your project.</li>
</ol>
<p>You may now use SoftLayer's API objects as local objects in your project.</p>
<h2 id="Making_API_Calls">Making API Calls</h2>
<h3 id="Creating_Service_Objects">Creating Service Objects</h3>
<p>Every API service in your project has an associated service class that is responsible for making API calls. Service classes are named according the API service you wish to call. For instance, the class name for the <i>SoftLayer_Account</i> API service is <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_AccountService</code></span> and the service class name for the <i>SoftLayer_Hardware_Serverservice</i> is <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Hardware_ServerService</code></span>. Service objects have properties corresponding to API features such as authentication, initialization parameters, object masks, and result limits.  API method calls are also made directly against these objects.</p>
<div class="geshifilter">
<pre class="vbnet geshifilter-vbnet" style="font-family:monospace;"><span style="color: #0600FF;">Dim</span> accountService <span style="color: #FF8000;">As</span> SoftLayer_AccountService <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_AccountService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span></pre></div>
<h3 id="Binding_Authentication">Binding Authentication</h3>
<p>Authenticate your API calls with your API username and key by defining an <span class="geshifilter"><code class="text geshifilter-text">authenticate</code></span> object. Set your authentication object's <span class="geshifilter"><code class="text geshifilter-text">username</code></span> and <span class="geshifilter"><code class="text geshifilter-text">apiKey</code></span> properties to your API username and key.  Bind the authenticate object to your API service object by setting its <span class="geshifilter"><code class="text geshifilter-text">authenticateValue</code></span> property to your authentication object.</p>
<div class="geshifilter">
<pre class="vbnet geshifilter-vbnet" style="font-family:monospace;"><span style="color: #0600FF;">Dim</span> username <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"set me"</span>
<span style="color: #0600FF;">Dim</span> apiKey <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"set me"</span>
&nbsp;
<span style="color: #0600FF;">Dim</span> authenticate <span style="color: #FF8000;">As</span> authenticate <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey
&nbsp;
accountService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate</pre></div>
<h3 id="Setting_Initialization_Parameters">Setting Initialization Parameters</h3>
<p>API call initialization (init) parameters also have classes defined that correspond to the API service you are calling. Init parameter classes are named according to the API service you are calling. For instance, the init parameter class name for the <i>SoftLayer_Account</i> service is <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_AccountInitParameters</code></span> and the init parameter class name for the <i>SoftLayer_Hardware_Server</i> service is <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Hardware_ServerInitParameters</code></span>. Init parameter objects each have a single integer type id property corresponding to the id number of the SoftLayer object you wish to query. Bind your init parameter object to your service object by setting it to your service object's <ServiceName><span class="geshifilter"><code class="text geshifilter-text">InitParameterValue</code></span> property, where <ServiceName> corresponds to the API service you're calling.<br />
If an API call doesn't correspond to a specific SoftLayer object, you do not need to bind an initialization parameter value to your service object.</servicename></servicename></p>
<div class="geshifilter">
<pre class="vbnet geshifilter-vbnet" style="font-family:monospace;"><span style="color: #0600FF;">Dim</span> serverId <span style="color: #FF8000;">As</span> <span style="color: #FF0000;">Integer</span> <span style="color: #008000;">=</span> <span style="color: #FF0000;">1234</span>
&nbsp;
<span style="color: #0600FF;">Dim</span> hardwareServerInitParameters <span style="color: #FF8000;">As</span> SoftLayer_Hardware_ServerInitParameters <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_Hardware_ServerInitParameters<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
hardwareServerInitParameters.<span style="color: #0000FF;">id</span> <span style="color: #008000;">=</span> serverId
hardwareServerService.<span style="color: #0000FF;">SoftLayer_Hardware_ServerInitParametersValue</span> <span style="color: #008000;">=</span> hardwareServerInitParameters</pre></div>
<h3 id="Making_the_API_Call">Making the API Call</h3>
<p>Once your service object is ready, place your API method call directly against your service object.  The example below outlines making the API call.</p>
<div class="geshifilter">
<pre class="vbnet geshifilter-vbnet" style="font-family:monospace;"><span style="color: #0600FF;">Dim</span> username <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"set me"</span>
<span style="color: #0600FF;">Dim</span> apiKey <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"set me"</span>
&nbsp;
<span style="color: #0600FF;">Dim</span> authenticate <span style="color: #FF8000;">As</span> authenticate <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey
&nbsp;
<span style="color: #008080; font-style: italic;">' Initialize the SoftLayer_Account API service.</span>
<span style="color: #0600FF;">Dim</span> accountService <span style="color: #FF8000;">As</span> SoftLayer_AccountService <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_AccountService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
accountService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate
&nbsp;
<span style="color: #0600FF;">Dim</span> account <span style="color: #FF8000;">as</span> SoftLayer_Account <span style="color: #008000;">=</span> accountService.<span style="color: #0000FF;">getObject</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
&nbsp;
&nbsp;
<span style="color: #008080; font-style: italic;">' Work directly with the SoftLayer_Hardware_Server record with the </span>
<span style="color: #008080; font-style: italic;">' hardware id 1234.</span>
<span style="color: #0600FF;">Dim</span> serverId <span style="color: #FF8000;">As</span> <span style="color: #FF0000;">Integer</span> <span style="color: #008000;">=</span> <span style="color: #FF0000;">1234</span>
&nbsp;
<span style="color: #0600FF;">Dim</span> hardwareServerService <span style="color: #FF8000;">As</span> SoftLayer_Hardware_ServerService <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_Hardware_ServerService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
hardwareServerService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate
&nbsp;
<span style="color: #0600FF;">Dim</span> hardwareServerInitParameters <span style="color: #FF8000;">As</span> SoftLayer_Hardware_ServerInitParameters <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_Hardware_ServerInitParameters<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
hardwareServerInitParameters.<span style="color: #0000FF;">id</span> <span style="color: #008000;">=</span> serverId
hardwareServerService.<span style="color: #0000FF;">SoftLayer_Hardware_ServerInitParametersValue</span> <span style="color: #008000;">=</span> hardwareServerInitParameters
&nbsp;
<span style="color: #0600FF;">Dim</span> server <span style="color: #FF8000;">as</span> SoftLayer_Hardware_Server <span style="color: #008000;">=</span> hardwareServerService.<span style="color: #0000FF;">getObject</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span></pre></div>
<p>Code imported into your project defines classes for every data type defined in the SoftLayer API. Instantiate new data type objects as necessary as call parameters or call results.</p>
<div class="geshifilter">
<pre class="vbnet geshifilter-vbnet" style="font-family:monospace;"><span style="color: #0600FF;">Dim</span> username <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"set me"</span>
<span style="color: #0600FF;">Dim</span> apiKey <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"set me"</span>
<span style="color: #0600FF;">Dim</span> domainId <span style="color: #FF8000;">As</span> <span style="color: #FF0000;">Integer</span> <span style="color: #008000;">=</span> <span style="color: #FF0000;">1234</span>
&nbsp;
<span style="color: #0600FF;">Dim</span> authenticate <span style="color: #FF8000;">As</span> authenticate <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey
&nbsp;
<span style="color: #0600FF;">Dim</span> domainService <span style="color: #FF8000;">As</span> SoftLayer_Dns_DomainService <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_Dns_DomainService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
domainService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate
&nbsp;
<span style="color: #0600FF;">Dim</span> domainInitParameters <span style="color: #FF8000;">As</span> SoftLayer_Dns_DomainInitParameters <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_Dns_DomainInitParameters<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
domainInitParameters.<span style="color: #0000FF;">id</span> <span style="color: #008000;">=</span> domainId
domainService.<span style="color: #0000FF;">SoftLayer_Dns_DomainInitParametersValue</span> <span style="color: #008000;">=</span> domainInitParameters
&nbsp;
<span style="color: #008080; font-style: italic;">' Create a new A record in a domain.</span>
<span style="color: #0600FF;">Dim</span> newRecord <span style="color: #FF8000;">As</span> SoftLayer_Dns_Domain_ResourceRecord_AType <span style="color: #008000;">=</span> domainService.<span style="color: #0000FF;">createARecord</span><span style="color: #000000;">&#40;</span><span style="color: #808080;">"myhost"</span>, <span style="color: #808080;">"127.0.0.1"</span>, <span style="color: #FF0000;">86400</span><span style="color: #000000;">&#41;</span>
Console.<span style="color: #0000FF;">WriteLine</span><span style="color: #000000;">&#40;</span><span style="color: #808080;">"New A record id: "</span> <span style="color: #008000;">+</span> newRecord.<span style="color: #0000FF;">id</span>.<span style="color: #0000FF;">toString</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#41;</span>
&nbsp;
&nbsp;
<span style="color: #008080; font-style: italic;">' Create a new domain record.</span>
<span style="color: #008080; font-style: italic;">'</span>
<span style="color: #008080; font-style: italic;">' This requires a null init parameter and a single SoftLayer_Dns_Domain</span>
<span style="color: #008080; font-style: italic;">' object defined.</span>
domainService.<span style="color: #0000FF;">SoftLayer_Dns_DomainInitParametersValue</span> <span style="color: #008000;">=</span> <span style="color: #FF8000;">Nothing</span>
&nbsp;
<span style="color: #0600FF;">Dim</span> domain <span style="color: #FF8000;">As</span> SoftLayer_Dns_Domain <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_Dns_Domain<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
<span style="color: #0600FF;">Dim</span> domainResourceRecords <span style="color: #FF8000;">As</span> SoftLayer_Dns_Domain_ResourceRecord_AType<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span> <span style="color: #008000;">=</span> <span style="color: #000000;">&#123;</span><span style="color: #FF8000;">New</span> SoftLayer_Dns_Domain_ResourceRecord_AType<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#125;</span>
domainResourceRecords<span style="color: #000000;">&#40;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#41;</span>.<span style="color: #0000FF;">host</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"@"</span>
domainResourceRecords<span style="color: #000000;">&#40;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#41;</span>.<span style="color: #0000FF;">data</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"127.0.0.1"</span>
domainResourceRecords<span style="color: #000000;">&#40;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#41;</span>.<span style="color: #0000FF;">type</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"a"</span>
domain.<span style="color: #0000FF;">name</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"example.org"</span>
domain.<span style="color: #0000FF;">resourceRecords</span> <span style="color: #008000;">=</span> domainResourceRecords
&nbsp;
<span style="color: #0600FF;">Dim</span> newDomain <span style="color: #FF8000;">As</span> SoftLayer_Dns_Domain <span style="color: #008000;">=</span> domainService.<span style="color: #0600FF;">createObject</span><span style="color: #000000;">&#40;</span>domain<span style="color: #000000;">&#41;</span>
Console.<span style="color: #0000FF;">WriteLine</span><span style="color: #000000;">&#40;</span><span style="color: #808080;">"New A record id: "</span> <span style="color: #008000;">+</span> newDomain.<span style="color: #0000FF;">id</span>.<span style="color: #0000FF;">toString</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#41;</span></pre></div>
<h2 id="Using_Object_Masks">Using Object Masks</h2>
<p>Bind an <a href="/article/Object mask">Object mask</a> to your API calls by first declaring an object mask object. Object mask class names correspond to the API service you're using, beginning with the name of your API service followed by "ObjectMask". For instance, an object mask for the <i>SoftLayer_Account</i> API service has the class name <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_AccountObjectMask</code></span> and the <i>SoftLayer_Hardware_Server</i> service's corresponding object mask class name is <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Hardware_ServerObjectMask</code></span>.</p>
<p>Every object mask class has a <span class="geshifilter"><code class="text geshifilter-text">mask</code></span> property that models the relational data you wish to retrieve. The <span class="geshifilter"><code class="text geshifilter-text">mask</code></span> property is on object of the data type represented by your API service. For instance, <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_AccountObjectMask.mask</code></span> is a <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Account</code></span> object and <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Hardware_ServerObjectMask.mask</code></span> is a <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Hardware_Server</code></span> object. Instantiate the relational properties you wish to retrieve in your object mask's mask property as new objects representing the data type of these properties. If your relational property is an array type then declare a one-item array containing a single objet representing the data type of the relational property you wish to retrieve.</p>
<p>Your API service object has a property corresponding to an optional object mask value. Object mask value property names correspond to the name of the API service you're using, beginning ith the name of your API service followed by "ObjectMaskValue". Bind your new object mask object to your service object by assigning it to your service object's <span class="geshifilter"><code class="text geshifilter-text">ObjectMaskValue</code></span> property. For instance, bind an object mask to a <i>SoftLayer_Account</i> service object by assigning its <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_AccountObjectMaskValueproperty</code></span> to your object mask object.</p>
<p>This example retrieves an account's physical hardware records along with that hardware's operating system record, operating system passwords, network components, the datacenter the hardware is located in, and the number of processors in each hardware:</p>
<div class="geshifilter">
<pre class="vbnet geshifilter-vbnet" style="font-family:monospace;"><span style="color: #0600FF;">Dim</span> username <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"set me"</span>
<span style="color: #0600FF;">Dim</span> apiKey <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"set me"</span>
&nbsp;
<span style="color: #0600FF;">Dim</span> authenticate <span style="color: #FF8000;">As</span> authenticate <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey
&nbsp;
<span style="color: #0600FF;">Dim</span> accountService <span style="color: #FF8000;">As</span> SoftLayer_AccountService <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_AccountService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
accountService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate
&nbsp;
<span style="color: #008080; font-style: italic;">' Retrieve items related to hardware.</span>
<span style="color: #008080; font-style: italic;">'</span>
<span style="color: #008080; font-style: italic;">' Operating system, operating system passwords, all network components, the</span>
<span style="color: #008080; font-style: italic;">' datacenter the server is located in, and the number of processors in each </span>
<span style="color: #008080; font-style: italic;">' server.</span>
<span style="color: #0600FF;">Dim</span> objectMask <span style="color: #FF8000;">As</span> SoftLayer_AccountObjectMask <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_AccountObjectMask<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
objectMask.<span style="color: #0000FF;">mask</span> <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_Account
&nbsp;
<span style="color: #0600FF;">Dim</span> objectMaskHardware <span style="color: #FF8000;">As</span> SoftLayer_Hardware_Server<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span> <span style="color: #008000;">=</span> <span style="color: #000000;">&#123;</span><span style="color: #FF8000;">New</span> SoftLayer_Hardware_Server<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#125;</span>
<span style="color: #0600FF;">Dim</span> objectMaskHardwareNetworkComponents <span style="color: #FF8000;">As</span> SoftLayer_Network_Component<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span> <span style="color: #008000;">=</span> <span style="color: #000000;">&#123;</span><span style="color: #FF8000;">New</span> SoftLayer_Network_Component<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#125;</span>
<span style="color: #0600FF;">Dim</span> objectMaskHardwareOperatingSystemPasswords <span style="color: #FF8000;">As</span> SoftLayer_Software_Component_Password<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span> <span style="color: #008000;">=</span> <span style="color: #000000;">&#123;</span><span style="color: #FF8000;">New</span> SoftLayer_Software_Component_Password<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#125;</span>
objectMaskHardware<span style="color: #000000;">&#40;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#41;</span>.<span style="color: #0000FF;">operatingSystem</span> <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_Software_Component_OperatingSystem<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
objectMaskHardware<span style="color: #000000;">&#40;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#41;</span>.<span style="color: #0000FF;">operatingSystem</span>.<span style="color: #0000FF;">passwords</span> <span style="color: #008000;">=</span> objectMaskHardwareOperatingSystemPasswords
objectMaskHardware<span style="color: #000000;">&#40;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#41;</span>.<span style="color: #0000FF;">networkComponents</span> <span style="color: #008000;">=</span> objectMaskHardwareNetworkComponents
objectMaskHardware<span style="color: #000000;">&#40;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#41;</span>.<span style="color: #0000FF;">datacenter</span> <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_Location_Datacenter<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
objectMaskHardware<span style="color: #000000;">&#40;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#41;</span>.<span style="color: #0000FF;">processorCount</span> <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> UInteger
objectMaskHardware<span style="color: #000000;">&#40;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#41;</span>.<span style="color: #0000FF;">processorCountSpecified</span> <span style="color: #008000;">=</span> <span style="color: #0600FF;">True</span>
&nbsp;
objectMask.<span style="color: #0000FF;">mask</span>.<span style="color: #0000FF;">hardware</span> <span style="color: #008000;">=</span> objectMaskHardware
accountService.<span style="color: #0000FF;">SoftLayer_AccountObjectMaskValue</span> <span style="color: #008000;">=</span> objectMask
&nbsp;
<span style="color: #0600FF;">Dim</span> hardware <span style="color: #FF8000;">As</span> SoftLayer_Hardware_Server<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span> <span style="color: #008000;">=</span> accountService.<span style="color: #0000FF;">getHardware</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span></pre></div>
<h2 id="Using_Result_Limits">Using Result Limits</h2>
<p>When calling data, especially queries that involve pulling snippets of information from larger groups, utilizing result limits will greatly decrease your wait time for the return.</p>
<p>Limit the number of results in your API call by creating a new resultLimit object and binding it to your API service object. ResultLimit has two properties:</p>
<ul>
<li><span class="geshifilter"><code class="text geshifilter-text">limit</code></span>: The number of results to limit your call.</li>
<li><span class="geshifilter"><code class="text geshifilter-text">offset</code></span>: An optional offset to begin your result set.</li>
</ul>
<p>Bind your new result limit to your API service object by setting your service object's <span class="geshifilter"><code class="text geshifilter-text">resultLimitValue</code></span> property to your result limit object.</p>
<div class="geshifilter">
<pre class="vbnet geshifilter-vbnet" style="font-family:monospace;"><span style="color: #0600FF;">Dim</span> username <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"set me"</span>
<span style="color: #0600FF;">Dim</span> apiKey <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"set me"</span>
&nbsp;
<span style="color: #0600FF;">Dim</span> authenticate <span style="color: #FF8000;">As</span> authenticate <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey
&nbsp;
<span style="color: #0600FF;">Dim</span> accountService <span style="color: #FF8000;">As</span> SoftLayer_AccountService <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_AccountService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
accountService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate
&nbsp;
<span style="color: #008080; font-style: italic;">' Retrieve our first two open support tickets</span>
<span style="color: #0600FF;">Dim</span> resultLimit <span style="color: #FF8000;">As</span> resultLimit <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> resultLimit<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
resultLimit.<span style="color: #0000FF;">limit</span> <span style="color: #008000;">=</span> <span style="color: #FF0000;">2</span>
resultLimit.<span style="color: #0000FF;">offset</span> <span style="color: #008000;">=</span> <span style="color: #FF0000;">0</span>
&nbsp;
accountService.<span style="color: #0000FF;">resultLimitValue</span> <span style="color: #008000;">=</span> resultLimit
&nbsp;
<span style="color: #0600FF;">Dim</span> tickets <span style="color: #FF8000;">As</span> SoftLayer_Ticket<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span> <span style="color: #008000;">=</span> accountService.<span style="color: #0000FF;">getOpenTickets</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span></pre></div>
<h2 id="Error_Handling">Error Handling</h2>
<p>SoftLayer API call errors are sent to .NET's SOAP handler as <a href="/article/exceptions">exceptions</a>. Place calls to the SoftLayer in Try/Catch blocks to ensure proper handling.</p>
<div class="geshifilter">
<pre class="vbnet geshifilter-vbnet" style="font-family:monospace;"><span style="color: #0600FF;">Dim</span> username <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"set me"</span>
<span style="color: #0600FF;">Dim</span> apiKey <span style="color: #FF8000;">As</span> <span style="color: #FF8000;">String</span> <span style="color: #008000;">=</span> <span style="color: #808080;">"an incorrect key"</span>
&nbsp;
<span style="color: #0600FF;">Dim</span> authenticate <span style="color: #FF8000;">As</span> authenticate <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey
&nbsp;
<span style="color: #0600FF;">Dim</span> accountService <span style="color: #FF8000;">As</span> SoftLayer_AccountService <span style="color: #008000;">=</span> <span style="color: #FF8000;">New</span> SoftLayer_AccountService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
accountService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate
&nbsp;
<span style="color: #008080; font-style: italic;">' Exit the script with the message:</span>
<span style="color: #008080; font-style: italic;">' "Unable to retrieve account information: Invalid API key"</span>
<span style="color: #0600FF;">Try</span>
    <span style="color: #0600FF;">Dim</span> account <span style="color: #FF8000;">As</span> SoftLayer_Account <span style="color: #008000;">=</span> accountService.<span style="color: #0000FF;">getObject</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
<span style="color: #0600FF;">Catch</span> ex <span style="color: #FF8000;">As</span> Exception
    Console.<span style="color: #0000FF;">WriteLine</span><span style="color: #000000;">&#40;</span><span style="color: #808080;">"Unable to retrieve account information: "</span> <span style="color: #008000;">+</span> ex.<span style="color: #0000FF;">Message</span><span style="color: #000000;">&#41;</span>
<span style="color: #0600FF;">End</span> <span style="color: #0600FF;">Try</span></pre></div>
<h2 id="Caveats">Caveats</h2>
<p>Working with the SoftLayer API's generated code in Visual Studio may require one or two extra steps when creating or using SoftLayer API objects.  These steps include setting “specified” properties and handling changes in API services.</p>
<h3 id="Setting_Specified_Properties">Setting "Specified" Properties</h3>
<p>Some object types in generated code have a "specified" property along with the object's property. If you're explicitly setting these properties, you must set their corresponding specified property to True. Use Visual Studio's IntelliSense to determine which properties have associated specified properties.</p>
<h3 id="What_to_do_When_API_Services_Change">What to do When API Services Change</h3>
<p>SoftLayer updates API WSDLs when new products and services are released. Re-consume these WSDLs in order to use these new features.<br />
If the SoftLayer API is imported as a web reference in your project then right click on your web reference's name in Visual Studio's Solution Explorer and select "Update Web Reference". Visual Studio will take a few moments to re-import the web service, then the latest SoftLayer offerings will be available in your project.<br />
If you used <span class="geshifilter"><code class="text geshifilter-text">wsdl.exe</code></span> to generate code files from SoftLayer's API WSDLs then re-run your full <span class="geshifilter"><code class="text geshifilter-text">wsdl.exe</code></span> command to re-import SoftLayer's latest API WSDLs into your project.</p>
<h2 id="Referenced_API_Components">Referenced API Components</h2>
<h3 id="Services">Services</h3>
<ul>
<li><a href="/reference/services/SoftLayer_Account/">SoftLayer_Account</a></li>
<li><a href="/reference/services/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a></li>
<li><a href="/reference/services/SoftLayer_Hardware_Server/">SoftLayer_Hardware_Server</a></li>
</ul>
<h3 id="Data_Types">Data Types</h3>
<ul>
<li><a href="/reference/services/SoftLayer_Hardware_Server/">SoftLayer_Hardware_Server</a></li>
</ul>
<h3 id="Methods">Methods</h3>
<ul>
<li><a href="/reference/services/SoftLayer_Account/getObject">SoftLayer_Account::getObject</a></li>
<li><a href="/reference/services/SoftLayer_Account/getHardware">SoftLayer_Account::getHardware</a></li>
<li><a href="/reference/services/SoftLayer_Account/getOpenTickets">SoftLayer_Account::getOpenTickets</a></li>
<li><a href="/reference/services/SoftLayer_Dns_Domain/createARecord">SoftLayer_Dns_Domain::createARecord</a></li>
</ul>
<h2 id="External_Links">External Links</h2>
<ul>
<li><a href="http://en.wikipedia.org/wiki/IntelliSense">IntelliSense Wikipedia Article</a></li>
<li><a href="http://msdn.microsoft.com/en-us/vbasic/">Visual Basic Developer Center</a></li>
<li><a href="http://msdn.microsoft.com/en-us/library/7h3ystb6(VS.80).aspxhttp://msdn.microsoft.com/en-us/library/7h3ystb6(VS.80).aspx">Web Services Definition Language Tool (Wsdl.exe)</a></li>
</ul>