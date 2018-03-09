---
title: "API Ordering: Automatic Upgrades to Discontinued Items"
description: "<p>We recently released changes to provide a smoother process for customers with integrated ordering systems through our"
date: "2013-09-06"
author: "bshato"
tags:
    - "blog"
---

<p>We recently released changes to provide a smoother process for customers with integrated ordering systems through our API.  Previously, if an order was placed for a product or service that no longer exists, such as a discontinued server or hard drive option, the API would stop the ordering process and throw an error.  Users would then be required to backtrack through the process and revise the order to ensure all components of the product or service being ordered were available.  Our Product Team now has the ability to create upgrade-paths to prevent this from happening.</p>
<p>Upgrade-paths are created when a component to a product or service has been discontinued.  The discontinued component is associated with a replacement option (equivalent or better) that is available at an equal or lesser cost to our customers.  What exactly does this mean?  If what you're looking for is unavailable, we'll do our best to provide a way for your order to go through with similar, or better, configuration for no more than the cost of the discontinued item.  If for some reason the product was discontinued and does not have an equivalent replacement, an error would still be issued on your order.  So if our 20 GB NAS service ($10/month) is retired, but we drop our 40 GB NAS service to $10/month, we'll automatically replace the discontinued NAS service with the better one without any additional action required from you.  If the 40 GB NAS service was available, but still at the cost of $20/month, the order would error out and allow you to choose how to proceed.</p>
<p>By now I'm sure you're thinking to yourself, "Well, Bill, what if I don't want an automatic upgrade?"  That's fine, too.  We understand that this may not be the best solution for all of our customers.  If you'd like to continue to receive error messages when the available option or <a href="reference/services/SoftLayer_Product_Item_Price/">item price</a> does not match your order, you have the ability to opt out of our auto-upgrade system for your account.</p>
<p>If you would like to opt out, please <a href="http://knowledgelayer.softlayer.com/topic/sales" target="_blank">contact our Sales team</a>.  They'll go through the necessary steps to deactivate this feature for your account.  We're pretty excited about this new feature and how it will make the ordering process a bit easier as we improve our product and service options, so be sure to let us know what you think!  We'll be happy to help you out by addressing any questions or concerns that you may have.</p>
<p>-Bill</p>

