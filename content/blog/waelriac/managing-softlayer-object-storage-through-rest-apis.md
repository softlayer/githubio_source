---
title: "Managing SoftLayer Object Storage Through REST APIs"
description: "<p>With <a href=http://www.softlayer.com/object-storage>SoftLayer object storage</a> you can archive, manage, and serv"
date: "2014-05-01"
author: "waelriac"
tags:
    - "blog"
---

<p>With <a href="http://www.softlayer.com/object-storage">SoftLayer object storage</a> you can archive, manage, and serve large amounts of unstructured data with ease and cost-effectiveness. Based on OpenStack Swift, SoftLayer object storage provides a robust, highly scalable object-based storage solution that is ideal for storing static data such as virtual machine images, media, and email archives.</p>
<p>With pay-as-you-go pricing, built-in SFTP and full integration with our content delivery network, you have the ability to store, retrieve, and leverage data the way you want to courtesy of the SoftLayer engineered tagging and search capabilities. You can add the capacity you need, when you need it, and access it however you like.</p>
<p>You can use different clients like PHP or Python for managing your object storage account. However, this blog will show how to manage your SoftLayer object storage directly through <strong>REST APIs</strong>.</p>
<h2>Retrieving SoftLayer Object Storage Accounts</h2>
<p>A list of all object storage accounts can be gathered from the <a href="http://sldn.softlayer.com/reference/services/SoftLayer_Account/">SoftLayer_Account</a> service with the <a href="http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHubNetworkStorage">SoftLayer_Account::getHubNetworkStorage</a> API. This API returns an array of <a href="/reference/services/SoftLayer_Network_Storage/">SoftLayer_Network_Storage</a> data-type objects. A simple GET request can be issued to this URL:<br />
<span class="geshifilter"><code class="text geshifilter-text">https://USERID:API_KEY@api.softlayer.com/rest/v3.1/SoftLayer_Account/getHubNetworkStorage</code></span></p>
<p>Note that you must replace <em>USERID</em> and <em>API_KEY</em> with the right values. The API will return basic information about the object storage accounts. You can further refine the response by adding an object mask with additional fields. For example, <span class="geshifilter"><code class="text geshifilter-text">&nbsp;SoftLayer_Account/getHubNetworkStorage?objectMask=username</code></span> will return only the usernames.</p>
<h2>Creating a SoftLayer Object Storage Account</h2>
<p>You can create a new SoftLayer object storage account using the <a href="http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder">SoftLayer_Product_Order::placeOrder</a> API. The API takes a Product Order template.<br />
In this example, the template will look like this:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">{
    "parameters" : [
      {
        "complexType": "SoftLayer_Container_Product_Order_Network_Storage_Hub",
        "quantity": 1,
        "packageId": 0,
        "prices": [
                {
                 "id": 30920
  }]}]}</pre></div>
<p>Notice that the packageId is set to 0, which is the additional services package. The price item is 30920, which corresponds to object storage pay-as-you-go. The price item ID might be different in your case.</p>
<p>To retrieve the right price, use: <span class="geshifilter"><code class="text geshifilter-text">https://USERID:API_KEY@api.softlayer.com/rest/v3/SoftLayer_Product_Package/0/getItems</code></span> API. This will return all the items under package 0 with their corresponding prices. Find the right price item ID for the object storage pay-as-you-go item.</p>
<p>Once you have the price item ID, issue a POST call on: <span class="geshifilter"><code class="text geshifilter-text">https://USERID:API_KEY@api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/placeOrder</code></span>, passing the above template as the body content.</p>
<p>The order information will be returned. Note the orderItemId value placedOrder->items->id, which is 30895044 in this example. In order to figure out the account ID associated with this order, let’s list the object storage accounts with the orderItemId values:</p>
<p>https://USERID:API_KEY@api.softlayer.com/rest/v3.1/SoftLayer_Account/getHubNetworkStorage?objectMask=mask[id,username,billingItem[id,orderItemId]]</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">    [{
    "id": 2646206,
    "username": "ACC-278436-13",
    "billingItem": {
       "id": 15545150,
    "orderItemId": 28708356
    }
    },
    {
    "id": 2724428,
    "username": " ACC-278436-14",
    "billingItem": {
       "id": 15545158,
    "orderItemId": 29773946
    }
    },
    {
    "id": 2792966,
    "username": " ACC-278436-15",
    "billingItem": {
      "id": 15545168,
    "orderItemId": 30895044
    }
     }]</pre></div>
<p>Order item ID 30895044 corresponds to account ID 2792966.</p>
<h2>Cancelling a SoftLayer Object Storage Account</h2>
<p>To cancel an existing object storage account, use the <span class="geshifilter"><code class="text geshifilter-text">SoftLayer_Billing_Item::cancelService</code></span>:</p>
<p><span class="geshifilter"><code class="text geshifilter-text">https://USERID:API_KEY@api.softlayer.com/rest/v3/SoftLayer_Billing_Item/15545168/cancelService</code></span><br />
Where 15545168 is the billingItem ID retrieved from the previous call.</p>
<h2>Managing the Object Storage</h2>
<p>This section provides examples on how to manage object storage with different REST API calls.</p>
<h3>Authenticating to the Object Storage</h3>
<p>To manage your object storage account, you can use a token for authentication. A token is usually valid for 24 hours and eliminates the need of using the credentials on every call.</p>
<p>You can obtain a token by passing the tenant:username/password to the object storage on your initial call. The tenant value is the username value retrieved in the above section. For example, our tenant value is ACC-278436-15, the username is the username used to log in to SoftLayer, and the password is the API-Key.<br />
To retrieve the authentication token, enter:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">curl -i -H "X-Auth-User: ACC-278436-15:USERID " -H "X-Auth-Key: API_KEY " https://dal05.objectstorage.softlayer.net/auth/v1.0</pre></div>
<p>This call will return multiple useful values:</p>
<ul>
<li>X-Auth-Token: AUTH_tkb26239d441d6401d9482b004d45f7259 – the token we need</li>
<li>X-Storage-Url: https://dal05.objectstorage.softlayer.net/v1/AUTH_df0de35c-d00a-40aa-b697-2b7f1b9331a6 - the URL to access the storage</li>
</ul>
<p>With these values, you can now manage your object storage account.</p>
<h3>Managing Containers</h3>
<h4>Listing Containers</h4>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">    $ curl -i -H "X-Auth-Token: AUTH_tkb26239d441d6401d9482b004d45f7259" https://dal05.objectstorage.softlayer.net/v1/AUTH_df0de35c-d00a-40aa-b697-2b7f1b9331a6
    HTTP/1.1 200 OK
    X-Account-Object-Count: 1
    X-Account-Meta-X-Account-Meta-Temp-Url-Key: b3968d0207b54ece87cccc06515a89d4
    X-Timestamp: 1395417488.69696
    X-Account-Meta-Cdn-Id: 7650
    X-Account-Meta-Temp-Url-Key: b3968d0207b54ece87cccc06515a89d4
    X-Account-Bytes-Used: 1659126
    X-Account-Container-Count: 1
    X-Account-Meta-Nas-Id: 2645584
    Accept-Ranges: bytes
    Content-Length: 55
    Content-Type: text/plain; charset=utf-8
    X-Trans-Id: txdf645ee4ef1342c3b9b6c4a27c46a036
    Date: Thu, 17 Apr 2014 20:55:27 GMT
&nbsp;
    container1</pre></div>
<h4>Adding a New Container</h4>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">    $ curl -i -XPUT -H "X-Auth-Token: AUTH_tkb26239d441d6401d9482b004d45f7259" https://dal05.objectstorage.softlayer.net/v1/AUTH_df0de35c-d00a-40aa-b697-2b7f1b9331a6/container2
    HTTP/1.1 201 Created
    Content-Length: 18
    Content-Type: text/html; charset=UTF-8
    X-Trans-Id: txf4798afe39f64cfb9526b77e3d2cb349
    Date: Thu, 17 Apr 2014 20:20:24 GMT
&nbsp;
    201 Created</pre></div>
<h4>Adding a File to a Container</h4>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">    $ curl -i -XPUT -H "X-Auth-Token: AUTH_tkb26239d441d6401d9482b004d45f7259" --data-binary "Created for testing REST client" https://dal05.objectstorage.softlayer.net/v1/AUTH_df0de35c-d00a-40aa-b697-2b7f1b9331a6/container2/file10.txt
    HTTP/1.1 201 Created
    Content-Length: 118
    Content-Type: text/html; charset=UTF-8
    Etag: 8ba9b504dc5961b4e328f9446f0a4f15
    Last-Modified: Thu, 17 Apr 2014 20:21:23 GMT
    X-Trans-Id: tx0263bbf654474189b73453dfcd8c59df
    Date: Thu, 17 Apr 2014 20:21:23 GMT
&nbsp;
    <html>
     <head>
      <title>201 Created</title>
     </head>
     <body>
      <h1>201 Created</h1>
      <br /><br />
     </body>
    </html></pre></div>
<h4>Listing Content of a Container</h4>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">    $ curl -i -H "X-Auth-Token: AUTH_tkb26239d441d6401d9482b004d45f7259" https://dal05.objectstorage.softlayer.net/v1/AUTH_df0de35c-d00a-40aa-b697-2b7f1b9331a6/container2
    HTTP/1.1 200 OK
    X-Container-Object-Count: 1
    X-Timestamp: 1397766024.59908
    X-Container-Bytes-Used: 31
    Accept-Ranges: bytes
    Content-Length: 11
    Content-Type: text/plain; charset=utf-8
    X-Trans-Id: tx186d234b956e49a49a40041c13e29ec9
    Date: Thu, 17 Apr 2014 20:22:05 GMT
&nbsp;
    file10.txt</pre></div>
<h4>Listing Content of a File</h4>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">    $ curl -i -H "X-Auth-Token: AUTH_tkb26239d441d6401d9482b004d45f7259" https://dal05.objectstorage.softlayer.net/v1/AUTH_df0de35c-d00a-40aa-b697-2b7f1b9331a6/container2/file10.txt
    HTTP/1.1 200 OK
    Content-Length: 31
    Accept-Ranges: bytes
    Last-Modified: Thu, 17 Apr 2014 20:21:23 GMT
    Etag: 8ba9b504dc5961b4e328f9446f0a4f15
    X-Timestamp: 1397766083.52836
    Content-Type: application/x-www-form-urlencoded
    X-Trans-Id: tx637e301b19e247838fd21-0053503820
    Date: Thu, 17 Apr 2014 20:22:56 GMT
&nbsp;
    Created for testing REST client</pre></div>
<h4>Creating a Directory</h4>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">    $ curl -i -XPUT -H "X-Auth-Token: AUTH_tkb26239d441d6401d9482b004d45f7259" -H "Content-Length: 0" -H "content-type: application/directory" https://dal05.objectstorage.softlayer.net/v1/AUTH_df0de35c-d00a-40aa-b697-2b7f1b9331a6/container2/folder3
    HTTP/1.1 201 Created
    Last-Modified: Thu, 17 Apr 2014 20:53:38 GMT
    Content-Length: 118
    Etag: d41d8cd98f00b204e9800998ecf8427e
    Content-Type: text/html; charset=UTF-8
    X-Trans-Id: tx2794c386946d479eb7df9-0053503f51
    Date: Thu, 17 Apr 2014 20:53:37 GMT
&nbsp;
    <html>
     <head>
      <title>201 Created</title>
     </head>
     <body>
      <h1>201 Created</h1>
      <br /><br />
     </body>
    </html></pre></div>
<h4>Adding a File to a Directory</h4>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">    $ curl -i -XPUT -H "X-Auth-Token: AUTH_tkb26239d441d6401d9482b004d45f7259" --data-binary "Created for testing REST client" https://dal05.objectstorage.softlayer.net/v1/AUTH_df0de35c-d00a-40aa-b697-2b7f1b9331a6/container2/folder3/file1.txt
    HTTP/1.1 201 Created
    Content-Length: 118
    Content-Type: text/html; charset=UTF-8
    Etag: 8ba9b504dc5961b4e328f9446f0a4f15
    Last-Modified: Thu, 17 Apr 2014 20:54:08 GMT
    X-Trans-Id: tx35669eb4d33f4dce821215173456325e
    Date: Thu, 17 Apr 2014 20:54:08 GMT
&nbsp;
    <html>
     <head>
      <title>201 Created</title>
     </head>
     <body>
      <h1>201 Created</h1>
      <br /><br />
     </body>
    </html></pre></div>
<p>For additional APIs and information, refer to the latest documentation on the <a href="http://docs.openstack.org/api/openstack-object-storage/1.0/content/">OpenStack site</a>.</p>
<h3>Using Swift Client to Manage Object Storage</h3>
<p>An easier way to use object storage is by using the OpenStack Swift client. On an Ubuntu machine, first install the client using <span class="geshifilter"><code class="text geshifilter-text">apt-get install swift</code></span>.</p>
<p>Now, you can use the Swift command to interact with SoftLayer object storage.<br />
Run the commands to export the variables needed by the client. This will save you from entering them on every command.</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">    export ST_AUTH=https://dal05.objectstorage.softlayer.net/auth/v1.0 
    export ST_USER= ACC-278436-15:USERID
    export ST_KEY=API_KEY</pre></div>
<p>You are now ready to use Swift.</p>
<h4>List Containers</h4>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">    root@ubuntu-vm:~# swift list
    container1
    container2
&nbsp;
    root@ ubuntu-vm:~# swift list container2
    file10.txt
    folder1
    folder1/file1.txt
    folder2
    folder2/file2.txt
    folder3
    folder3/file1.txt</pre></div>
<p>There’s much more you can do with the Swift client. For additional information, refer to the <a href="http://docs.openstack.org/developer/swift/">OpenStack documentation</a>.</p>
<p>-Wissam</p>

