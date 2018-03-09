---
title: "New Features In the ExtJS 4 Model Class"
description: "<p>In 2011, Ext JS 3 was <a href=http://www.sencha.com/blog/ext-js-3-to-4-migration/>rewritten</a> from the ground up,"
date: "2013-07-18"
author: "apunjani"
tags:
    - "blog"
---

<p>In 2011, Ext JS 3 was <a href="http://www.sencha.com/blog/ext-js-3-to-4-migration/">rewritten</a> from the ground up, giving birth to <a href="http://docs.sencha.com/extjs/4.1.3/#!/guide/getting_started">Ext JS 4</a>.  With the changes, Ext JS 3's Ext.data.Record is replaced by Ext JS 4's <a href="http://docs.sencha.com/extjs/4.1.3/#!/api/Ext.data.Model">Ext.data.Model</a> class.  This class introduces a host of new capabilities that generally revolve around the data contained in the Models, which are fully customizable based on user or business preferences.  While each user may have a different need for utilizing Models, there are a few tasks that are universal when it comes to this new class:</p>
<ol>
<li>Creating Models</li>
<li>Defining relationships between Models</li>
<li>Validating Models</li>
</ol>
<p>Prior to working with Models in Ext JS 4, one or more Models must be created.  That is where we'll begin.</p>
<h2>Creating Models</h2>
<p>The Ext.data.Model class is used to represent an entity within the application, like a user, a vehicle or an account.</p>
<p>Let's look at how we would create a user Model...</p>
<p>We start by using Ext.define function to create a new class that extends the base Ext.data.Model class:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;">Ext<span style="color: #339933;">.</span><a href="http://www.php.net/define"><span style="color: #990000;">define</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'User'</span><span style="color: #339933;">,</span> <span style="color: #009900;">&#123;</span>
            extend<span style="color: #339933;">:</span> <span style="color: #0000ff;">'Ext.data.Model'</span>
<span style="color: #009900;">&#125;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>The user Model will contain one or more <a href="http://docs.sencha.com/extjs/4.1.3/#!/api/Ext.data.Field">Field</a> properties.  Fields are an array of configuration objects which define how the data will be made up:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;">Ext<span style="color: #339933;">.</span><a href="http://www.php.net/define"><span style="color: #990000;">define</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'User'</span><span style="color: #339933;">,</span> <span style="color: #009900;">&#123;</span>
            extend<span style="color: #339933;">:</span> <span style="color: #0000ff;">'Ext.data.Model'</span><span style="color: #339933;">,</span>
            fields<span style="color: #339933;">:</span><span style="color: #009900;">&#91;</span>
                <span style="color: #009900;">&#123;</span> name<span style="color: #339933;">:</span> <span style="color: #0000ff;">'id'</span><span style="color: #339933;">,</span>  type<span style="color: #339933;">:</span> <span style="color: #0000ff;">'int'</span> <span style="color: #009900;">&#125;</span><span style="color: #339933;">,</span>
                <span style="color: #009900;">&#123;</span> name <span style="color: #339933;">:</span> <span style="color: #0000ff;">'name'</span><span style="color: #339933;">,</span> type<span style="color: #339933;">:</span> <span style="color: #0000ff;">'string'</span> <span style="color: #009900;">&#125;</span>
            <span style="color: #009900;">&#93;</span>
<span style="color: #009900;">&#125;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>Now that the Model has been defined let's create an instance of it containing some arbitrary data:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">var</span> user <span style="color: #339933;">=</span> Ext<span style="color: #339933;">.</span>create<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'User'</span><span style="color: #339933;">,</span> <span style="color: #009900;">&#123;</span>
            id<span style="color: #339933;">:</span> <span style="color: #cc66cc;">1</span><span style="color: #339933;">,</span>
            name<span style="color: #339933;">:</span> <span style="color: #0000ff;">'Henry Brown'</span>
<span style="color: #009900;">&#125;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>To retrieve the data that we just set, we can use the .get property on the Model.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #666666; font-style: italic;">//prints "Henry Brown"</span>
console<span style="color: #339933;">.</span><a href="http://www.php.net/log"><span style="color: #990000;">log</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'First Name  is '</span> <span style="color: #339933;">+</span> user<span style="color: #339933;">.</span>get<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'name'</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>   </pre></div>
<h2>Defining relationships between Models</h2>
<p>Models can be linked to one another using <a href="http://docs.sencha.com/extjs/4.1.3/#!/api/Ext.data.association.Association">associations</a>. Take the SLDN, for example. It has many posts and each post is written by a user. If we were to define the relationship between a post and a user then we would say, a user has many posts and a post belongs to a user.</p>
<p>Ext JS 4 supports three types of relationships between Models.</p>
<ul>
<li><em>hasMany</em> defines a one-to-many relationship. </li>
<li><em>belongsTo</em> defines a many-to-one relationship. </li>
<li><em>hasOne</em> defines a one-to-one relationship.</li>
</ul>
<p>Let's take a look at the code for defining the relationship we just discussed.  For this example, ëUserí indicates an SLDN user, while ëPostí indicates a blog post on the SLDN.</p>
<p>The User Model now has a hasMany property which references Post.   This example indicates a single User has multiple Posts.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;">Ext<span style="color: #339933;">.</span><a href="http://www.php.net/define"><span style="color: #990000;">define</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'User'</span><span style="color: #339933;">,</span> <span style="color: #009900;">&#123;</span>
            extend<span style="color: #339933;">:</span> <span style="color: #0000ff;">'Ext.data.Model'</span><span style="color: #339933;">,</span>
            fields<span style="color: #339933;">:</span><span style="color: #009900;">&#91;</span>
                <span style="color: #009900;">&#123;</span> name<span style="color: #339933;">:</span> <span style="color: #0000ff;">'id'</span><span style="color: #339933;">,</span>  type<span style="color: #339933;">:</span> <span style="color: #0000ff;">'int'</span> <span style="color: #009900;">&#125;</span><span style="color: #339933;">,</span>
                <span style="color: #009900;">&#123;</span> name <span style="color: #339933;">:</span> <span style="color: #0000ff;">'name'</span><span style="color: #339933;">,</span> type<span style="color: #339933;">:</span> <span style="color: #0000ff;">'string'</span> <span style="color: #009900;">&#125;</span>
            <span style="color: #009900;">&#93;</span><span style="color: #339933;">,</span> 
            hasMany<span style="color: #339933;">:</span> <span style="color: #0000ff;">'Post'</span>
<span style="color: #009900;">&#125;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>The Post Model would look as follows, with the converse property of belongsTo which references User.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;">Ext<span style="color: #339933;">.</span><a href="http://www.php.net/define"><span style="color: #990000;">define</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Post'</span><span style="color: #339933;">,</span> <span style="color: #009900;">&#123;</span>
            extend<span style="color: #339933;">:</span> <span style="color: #0000ff;">'Ext.data.Model'</span><span style="color: #339933;">,</span>
            fields<span style="color: #339933;">:</span><span style="color: #009900;">&#91;</span>
                <span style="color: #009900;">&#123;</span> name<span style="color: #339933;">:</span> <span style="color: #0000ff;">'id'</span><span style="color: #339933;">,</span>  type<span style="color: #339933;">:</span> <span style="color: #0000ff;">'int'</span> <span style="color: #009900;">&#125;</span><span style="color: #339933;">,</span>
                <span style="color: #009900;">&#123;</span> name<span style="color: #339933;">:</span> <span style="color: #0000ff;">'user_id'</span><span style="color: #339933;">,</span>  type<span style="color: #339933;">:</span> <span style="color: #0000ff;">'int'</span> <span style="color: #009900;">&#125;</span><span style="color: #339933;">,</span>
                <span style="color: #009900;">&#123;</span> name <span style="color: #339933;">:</span> <span style="color: #0000ff;">'title'</span><span style="color: #339933;">,</span> type<span style="color: #339933;">:</span> <span style="color: #0000ff;">'string'</span> <span style="color: #009900;">&#125;</span><span style="color: #339933;">,</span>
                <span style="color: #009900;">&#123;</span> name<span style="color: #339933;">:</span> <span style="color: #0000ff;">'body'</span><span style="color: #339933;">,</span> type<span style="color: #339933;">:</span> <span style="color: #0000ff;">'string'</span> <span style="color: #009900;">&#125;</span>
            <span style="color: #009900;">&#93;</span><span style="color: #339933;">,</span>
            belongsTo<span style="color: #339933;">:</span> <span style="color: #0000ff;">'User'</span>
<span style="color: #009900;">&#125;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>After defining the Models with the relationships we can now create an instance of the user Model:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">var</span> user <span style="color: #339933;">=</span> Ext<span style="color: #339933;">.</span>create<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'User'</span><span style="color: #339933;">,</span> <span style="color: #009900;">&#123;</span>
            id<span style="color: #339933;">:</span> <span style="color: #cc66cc;">1</span><span style="color: #339933;">,</span>
            name<span style="color: #339933;">:</span> <span style="color: #0000ff;">'Henry Brown'</span>
<span style="color: #009900;">&#125;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>Let's add a post to the user we created above</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;">user<span style="color: #339933;">.</span>posts<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">.</span>add<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#123;</span>
            title<span style="color: #339933;">:</span> <span style="color: #0000ff;">'This is the post title'</span><span style="color: #339933;">,</span>
            body<span style="color: #339933;">:</span> <span style="color: #0000ff;">'This is the body of the post'</span>
<span style="color: #009900;">&#125;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>  </pre></div>
<p>To look at the data for the post that you just added, get the first post and print it to the console using the code below.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #666666; font-style: italic;">// prints the post object we inserted above</span>
console<span style="color: #339933;">.</span><a href="http://www.php.net/log"><span style="color: #990000;">log</span></a><span style="color: #009900;">&#40;</span> user<span style="color: #339933;">.</span>posts<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">.</span>first<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">.</span>data <span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<h2>Validating Models</h2>
<p>Model <a href="http://docs.sencha.com/extjs/4.1.3/#!/api/Ext.data.validations">validations</a> follow the same format as Field definitions. We specify a Field and a type of validation. The five types of validations built in by default are:</p>
<ul>
<li><em>presence</em> ensures that the field has a value.</li>
<li><em>length</em> ensures the string is between a min and max length.</li>
<li><em>format</em> ensures that the string matches a regular expression.</li>
<li><em>inclusion</em> ensures that a value is within a specific set of values.</li>
<li><em>exclusion</em> ensures that a value is not one of the specific set of values.</li>
</ul>
<p>Let's build on our User Model from the previous example and add validation checks to it. Specifically, we will check to make sure that the name is present.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;">Ext<span style="color: #339933;">.</span><a href="http://www.php.net/define"><span style="color: #990000;">define</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'User'</span><span style="color: #339933;">,</span> <span style="color: #009900;">&#123;</span>
            extend<span style="color: #339933;">:</span> <span style="color: #0000ff;">'Ext.data.Model'</span><span style="color: #339933;">,</span>
            fields<span style="color: #339933;">:</span><span style="color: #009900;">&#91;</span>
                <span style="color: #009900;">&#123;</span> name<span style="color: #339933;">:</span> <span style="color: #0000ff;">'id'</span><span style="color: #339933;">,</span>  type<span style="color: #339933;">:</span> <span style="color: #0000ff;">'int'</span> <span style="color: #009900;">&#125;</span><span style="color: #339933;">,</span>
                <span style="color: #009900;">&#123;</span> name <span style="color: #339933;">:</span> <span style="color: #0000ff;">'name'</span><span style="color: #339933;">,</span> type<span style="color: #339933;">:</span> <span style="color: #0000ff;">'string'</span> <span style="color: #009900;">&#125;</span>
            <span style="color: #009900;">&#93;</span><span style="color: #339933;">,</span>
            validations<span style="color: #339933;">:</span> <span style="color: #009900;">&#91;</span>
                <span style="color: #009900;">&#123;</span> type<span style="color: #339933;">:</span> <span style="color: #0000ff;">'presence'</span><span style="color: #339933;">,</span> name<span style="color: #339933;">:</span> <span style="color: #0000ff;">'name'</span> <span style="color: #009900;">&#125;</span>
            <span style="color: #009900;">&#93;</span><span style="color: #339933;">,</span>
            hasMany<span style="color: #339933;">:</span> <span style="color: #0000ff;">'Post'</span>
<span style="color: #009900;">&#125;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>To see how the validations work, create a User instance and populate just the id. Then validate the instance.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #666666; font-style: italic;">// Create a user instance with just the id</span>
<span style="color: #000000; font-weight: bold;">var</span> newUser <span style="color: #339933;">=</span> Ext<span style="color: #339933;">.</span>create<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'User'</span><span style="color: #339933;">,</span> <span style="color: #009900;">&#123;</span>
            id<span style="color: #339933;">:</span> <span style="color: #cc66cc;">1</span>
<span style="color: #009900;">&#125;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #666666; font-style: italic;">// validate the new user</span>
<span style="color: #000000; font-weight: bold;">var</span> errors <span style="color: #339933;">=</span> newUser<span style="color: #339933;">.</span>validate<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
&nbsp;
<span style="color: #666666; font-style: italic;">// isValid would return false</span>
console<span style="color: #339933;">.</span><a href="http://www.php.net/log"><span style="color: #990000;">log</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Is this user valid ? '</span><span style="color: #339933;">,</span> errors<span style="color: #339933;">.</span>isValid<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;">//error.items would return the array of errors found on this User Model.</span>
console<span style="color: #339933;">.</span><a href="http://www.php.net/log"><span style="color: #990000;">log</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Errors'</span>  <span style="color: #339933;">,</span> errors<span style="color: #339933;">.</span>items<span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
<span style="color: #666666; font-style: italic;">//get array of errors specific to a field by using getByField</span>
console<span style="color: #339933;">.</span><a href="http://www.php.net/log"><span style="color: #990000;">log</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Name errors '</span><span style="color: #339933;">,</span> errors<span style="color: #339933;">.</span>getByField<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'name'</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span></pre></div>
<p>The new Ext JS 4 Data Package has a lot more to offer than what we have covered, but, hopefully you gained an understanding of creating, associating and validating Models.  For more information on using Ext JS 4.1, refer to Sencha's <a href="http://docs.sencha.com/extjs/4.1.3/">online documentation</a>.</p>
<p>-Aziz</p>

