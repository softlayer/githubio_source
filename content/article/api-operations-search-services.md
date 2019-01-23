---
title: "Searching SoftLayer Object Storage"
description: "(DEPRECIATED) Unique to SoftLayer Object Storage is a comprehensive search tool unlike any you have seen before.  SoftLayer’s integrated search service allows users to search the index based on account, container or path and provides numerous parameters to assist in filtering the search results. The Search Service API is built on top of the existing Object Storage API and indexes metadata on accounts, containers, and objects while providing a familiar interface to search the index."
date: "2012-02-08"
tags:
    - "article"
    - "sldn"
    - "storage"
    - "deprecated"
---

## Search EOS Message

Subject: Event 72839777 - End of Support for Object Storage OpenStack Swift (Infrastructure) select features and datacenter locations- Action Required
Severity: Major

Effective March 31st, 2019, IBM Cloud will no longer support the following Object Storage OpenStack Swift (infrastructure) features:

-Static Site Access
-Content Delivery Network (CDN)
-Search
-Image Templates import/export  

#### Migration Assistance
Need migration help? Refer to the IBM Cloud Object Storage documentation for migration instructions and how to use the data migration tool to efficiently migrate your data
- https://cloud.ibm.com/docs/services/cloud-object-storage/tutorials/migrate.html#migrating-data-from-openstack-swift


## Requests
Search requests can be made to search an entire account, a particular container or a specified path, based on the URL entered at the time of search.  Utilize one of the following examples and your authentication code to perform the desired search.

<table>
<tr><th>Desired Search</th><th>URL</th></tr>
<tr>
<td>Account</td><td>https://dal05.objectstorage.softlayer.net/v1/AUTH_12345ABCDE</td>
</tr>
<tr>
<td>Container</td><td>https://dal05.objectstorage.softlayer.net/v1/AUTH_12345ABCDE/container</td>
</tr>
<tr>
<td>Path</td><td>https://dal05.objectstorage.softlayer.net/v1/AUTH_12345ABCDE/container/path</td>
</tr>
</table>

After accessing the desired area of the Search Service API, a '''GET''' request is performed utilizing the '''X-Context''' header with the value of '''search'''.  To filter results, a number of parameters are available for use:

## Parameters
### q
The search query string.
Example:
<code>
?q=test
</code>
If you specify fields (including meta information) when use a period to separate 'q' and the field names.
Example:
<code>
?q.content_type=application
</code>
For meta fields, you can use a period or a dash to separate 'meta' from the actual meta key name.
Examples (these produce identical results):
<code>
?q.meta.foo=bar
</code>
<code>
?q.meta-foo=bar
</code>


### field
Field to search.  Default settings search for name and custom meta values.

* container: name of the container
* content_type: Content type of the object
* count: number of objects in a container
* hash: a summarized hash of the file (etag)
* last_modified: dateTime stamp indicating the object’s most recent modify date
* meta.myfield: custom meta values defined on the container or object
* name: name of the object or container
* object: object name
* read: x-container read header value (used for ACL)
* write: x-container write header value (used for ACL)

### type
The type of entity to search for. The default displays all types (containers and objects)

* container
* object

### format
The return format. Examples are shown below. Default: plain

* json
* xml
* plain

### recursive
Defines whether or not the search will be limited to one directory level or to search recursively. Default: true

* true
* false

A basic search query may contain one or more parameters, based on your desired return.  When inputting more than one search parameter, separate parameters with an ampersand (&).  For example, to search an account recursively for objects with the content type of "application/directory" and request the return in XML format, format the request as follows:

<code>
GET /v1/<account>?q=application%2Fdirectory&field=content_type&recursive=true&format=xml
X-Context: search
X-Auth-Token: AUTH_SADASDM43423DMSSAZXC234
</code>

## Responses
The Search API’s response to your query is returned with a basic header and a body that can be formatted for json, xml or in plain text.  The response header indicates the dateTime stamp of your query, the content and return type, the return count and the total number of items related to your query. The response header is formatted as follows:

<code>
HTTP/1.1 200 OK
Date: Thu, 19 Oct 2011 12:00:00 GMT
Content-Type: application/xml; charset=utf-8
X-Search-Items-Count: 3
X-Search-Items-Total: 29
</code>

In your response header, **X-Search-Items-Count** indicates the number of items included in the response, while **X-Search-Items-Total** indicates the total number of items available.  If the total exceeds the count, there are additional items that may be fetched.  Amending your parameters can result in additional information included in your return.

The response body contains a number of properties relating to your query, including the content type, last modified date, MD5 hash, etc.  It is important to note that for any response, all properties associated with the data will be returned – there are no relational or count properties as there is currently no application for object masks in the Object Storage API.  Examples of a potential response body are below in json, XML and in plain text.

### JSON Response Body (application/json)
<code>
[
    {
        "container": "test1",
        "content_type": "application/x-python-code",
        "hash": "c23c402de9d67332bce2a73f31a503c3",
        "last_modified": "Wed, 19 Oct 2011 21:26:30 GMT",
        "meta_mtime": "1318343501.0",
        "name": "test.py",
        "object": "test.py",
        "type": "object"
    },
    {
        "container": "test",
        "content_type": "text/plain",
        "hash": "d41d8cd98f00b204e9800998ecf8427e",
        "last_modified": "Mon, 17 Oct 2011 14:31:11 GMT",
        "meta_mtime": "1318861839.0",
        "name": "test_data/3.txt",
        "object": "test_data/3.txt",
        "type": "object"
    }   
]
</code>

### XML Response Body (text/xml)
<xml>
<?xml version="1.0" encoding="UTF-8"?>
<results>
    <object>
        <container>test1</container>
        <name>test.py</name>
        <object>test.py</object>
        <last_modified>Wed, 19 Oct 2011 21:26:30 GMT</last_modified>
        <content_type>application/x-python-code</content_type>
        <hash>c23c402de9d67332bce2a73f31a503c3</hash>
        <type>object</type>
        <meta_mtime>1318343501.0</meta_mtime>
    </object>
    <object>
        <container>test</container>
        <name>test_data/3.txt</name>
        <object>test_data/3.txt</object>
        <last_modified>Mon, 17 Oct 2011 14:31:11 GMT</last_modified>
        <content_type>text/plain</content_type>
        <hash>d41d8cd98f00b204e9800998ecf8427e</hash>
        <type>object</type>
        <meta_mtime>1318861839.0</meta_mtime>
    </object>
</results>
</xml>

### Plain Text Response Body (text/plain)
<code>
container: test1
name: test.py
object: test.py
last_modified: Wed, 19 Oct 2011 21:26:30 GMT
content_type: application/x-python-code
hash: c23c402de9d67332bce2a73f31a503c3
type: object
meta_mtime: 1318343501.0
 
container: test
name: test_data/3.txt
object: test_data/3.txt
last_modified: Mon, 17 Oct 2011 14:31:11 GMT
content_type: text/plain
hash: d41d8cd98f00b204e9800998ecf8427e
type: object
meta_mtime: 1318861839.0
</code>

As mentioned before, all requests can be structured to invoke a specific type of response utilizing the parameters listed in the previous section.  When you’re familiar with the functionality of this service, please refer to the Methods page for basic details on this and all methods pertaining to the Object Storage and Search Service APIs.