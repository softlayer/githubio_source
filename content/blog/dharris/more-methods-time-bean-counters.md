---
title: "More methods, this time for the bean counters."
description: "<p>(This post refers to SoftLayer API version 1. Check out <a href=http://sldn.softlayer.com/03/2008/and-now-for-someth"
date: "2007-07-16"
author: "dharris"
tags:
    - "blog"
---

<p>(This post refers to SoftLayer API version 1. Check out <a href="http://sldn.softlayer.com/03/2008/and-now-for-something-completely-different/">API version 3</a> for our latest updates.)</p>
<p>We've put four new methods into the API. They are:</p>
<p><strong>getInvoiceList()</strong><br />
Return a listing for each account that includes the invoice id, date, starting balance, ending balance, invoice amount, payment amount, and account type.</p>
<p><strong>getAccountBalance()</strong><br />
Return the current balance and next bill date for an account.</p>
<p><strong>getInvoice(intInvoiceId)</strong><br />
Retrieve a copy of an invoice in PDF format.</p>
<p>And by <a href="http://forums.softlayer.com/showthread.php?t=1797">request</a>:</p>
<p><strong>getServerCost(strServerIdentifier)</strong><br />
Return the "Total cost of a single server."</p>
<p>Keep’em comin’, epratt!</p>
<p>By the way, users running each of these methods must have the "View Account Summary" priviledge. You should not have any problem if you can access the accounting tools in the portal.</p>

