---
title: "Going Further with the SoftLayer API Python Client - Part 1"
description: "So you want to code to the SoftLayer API, your language of choice is python (well done), and you’ve read the <a href=ht"
date: "2015-02-06"
author: "bpotter"
tags:
    - "blog"
---

So you want to code to the SoftLayer API, your language of choice is python (well done), and you’ve read the <a href="http://sldn.softlayer.com/article/SoftLayer-API-Overview">SoftLayer API Overview</a> on the <a href="http://sldn.softlayer.com/">SLDN</a> site. You've even read the article <a href="http://sldn.softlayer.com/article/Python">using the SoftLayer API from python</a>, but it just felt like a tease. So you follow the web trail to <a href="https://softlayer-api-python-client.readthedocs.org/en/latest/api/client/">readthedocs</a> for the slightly longer <a href="https://softlayer-api-python-client.readthedocs.org/en/latest/api/client/">API Documentation</a>. You think, “maybe that’s all I need to know.” You dive in and start your first program. But as soon as you create the Client object and get your first Account object, questions start flooding in, and you realize you need a lot more information. So you look to your trusted friend Google and find a few hits in the <a href="https://forums.softlayer.com/forum/softlayer-developer-network">SLDN Forums</a>, and a few short examples scattered around the Internet, but you realize something very quickly: The SoftLayer API has bindings for many different languages/formats in addition to python (ruby, perl, c#, SOAP, RESTful, etc.), and it’s not clear at all how to translate the code snippets in those other languages to your situation, because each binding seems to interact with the SoftLayer API in a different way. What do you do? 
 
<p>Keep reading. This article was created to fill in some of those gaps.</p>

  <p>The first thing you might want to know is that when you create the SoftLayer Client object, you can either connect to the API end point on the private network, like the examples in the links above show (which means you have to run your code on a SoftLayer machine), or you can use the public end point so you can run/test your code from your laptop: 
  </p>

<code>
client = SoftLayer.Client(username=myuser, api_key=mykey, endpoint_url=SoftLayer.API_PUBLIC_ENDPOINT)
</code>

Services vs. Managers
------------------
  <p>There are 2 different ways to access SoftLayer data and run SoftLayer methods: <a href="http://sldn.softlayer.com/reference/services/SoftLayer_Account">Services</a> and <a href="https://softlayer-api-python-client.readthedocs.org/en/latest/api/client/#managers">Managers</a>. Using the managers is a little easier to learn, but not all data and functionality is covered by them. So if you are doing more than just the basics, chances are you will need to learn how to use the services anyway. Personally, I find it more consistent to just use services for everything, so I will focus on that here. But you may find you prefer to use the managers where you can. Many of the tips I cover below apply to both.
  </p>

Navigating the Services Web Site
---------------------------
  <p>Go to the <a href="http://sldn.softlayer.com/reference/services/SoftLayer_Account">SoftLayer Services</a> website.</p>

<p>You’ll spend a lot of time here, so let’s get comfortable with it. The first thing to notice, if you scroll the list of services on the left, is that there are a boat load of services. The SoftLayer API is super extensive. This is good news, once you learn how to harness it. Each service is essentially a class with methods and data, although from python you don’t access them exactly like you would a real python class (i.e., you don’t use a constructor for an individual class to get a handle to an instance). Instead, the main Client object is a dictionary of service objects. Each page in the services website shows the methods that can be run from that service (shown when you click the blue Service tab), and the data structure of that service (shown when you click on the green Data Type tab) when this service data type is returned by any of the methods in this service or another service. Don’t worry, this will become clearer when you start using it. 
  </p>

  <img src="http://i61.tinypic.com/9u3pe0.png" border="0">

  <p>Click on any of the get methods and you’ll see the data type that is returned by that method. If you go back to the <a href="http://sldn.softlayer.com/reference/services/SoftLayer_Account">Account service page</a> and click on the green Data Type tab you'll see a list of Local Properties and Relational &amp; Count Properties. The local properties are directly part of this service data type. The relational properties are pointers to other service data types. You can get quite lost following this trail to all the data you need. I find it easiest to open each link in a new tab so you have a history of how you got there (because you’ll need that history to write your code properly). 
  </p>
  <p>An example will help clarify this. Say you wanted to get a list of VLANs (and their subnets) in your SoftLayer account. Looking through the methods under the blue Services tab of the Account page, you find a <a href="http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNetworkVlans">getNetworkVlans</a> method that returns the <a href="http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Vlan">Network_Vlan</a> service data type. On that page you see that one of the local properties is vlanNumber, which you want to know, but how do you tell SoftLayer exactly which properties you want returned? This is where the <strong>object mask</strong> comes in. The mask is a string of comma-separated property names that you want returned. 
</p>
<p>What other properties are of interest here? I learned the hard way that VLAN numbers aren’t unique in SoftLayer, not within an account, not within a data center, not even within a pod. The best way to uniquely specify a VLAN is to include the primary router it is on. Look at the list of relational properties and you’ll see one called primaryRouter, which clearly is better than the property called secondaryRouter.  Click on the link in the primaryRouter section and it takes you to a page for the <a href="http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Router">Hardware_Router</a> data type. It turns out hostname is the best router property (I’ll explain how to figure that out later), so primaryRouter.hostname will be the second property listed in your mask. You also want to know the subnets that are part of this VLAN, so go back to the Network_Vlan page and you’ll find another relational property called primarySubnets. Follow that link to the <a href="http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Subnet">Network_Subnet</a> data type page, and you’ll see two local properties named networkIdentifier and cidr. Add these to your mask and it becomes: 
  </p>

  <code>mask = 'vlanNumber, primaryRouter.hostname, subnets.networkIdentifier, subnets.cidr'</code>

  <p>Putting it all together, here’s your first SoftLayer API python program:</p>

  <code>import SoftLayer
import pprint

client = SoftLayer.Client(username=myuser, api_key=mykey, endpoint_url=SoftLayer.API_PUBLIC_ENDPOINT)
mask = 'vlanNumber, primaryRouter.hostname, subnets.networkIdentifier, subnets.cidr'
allVlans = client['Account'].getNetworkVlans(mask=mask)
pprint.pprint(allVlans)</code>

  <p>In a real world program, you would access the members of the data structure returned and do something with them. But pprint is really useful to view the structure so you know how to write the code to access it, especially when it is dictionaries inside of lists inside of dictionaries.
  </p>

  <p>Notice that I referred to all of the SoftLayer services/data types without the leading “SoftLayer_”. This is because that's the way SoftLayer often does it in their documentation, and that’s the way you refer to them in your code. 
</p>

Efficient Use of the API
---------------------
#####Masks

  <p>In the mask above, we specified some specific local properties we wanted at each level in the data structure:</p>
  <ul><li>vlanNumber in Network_Vlan
  <li>hostname in Hardware_Router
  <li>networkIdentifier and cidr in Network_Subnet
  </ul>
  <p>This wasn’t by accident; it was very intentional. If at any level in the data type hierarchy you don’t specify at least one local property, the SoftLayer API will return all of the local properties for that data type. This can be very useful (combined with pprint) to explore what properties have the values you want. This is because the documentation for each property is often not very specific. But the API call also takes longer, by a non-trivial amount, when it returns a lot of properties. In the example above, if we just change the mask to:</p>

  <code>mask = 'primaryRouter, subnets'</code>

  <p>We still get the properties we are interested in (among others), but code takes 70 percent longer (1.7 seconds compared to the original 1 second in my account that has 90 VLANs), because it
returns all of the local properties of Network_Vlan, Hardware_Router, and Network_Subnet for every VLAN. Combined with pprint, this is very useful when you are trying to figure out exactly what properties you want (this is how I figured out that hostname was the most useful property of Hardware_Router). Once you are finished exploring, you should limit the data returned to exactly what you need. In one case in my work, an API call took five times longer before I limited the mask like this.
</p>

  So the rule of thumb is:

  <ul><li>In your mask, for every data type that you refer to, specify at least 1 local property (remote properties don't count for this). If you don't need any local properties (you are only following remote properties to other data types), at least specify the “id” property.</ul>

  <p>A mask can be passed into any method that lists ObjectMask in the Optional Headers section of its Web page. 
</p>

#####Ids

<p>Ids are the unique integer identifiers SoftLayer uses as the primary keys for its data objects. They are unique within an account and data type, but they can repeat across accounts or data types. The most common time to use an id is with the getObject method of any service. For example:</p>

  <code>client['Network_Gateway'].getObject(id=gatewayid, mask=mask)</code>

  <p>An id can also be specified in some methods that would normally return a list of objects, to get just one specific object:</p>

<code>
  client['Network_Gateway'].getInsideVlans(id=gatewayid, mask=mask)
client['User_Customer'].getChildUsers(id=id, mask='username, email, displayName, firstName, lastName')
</code>

  <p>Or to run an action against a particular object:</p>

 <code>
 client['Network_Gateway'].bypassVlans(objs, id=gatewayid)
client['Ticket'].getStatus(id=12497530)
</code>

  <p>It appears that any method that has InitParameters listed in the Optional or Required Headers sections will accept id as an argument. You would usually get the value of the id from a previous query of the API.</p>

#####Filters

  <p>We’ve seen that limiting the amount of data you ask the SoftLayer API to return speeds it up. The mask enables you to accurately specify the <strong>properties</strong> of each object (service instance) you want returned. But how do you specify which <strong>objects</strong> should be returned instead of getting all of the objects of a given type? This is what the filter is for. There is very little documentation available on using filters, so I’ll explain it here. Like “mask”, “filter” is another optional parameter that can be used on most methods. For its value, you specify nested dictionaries that start with a property in the service you are running the method against, and follow the trail of properties until you get to the one you want to base your filter selection on. Within that, you specify a dictionary with a key called “operation” and an operator and value. This will be much clearer with an example. If I want to get all of the virtual guests (virtual servers) in my account that have a domain name that contains the string “feat”, I would code it like this:
  </p>

 <code>
 guests = client['Account'].getVirtualGuests(mask=mask, filter={'virtualGuests': {'domain': {'operation': '*= feat'}}})
</code>

  <p>Note that even though getVirtualGuests() returns the Virtual_Guest data type, I don’t start there to specify the properties. The method is in the Account service, so I start at that data type. The <a href="http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account">Account data type</a> has a remote property called “virtualGuests”, which then takes me to the Virtual_Guest data type, which has a local property called “domain”, the one I'm interested in. Also note that the operator and the value it is matching are in the same string. The operator I used in my example, “*=”, means “contains”, but here’s the whole list of operators:
  </p>

  <ul>
  <li>'*=' means Contains (ignoring case)
  <li>'^=' means Begins with (ignoring case)
  <li>'$=' means Ends with (ignoring_case)
  <li>'_=' means Matches completely (ignoring case) - this is the default operator if none is specified
  <li>'!=' means Is not Equal To (case sensitive)
  <li>'<=' means Less than or Equal To (case sensitive)
  <li>'>=' means Greater than or Equal To (case sensitive)
  <li>'<' means Less Than (case sensitive)
  <li>'>' means Greater Than (case sensitive)
  <li>'~' means Contains (case sensitive)
  <li>'!~' means Does not Contain (case sensitive)
  </ul>
  
  <p>If you want to match more than one property, you can add additional keys to the dictionary, and all the operations are essentially ANDed together. For example, this will select virtual guests that have “feat” in the domain, and the hostname is exactly “myvm”: 
  </p>

  <code>
guests = client['Account'].getVirtualGuests(mask=mask, filter={'virtualGuests': {'hostname': {'operation': 'myvm'}, 'domain': {'operation': '*= feat'}}})
</code>

  <p>There is also an “extended” operator called “betweenDate” in which the values for the operator are given in subsequent keys in the dictionary. You can see an <a href="https://softlayer-api-python-client.readthedocs.org/en/latest/api/client/#making-api-calls">example</a> of this. There might be other extended operators; I’ve never seen a list of them.
  </p>

  <p>In my next blog post, I’ll cover where to start navigating from, using SoftLayer API calls to modify resources, and handling SoftLayer exceptions.</p>


\\- Bruce

