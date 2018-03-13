---
title: "Permission Enforcement in the SoftLayer API"
description: "he SoftLayer API is built around the same system of user permissions that power the SoftLayer customer portal. What the API exposes and allows depends on the user account that is making the call and that user's permission set."
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
    - "permissions"
---


<p>The SoftLayer API is built around the same system of user permissions that power the SoftLayer customer portal. What the API exposes and allows depends on the <a href="/article/authenticated">authenticated</a> user account that is making the call and that user's permission set. Your account's master user has full permissions to every service and method associated with your account. Please be wary if you choose to execute API method calls using your account's master user.</p>
<p>The SoftLayer API treats a permission error like an object not found error, returning an <a href="/article/exception">exception</a> stating that it can't find an object rather than say that the current user does not have permission to view it.</p>
<h2>Functionality Permissions</h2>
<p>Every portal and API user has a set of functionality-based permissions. These permissions govern the ability to:</p>
<ul>
<li>Add a server</li>
<li>Add and edit tickets</li>
<li>Add IP addresses</li>
<li>Add new users</li>
<li>Add services and upgrades</li>
<li>Add StorageLayer services</li>
<li>Cancel a server</li>
<li>Edit your company profile </li>
<li>Initiate RescueLayer</li>
<li>Initiate vulnerability scanning</li>
<li>Issue OS reloads</li>
<li>Manage a hardware firewall</li>
<li>Manage antivirus and spyware software</li>
<li>Manage DNS</li>
<li>Manage Host IDS software</li>
<li>Mange load balancers</li>
<li>Manage network IDS services</li>
<li>Manage network port control</li>
<li>Manage reverse DNS</li>
<li>Mange RWHOIS records</li>
<li>Manage server monitoring</li>
<li>Mange SWIP requests</li>
<li>Reboot a server</li>
<li>Search tickets</li>
<li>Submit one-time payments</li>
<li>Update payment details</li>
<li>View hardware details</li>
<li>View tickets</li>
<li>View your account summary</li>
<li>View software licenses</li>
<li>View bandwidth statistics</li>
<li>And much more…</li>
</ul>
<h2>Adding and Removing User Permissions</h2>
<p>If a method requires a special permission to execute, it is noted on its associated manual page. Likewise, if viewing a data type property requires a special permission, it is noted on that data type's manual page.  Permissions can be added or removed by either the SoftLayer Customer Portal or using a direct API call.<br />
 To change your user's permission set via the SoftLayer Customer Portal, complete the steps below.</p>
<ol>
<li>Access the <a href="https://manage.softlayer.com/">SoftLayer customer portal</a>.</li>
<li>Enter the account master’s username in the <b>User name field</b>.</li>
<li>Enter the Portal password in the <b>Password</b> field.</li>
<li>Click the <b>Administrative</b> link.  </li>
<li>Click on the username of the user whose permissions you wish to change in the <b>User List</b>.</li>
<li>Check or uncheck the desired user permissions.</li>
<li>Click the <b>Edit User Profile</b> button.</li>
</ol>
<p>To change your user’s permission set using a direct API call, use the following guidelines based on the task you would like to accomplish:</p>
<ul>
<li>To add permissions, execute either the addPortalPermission or addBulkPortalPermission methods in the <a href="/article/SoftLayer_User_Customer service">SoftLayer_User_Customer service</a>.</li>
<li>To remove permissions, execute either the removePortalPermission or removeBulkPortalPermission methods in the <a href="/reference/services/SoftLayer_User_Customer/">SoftLayer_User_Customer</a> service.<br />
<b>Notes:</b>
<ul>
<li>You can retrieve a list of valid hardware to assign user access to with the getAllObjects method in the <a href="/article/SoftLayer_User_Customer_CustomerPermission_Permission service">SoftLayer_User_Customer_CustomerPermission_Permission service</a>.</li>
<li>The addBulkPortalPermission and removeBulkPortalPermission methods allow you to add or remove multiple permission for the user at one time.</li>
</ul>
</li></ul>
<h2>Hardware Restrictions</h2>
<p>It is also possible to limit user interactivity to only certain servers purchased by a customer account or to none of the servers listed on the account.  As with adding and removing user permissions, this task may also be completed through either the SoftLayer Customer Portal or by using a direct API call.</p>
<p>Follow the steps below to update hardware restrictions for a user through the SoftLayer Customer Portal.</p>
<ol>
<li>Access the <a href="https://manage.softlayer.com/">SoftLayer customer portal</a>.</li>
<li>Enter the account master’s username in the <b>User name</b> field.</li>
<li>Enter the portal password in the <b>Password</b> field.</li>
<li>Click the <b>Administrative</b> link.</li>
<li>Click on your username of the user whose permissions you wish to change in the <b>User List</b>.</li>
<li>Scroll to the <b>User Hardware Access</b> section.</li>
<li>Determine if access to all hardware is to be granted, or if access to individual servers is required.
<ul>
<li>If access to <b>all hardware</b> is to be granted, select the Allow Access to All Hardware radio button.</li>
<li>If access to <b>individual servers</b> is required
<ul>
<li>Click the applicable server(s) to which the user requires access from the Server Access window.</li>
<li>Select the <b>Limit Access to the Following Hardware</b> radio button.</li>
</ul>
</li></ul>
</li>
<li>Click the <b>Edit User Profile</b> button.</li>
</ol>
<p>To change a user’s hardware restrictions using a direct API call, use the following guidelines based on the task you would like to accomplish:</p>
<ul>
<li>To add user hardware access, execute either the addHardwareAccess or addBulkHardwareAccess methods in the <a href="/reference/services/SoftLayer_User_Customer/">SoftLayer_User_Customer</a> service.</li>
<li>To remove user hardware access execute either the removeHardwareAccess or removeBulkHardwareAccess methods in the <a href="/reference/services/SoftLayer_User_Customer/">SoftLayer_User_Customer</a>  service.<br />
<b>Notes:</b>  
<ul>
<li>You can retrieve a list of valid hardware to assign user access to with the getHardware method in the SoftLayer_Account service.</li>
<li>The addBulkHardwareAccess and removeBulkHardwareAccess methods allow you to add or remove access to multiple pieces of hardware for the user at one time.</li>
</ul>
</li>
</ul>
<h2>Cloud Computing Instance (CCI) Restrictions</h2>
<p>Similar to the restriction of hardware interactivity, the Account Master also has the ability to restrict a specific user’s (or users’) ability to interact with and view Cloud Computing Instances (CCIs).  Like the two previous actions outlined in this article, this task, too, is completed through either the SoftLayer Customer Portal or through the use of a direct API call.<br />
Follow the steps below to update CCI restrictions for a user through the SoftLayer Customer Portal.</p>
<ol>
<li>Access the <a href="https://manage.softlayer.com/">SoftLayer customer portal</a>.</li>
<li>Enter the account master’s username in the <b>User name</b> field.</li>
<li>Enter the portal password in the <b>Password</b> field.</li>
<li>Click the <b>Administrative</b> link.</li>
<li>Click on your username of the user whose permissions you wish to change in the <b>User List</b>.</li>
<li>Scroll to the <b>User CCI Access</b> section.</li>
<li>Determine if access to all hardware is to be granted, or if access to individual servers is required.
<ul>
<li>If access to <b>all CCIs</b> is to be granted, select the <b>Allow Access to All CCI</b> radio button.</li>
<li>If access to <b>individual CCIs</b> is to be granted
<ul>
<li>Click the applicable CCI(s) to which the user requires access in the CCI Access window.</li>
<li>Select the <b>Limit Access to the Following CCI</b> radio button.</li>
</ul>
</li>
</ul>
</li><li>Click the <b>Edit User Profile button</b>.</li>
</ol>
<p>To change a user’s CCI restrictions using a direct API call, use the following guidelines based on the task you would like to accomplish:</p>
<ul>
<li>To add user CCI access, execute either the addVirtualGuestAccess or addBulkVirtualGuestAccess methods in the <a href="/reference/services/SoftLayer_User_Customer/">SoftLayer_User_Customer</a> service.</li>
<li>
<p>To remove user CCI access execute either the removeVirtualGuestAccess or removeBulkVirtualGuestAccess methods in the <a href="/reference/services/SoftLayer_User_Customer/">SoftLayer_User_Customer</a> service.<br />
<b>Notes:</b></p>
</li>
<li>
<p>You can retrieve a list of valid CCIs to assign user access with the getVirtualGuests method in the <a href="/reference/services/SoftLayer_Account/">SoftLayer_Account</a> service.</p>
</li>
<li>The addBulkVirtualGuestAccess  and removeBulkVirtualGuestAccess methods allow you to add or remove access to multiple pieces of hardware for the user at one time.</li>
</ul>
<h2>Associated Methods</h2>
<ul>
<li><a href="/reference/services/SoftLayer_User_Customer/getPermissions">SoftLayer_User_Customer::getPermissions</a></li>
<li><a href="/reference/services/SoftLayer_User_Customer/addPortalPermission">SoftLayer_User_Customer::addPortalPermission</a></li>
<li><a href="/reference/services/SoftLayer_User_Customer/addBulkPortalPermission">SoftLayer_User_Customer::addBulkPortalPermission</a></li>
<li><a href="/reference/services/SoftLayer_User_Customer/removePortalPermission">SoftLayer_User_Customer::removePortalPermission</a></li>
<li><a href="/reference/services/SoftLayer_User_Customer/removeBulkPortalPermission">SoftLayer_User_Customer::removeBulkPortalPermission</a></li>
<li><a href="/reference/services/SoftLayer_User_Customer/addHardwareAccess">SoftLayer_User_Customer::addHardwareAccess</a></li>
<li><a href="/reference/services/SoftLayer_User_Customer/addBulkHardwareAccess">SoftLayer_User_Customer::addBulkHardwareAccess</a></li>
<li><a href="/reference/services/SoftLayer_User_Customer/removeHardwareAccess">SoftLayer_User_Customer::removeHardwareAccess</a></li>
<li><a href="/reference/services/SoftLayer_User_Customer/removeBulkHardwareAccess">SoftLayer_User_Customer::removeBulkHardwareAccess</a></li>
</ul>
<h2>See Also</h2>
<ul>
<li><a href="/reference/services/SoftLayer_User_Customer/">SoftLayer_User_Customer</a></li>
<li><a href="/reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/">SoftLayer_User_Customer_CustomerPermission_Permission</a></li>
</ul>
<h2>External Links</h2>
<ul>
<li>The <a href="https://manage.softlayer.com/UserManagement/listUsers">User Administration</a> page at the <a href="https://manage.softlayer.com/">SoftLayer customer portal</a></li>
</ul>