---
title: "Date Handling in the SoftLayer API"
description: "Working with datatypes from the SoftLayer API"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
---


<script type="text/javascript">toc_collapse=0;</script><div class="toc" id="toc6">
<div class="toc-title">Table of contents<span class="toc-toggle-message">&nbsp;</span></div>
<div class="toc-list">
<ol>
<li class="toc-level-1"><a href="#The_dateTime_Datatype">The dateTime Datatype</a></li>
<li class="toc-level-1"><a href="#Setting_Your_Time_Zone">Setting Your Time Zone</a>
<ol>
<li class="toc-level-2"><a href="#Portal">Portal</a></li>
<li class="toc-level-2"><a href="#API">API</a></li>
</ol>
</li>
<li class="toc-level-1"><a href="#See_Also">See Also</a></li>
<li class="toc-level-1"><a href="#External_Links">External Links</a></li>
</ol>
</div>
</div>
Most of the data presented in the SoftLayer API is date-sensitive. Servers have provision dates, tickets have modify dates, and nearly everything has a creation date. To maintain compliancy and consistency standards for all of our users worldwide, SoftLayer presents its dates in [http://www.iso.org/iso/date_and_time_format ISO 8601] format under the data type ''dateTime''. ISO 8601 represents a complete date including date, time and time zone. Every data type property in the SoftLayer API that ends with the string "Date" is represented by the ''dateTime'' format.

##The dateTime Datatype
The ''dateTime'' data type uses the following format:
    <code><YYYY>-<MM>-<DD>T<HH>:<MM>:<SS>-<TZ></code>

For example the ''dateTime'' value ''2007-07-19T15:21:48-05:00'' translates to:
<code>July 19, 2007, 3:21:48 P.M., GMT -0500</code>

Refer to the information below for more information regarding the data represented in the dateTime data type:
<ul>
<li>'''YYYY''':  A four digit representation of the year</li>
<li>'''MM''':  A two digit representation of the month, including a leading zero, if applicable.  (Acceptable range of 01 to 12)
<br>'''Example:''' February = 02
<br></li>
<li>'''DD''':  A two digit representation of the day, including a leading zero, if applicable.  (Acceptable range of 01 to 31)</li>
<li>'''HH''':  A two digit representation of the hour in 24-hour format, including a leading zero, if applicable.  (Acceptable range of 00 to 23)
<br>'''Examples:'''
<ul>
<li>1:00 a.m. = 01</li>
<li>1:00 p.m. = 13
<br></li>
</ul></li>
<li>'''MM''':  A two digit representation of the minute, including a leading zero, if applicable.  (Acceptable range of 00-59)</li>
<li>'''SS''':  A two digit representation of the second, including a leading zero, if applicable.  (Acceptable range of 00-59)</li>
<li>'''TZ''':  The time zone, represented as the different between the current time zone and GMT in HH:MM format.
<br>'''Example:''' -05:00 = GMT-0500</li>
</ul>



##Setting Your Time Zone
If your API calls return incorrect times for your location, you likely need to set (or reset) the time zone and/or Daylight Savings Time options for the user making API calls.  A user's time zone and Daylight Savings Time options can be reset through the '''SoftLayer Customer Portal''' or using a direct API call.

###Portal
Follow the steps below to set your user's time zone via the '''SoftLayer Customer Portal'''
<ol>
<li>Access the [http://manage.softlayer.com SoftLayer Customer Portal]</li>
<li>Enter your username in the '''User name''' field</li>
<li>Enter your password in the '''Password''' field</li>
<li>Click the '''Administrative''' link</li>
<li>Click on your username in the '''User List'''</li>
<li>Select the desired time zone from the '''Time Zone''' drop down list</li>
<li>Determine if '''Daylight Savings Time''' should be active for the user
    '''Note:''' The system defaults to active Daylight Savings Time return<br>
<ul>
<li>If Daylight Savings Time should be '''active''' for the user click the '''Yes''' radio button under the '''Daylight Savings Time''' option</li>
<li>If Daylight Savings Time should be '''inactive''' for the user click the '''No''' radio button under the '''Daylight Savings Time''' option
<br></li>
</ul></li>
<li>Click the '''Edit User Profile''' button</li>
</ol>
###API
To set your user's time zone using a direct API call, complete the following steps:
<ol>
<li>Invoke the editObject method in the SoftLayer_User_Customer service</li>
<li>Set the ''timeZoneId'' property in the template object passed to the call
    '''Note:''' Retrieve a list of time zones from [[SoftLayer_Locale_Timezone::getAllObjects]]</li>
<li>Determine if '''Daylight Savings Time''' should be active for the user
    '''Note:''' The system defaults to an active Daylight Savings Time return
<ul>
<li>If Daylight Savings Time should be '''active''' for the user enter '''1''' under the '''daylightSavingsTimeFlag''' property</li>
<li>If Daylight Savings Time should be '''inactive''' for the user enter '''0''' under the '''daylightSavingsTimeFlag''' property</li>
</ul>
</li></ol>

##See Also
[[SoftLayer_Locale_Timezone]]
[[SoftLayer_Hardware_Server::getObject]]

##External Links
[http://www.iso.org/iso/date_and_time_format ISO 8601] at [http://wikipedia.org Wikipedia]