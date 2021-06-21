---
title: "Searching with the SoftLayer API"
description: "An explanation of how to use the SoftLayer_Search service."
date: "2021-06-18"
tags:
    - "article"
    - "sldn"
---

# Introduction

>The SoftLayer_Search service is only available in v3.1 of the API. You will get a "Service does not exist" error if you use v3

The [SoftLayer_Search](/reference/services/SoftLayer_Search/) is an API service that lets you make complex queries about data indexed by the service. While most of the SoftLayer API is contained in a SQL database, the SoftLayer_Search service uses an Elastic Search database to generate its results, allowing for more complex and responsive queries.

To start off, we need to understand what type of objects SoftLayer_Search knows about, and do to this, we use the [SoftLayer_Search::getObjectTypes()](/reference/services/SoftLayer_Search/getObjectTypes/) API Call.

## Searchable Types
As of this writing (2021)

- SoftLayer_Event_Log
- SoftLayer_Virtual_DedicatedHost
- SoftLayer_Hardware
- SoftLayer_Network_Application_Delivery_Controller
- SoftLayer_Network_Subnet_IpAddress
- SoftLayer_Network_Vlan
- SoftLayer_Network_Vlan_Firewall
- SoftLayer_Ticket
- SoftLayer_Virtual_Guest


# [SoftLayer_Search::getObjectTypes](#getObjectTypes) {#getObjectTypes .anchor-link}

The API call here is simple enough.


```bash
curl -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/getObjectTypes.json'
```

```bash
slcli --format=json call-api SoftLayer_Search getObjectTypes
```

```
ibmcloud sl call-api call-api SoftLayer_Search getObjectTypes
```

The output will look something like this:

```json
{
    "name": "SoftLayer_Virtual_Guest",
    "properties": [
        {
            "name": "accountId",
            "sortableFlag": true,
            "type": "integer"
        },
        {
            "name": "datacenter.longName",
            "sortableFlag": true,
            "type": "string"
        },
```

The `name` property referes to the type of SoftLayer Datatype being tracked, and the `properties` are the searchable fields, which are relational properties on the named datatype.

# [SoftLayer_Search::search](#search_search) {#search_search .anchor-link}

[SoftLayer_Search::search(search_term)](/reference/services/SoftLayer_Search/search/) takes in one parameter, and that is a string representing what you want to search for. The documentation here has a nice rundown of how to build out the API call. Basically you need to define which object types you want to search in, and what terms you want to search in those types for.

## Find all Virtual and Hardware servers.

By specifying an `_objectType` of `SoftLayer_Hardware` and `SoftLayer_Virtual_Guest` and not defining a search term, this API call will return all Hardware and Virtual objects on your account.


```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": ["_objectType:SoftLayer_Hardware,SoftLayer_Virtual_Guest"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/search.json'
```

To search for a specific string, just do the following:

```bash
curl -u $SL_USER:$SL_APIKEY -X POST  -d '{"parameters": ["_objectType:SoftLayer_Hardware,SoftLayer_Virtual_Guest test1234"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/search.json'
```

This will return all the hardware and virtual objects with the string `test1234` anywhere in their indexed properties.


## Pulling in extra data

While you can search by tags, they are not included in the default output. To fix this you can add an objectMask to your query, however this is a little trickier than normal as the result is a [SoftLayer_Container_Search_Result](/reference/datatypes/SoftLayer_Container_Search_Result) datatype, and the Entity property is a generic, so you have to use Object Mask casting to get the data you need.

If you want to search for both Hardware and Virtual servers, and get both of their tags included in the output, your mask would look like this:

```
mask[
    resource(SoftLayer_Virtual_Guest)[tagReferences.tag.name],
    resource(SoftLayer_Hardware)[tagReferences.tag.name]
]
```

The `resource(SoftLayer_Virtual_Guest)` bit forces that object mask to be of the SoftLayer_Virtual_Guest type, allowing you to specify those datatype properties. 


```
slcli -vvv --format=json call-api SoftLayer_Search search "_objectType:SoftLayer_Hardware,SoftLayer_Virtual_Guest test1234"  --mask="mask[resource(SoftLayer_Virtual_Guest)[tagReferences.tag.name],resource(SoftLayer_Hardware)[tagReferences.tag.name]]"

curl -u $SL_USER:$SL_APIKEY -X POST  -d '{"parameters": ["_objectType:SoftLayer_Hardware,SoftLayer_Virtual_Guest test1234"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/search.json?objectMask=mask%5Bresource%28SoftLayer_Virtual_Guest%29%5BtagReferences.tag.name%5D%2Cresource%28SoftLayer_Hardware%29%5BtagReferences.tag.name%5D%5D'
```


You can use the same strategy to pull in other details as well, like Billing Item, or Active Transactions.

```
slcli -vvv --format=json call-api SoftLayer_Search search "_objectType:SoftLayer_Hardware,SoftLayer_Virtual_Guest test1234"  --mask="mask[resource(SoftLayer_Virtual_Guest)[tagReferences.tag.name,billingItem,activeTransactions],resource(SoftLayer_Hardware)[tagReferences.tag.name]]"

curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": ["_objectType:SoftLayer_Hardware,SoftLayer_Virtual_Guest test1234"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/search.json?objectMask=mask%5Bresource%28SoftLayer_Virtual_Guest%29%5BtagReferences.tag.name%2CbillingItem%2CactiveTransactions%5D%2Cresource%28SoftLayer_Hardware%29%5BtagReferences.tag.name%5D%5D'
```

In that example, I only included billingItem and activeTransaction properties in the Virtual_Guest resource, which results in any Hardware items included in the search results not having those properties, which is expected.


# [SoftLayer_Search::advancedSearch](#search_advanced) {#search_advanced .anchor-link}

The format for [SoftLayer_Search::advancedSearch(search_term)](/reference/services/SoftLayer_Search/advancedSearch/) is very similar to SoftLayer_Search::search() expect here you can specific which property you want to match, instead of just a general matching. 

For example, finding all Network_Vlans with a specific name and number would look like this:

```
slcli -vvv --format=json call-api SoftLayer_Search advancedSearch "_objectType:SoftLayer_Network_Vlan name: testdemo0604 vlanNumber: 808"

[
    {
        "matchedTerms": [
            {"value": "testdemo0604"},
            {"value": "808"}
        ],
        "relevanceScore": "17.810793",
        "resource": {
            "accountId": 307608,
            "id": 3101096,
            "modifyDate": "2021-06-04T13:39:16-06:00",
            "name": "testdemo0604",
            "primarySubnetId": 260011,
            "vlanNumber": 808
        },
        "resourceType": "SoftLayer_Network_Vlan"
    }
]
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": ["_objectType:SoftLayer_Network_Vlan name: testdemo0604 vlanNumber: 808"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/advancedSearch.json'
```



# [Special Notes](#search_notes) {#search_notes .anchor-link}

## Valid Characters

+ `[a-zA-Z]`
+ `-` *NOTE* a `-` at the START of a string means negation, and so any search for `-term` will not have that search term in the results.
+ `.`
+ `:`
+ `@`


## [Sorting](#search_sorting) {#search_sorting .anchor-link}

To sort, simply add something like this to your search string `_sort:[index1:asc,index2:desc]`. You can only sort by indexed properties though, any non-indexed property will be ignored.


```
slcli -vvv --format=json call-api SoftLayer_Search advancedSearch '_objectType:SoftLayer_Event_Log _sort:[eventCreateDate:asc] eventName:"Login Successful"'  --limit=20

curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": ["_objectType:SoftLayer_Event_Log _sort:[eventCreateDate:asc] eventName:\"Login Successful\""]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/advancedSearch.json?resultLimit=0%2C20'
```

## [Date Ranges](#search_date) {#search_date .anchor-link}

On date properties, you can specify a date range to search for. Either with exact date like `eventCreateDate:[2021-06-01 TO 2021-06-16]` 

```
slcli -vvv --format=json call-api SoftLayer_Search advancedSearch '_objectType:SoftLayer_Event_Log  eventCreateDate:[2021-06-01 TO 2021-06-16]'   --limit=20

curl -u $SL_USER:$SL_APIKEY -X POST-d '{"parameters": ["_objectType:SoftLayer_Event_Log  eventCreateDate:[2021-06-01 TO 2021-06-16]"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/advancedSearch.json?resultLimit=0%2C20'
```

Or relative dates like `eventCreateDate:[now-1M TO now]`

```
slcli -vvv --format=json call-api SoftLayer_Search advancedSearch '_objectType:SoftLayer_Event_Log  eventCreateDate:[now-1M TO now]'   --limit=20

curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": ["_objectType:SoftLayer_Event_Log  eventCreateDate:[now-1M TO now]"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/advancedSearch.json?resultLimit=0%2C20'
```

Supported units here are M(month), w(week), h(hour), m(minute), and s(second)


Make sure to capitalize the term `TO`, it is required to be that way.

## [And, Or, Not](#search_andornot) {#search_andornot .anchor-link}

Will match Virtual_Guests with a domain of test.com AND a hostname of testTor01
```
slcli -vvv --format=json call-api SoftLayer_Search advancedSearch "_objectType:SoftLayer_Virtual_Guest  domain:test.com && hostname:testTor01"

curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": ["_objectType:SoftLayer_Virtual_Guest  domain:test.com && hostname:testTor01"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/advancedSearch.json'

```

Will match Virtual_Guests with a domain of test.com OR a hostname of testTor01
```
slcli -vvv --format=json call-api SoftLayer_Search advancedSearch "_objectType:SoftLayer_Virtual_Guest  domain:test.com || hostname:testTor01"

curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": ["_objectType:SoftLayer_Virtual_Guest  domain:test.com || hostname:testTor01"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/advancedSearch.json'

```

Will match Virtual_Guests with a domain of test.com but NOT a hostname of testTor01
```
slcli -vvv --format=json call-api SoftLayer_Search advancedSearch "_objectType:SoftLayer_Virtual_Guest  domain:test.com hostname:-testTor01"

curl -u $SL_USER:$SL_APIKEY -X POST  -d '{"parameters": ["_objectType:SoftLayer_Virtual_Guest  domain:test.com hostname:-testTor01"]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Search/advancedSearch.json'
```
