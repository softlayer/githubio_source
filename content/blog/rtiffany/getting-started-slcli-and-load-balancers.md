---
title: "Getting started with the SLCLI and Load Balancers "
description: "Load Balancing is a way to distribute processing and communications evenly across multiple servers within a data center "
date: "2016-01-26"
author: "rtiffany"
tags:
    - "blog"
---

Load Balancing is a way to distribute processing and communications evenly across multiple servers within a data center so that a single device does not carry an entire load.   SoftLayer Load Balancing enables customers to employ a variety of balancing methods to distribute traffic, including persistent and non-persistent options, that can be changed, activated and deactivated at any time. Today we are going to look at how to use the [Python slcli client](https://softlayer-python.readthedocs.org/en/latest/cli.html) to manage your SoftLayer Local Load balancers.

### Load Balancer details
To obtain information about our load balancer we will use the `detail` command. This will provide us with a good overview of the basic configuration of our load balancer.

<code>
$ slcli --format=raw loadbal detail local:123456
General properties  ----------
ID                 local:123456
IP Address         172.20.31.30
Datacenter         hou02
Connections limit  250
Dedicated          False
HA                 False
SSL Enabled        True
SSL Active         False
</code>

### Adding new service groups
A Service Group is used to specify the type of traffic we want to distribute between our various servers. The current options are HTTP, DNS, FTP, HTTPS, TCP, and UDP. A service group will also determine the [Balancing Methods](http://knowledgelayer.softlayer.com/faqs/27#330) or routing-methods we will use to balance our traffic. The routing-type and routing method take integer arguments which can be obtained using `slcli loadbal routing-types` and `slcli loadbal routing-methods` respectively.

In the following example we are setting up a 50/50 allocation group to balance both HTTP (routing type 2 using Round Robin) and FTP (routing type 3 using Consistent Hash IP).

<code>
$ slcli loadbal group-add --allocation 50 --port 80 --routing-type 2 --routing-method 10 local:123456
Load balancer service group is being added!

$ slcli loadbal group-add --allocation 50 --port 21 --routing-type 5 --routing-method 21 local:123456
Load balancer service group is being added!
</code>

### Adding services to an existing group
In order to add a service to an existing group we need 2 pieces of information: the Service Group ID and the ID of the health check we want to set up for the service. We can get the health check ID with the command `slcli loadbal health-checks`

<code>
$ slcli loadbal health-checks
1   TCP
2   HTTP
3   DNS
4   Ping
5   HTTP-CUSTOM
21  Default
</code>
To set up an new service to balance port 80 on the server 172.16.0.1 we set the healthcheck-type to 2 and pass the `--enabled` flag.

<code>
$ slcli loadbal service-add 123456:222089 --enabled --port 80 --weight 1 --healthcheck-type 2 --ip-address 172.16.0.1
Load balancer service is being added!

$ slcli --format=raw loadbal detail local:123456
General properties  ----------
ID                 local:123456
IP Address         172.20.31.30
Datacenter         hou02
Connections limit  250
Dedicated          False
HA                 False
SSL Enabled        True
SSL Active         False
Service group 1     **************
Group Properties   123456:222089  21  50 %  3:TCP  10:Round Robin
Services           123456:428745  172.16.0.1  80  2:HTTP  1  1  UP
Service group 2     **************
Group Properties   123456:222087  80  50 %  2:HTTP  10:Round Robin 
Services           None
</code>

### Toggle service
We can quick enable and disable a service using the `service-toggle` option and specifying the service ID:

<code>
$ slcli loadbal service-toggle 123456:428745
This action will toggle the status on the service. Continue? [y/N]: y
Load balancer service 123456:428745 status updated!
</code>

When we check the details of the Load Balancer again we can see that the Enabled flag is now set to 0 (Disabled).
<code>
$ slcli --format=raw loadbal detail local:124185|grep '123456:428745'
 Services           124185:436345  172.0.6.1 80  2:HTTP  10  0 
</code>

### Service delete
<code>
$ slcli loadbal service-delete 124185:428745
This action will cancel a service from your load balancer. Continue? [y/N]: y
Load balancer service 428745 is being cancelled!
</code>

### Service group delete
<code>
$ slcli loadbal group-delete 124185:222089
This action will cancel a service group. Continue? [y/N]: y
Service group 124185:222089 is being deleted!
</code>


