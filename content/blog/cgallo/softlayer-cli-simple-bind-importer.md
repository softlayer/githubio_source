---
title: "SoftLayer CLI Simple Bind Importer"
description: "We added a new feature, a simple bind importer, to the python CLI client that allows users to easily import bind style D"
date: "2015-01-02"
author: "cgallo"
tags:
    - "blog"
---

We added a new feature, a simple bind importer, to the python CLI client that allows users to easily import bind style DNS zones into the SoftLayer DNS system. Before diving into the caveats that come with dealing with a file format that seems to be more human readable than machine readable, let’s discuss how to use it.

<code>~$ sl dns import 
usage: sl dns import <file> [—dryRun]
~$ sl dns import realtest.test </code>

It’s quite simple—specify which zone file to import, and then the magic happens. By adding the optional argument “—dryRun”, no records will actually be created on the SoftLayer side and will give a good idea of what records it will try to create. 

<strong>Importer in Action</strong>

Here is an example of a file I will try to import. Although simple it does have most of the common record types and some randomly formatted records of a typical bind file.

<code>~$ cat realtest.test 
$ORIGIN realtest.test.
$TTL 86400
@ IN SOA ns1.softlayer.com. support.softlayer.com. (
                       2014052300        ; Serial
                       7200              ; Refresh
                       600               ; Retry
                       1728000           ; Expire
                       43200)            ; Minimum
@                      86400    IN NS    ns1.softlayer.com.
@                      86400    IN NS    ns2.softlayer.com.
                        IN MX 10 test.realtest.test.
testing                86400    IN A     127.0.0.1
testing1               86400    IN A     12.12.0.1
server2      IN   A  1.0.3.4
ftp                             IN  CNAME server2
dev.realtest.test    IN  TXT "This is just a test of the txt record"
    IN  AAAA  2001:db8:10::1
spf  IN TXT "v=spf1 ip4:192.0.2.0/24 ip4:198.51.100.123 a -all”</code>

<strong>Here is the output of a dryRun.</strong>

<code>~$ ./sl dns import realtest.test --dryRun
Starting up a dry run...
SKIPPED: Host: @ TTL: None Type: IN Record: SOA ns1.softlayer.com. support.softlayer.com. (
Parsed: Host: @ TTL: 86400 Type: NS Record: ns1.softlayer.com.
Parsed: Host: @ TTL: 86400 Type: NS Record: ns2.softlayer.com.
Parsed: Host: @ TTL: None Type: MX Record: test.realtest.test.
Parsed: Host: testing TTL: 86400 Type: A Record: 127.0.0.1
Parsed: Host: testing1 TTL: 86400 Type: A Record: 12.12.0.1
Parsed: Host: server2 TTL: None Type: A Record: 1.0.3.4
Parsed: Host: ftp TTL: None Type: CNAME Record: server2
Parsed: Host: dev.realtest.test TTL: None Type: TXT Record: "This is just a test of the txt record"
Parsed: Host: @ TTL: None Type: AAAA Record: 2001:db8:10::1
Parsed: Host: spf TTL: None Type: TXT Record: "v=spf1 ip4:192.0.2.0/24 ip4:198.51.100.123 a -all"
Finished</code>

<strong>Caveats and Special Considerations</strong>

If the importer encounters a record it does not know what to do with, it will mark it as SKIPPED. The SOA record is skipped automatically because SoftLayer adds its own SOA record to all zones. 
While specifying a hostname is optional in bind, SoftLayer requires one, so any empty hostname is replaced with the @ symbol, which has the same meaning. 

If the importer has problems adding a record, it will display the error, but keep trying to import the rest of the zone.

The importer will only read a single line entry, so records that span multiple lines will be skipped.

MX records will always have a weight of 10 because the python client doesn’t support differing weights (yet).

If you have a zone that this importer fails, please feel free to open an issue on <a href="https://github.com/softlayer/softlayer-python">github</a>  with the zone file, and I’ll see about getting it corrected. Or, since it is an open source project, I’d love to see pull requests if you are into that sort of thing.

Hopefully you find this tool to be useful.

\\-Chris


