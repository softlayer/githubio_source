---
title: "More SoftLayer REST API Examples"
description: "The SoftLayer REST API is powerful and convenient because you can use it from any language or no language (the command l"
date: "2015-06-24"
author: "bpotter"
tags:
    - "blog"
---

The SoftLayer REST API is powerful and convenient because you can use it from any language or no language (the command line or browser). The basics of using the REST API are explained in an [SLDN article on REST](http://sldn.softlayer.com/article/rest), and some examples are given in an [SLDN blog post on REST](http://sldn.softlayer.com/blog/klaude/Time-REST-Everyone). But even with this good information, it can be a little confusing understanding how to map what you see in the [SoftLayer API Services and Data Reference](http://sldn.softlayer.com/reference/services/SoftLayer_Account) to the exact REST API invocation that should be made. Some additional examples and guidelines are presented here to help with that.

The examples given in this article will be in the form of curl commands so that you see not only the proper URI, but also the REST verb and data.

##**GET Verb**
As explained in the referenced articles, the general format of the GET URI is,

<code>
https://<username>:<apiKey>@api.[service.]softlayer.com/rest/v3/<serviceName>[/initializationParameter][/method].<returnDatatype>
</code>
where “initializationParameter” is most commonly the id of the object.  This is needed whenever calling a service method that you want to operate on a single object.  If the method isn't specified, getObject is implied.  If the method is specified, the REST API will look for a method with that name, and if that doesn't exist, it will prepend “get” to the name and look again.  So these 2 commands are equivalent:

<code>
curl -# -X GET https://$SLUSERNAME:$SLAPIKEY@api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/8348063/PowerState.json

curl -# -X GET https://$SLUSERNAME:$SLAPIKEY@api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/8348063/getPowerState.json
</code>

Note that strictly speaking, what is specified in the previous commands are methods on the Virtual_Guest service, not relational properties, but fortunately there are get methods for most relational properties.  You **can** use the object mask to return relational properties directly:
<code>
mask='id;fullyQualifiedDomainName;provisionDate;powerState;operatingSystem.id;operatingSystem.passwords.password;operatingSystem.passwords.username;operatingSystem.softwareDescription.longDescription'
curl -# -X GET https://$SLUSERNAME:$SLAPIKEY@api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/8348063.json?objectMask=$mask
</code>

You might find the filteredMask form of the mask more readable for nested relational properties with the only problem being you have to escape the brackets when using curl:
<code>
mask='filteredMask\\[id,fullyQualifiedDomainName,provisionDate,powerState,operatingSystem\\[id,passwords\\[password,username\\],softwareDescription\\[longDescription\\]\\]\\]'
curl -# -X GET https://$SLUSERNAME:$SLAPIKEY@api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/8348063.json?objectMask=$mask
</code>

If in your code you don't want to specify an id to identify the object you want to operate on, you can use an objectFilter instead.  Here's an example of using objectMask and objectFilter together:
<code>
mask='filteredMask\\[id,fullyQualifiedDomainName,provisionDate,powerState,operatingSystem\\[id,passwords\\[password,username\\],softwareDescription\\[longDescription\\]\\]\\]'
filter='\\{"virtualGuests":\\{"hostname":\\{"operation":"slresttest"\\},"domain":\\{"operation":"feat.com"\\}\\}\\}'
curl -# -X GET https://$SLUSERNAME:$SLAPIKEY@api.softlayer.com/rest/v3/SoftLayer_Account/getVirtualGuests.json?objectMask=$mask\\&objectFilter=$filter
</code>

That objectFilter matches both the short hostname and the domain name.

##**POST Verb**
By default, the POST verb will run the createObject method on whatever SoftLayer service is specified in the URI.  But you can also explicitly specify many other service methods with POST.  If the service method takes arguments, they should be specified in the data portion and wrapped in a JSON object and array like <code>{ "parameters": [] }</code>.  For example, the Virtual_Guest [settags method](http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setTags) takes a single string argument that is a comma-separated list of tag names, so you run it like this:
<code>
curl -X POST -d '{"parameters":["tag1,foobar"]}' https://$SLUSERNAME:$SLAPIKEY@api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/9824021/setTags.json
</code>

To order a VSI, do this:
<code>
params='{ 
    "hostname": "slresttest", 
    "domain": "feat.com", 
    "datacenter" : { "name" : "tor01" },
    "startCpus": 2, 
    "maxMemory": 1024, 
    "hourlyBillingFlag": true, 
    "localDiskFlag": true, 
    "blockDevices": [{"device": "0", "diskImage": {"capacity": 25}}],
    "networkComponents": [{"maxSpeed": 1000}],
    "operatingSystemReferenceCode": "UBUNTU_LATEST" 
}'
echo '{"parameters":['$params']}' | curl -X POST -d @- https://$SLUSERNAME:$SLAPIKEY@api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest.json
</code>

In this example, note that since no method on the Virtual_Guest is specified, createObject is run by default.  Also, for clarity and convenience, if you are running this in a script, the arguments to createObject are specified in the params variable like the createObject method needs them and then that is wrapped in the required parameters array.  This can make your script code more readable because the format of the parameters assigned the params variable is exactly like you see documented in the [Virtual_Guest createObject](http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject) method.  Also note that when you specify part of the data object in a shell variable, curl will complain about the braces and brackets unless you escape them or pass them in via stdin as is done here.

If you just want to verify a VSI order, instead of actually ordering it, you can use a couple of other methods:
<code>
params='{ 
    "hostname": "slresttest", 
    "domain": "feat.com", 
    "datacenter" : { "name" : "tor01" },
    "startCpus": 2, 
    "maxMemory": 1024, 
    "hourlyBillingFlag": true, 
    "localDiskFlag": true, 
    "blockDevices": [{"device": "0", "diskImage": {"capacity": 25}}],
    "networkComponents": [{"maxSpeed": 1000}],
    "operatingSystemReferenceCode": "UBUNTU_LATEST" 
}'
response=`echo '{"parameters":['$params']}' | curl -X POST -d @- https://$SLUSERNAME:$SLAPIKEY@api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/generateOrderTemplate.json`

echo '{"parameters":['$response']}' | curl -X POST --data @- https://$SLUSERNAME:$SLAPIKEY@api.softlayer.com/rest/v3/SoftLayer_Product_Order/verifyOrder.json
</code>

In this example, the [generateOrderTemplate](http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate) method is run via REST to get the order template object for this order.  Then that is passed to the [verifyOrder](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/verifyOrder/) method of the Product_Order service.

If you are ever unsure which REST verb (GET, PUT, POST, DELETE) to use for a particular service method that doesn't start with one of the obvious verbs (“get”, “edit”, “create”, “delete”), POST is the best REST verb to try first.  But there are some exceptions to that rule.  For example, the state change methods (powerOn, powerOff, powerOffSoft, powerCycle, rebootDefault, rebootHard, rebootSoft, pause, resume) of both the Virtual_Guest and Hardware services need to be invoked via the GET verb, not the POST verb.

##**PUT Verb**
The PUT verb invokes the editObject service method by default and takes parameters in the same way POST does.  For example, to change the phone number associated with a SoftLayer user:
<code>
params='{ 
\t"officePhone": "123-456-7896"
}'
echo '{"parameters":['$params']}' | curl -X PUT -d @- https://$SLUSERNAME:$SLAPIKEY@api.softlayer.com/rest/v3/SoftLayer_User_Customer/272894.json
</code>

##**DELETE Verb**
The DELETE verb invokes deleteObject by default and generally takes no data parameters.  To delete a VSI:
<code>
curl -X DELETE https://$SLUSERNAME:$SLAPIKEY@api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/9957445.json
</code>

I hope these REST examples have helped solidify your understanding of the very useful SoftLayer REST API.

-Bruce

