---
title: "The End Is Nigh"
description: "<p>As the depletion of IPv4 space draws nearer we have added a new requirement when placing an order which contains addt"
date: "2011-06-03"
author: "phil"
tags:
    - "blog"
---

<p>As the depletion of IPv4 space draws nearer we have added a new requirement when placing an order which contains addtional IP addresses.  In addition to the usual suspects you will need to add an additional array to your order <a href="/reference/datatypes/SoftLayer_Container_Product_Order/">container object</a>: itemCategoryQuestionAnswers.<br />
One of the SL developers, Kien Phan, was kind enough to provide the example which can be found at the bottom of this post, but for the johnny-on-the-spots out there you can get a list of the possible questions with an Object Mask of questions for <a href="http://sldn.softlayer.com/wiki/index.php/SoftLayer_Product_Item_Category">SoftLayer_Product_Item_Category</a> with a categoryId of 14(secondary IP addresses).</p>
<p>And if you happen to have your API username and key handy you can follow the link:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">https://api.softlayer.com/rest/v3/SoftLayer_Product_Item_Category/14/getObject.xml?objectMask=questions.description</pre></div>
<ul>
<li>The number of IP addresses expected to be used within the next 30 days.</li>
<li>The number of IP addresses expected to be used within the next 6 months.</li>
<li>A brief explanation of the reason(s) that additional IPs are needed.</li>
<li>The name of the contact person.</li>
<li>The job title of the contact person.</li>
<li>The email address of the contact person.</li>
<li>The phone number of the contact person.</li>
<li>The flag indicating that the user confirms that the contact information is current and accurate.</li>
</ul>
<p>-Phil</p>
<p>&nbsp;</p>
<script src="https://gist.github.com/1006343.js"> </script></p>

