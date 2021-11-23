---
title: "SoftLayer_Network_Pod"
description: "SoftLayer_Network_Pod refers to a portion of a data center that share a Backend Customer Router (BCR) and usually a front-end counterpart known as a Frontend Customer Router (FCR). A Pod primarily denotes a logical location within the network and the physical aspects that support networks. This is in contrast to representing a specific physical location. 

A ``Pod`` is identified by a ``name``, which is unique. A Pod name follows the format 'dddnn.podii', where 'ddd' is a data center code, 'nn' is the data center number, 'pod' is a literal string and 'ii' is a two digit, left-zero- padded number which corresponds to a Backend Customer Router (BCR) of the desired data center. Examples: <ul> <li>dal09.pod01 = Dallas 9, Pod 1 (ie. bcr01)</li> <li>sjc01.pod04 = San Jose 1, Pod 4 (ie. bcr04)</li> <li>ams01.pod01 = Amsterdam 1, Pod 1 (ie. bcr01)</li> </ul> "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Pod"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Network_Pod"
---
