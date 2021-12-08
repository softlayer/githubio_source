---
title: "Deprecation"
description: "How Deprecation works with the SoftLayer API."
date: "2021-12-01"
tags:
    - "article"
    - "sldn"
    - "debugging"
author: "sldn"
---

As of the publication of this article, [SLDN](https://sldn.softlayer.com) will now highlight areas of the API that are deprecated in red. These features still exist, but will usually not actually do anything, and will be removed in a future version of the API.

Deprecated features will usually still return the same type of data, but with a placeholder values instead of valid data. For example a property that returned an array of objects might now just return an empty array (`[]`), or a boolean might just return `false` at all times now.

Using a deprecated object in an objectMask can cause your API call to throw an exception if that object is ever removed from the API entirely, so be careful using those properties.

As always, keep an eye on the [SLDN Release Notes](https://sldn.softlayer.com/release_notes/) for any changes to our API. A [SLDN RSS Feed](https://sldn.softlayer.com/index.xml) is available as well.