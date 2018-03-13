---
title: "Getting Started with Tickets"
description: "<p>SoftLayer's ticket system is a primary communication medium for customers to interact with the SoftLayer <a href=htt"
date: "2013-07-09"
author: "waelriac"
tags:
    - "blog"
---

<p>SoftLayer's ticket system is a primary communication medium for customers to interact with the SoftLayer <a href="http://www.softlayer.com/support/">support</a> groups. The <a href="/reference/services/SoftLayer_Ticket/">SoftLayer_Ticket</a> service provides an interaction point for individual tickets, and all tickets on an account can be interfaced through <a href="/reference/services/SoftLayer_Account/">SoftLayer_Account</a>.</p>
<h2>Listing</h2>
<p>A list of all tickets can be gathered from the SoftLayer_Account service with <a href="/reference/services/SoftLayer_Account/getTickets">SoftLayer_Account::getTickets</a>. This method returns an array of <a href="/reference/datatypes/SoftLayer_Ticket/">SoftLayer_Ticket</a> data type objects.</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">import</span> SoftLayer
client <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">Client</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
tickets <span style="color: #66cc66;">=</span> client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Account'</span><span style="color: black;">&#93;</span>.<span style="color: black;">getTickets</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span></pre></div>
<p>Additionally, you can retrieve only open or closed tickets with <a href="/reference/services/SoftLayer_Account/getOpenTickets">SoftLayer_Account::getOpenTickets</a> and <a href="/reference/services/SoftLayer_Account/getClosedTickets">SoftLayer_Account::getClosedTickets</a>.</p>
<h2>Details</h2>
<p>To get information about a specific ticket, such as its ID, last modified date, or status, we can use <a href="/reference/services/SoftLayer_Ticket/getObject">SoftLayer_Ticket::getObject</a> that returns a <a href="/reference/datatypes/SoftLayer_Ticket/">SoftLayer_Ticket</a> object. Object masks can be used to include SoftLayer_Ticket’s relational properties. Below is an example of using <a href="/reference/services/SoftLayer_Ticket/getObject">getObject</a> on the SoftLayer_Ticket service with an object mask that provides the name of the assigned <a href="/reference/datatypes/SoftLayer_User_Customer/">user</a> and all the ticket <a href="/reference/datatypes/SoftLayer_Ticket_Update/">updates</a>.</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">mask <span style="color: #66cc66;">=</span> <span style="color: black;">&#40;</span><span style="color: #483d8b;">'mask[id, title, assignedUser[firstName, lastName],'</span>
                <span style="color: #483d8b;">'createDate,lastEditDate,updates[entry],updateCount]'</span><span style="color: black;">&#41;</span>
<span style="color: #ff7700;font-weight:bold;">return</span> client<span style="color: black;">&#91;</span>‘Ticket’<span style="color: black;">&#93;</span>.<span style="color: black;">getObject</span><span style="color: black;">&#40;</span><span style="color: #008000;">id</span><span style="color: #66cc66;">=</span>ticket_id<span style="color: #66cc66;">,</span> mask<span style="color: #66cc66;">=</span>mask<span style="color: black;">&#41;</span></pre></div>
<h2>Creating</h2>
<h3>Listing Subjects</h3>
<p>When creating a ticket, a valid <a href="/reference/datatypes/SoftLayer_Ticket_Subject/">subject</a> ID is needed. A list of all possible subjects is gathered with <a href="/reference/services/SoftLayer_Ticket_Subject/getAllObjects">SoftLayer_Ticket_Subject::getAllObjects</a>:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">subjects <span style="color: #66cc66;">=</span> client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Ticket_Subject'</span><span style="color: black;">&#93;</span>.<span style="color: black;">getAllObjects</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
ID SUBJECT
<span style="color: #ff4500;">1001</span> <span style="color: #483d8b;">'Accounting Request'</span>
<span style="color: #ff4500;">1002</span> <span style="color: #483d8b;">'Sales Request'</span>
<span style="color: #ff4500;">1003</span> <span style="color: #483d8b;">'Reboots and Console Access'</span>
<span style="color: #ff4500;">1041</span> <span style="color: #483d8b;">'DNS Request'</span>
<span style="color: #ff4500;">1021</span> <span style="color: #483d8b;">'Hardware Issue'</span>
<span style="color: #ff4500;">1022</span> <span style="color: #483d8b;">'Public Network Question'</span>
<span style="color: #ff4500;">1061</span> <span style="color: #483d8b;">'Private Network Question'</span>
<span style="color: #ff4500;">1201</span> <span style="color: #483d8b;">'DOS/Abuse Issue'</span>
<span style="color: #ff4500;">1101</span> <span style="color: #483d8b;">'Security Issue'</span>
<span style="color: #ff4500;">1121</span> <span style="color: #483d8b;">'Hardware Firewall Question'</span>
<span style="color: #ff4500;">1122</span> <span style="color: #483d8b;">'Hardware Load Balancer Question'</span>
<span style="color: #ff4500;">1004</span> <span style="color: #483d8b;">'OS Reload Question'</span>
<span style="color: #ff4500;">1005</span> <span style="color: #483d8b;">'Portal Information Question'</span>
<span style="color: #ff4500;">1081</span> <span style="color: #483d8b;">'Licensing Question'</span>
<span style="color: #ff4500;">1141</span> <span style="color: #483d8b;">'Mail Server Issue'</span>
<span style="color: #ff4500;">1161</span> <span style="color: #483d8b;">'StorageLayer Question'</span>
<span style="color: #ff4500;">1181</span> <span style="color: #483d8b;">'CDNLayer Question'</span>
<span style="color: #ff4500;">1221</span> <span style="color: #483d8b;">'Transcoding Question'</span>
<span style="color: #ff4500;">1261</span> <span style="color: #483d8b;">'Colocation Service Request'</span></pre></div>
<h3>Ticket Submission</h3>
<p>Creating a new ticket is accomplished with the <a href="/reference/services/SoftLayer_Ticket/createStandardTicket">SoftLayer_Ticket::createStandardTicket</a> method. First, a  <a href="/reference/datatypes/SoftLayer_Ticket/">SoftLayer_Ticket</a> template object is created that contains the details of the ticket. Every ticket template object will need, at minimum, the following properties defined:<br />
• subjectId: the ID of the <a href="/reference/datatypes/SoftLayer_Ticket/">subject</a> to be used as title for the ticket<br />
• assignedUserId: An assigned <a href="/reference/datatypes/SoftLayer_User_Customer/">user</a> for the ticket, which is usually set to the ticket creator.<br />
<a href="/reference/services/SoftLayer_Ticket/createStandardTicket">SoftLayer_Ticket::createStandardTicket</a> can be called with the template object and the content for the first ticket message.</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;"><span style="color: #ff7700;font-weight:bold;">import</span> SoftLayer
client <span style="color: #66cc66;">=</span> SoftLayer.<span style="color: black;">Client</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
currentUser <span style="color: #66cc66;">=</span> client<span style="color: black;">&#91;</span>‘Account’<span style="color: black;">&#93;</span>.<span style="color: black;">getCurrentUser</span><span style="color: black;">&#40;</span><span style="color: black;">&#41;</span>
new_ticket <span style="color: #66cc66;">=</span> <span style="color: black;">&#123;</span>
       <span style="color: #483d8b;">'subjectId'</span>: ID<span style="color: #66cc66;">,</span>
       <span style="color: #483d8b;">'assignedUserId'</span>: currentUser<span style="color: black;">&#91;</span><span style="color: #483d8b;">'id'</span><span style="color: black;">&#93;</span>
<span style="color: black;">&#125;</span>
created_ticket <span style="color: #66cc66;">=</span> client<span style="color: black;">&#91;</span>‘Ticket’<span style="color: black;">&#93;</span>.<span style="color: black;">createStandardTicket</span><span style="color: black;">&#40;</span>new_ticket<span style="color: #66cc66;">,</span> “This <span style="color: #ff7700;font-weight:bold;">is</span> the content of the ticket xxxx”<span style="color: black;">&#41;</span></pre></div>
<h2>Updating</h2>
<p>An update to a ticket can be made with <a href="/reference/services/SoftLayer_Ticket/addUpdate">SoftLayer_Ticket::addUpdate</a>. A <a href="/reference/datatypes/SoftLayer_Ticket_Update/">template object</a> must be provided:</p>
<div class="geshifilter">
<pre class="python geshifilter-python" style="font-family:monospace;">ticket_update <span style="color: #66cc66;">=</span> <span style="color: black;">&#123;</span>
                 <span style="color: #483d8b;">'entry'</span>: <span style="color: #483d8b;">"This is a test update, please ignore"</span><span style="color: #66cc66;">,</span>
                 <span style="color: black;">&#125;</span>
tickets <span style="color: #66cc66;">=</span> client<span style="color: black;">&#91;</span><span style="color: #483d8b;">'Ticket'</span><span style="color: black;">&#93;</span>.<span style="color: black;">addUpdate</span><span style="color: black;">&#40;</span>ticket_update<span style="color: #66cc66;">,</span> <span style="color: #008000;">id</span><span style="color: #66cc66;">=</span><span style="color: #ff4500;">8988302</span><span style="color: black;">&#41;</span></pre></div>

