---
title: "SoftLayer SDKs"
description: "A list of the various SDKs for easily interacting with the SoftLayer API."
date: "2012-03-24"
tags:
    - "tools"
---

The following is a list of language specific bindings for interacting with the SoftLayer API. None of these are strictly required to use the API, but will likely make using the API a lot easier.



### [Softlayer-Python](https://github.com/softlayer/softlayer-python)

This library provides a simple Python client to interact with SoftLayer's XML-RPC or REST API.

A command-line interface is also included and can be used to manage various SoftLayer products and services.

### [SoftLayer-Go](https://github.com/softlayer/softlayer-go)

This library contains a complete implementation of the SoftLayer API for client application development in the Go programming language. Code for each API data type and service method is pre-generated, using the SoftLayer API metadata endpoint as input, thus ensuring 100% coverage of the API right out of the gate.

It was designed to feel as natural as possible for programmers familiar with other popular SoftLayer SDKs, and attempts to minimize unnecessary boilerplate and type assertions where possible.

### [SoftLayer-Java](https://github.com/softlayer/softlayer-java)

This library provides a JVM client for the SoftLayer API. It has code generated and compiled via Maven. The client can work with any Java 8+ runtime. It uses the code generation project in gen/ to generate the service and type related code. Although likely to work in resource-constrained environments (i.e. Android, J2ME, etc), using this is not recommended; Use the REST API instead.

### [SoftLayer-Ruby](https://github.com/softlayer/softlayer-ruby)

The softlayer-ruby project creates a Ruby Gem which provides language bindings to the SoftLayer API for the Ruby programming language.

The heart of the project a foundation layer (represented by the Client and Service classes) that allows SoftLayer customers to make direct calls to the SoftLayer API. The Gem also builds a object heirarchy on top of that foundation which provides an abstract model which insulates scripts from direct dependency on the low-level details of the SoftLayer API.

More comprehensive documentation on using the softlayer_api Gem, and contributing to the project, may be found by cloning this project and generating the documentation.

### [SoftLayer-PHP](https://github.com/softlayer/softlayer-api-php-client)

The SoftLayer API PHP client classes provide a simple method for connecting to and making calls from the SoftLayer API and provides support for many of the SoftLayer API's features. Method calls and client management are handled by the PHP SOAP and XML-RPC extensions.