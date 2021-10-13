---
title: "Deprecation"
description: "How Deprecation works with the SoftLayer API."
date: "2021-10-13"
tags:
    - "article"
    - "sldn"
    - "debugging"
author: "sldn"
---

If you see a notice of Deprecation on a property, method, or service on SLDN, that will generally mean that object is no longer doing anything useful, and should no longer be used. That property will be removed in a future version noted in the Deprecation Notice. `v3.2` for example would indicate that feature would no longer exist whenever v3.2 of the API comes out.

Generally once a propety or method is deprecated, it will simply return a placeholder value that matches the type it previously returned. So if a method returned an array of objects, it would instead just return an empty array.

Deprecating functionality is a rare occurance, but it does happen, and usually without much notice depending on the functionality.
