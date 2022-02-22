---
title: "SoftLayer_Dns_Domain_ResourceRecord_PtrType"
description: "SoftLayer_Dns_Domain_ResourceRecord_PtrType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type'' property is set to 'ptr' and defines a reverse DNS PTR record on the SoftLayer name servers. 

The format for a reverse DNS PTR record varies based on whether it is for an IPv4 or IPv6 address. 

For an IPv4 address the ''host'' property for every PTR record is the last octet of the IP address that the PTR record belongs to, while the ''data'' property is the canonical name of the host that the reverse lookup resolves to. Every PTR record belongs to a domain on the SoftLayer name servers named by the first three octets of an IP address in reverse order followed by '.in-addr.arpa'. 

For instance, if the reverse DNS record for 10.0.0.1 is 'host.example.org' then it's corresponding SoftLayer_Dns_Domain_ResourceRecord_PtrType host is '1', while it's data property equals 'host.example.org'. The full name of the reverse record for host.example.org including the domain name is '1.0.0.10.in-addr.arpa'. 

For an IPv6 address the ''host'' property for every PTR record is the last four octets of the IP address that the PTR record belongs to.  The last four octets need to be in reversed order and each digit separated by a period.  The ''data'' property is the canonical name of the host that the reverse lookup resolves to.  Every PTR record belongs to a domain on the SoftLayer name servers named by the first four octets of an IP address in reverse order, split up by digit with a period, and followed by '.ip6.arpa'. 

For instance, if the reverse DNS record for fe80:0000:0000:0000:0000:0000:0a00:0001 is 'host.example.org' then it's corresponding SoftLayer_Dns_Domain_ResourceRecord_PtrType host is '1.0.0.0.0.0.a.0.0.0.0.0.0.0.0.0', while it's data property equals 'host.example.org'. The full name of the reverse record for host.example.org including the domain name is '1.0.0.0.0.0.a.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.e.f.ip6.arpa'. 

PTR record host names may not be changed by [SoftLayer_Dns_Domain_ResourceRecord::editObject](/reference/datatypes/$1/#$2) or [SoftLayer_Dns_Domain_ResourceRecord::editObjects](/reference/datatypes/$1/#$2). "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_ResourceRecord_PtrType"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Dns_Domain_ResourceRecord_PtrType"
---
