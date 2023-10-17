---
title: "Threads for improved API performance"
description: "Describes how to use Python's Thread library to improve how quickly API commands can be executed by doing them in parallel instead of in series."
date: "2023-10-16"
classes: 
    - "SoftLayer_Account"
tags:
    - "article"
    - "examples"
    - "objectfilter"
    - "slcli"
---


# Basic of Threads
If you are unfamiliar with Threads these examples will use the [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures) library within the python standard library (available after python3.2) which is fairly simple to get setup. 

For some technical details on how python handles Threads the following are good reading on the topic
- [Python Threading Tutorial: Run Code Concurrently Using the Threading Module](https://youtu.be/IEEhzQoKtQU?si=5F9NvQcf6km9QHan)
- [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)

The basic pattern will look something like this

```python
import concurrent.futures as cf
import SoftLayer

client = SoftLayer.Client()
with cf.ThreadPoolExecutor(max_workers=10) as executor:
    # Adds this API call to the ThreadPool, to be executed at some point in the future
    api_call = executor.submit(
        client.call, 'SoftLayer_Hardware_Server', 'getObject',
        id=9999, mask="mask[id,hostname]"
    )
    # Waits for the API call to return, then prints out the result
    print(api_call.result())
```

With regards to the SoftLayer API, threads are useful in two situations. First is Pagination, when you make a series of API calls with a [resultLimit](/article/using-result-limits-softlayer-api/) to get chunks of data from a long list of results. Instead of making 1 api call, then another and another, you can make them all at the same time (up to your max_works limit). Also threads are great to break up a single API call that might take a long time to complete, into multiple smaller api calls that each execute quickly, thus making the overall execution time faster.

# Threads for Pagination

[v6.2.0](https://github.com/softlayer/softlayer-python/releases/tag/v6.2.0) implements a new feature to easily enable threaded API calls to page through data in the client.cf_call() method. Here is that code and I will explain a bit on how it works.

```python
def cf_call(self, service, method, *args, **kwargs):
    """Uses threads to iterate through API calls.

    :param service: the name of the SoftLayer API service
    :param method: the method to call on the service
    :param integer limit: result size for each API call (defaults to 100)
    :param \\*args: same optional arguments that ``Service.call`` takes
    :param \\*\\*kwargs: same optional keyword arguments that ``Service.call`` takes
    """
    limit = kwargs.pop('limit', 100)
    offset = kwargs.pop('offset', 0)

    if limit <= 0:
        raise AttributeError("Limit size should be greater than zero.")
    # This initial API call is to determine how many API calls we need to make after this first one.
    first_call = self.call(service, method, offset=offset, limit=limit, *args, **kwargs)

    # This was not a list result, just return it.
    if not isinstance(first_call, transports.SoftLayerListResult):
        return first_call
    # How many more API calls we have to make
    api_calls = math.ceil((first_call.total_count - limit) / limit)


    def this_api(offset):
        """Used to easily call executor.map() on this fuction"""
        return self.call(service, method, offset=offset, limit=limit, *args, **kwargs)

    with cf.ThreadPoolExecutor(max_workers=10) as executor:
        future_results = {}
        offset_map = [x * limit for x in range(1, api_calls)]
        future_results = list(executor.map(this_api, offset_map))
    # Append the results in the order they were called
    for call_result in future_results:
        first_call = first_call + call_result
    return first_call
```

First, we need to get (or set a default) for the `limit` and `offset` properties. 

This removes them from the kwargs (if any other properties like mask/filter are set, we keep those), and will set them to a default value if they do not exist.
```python
limit = kwargs.pop('limit', 100)
offset = kwargs.pop('offset', 0)
```


From there, we need to make the first api call so we can determine how many total results we have to get. API results will have a special header called `softlayer-total-items` that we make use of here for that count. If the result is a List, the transport will set the result to a transports.SoftLayerListResult that has the `total_count` property with this header in it.

```python
first_call = self.call(service, method, offset=offset, limit=limit, *args, **kwargs)
# This was not a list result, just return it.
if not isinstance(first_call, transports.SoftLayerListResult):
    return first_call
# How many more API calls we have to make
api_calls = math.ceil((first_call.total_count - limit) / limit)
```

Once we have `total_count`, we subtract the `limit` (we don't want to get those results again), and divide by the limit (rounding up to the nearest whole number), and that gives us the count of how many API calls to make.

Next we need to define a small function we can use with the ThreadPoolExecutor to make things a little easier. The only variable that changes here is the offset, so that is our only parameter. The rest are set to whatever was passed in originally.

```python
def this_api(offset):
    """Used to easily call executor.map() on this fuction"""
    return self.call(service, method, offset=offset, limit=limit, *args, **kwargs)
```

Then we add the function calls to the ThreadPoolExecutor as follows

```python
with cf.ThreadPoolExecutor(max_workers=10) as executor:
    offset_map = [x * limit for x in range(1, api_calls)]
    future_results = list(executor.map(this_api, offset_map))
```

`offset_map` is just a list of ints we will pass into our `this_api` function, defining our offset. We start at `1 * limit` since we already have the `0 -> limit` results from our first api call. [Executor.map()](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map) will add a call to `this_api()` for each element in `offset_map`

Finally we leave the `with cf.ThreadPoolExecutor` block once all the API calls have executed, and we can simply add them together and return the result.

```python
for call_result in future_results:
    first_call = first_call + call_result
return first_call
```

# Threads for large API calls

For API calls that get a single resources (for example, SoftLayer_Hardware_Server::GetObject()), it can still be possible to use threading to improve performance if you are getting a lot of relational properties about the object. [get_hardware_fast()](https://github.com/softlayer/softlayer-python/blob/master/SoftLayer/managers/hardware.py#L281) is a good example of this pattern. 

The basic process is to remove any relational properties from your object mask that have corresponding methods, and call those methods instead.


```python
def get_hardware_fast(self, hardware_id):
    """Get details about a hardware device. Similar to get_hardware() but this uses threads

    :param integer id: the hardware ID
    :returns: A dictionary containing a large amount of information about the specified server.
    """

    hw_mask = (
        'id, globalIdentifier, fullyQualifiedDomainName, hostname, domain,'
        'provisionDate, hardwareStatus, bareMetalInstanceFlag, processorPhysicalCoreAmount,'
        'memoryCapacity, notes, privateNetworkOnlyFlag, primaryBackendIpAddress,'
        'primaryIpAddress, networkManagementIpAddress, userData, datacenter, hourlyBillingFlag,'
        'lastTransaction[transactionGroup], hardwareChassis[id,name]'
    )
    server = self.client.call('SoftLayer_Hardware_Server', 'getObject', id=hardware_id, mask=hw_mask)
    with cf.ThreadPoolExecutor(max_workers=10) as executor:
        networkComponents = executor.submit(
            self.client.call, 'SoftLayer_Hardware_Server', 'getNetworkComponents', id=hardware_id
        )
        activeComponents = executor.submit(
            self.client.call, 'SoftLayer_Hardware_Server', 'getActiveComponents', id=hardware_id
        )
        activeTransaction = executor.submit(
            self.client.call, 'SoftLayer_Hardware_Server', 'getActiveTransaction', id=hardware_id
        )
        operatingSystem = executor.submit(
            self.client.call, 'SoftLayer_Hardware_Server', 'getOperatingSystem', id=hardware_id
        )
        softwareComponents = executor.submit(
            self.client.call, 'SoftLayer_Hardware_Server', 'getSoftwareComponents', id=hardware_id
        )
        billingItem = executor.submit(
            self.client.call, 'SoftLayer_Hardware_Server', 'getBillingItem', id=hardware_id
        )
        networkVlans = executor.submit(
            self.client.call, 'SoftLayer_Hardware_Server', 'getNetworkVlans', id=hardware_id
        )
        remoteManagementAccounts = executor.submit(
            self.client.call, 'SoftLayer_Hardware_Server', 'getRemoteManagementAccounts', id=hardware_id
        )

        server['networkComponents'] = networkComponents.result()
        server['activeComponents'] = activeComponents.result()
        server['activeTransaction'] = activeTransaction.result()
        server['operatingSystem'] = operatingSystem.result()
        server['softwareComponents'] = softwareComponents.result()
        server['billingItem'] = billingItem.result()
        server['networkVlans'] = networkVlans.result()
        server['remoteManagementAccounts'] = remoteManagementAccounts.result()
        server['tagReferences'] = tagReferences.result()

    return server
```

So instead of having `networkComponents` in the Hardware_Server objectMask, you remove it and make its own API call to `Hardware_Server::getNetworkComponents`, and put the result in the `networkComponents` property of the Hardware_Server object. Then do the same for all the other properties as shown above. 

This can overall be faster than a single API call because with all the properties we are selecting originally, the database has to join in quite a few different tables and that can be very complex for the database. However each individual query is much simpler and can be returned very quickly. Since we are making all the seperate calls at the same time, the overall API execution time is much faster.

# Threads for two stage API calls

For this pattern, we will get a list of object Ids with one api call, then use Threads to get the details of each of those Ids. For example, instead of using SoftLayer_Account::getVirtualGuests to get all the details about all of the Virtual_Guests on your account, you would use SoftLayer_Account::getVirtualGuests to simply get the Ids of each guest, then a bunch of calls to SoftLayer_Virtual_Guest::getObject(id=guest_id) to get all of the details. For accounts with a large number of guests this can be quite a lot faster than a single API call.

[slcli bandwidth pools](https://github.com/softlayer/softlayer-python/blob/master/SoftLayer/CLI/bandwidth/pools.py#L48) is a good example of this pattern. First it gets all the bandwidth pool Ids, then uses threads to get the information about each pool (which can be a fairly long API call).

```python
def cli(env):

    # Initialize the AccountManager
    manager = AccountManager(env.client)
    # Get a lit of bandwidth pools, including the ID
    items = manager.get_bandwidth_pools()

    # Setup ThreadPool
    with cf.ThreadPoolExecutor(max_workers=5) as executor:
        # List of pool ids, to be passed into AccountManager.get_bandwidth_pool_counts()
        item_ids = [item.get('id') for item in items]
        # Builds the map, returning a tuple of the item, and the result of manager.get_bandwidth_pool_counts
        for item, servers in zip(items, executor.map(manager.get_bandwidth_pool_counts, item_ids)):
            id_bandwidth = item.get('id')
            name = item.get('name')
            print(f"{id_bandwidth}, {name}, {servers}")
```