---
title: "SoftLayer_Network_Bandwidth_Version1_Allotment"
description: "Every SoftLayer Bandwidth Pooling, Virtual Datacenter, Virtual Private Rack(VPR) is defined in the SoftLayer_Network_Bandwidth_Version1_Allotment service as an allotment. SoftLayer allotments are a collection of servers that share all of the servers allocated bandwidth together. 

Virtual Private Rack Each server is by default a part of your Virtual Private Rack. Bandwidth overages are billed individually per server for all hardware in your Virtual Private Rack. If any one server uses more bandwidth than it is allocated, an overage charge will result. 

Bandwidth Pooling Bandwidth Pooling allow you to optimize your bandwidth usage by 'pooling' all of the bandwidth together for servers in a Bandwidth Pooling. Bandwidth overages for servers in a Bandwidth Pooling are summed up as a whole and overages are calculated only if the total bandwidth of all servers exceeds the total allocated bandwidth for all servers. 

For example, if you had 5 servers, each with 2000 GB of bandwidth, and one server used 3000 GB of bandwidth while the other used only 1500 GB of bandwidth, you would not be billed for an overage because your total usage would be 9000 GB and your total allocated would be 10000 GB. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Network_Bandwidth_Version1_Allotment"
---
