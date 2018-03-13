---
title: "How to Solve: Error fetching http headers"
description: "<p><strong>Error Fetching http headers</strong> is a common error to encounter when working with the SLAPI. Fortunatel"
date: "2013-03-19"
author: "phil"
tags:
    - "blog"
---

<p><strong>"Error Fetching http headers"</strong> is a common error to encounter when working with the SLAPI. Fortunately, it is not terribly difficult to avoid. This error most commonly met when working with a large sets of data and can be a bit cryptic, as it seems to imply some sort of connection issue. In truth, it is a client side error provided when a timeout occurs while waiting for a response from the API.</p>
<p>When this error is encountered, there are three common solutions to head off the error by remedying either the timeout directly or how the API returns the results.</p>
<h2>default_socket_timeout</h2>
<p>Raising the value of the <a href="http://www.php.net/manual/en/filesystem.configuration.php#ini.default-socket-timeout" target="_blank">default_socket_timeout</a> setting can solve this error in many situations. Some shared hosting providers may limit the use of <a href="http://php.net/manual/en/function.ini-set.php">ini_set()</a>.</p>
<h2>Object masks</h2>
<p>You can also use <a href=”http://sldn.softlayer.com/article/Extended-Object-Masks” target=”_blank”>Extended Object Masks</a> to reduce the payload to only the properties needed for the project. Unfortunately this fix may be temporary, as adding more objects to your account may push the call back into timeout. If you do not anticipate adding additional resources or  if you are confident in the low amount of required properties, this may be a long term solution to continue to avoid this error.</p>
<h2>Result limits</h2>
<p>The use of result limits allows for <a href=”http://en.wikipedia.org/wiki/Pagination#Pagination_in_Web_content_.28HTML.2C_ASP.2C_PHP.2C_and_others.29” target=”_blank”>pagination</a> of the returned objects. By setting the number of objects to return and an offset to start from, batch processing of results is possible, which results in a quicker processing time overall.</p>
<p>While the examples above are simple, hopefully it is clear how to take these concepts and modify them for your specific use case. If you continue to experience issues or run into a problem executing one of the solutions we’ve provided, feel free to reach out to sldn@softlayer.com.</p>
<p>-Phil</p>

