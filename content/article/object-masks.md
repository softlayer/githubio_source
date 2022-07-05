---
title: "Object-Masks"
description: "How Object Masks work. Used to specify which relational properties you would like included in your query."
date: "2012-12-03"
tags:
    - "article"
    - "sldn"
    - "objectmask"
---

## Overview

<iframe width="100%" height="630" src="https://www.youtube.com/embed/opuvAMp75co" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In order to obtain relational data from an object in the API you must declare an object mask in your API call. With standard object masks, relational data is pulled using a SOAP header, an XML-RPC struct or a GET parameter in REST.

Extended object masks make use of a <a href="http://en.wikipedia.org/wiki/Domain-specific_language" target="_blank">Domain-specific language</a> to reduce the effort required to express what data should be returned from the API. In order to support this new method of object mask, a new input method has been added to each protocol.


## Structure

### Root Node

Extended object masks start from a "root node" which is the datatype of the object being returned from your API call. 

For example, when calling [SoftLayer_Hardware::getObject](/reference/services/SoftLayer_Hardware/getObject) the root node will represent a [SoftLayer_Hardware Object](/reference/datatypes/SoftLayer_Hardware/) because that is what is returned by SoftLayer_Hardware::getObject, as seen by the `Return Values` section in the documentation. If my mask is `mask[id]` that means I want [SoftLayer_Hardware->id](/reference/datatypes/SoftLayer_Hardware/#id).

So if we were to send `mask[]` as our object mask for SoftLayer_Hardware::getObject, the entire SoftLayer_Hardware object would be returned as if no mask was included.

### Property

A property can be the name of any local or relational property of the returned object type and is appended to the mask with a period: `.` .

`mask.networkComponents` when used in calling SoftLayer_Hardware::getObject will return the SoftLayer_Hardware object, in addition to an array "networkComponents" containing the SoftLayer_Network_Components associated with that hardware.

It is possible to chain together multiple properties in order to drill down and receive even relational properties of relational properties.  For example, if we wanted to receive a list of network components related to a specific hardware device, a list of VLANs related to those network components and even the primary subnet of each of those VLANs we could use an object mask:

`mask.networkComponents.networkVlans.primarySubnet`
Multiple properties may be defined by listing in the object mask separated by a comma.

`mask.networkComponents,mask.primaryIpAddress,mask.billingItem`

### Property Set

Property Sets are a way to submit object masks in a nested structure format. A property set is used to declare a list of properties to obtain from an object and is helpful for reducing the verbosity of an object mask.

A property set is a nested, comma-separated list of properties enclosed in brackets `[]` which follows a property name. Each relational property in an object mask can have brackets appended to it, to go into other objects and relations.
For example `mask[networkComponents[ipAddresses[ipAddress]]]` can be used to get the ipAddress of every networkComponent on a Hardware_server.

The following masks can be considered equivalent:

`mask.id,mask.fullyQualifiedDomainName,mask.networkComponents.networkHardware,mask.networkComponents.uplinkComponent]`

```text
mask [
    id, fullyQualifiedDomainName,
    networkComponents[networkHardware, uplinkComponent]
]
```


### Payload reduction

Any local properties defined in a mask will result in the API returning only the specified local properties of the object. This feature allows for reduction of the API return data size and can help avoid the need for pagination or additional complication.


For example, when invoking [SoftLayer_Hardware::getObject](/reference/services/SoftLayer_Hardware/getObject) the following mask may be used to retrieve only the `id`, `fullyQualifiedDomainName`, and `primaryIpAddress` from the [SoftLayer_Hardware](/reference/datatypes/SoftLayer_Hardware/) record. In addition, it will return only the  `longName` from the `datacenter`, and the  `id`, `name`, and `port` of each  `networkComponent`.

```text
mask[
    id,fullyQualifiedDomainName,primaryIpAddress,
    datacenter[longName],
    networkComponents[id,name,port]
]
```


### Type

By default the type of returned objects will be inferred and is not required. However it is possible to declare a type for a specific property.

A type is defined by placing a parenthesis set after the property name with the type name enclosed. A type will need to be defined when the default property type does not have a particular property that you need.

For example, the `controlPanel` property is not defined on SoftLayer_Hardware and as such you will get an error if requesting it via `mask[controlPanel]`< on a call to  [SoftLayer_Account::getHardware](/reference/services/SoftLayer_Account/getHardware/). In order to request the value you must declare the `root property` to be of a particular type. An example is below.


`mask(SoftLayer_Hardware_Server)[controlPanel]`

If necessary, a property may be defined multiple times on the same level with different types.
The mask below is an example for invoking SoftLayer_Search::search with two expected data types to be returned:

```text
mask[
    resource(SoftLayer_Hardware)
    [
        id,
        fullyQualifiedDomainName,
        datacenter[longName],
        networkComponents[primaryIpAddress]
    ],
    resource(SoftLayer_Virtual_Guest)
    [
        id,
        fullyQualifiedDomainName,
        datacenter[longName],
        networkComponents[primaryIpAddress]
    ]
]
```


## Filtered Masks

A filtered mask is like a normal object mask, except it allows you to use an objectFilter to restrict the results of non-root relationships.

As an example, lets try to get the Motherboard component for all of our servers. You might try to make an API call to `SoftLayer_Account::getHardware()` with an objectMask of 

```
mask[id,hostname,
    components[id,serialNumber,
        hardwareComponentModel[description,
            hardwareGenericComponentModel[id,
                hardwareComponentType[keyName]
            ]
        ]
    ]
]
```

and an objectFilter of 

```
{"hardware":
    {"components":
        {"hardwareComponentModel":
            {"hardwareGenericComponentModel":
                {"hardwareComponentType":
                    {"keyName":{"operation":"MOTHERBOARD"}}
                }
            }
        }
    }
}
```

The problem is this will return all Hardware_Server objects that have a motherboard component, which is not quite what we want.

To get all Hardware_Server objects and only their motherboard component, we just need to use `filteredMask[]` instead of `mask[]`

for an API call that would look something like this:

```
curl -u $SL_USER:$SL_APIKEY  'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getHardware.json?objectMask=filteredMask[id,hostname,components[id,serialNumber,hardwareComponentModel[description,hardwareGenericComponentModel[id,hardwareComponentType[keyName]]]]]&objectFilter={"hardware":{"components":{"hardwareComponentModel":{"hardwareGenericComponentModel":{"hardwareComponentType":{"keyName":{"operation":"MOTHERBOARD"}}}}}}}'
```


## API interaction
### SOAP
To send the object mask to the SOAP API you will need to provide a `SoftLayer_ObjectMask` header with the string object mask for the value in the `mask` property of the header.

### XML-RPC
The same SoftLayer_ObjectMask header may be provided in the XML-RPC headers section of the request.

### REST
The REST interface will accept the object mask via the `objectMask` URL parameter.

