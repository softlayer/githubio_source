---
title: "C Sharp"
description: "C Sharp"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
---


<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc5">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#Consuming_SOAP_WSDLs">Consuming SOAP WSDLs</a>
<ol>
<li class="toc-level-2"><a href="#Creating_Web_References">Creating Web References</a></li>
<li class="toc-level-2"><a href="#Using_wsdl.exe">Using wsdl.exe</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#Making_API_Calls">Making API Calls</a>
<ol>
<li class="toc-level-2"><a href="#Creating_Service_Objects">Creating Service Objects</a></li>
<li class="toc-level-2"><a href="#Binding_Authentication">Binding Authentication</a></li>
<li class="toc-level-2"><a href="#Setting_Initialization_Parameters">Setting Initialization Parameters</a></li>
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
<p>There are two ways to import SoftLayer's API WSDLs into your project. Visual Studio can consume a SOAP service into a web reference accessible by your project. Visual Studio also comes with a utility called <a href="http://msdn.microsoft.com/en-us/library/7h3ystb6(VS.80).aspx">wsdl.exe</a> that is executed from a command prompt to read one or more WSDL files and directly convert them into source code that you can add to your project. Web services are typically easier to use in Visual Studio, but can become cumbersome if your project uses many SoftLayer API services.  Wsdl.exe is useful if your project requires many API services.</p>
<p>The code samples in this article reflect code generated from SoftLayer API services by wsdl.exe.</p>
<h3 id="Creating_Web_References">Creating Web References</h3>
<p>Creating web references is the first task required when consuming SOAP WSDLs.  Follow the steps below to create a Web Reference in Visual Studio.</p>
<ol>
<li>Click the Project menu in Visual Studio</li>
<li>Select <b>Add Service Reference</b> from the <b>Project menu dropdown box</b></li>
<li>Click the <b>Advanced</b> button in the <b>Add Service Reference</b> Window<br />
<br /><b>Note:</b> The <b>Service Reference Settings</b> window will appear<br />
<br /></li>
<li>Click the <b>Add Web Reference</b> button in the <b>Service Reference Settings</b> window</li>
<li>Enter the <b>URL to the WSDL</b> of the SoftLayer API service you wish to use in the <b>URL</b> field</li>
<li>Click the green arrow to the right of the <b>URL</b> field<br />
<br />'''Note: Visual Studio will download the WSDL file and analyze the methods and data types it contains.<br />
<br /></li>
<li>Enter a name of your new web reference in the <b>Web reference name</b> field<br />
'''Note: Any references to the API service added to the project will be referenced by the project</li>
<li>Click the <b>Add Reference</b> button to import your new web service<br />
<br /><b>Note:</b> You will now be returned to your project and your new API service will be visible in Visual Studio's <b>Solution Explorer</b><br />
<br /></li>
</ol>
<p>This example creates a service reference called "com.softlayer.api", but you may create web services with any name you prefer. Your web references name is a namespace in your project. Utilize the <span class="geshifilter"><code class="text geshifilter-text">using</code></span> statement at the beginning of your program so you won't have to type the name of your web reference with every API-related statement you use. For instance, use the statement:</p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #0600FF;">using</span> <span style="color: #008080;">projectName.com.softlayer.api</span><span style="color: #008000;">;</span></pre></div>
<p>Replace "projectName" with the name of your Visual Studio project, to set your web reference as a default namespace.</p>
<h3 id="Using_wsdl.exe">Using wsdl.exe</h3>
<p>Wsdl.exe is located in C:\Program Files\Microsoft SDKs\Windows\v7.0A\bin&#46; Execute Wsdl.exe with the following switches to convert SoftLayer's API WSDLs into C# code:</p>
<ul>
<li><span class="geshifilter"><code class="text geshifilter-text">/language:CS</code></span> - Tells wsdl.exe to export C# code.</li>
<li><span class="geshifilter"><code class="text geshifilter-text">/sharetypes</code></span> - SoftLayer's WSDL files share a number of similar data types. The /sharetypes switch compiles these data types into single class files, making for a smaller source footprint and more efficiency when working in Visual Studio.</li>
<li><span class="geshifilter"><code class="text geshifilter-text">/out:C:\path\to\project\SoftLayer_API.cs</code></span> - Exports generated code to a path within your project hierarchy. In this case we'll save code to the fileSoftLayer_API.cs.</li>
</ul>
<p>End the command with a space- separated list of the URLs of the API WSDLS you wish to import.  You can import as many WSDL files as you like.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">wsdl.exe /language:CS /out:"C:\Path\to\Project\SoftLayer_API.cs" /sharetypes 
https://api.softlayer.com/soap/v3/SoftLayer_Account?wsdl 
https://api.softlayer.com/soap/v3/SoftLayer_Hardware_Server?wsdl 
https://api.softlayer.com/soap/v3/SoftLayer_Dns_Domain?wsdl</pre></div>
<p>Note:  To make private API calls, replace <span class="geshifilter"><code class="text geshifilter-text">https://api.softlayer.com</code></span> with <span class="geshifilter"><code class="text geshifilter-text">http://api.service.softlayer.com</code></span>.  Refer to our <a href="/article/Getting Started">Getting Started</a> article for more information on making private API calls.</p>
<p>Re-run this command if you wish to import more API services into your project.</p>
<p>Once your code file is created, you must add it to your project.  To add the newly created code file to your project, complete the steps below:</p>
<ol>
<li>Right click the name of your project in the <b>Visual Studio Solution Explorer</b></li>
<li>Scroll over the <b>Add</b> option in the expanded menu</li>
<li>Click the <b>Existing Item</b> button in the <b>Add</b> menu</li>
<li>Locate your generated code file in the <b>Add Existing Item</b> dialog window</li>
<li>Click to highlight your <b>generated code file</b></li>
<li>Click the <b>OK</b> button to continue</li>
</ol>
<p>Finally, your project must include the <span class="geshifilter"><code class="text geshifilter-text">System.Web.Services</code></span> service reference to make SOAP calls from your imported code.</p>
<ol>
<li>Click to expand the <b>Project</b> menu in Visual Studio</li>
<li>Select <b>Add Reference</b></li>
<li>Click the <b>.NET</b> tab</li>
<li>Select <b>System.Web.Services</b></li>
<li>Click the <b>OK</b> button to add the reference to your project</li>
</ol>
<h2 id="Making_API_Calls">Making API Calls</h2>
<h3 id="Creating_Service_Objects">Creating Service Objects</h3>
<p>Every API service in your project has an associated service class that's responsible for making API calls.  Service classes are named according the API service you wish to call. For instance, the class name for the <i>SoftLayer_Account</i> API service is <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_AccountService</code></span> and the service class name for the <i>SoftLayer_Hardware_Server</i> service is <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Hardware_ServerService</code></span>. Service objects have properties corresponding to API features such as authentication, initialization parameters, object masks, and result limits.  API method calls are also made directly against these objects.  For example:<br />
<span class="geshifilter"><code class="csharp geshifilter-csharp">SoftLayer_AccountService accountService <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_AccountService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span></code></span></p>
<h3 id="Binding_Authentication">Binding Authentication</h3>
<p>Authenticate your API calls with your API username and key by defining an <span class="geshifilter"><code class="text geshifilter-text">authenticate</code></span> object. Set your authentication object's <span class="geshifilter"><code class="text geshifilter-text">username</code></span> and <span class="geshifilter"><code class="text geshifilter-text">apiKey</code></span> properties to your API username and key. Bind the authenticate object to your API service object by setting its <span class="geshifilter"><code class="text geshifilter-text">authenticateValue</code></span> property to your authentication object.</p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #FF0000;">String</span> username <span style="color: #008000;">=</span> <span style="color: #666666;">"set me"</span><span style="color: #008000;">;</span>
<span style="color: #FF0000;">String</span> apiKey <span style="color: #008000;">=</span> <span style="color: #666666;">"set me"</span><span style="color: #008000;">;</span>
&nbsp;
authenticate authenticate <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username<span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey<span style="color: #008000;">;</span>
&nbsp;
accountService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate<span style="color: #008000;">;</span></pre></div>
<h3 id="Setting_Initialization_Parameters">Setting Initialization Parameters</h3>
<p>API call initialization (init) parameters also have classes defined that correspond to the API service you are calling.  Init parameter classes are named according to the API service you're calling.  For instance, the init parameter class name for the <i>SoftLayer_Account</i> service is <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_AccountInitParameters</code></span> and the init parameter class name for the <i>SoftLayer_Hardware_Server</i> service is <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Hardware_ServerInitParameters</code></span>. Init parameter objects each have a single integer type <span class="geshifilter"><code class="text geshifilter-text">id</code></span> property corresponding to the id number of the SoftLayer object you wish to query. Bind your init parameter object to your service object by setting it to your service object's <span class="geshifilter"><code class="text geshifilter-text"><ServiceName>InitParameterValue</code></span> property, where <i><ServiceName></servicename></i> corresponds to the API service you're calling.<br />
If an API call doesn't correspond to a specific SoftLayer object then you do not need to bind an initialization parameter value to your service object.  The code snippet below outlines this scenario:</p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #FF0000;">int</span> serverId <span style="color: #008000;">=</span> <span style="color: #FF0000;">1234</span><span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Hardware_ServerInitParameters hardwareServerInitParameters <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Hardware_ServerInitParameters<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
hardwareServerInitParameters.<span style="color: #0000FF;">id</span> <span style="color: #008000;">=</span> serverId<span style="color: #008000;">;</span>
hardwareServerService.<span style="color: #0000FF;">SoftLayer_Hardware_ServerInitParametersValue</span> <span style="color: #008000;">=</span> hardwareServerInitParameters<span style="color: #008000;">;</span></pre></div>
<p>Making the API Call<br />
Once your service object is ready, place your API method call directly against your service object.  Utilize the code below complete this action:</p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #FF0000;">String</span> username <span style="color: #008000;">=</span> <span style="color: #666666;">"set me"</span><span style="color: #008000;">;</span>
<span style="color: #FF0000;">String</span> apiKey <span style="color: #008000;">=</span> <span style="color: #666666;">"set me"</span><span style="color: #008000;">;</span>
&nbsp;
authenticate authenticate <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username<span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey<span style="color: #008000;">;</span>
&nbsp;
<span style="color: #008080; font-style: italic;">// Initialize the SoftLayer_Account API service.</span>
SoftLayer_AccountService accountService <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_AccountService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
accountService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate<span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Account account <span style="color: #008000;">=</span> accountService.<span style="color: #0000FF;">getObject</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
&nbsp;
&nbsp;
<span style="color: #008080; font-style: italic;">// Work directly with the SoftLayer_Hardware_Server record with the </span>
<span style="color: #008080; font-style: italic;">// hardware id 1234.</span>
<span style="color: #FF0000;">int</span> serverId <span style="color: #008000;">=</span> <span style="color: #FF0000;">1234</span><span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Hardware_ServerService hardwareServerService <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Hardware_ServerService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Hardware_ServerInitParameters hardwareServerInitParameters <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Hardware_ServerInitParameters<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
hardwareServerInitParameters.<span style="color: #0000FF;">id</span> <span style="color: #008000;">=</span> serverId<span style="color: #008000;">;</span>
hardwareServerService.<span style="color: #0000FF;">SoftLayer_Hardware_ServerInitParametersValue</span> <span style="color: #008000;">=</span> hardwareServerInitParameters<span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Hardware_Server server <span style="color: #008000;">=</span> hardwareServerService.<span style="color: #0000FF;">getObject</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span></pre></div>
<p>Code imported into your project defines classes for every data type defined in the SoftLayer API. Instantiate new data type objects as necessary as call parameters or call results.</p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #FF0000;">String</span> username <span style="color: #008000;">=</span> <span style="color: #666666;">"set me"</span><span style="color: #008000;">;</span>
<span style="color: #FF0000;">String</span> apiKey <span style="color: #008000;">=</span> <span style="color: #666666;">"set me"</span><span style="color: #008000;">;</span>
<span style="color: #FF0000;">int</span> domainId <span style="color: #008000;">=</span> <span style="color: #FF0000;">1234</span><span style="color: #008000;">;</span>
&nbsp;
authenticate authenticate <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username<span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey<span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Dns_DomainService domainService <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Dns_DomainService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
domainService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate<span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Dns_DomainInitParameters domainInitParameters <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Dns_DomainInitParameters<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
domainInitParameters.<span style="color: #0000FF;">id</span> <span style="color: #008000;">=</span> domainId<span style="color: #008000;">;</span>
domainService.<span style="color: #0000FF;">SoftLayer_Dns_DomainInitParametersValue</span> <span style="color: #008000;">=</span> domainInitParameters<span style="color: #008000;">;</span>
&nbsp;
<span style="color: #008080; font-style: italic;">// Create a new A record in a domain.</span>
SoftLayer_Dns_Domain_ResourceRecord_AType newRecord <span style="color: #008000;">=</span> domainService.<span style="color: #0000FF;">createARecord</span><span style="color: #000000;">&#40;</span><span style="color: #666666;">"myhost"</span>, <span style="color: #666666;">"127.0.0.1"</span>, <span style="color: #FF0000;">86400</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
&nbsp;
Console.<span style="color: #0000FF;">WriteLine</span><span style="color: #000000;">&#40;</span><span style="color: #666666;">"New A record id: "</span> <span style="color: #008000;">+</span> newRecord.<span style="color: #0000FF;">id</span>.<span style="color: #0000FF;">ToString</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
&nbsp;
<span style="color: #008080; font-style: italic;">// Create a new domain record.</span>
<span style="color: #008080; font-style: italic;">//</span>
<span style="color: #008080; font-style: italic;">// This requires a null init parameter and a single SoftLayer_Dns_Domain</span>
<span style="color: #008080; font-style: italic;">// object defined.</span>
domainService.<span style="color: #0000FF;">SoftLayer_Dns_DomainInitParametersValue</span> <span style="color: #008000;">=</span> null<span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Dns_Domain domain <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Dns_Domain<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
SoftLayer_Dns_Domain_ResourceRecord_AType<span style="color: #000000;">&#91;</span><span style="color: #000000;">&#93;</span> domainResourceRecords <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Dns_Domain_ResourceRecord_AType<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">1</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
domainResourceRecords<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#93;</span>.<span style="color: #0000FF;">host</span> <span style="color: #008000;">=</span> <span style="color: #666666;">"@"</span><span style="color: #008000;">;</span>
domainResourceRecords<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#93;</span>.<span style="color: #0000FF;">data</span> <span style="color: #008000;">=</span> <span style="color: #666666;">"127.0.0.1"</span><span style="color: #008000;">;</span>
domainResourceRecords<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#93;</span>.<span style="color: #0000FF;">type</span> <span style="color: #008000;">=</span> <span style="color: #666666;">"a"</span><span style="color: #008000;">;</span>
domain.<span style="color: #0000FF;">name</span> <span style="color: #008000;">=</span> <span style="color: #666666;">"example.org"</span><span style="color: #008000;">;</span>
domain.<span style="color: #0000FF;">resourceRecords</span> <span style="color: #008000;">=</span> domainResourceRecords<span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Dns_Domain newDomain <span style="color: #008000;">=</span> domainService.<span style="color: #0000FF;">createObject</span><span style="color: #000000;">&#40;</span>domain<span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
Console.<span style="color: #0000FF;">WriteLine</span><span style="color: #000000;">&#40;</span><span style="color: #666666;">"New domain id: "</span> <span style="color: #008000;">+</span> newDomain.<span style="color: #0000FF;">id</span>.<span style="color: #0000FF;">ToString</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span></pre></div>
<h2 id="Using_Object_Masks">Using Object Masks</h2>
<p>Bind an <a href="/article/Object mask">Object mask</a> to your API calls by first declaring an object mask object. Object mask class names correspond to the API service you're using, beginning with the name of your API service followed by <span class="geshifilter"><code class="text geshifilter-text">ObjectMask</code></span>. For instance, an object mask for the <i>SoftLayer_Account</i> API service has the class name <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_AccountObjectMask</code></span> and the <i>SoftLayer_Hardware_Server</i> service's corresponding object mask class name is <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Hardware_ServerObjectMask</code></span>.</p>
<p>Every object mask class has a <span class="geshifilter"><code class="text geshifilter-text">mask</code></span> property that models the relational data you wish to retrieve. The <span class="geshifilter"><code class="text geshifilter-text">mask</code></span> property is on object of the data type represented by your API service. For instance, <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_AccountObjectMask.mask</code></span> is a <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Account</code></span> object and <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Hardware_ServerObjectMask.mask</code></span> is a <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Hardware_Server</code></span> object. Instantiate the relational properties you wish to retrieve in your object mask's <span class="geshifilter"><code class="text geshifilter-text">mask</code></span> property as new objects representing the data type of these properties. If your relational property is an array type then declare a one-item array containing a single objet representing the data type of the relational property you wish to retrieve.</p>
<p>Your API service object has a property corresponding to an optional object mask value. Object mask value property names correspond to the name of the API service you're using, beginning with the name of your API service followed by <span class="geshifilter"><code class="text geshifilter-text">ObjectMaskValue</code></span>.  Bind your new object mask object to your service object by assigning it to your service object's <span class="geshifilter"><code class="text geshifilter-text">ObjectMaskValue</code></span> property.  For instance, bind an object mask to a <i>SoftLayer_Account</i> service object by assigning its <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_AccountObjectMaskValue</code></span> property to your object mask object.</p>
<p>This example retrieves an account's physical hardware records along with that hardware's operating system record, operating system passwords, network components, the datacenter the hardware is located in, and the number of processors in each hardware:</p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #FF0000;">String</span> username <span style="color: #008000;">=</span> <span style="color: #666666;">"set me"</span><span style="color: #008000;">;</span>
<span style="color: #FF0000;">String</span> apiKey <span style="color: #008000;">=</span> <span style="color: #666666;">"set me"</span><span style="color: #008000;">;</span>
&nbsp;
authenticate authenticate <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username<span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey<span style="color: #008000;">;</span>
&nbsp;
SoftLayer_AccountService accountService <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_AccountService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
accountService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate<span style="color: #008000;">;</span>
&nbsp;
<span style="color: #008080; font-style: italic;">// Retrieve items related to hardware.</span>
<span style="color: #008080; font-style: italic;">//</span>
<span style="color: #008080; font-style: italic;">// Operating system, operating system passwords, all network components, the</span>
<span style="color: #008080; font-style: italic;">// datacenter the server is located in, and the number of processors in each </span>
<span style="color: #008080; font-style: italic;">// server.</span>
SoftLayer_AccountObjectMask objectMask <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_AccountObjectMask<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
objectMask.<span style="color: #0000FF;">mask</span> <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Account<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Hardware_Server<span style="color: #000000;">&#91;</span><span style="color: #000000;">&#93;</span> objectMaskHardware <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Hardware_Server<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">1</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
SoftLayer_Network_Component<span style="color: #000000;">&#91;</span><span style="color: #000000;">&#93;</span> objectMaskHardwareNetworkComponents <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Network_Component<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">1</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
SoftLayer_Software_Component_Password<span style="color: #000000;">&#91;</span><span style="color: #000000;">&#93;</span> objectMaskHardwareOperatingSystemPasswords <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Software_Component_Password<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">1</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
objectMaskHardware<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#93;</span>.<span style="color: #0000FF;">operatingSystem</span> <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Software_Component_OperatingSystem<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
objectMaskHardware<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#93;</span>.<span style="color: #0000FF;">operatingSystem</span>.<span style="color: #0000FF;">passwords</span> <span style="color: #008000;">=</span> objectMaskHardwareOperatingSystemPasswords<span style="color: #008000;">;</span>
objectMaskHardware<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#93;</span>.<span style="color: #0000FF;">networkComponents</span> <span style="color: #008000;">=</span> objectMaskHardwareNetworkComponents<span style="color: #008000;">;</span>
objectMaskHardware<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#93;</span>.<span style="color: #0000FF;">datacenter</span> <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_Location_Datacenter<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
objectMaskHardware<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#93;</span>.<span style="color: #0000FF;">processorCount</span> <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> <span style="color: #FF0000;">uint</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
objectMaskHardware<span style="color: #000000;">&#91;</span><span style="color: #FF0000;">0</span><span style="color: #000000;">&#93;</span>.<span style="color: #0000FF;">processorCountSpecified</span> <span style="color: #008000;">=</span> true<span style="color: #008000;">;</span>
objectMask.<span style="color: #0000FF;">mask</span>.<span style="color: #0000FF;">hardware</span> <span style="color: #008000;">=</span> objectMaskHardware<span style="color: #008000;">;</span>
accountService.<span style="color: #0000FF;">SoftLayer_AccountObjectMaskValue</span> <span style="color: #008000;">=</span> objectMask<span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Hardware_Server<span style="color: #000000;">&#91;</span><span style="color: #000000;">&#93;</span> hardware <span style="color: #008000;">=</span> <span style="color: #000000;">&#40;</span>SoftLayer_Hardware_Server<span style="color: #000000;">&#91;</span><span style="color: #000000;">&#93;</span><span style="color: #000000;">&#41;</span>accountService.<span style="color: #0000FF;">getHardware</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span></pre></div>
<h2 id="Using_Result_Limits">Using Result Limits</h2>
<p>When calling data, especially queries that involve pulling snippets of information from larger groups, utilizing result limits will greatly decrease your wait time for the return.</p>
<p>Limit the number of results in your API call by creating a new <span class="geshifilter"><code class="text geshifilter-text">resultLimit</code></span> object and binding it to your API service object.  <span class="geshifilter"><code class="text geshifilter-text">ResultLimit</code></span> has two properties:</p>
<ul>
<li><span class="geshifilter"><code class="text geshifilter-text">limit</code></span>: The number of results to limit your call</li>
<li><span class="geshifilter"><code class="text geshifilter-text">offset</code></span>: An optional offset to begin your result set</li>
</ul>
<p>Bind your new result limit to your API service object by setting your service object's <span class="geshifilter"><code class="text geshifilter-text">resultLimitValue</code></span> property to your result limit object.</p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #FF0000;">String</span> username <span style="color: #008000;">=</span> <span style="color: #666666;">"set me"</span><span style="color: #008000;">;</span>
<span style="color: #FF0000;">String</span> apiKey <span style="color: #008000;">=</span> <span style="color: #666666;">"set me"</span><span style="color: #008000;">;</span>
&nbsp;
authenticate authenticate <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username<span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey<span style="color: #008000;">;</span>
&nbsp;
SoftLayer_AccountService accountService <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_AccountService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
accountService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate<span style="color: #008000;">;</span>
&nbsp;
<span style="color: #008080; font-style: italic;">// Retrieve our first two open support tickets</span>
resultLimit resultLimit <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> resultLimit<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
resultLimit.<span style="color: #0000FF;">limit</span> <span style="color: #008000;">=</span> <span style="color: #FF0000;">2</span><span style="color: #008000;">;</span>
resultLimit.<span style="color: #0000FF;">offset</span> <span style="color: #008000;">=</span> <span style="color: #FF0000;">0</span><span style="color: #008000;">;</span>
&nbsp;
accountService.<span style="color: #0000FF;">resultLimitValue</span> <span style="color: #008000;">=</span> resultLimit<span style="color: #008000;">;</span>
&nbsp;
SoftLayer_Ticket<span style="color: #000000;">&#91;</span><span style="color: #000000;">&#93;</span> tickets <span style="color: #008000;">=</span> accountService.<span style="color: #0000FF;">getOpenTickets</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span></pre></div>
<h2 id="Error_Handling">Error Handling</h2>
<p>SoftLayer API call errors are sent to .NET's SOAP handler as <a href="/article/exceptions">exceptions</a>.  Place calls to the SoftLayer in try/catch blocks to ensure proper handling.  For example:</p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #FF0000;">String</span> username <span style="color: #008000;">=</span> <span style="color: #666666;">"set me"</span><span style="color: #008000;">;</span>
<span style="color: #FF0000;">String</span> apiKey <span style="color: #008000;">=</span> <span style="color: #666666;">"an incorrect key"</span><span style="color: #008000;">;</span>
&nbsp;
authenticate authenticate <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> authenticate<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">username</span> <span style="color: #008000;">=</span> username<span style="color: #008000;">;</span>
authenticate.<span style="color: #0000FF;">apiKey</span> <span style="color: #008000;">=</span> apiKey<span style="color: #008000;">;</span>
&nbsp;
SoftLayer_AccountService accountService <span style="color: #008000;">=</span> <a href="http://www.google.com/search?q=new+msdn.microsoft.com"><span style="color: #008000;">new</span></a> SoftLayer_AccountService<span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
accountService.<span style="color: #0000FF;">authenticateValue</span> <span style="color: #008000;">=</span> authenticate<span style="color: #008000;">;</span>
&nbsp;
<span style="color: #008080; font-style: italic;">// Exit the script with the message:</span>
<span style="color: #008080; font-style: italic;">// "Unable to retrieve account information: Invalid API key"</span>
<span style="color: #0600FF;">try</span> 
<span style="color: #000000;">&#123;</span>
    SoftLayer_Account account <span style="color: #008000;">=</span> accountService.<span style="color: #0000FF;">getObject</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
<span style="color: #000000;">&#125;</span>
<span style="color: #0600FF;">catch</span> <span style="color: #000000;">&#40;</span>Exception ex<span style="color: #000000;">&#41;</span>
<span style="color: #000000;">&#123;</span>
    Console.<span style="color: #0000FF;">WriteLine</span><span style="color: #000000;">&#40;</span><span style="color: #666666;">"Unable to retrieve account information: "</span> <span style="color: #008000;">+</span> ex.<span style="color: #0000FF;">Message</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
<span style="color: #000000;">&#125;</span></pre></div>
<h2 id="Caveats">Caveats</h2>
<p>Working with the SoftLayer API's generated code in Visual Studio may require one or two extra steps when creating or using SoftLayer API objects.  These steps include setting “specified” properties and handing changes in API services.</p>
<h3 id="Setting_Specified_Properties">Setting "Specified" Properties</h3>
<p>Some object types in generated code have a "specified" property along with the object's property. If you're explicitly setting these properties, you must set their corresponding specified property to True. Use Visual Studio's <a href="http://en.wikipedia.org/wiki/IntelliSense">IntelliSense</a> to determine which properties have associated specified properties.</p>
<h3 id="What_to_do_When_API_Services_Change">What to do When API Services Change</h3>
<p>SoftLayer updates API WSDLs when new products and services are released. Re-consume these WSDLs in order to use these new features.</p>
<p>If the SoftLayer API is imported as a web reference in your project, right click on your web reference's name in Visual Studio's Solution Explorer and select "Update Web Reference". Visual Studio will take a few moments to re-import the web service.  After complete,  the latest SoftLayer offerings will be available in your project.</p>
<p>If you used <span class="geshifilter"><code class="text geshifilter-text">wsdl.exe</code></span> to generate code files from SoftLayer's API WSDLs, re-run your full <span class="geshifilter"><code class="text geshifilter-text">wsdl.exe</code></span> command to re-import SoftLayer's latest API WSDLs into your project.</p>
<h2 id="Referenced_API_Components">Referenced API Components</h2>
<h3 id="Services">Services</h3>
<ul>
<li><a href="/reference/services/SoftLayer_Account/">SoftLayer_Account</a></li>
<li><a href="/reference/services/SoftLayer_Dns_Domain/">SoftLayer_Dns_Domain</a></li>
<li><a href="/reference/services/SoftLayer_Hardware_Server/">SoftLayer_Hardware_Server</a></li>
</ul>
<h3 id="Data_Types">Data Types</h3>
<ul>
<li><a href="/reference/datatypes/SoftLayer_Hardware_Server/">SoftLayer_Hardware_Server</a></li>
</ul>
<h3 id="Methods">Methods</h3>
<ul>
<li><a href="/reference/services/SoftLayer_Account/getObject">SoftLayer_Account::getObject</a></li>
<li><a href="/reference/services/SoftLayer_Account/getHardware">SoftLayer_Account::getHardware</a></li>
<li><a href="/reference/services/SoftLayer_Account/getOpenTickets">SoftLayer_Account::getOpenTickets</a></li>
</ul>
<h2 id="External_Links">External Links</h2>
<ul>
<li><a href="http://msdn.microsoft.com/en-us/library/hcw1s69b.aspx">IntelliSense (Visual Studio) MSDN Coding Aid</a></li>
</ul>