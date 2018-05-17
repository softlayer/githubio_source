---
title: "How to Solve: Error fetching http headers"
description: "<p><strong>Error Fetching http headers</strong> is a common error to encounter when working with the SLAPI. Fortunatel"
date: "2013-03-19"
author: "phil"
tags:
    - "blog"
---

*"Error Fetching http headers"* is a common error to encounter when working with the SLAPI. Fortunately, it is not terribly difficult to avoid. This error most commonly met when working with a large sets of data and can be a bit cryptic, as it seems to imply some sort of connection issue. In truth, it is a client side error provided when a timeout occurs while waiting for a response from the API.


When this error is encountered, there are three common solutions to head off the error by remedying either the timeout directly or how the API returns the results.

### default_socket_timeout

Raising the value of the [default_socket_timeout](http://www.php.net/manual/en/filesystem.configuration.php#ini.default-socket-timeout) setting can solve this error in many situations. Some shared hosting providers may limit the use of [ini_set()](http://php.net/manual/en/function.ini-set.ph).


### Object masks

You can also use [Extended Object Masks](article/object-masks/) to reduce the payload to only the properties needed for the project. Unfortunately this fix may be temporary, as adding more objects to your account may push the call back into timeout. If you do not anticipate adding additional resources or  if you are confident in the low amount of required properties, this may be a long term solution to continue to avoid this error.

### Result limits

The use of result limits allows for [pagination](https://en.wikipedia.org/wiki/Pagination) of the returned objects. By setting the number of objects to return and an offset to start from, batch processing of results is possible, which results in a quicker processing time overall. Read the article on [result limits](article/using-result-limits-softlayer-api/) for how to limit how much data the SLAPI returns.


While the examples above are simple, hopefully it is clear how to take these concepts and modify them for your specific use case. 

-Phil

