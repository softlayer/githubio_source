---
title: "Redirection and Controller Workflow"
description: "<p>A common problem when developing controller functionality is how to structure the workflow of the page. You have to m"
date: "2013-09-05"
author: "tvance"
tags:
    - "blog"
---

<p>A common problem when developing controller functionality is how to structure the workflow of the page. You have to make sure that the different scenarios are accounted for and make sense to the end user, but you also want to make sure that your code stays neat and easy to maintain. </p>
<p>A good solution to this common problem is to break up your functionality into two discrete categories and use header redirection to navigate between controller actions that only belong to one category or the other. One type of action is going to show information to the user. This includes tables, forms, reports, etc. that send information from the application out, usually to a user's web browser. The second type of action is to take data in, usually from a form submission. The top-level process flow is greatly simplified when these two basic categories of task are kept discrete.</p>
<p>I'll use a generic example. We needed a new management interface for resources. The way these resources work is that each resource has a date range during which the resource is in use. It is important that we do not modify any history, or change dates for resources that have already gone into use.</p>
<p>NOTE: This makes some assumptions about our strategy and architecture. If, for example, we were using a heavy client-side technology to make our pages single-page applications, this would be less relevant. For our architecture, however, this solution can simplify our controller logic and make our code efficient and simple.</p>
<h2>Category One: Display Actions</h2>
<p>Start by designing what your user is going to look at. In our case we have three basic displays: a listing page, a form to create/edit a resource, and a form to edit a resource that is already in progress. In this third display we will have a very limited set of information we can change. So our controller will start with three actions, one for each display: manage, edit, and limitedEdit.</p>
<p>Once you have those actions defined, it should be pretty simple to teach each action how to pull the information you need and then pass control to the template you want to display. I'll add some fake code (shorter than the real code) that will illustrate this step.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">public</span> <span style="color: #000000; font-weight: bold;">function</span> manage<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span>
<span style="color: #009900;">&#123;</span>
    <span style="color: #000088;">$resources</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">getResourceInformation</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">renderTempalte</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'manage.tpl.php'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span>
&nbsp;
<span style="color: #000000; font-weight: bold;">public</span> <span style="color: #000000; font-weight: bold;">function</span> edit<span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span>
<span style="color: #009900;">&#123;</span>
    <span style="color: #000088;">$resource</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">getResource</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">renderTemplate</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'edit.tpl.php'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span>
&nbsp;
<span style="color: #000000; font-weight: bold;">public</span> <span style="color: #000000; font-weight: bold;">function</span> limitedEdit<span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span>
<span style="color: #009900;">&#123;</span>
    <span style="color: #000088;">$resource</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">getResource</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">renderTemplate</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'limitedEdit.tpl.php'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span></pre></div>
<h2>Category Two: Data Submission</h2>
<p>Next, figure out how data will get into your system. In our case, we really need two actions to take data in, one to save changes to a record or a new record entirely and an action to cancel an already created record. Make sure to use enough different types of actions so that each one is fairly straightforward.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">public</span> <span style="color: #000000; font-weight: bold;">function</span> save<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span>
<span style="color: #009900;">&#123;</span>
    <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">updateRecordFromData</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$_POST</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span>
&nbsp;
<span style="color: #000000; font-weight: bold;">public</span> <span style="color: #000000; font-weight: bold;">function</span> cancel<span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span>
<span style="color: #009900;">&#123;</span>
    <span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span><span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceAlreadyInUse</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
        <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">endAlreadyInUseResource</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #009900;">&#125;</span>
    <span style="color: #b1b100;">else</span> <span style="color: #009900;">&#123;</span>
        <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">deleteResourceRecord</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #009900;">&#125;</span>
<span style="color: #009900;">&#125;</span></pre></div>
<h2>Final Step - Piecing it Together</h2>
<p>This is great, but we have a problem: our save and cancel don't do anything or send the user anywhere useful. This is easy to fix. We also have a new tool to help us have good user interaction when using this strategy, the setPersistentMessage() method in the controller class. What this new method allows us to do is to tell the controller to display a message after our next redirect. That way we can perform data updates in a save() method, tell the system to display a message after a redirect, then do that redirect. The user will then see a message on the listing page which will tell them their operation succeeded. The setPersistentMessage() calls in this code example will be real and usable in your own code.</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;">public</span> <span style="color: #000000; font-weight: bold;">function</span> save<span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span>
<span style="color: #009900;">&#123;</span>
    <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">updateRecordFromData</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$_POST</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
&nbsp;
    <span style="color: #666666; font-style: italic;">// note how we are using the action we are about to redirect to, not the action we are in right now for the message key</span>
    <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">setPersistentMessage</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Resource/manage'</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">'Your data was saved successfully.'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">headerRedirect</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'manage'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span>
&nbsp;
<span style="color: #000000; font-weight: bold;">public</span> <span style="color: #000000; font-weight: bold;">function</span> cancel<span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span>
<span style="color: #009900;">&#123;</span>
    <span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span><span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">resourceAlreadyInUse</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
        <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">endAlreadyInUseResource</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #009900;">&#125;</span>
    <span style="color: #b1b100;">else</span> <span style="color: #009900;">&#123;</span>
        <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">deleteResourceRecord</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$id</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #009900;">&#125;</span>
&nbsp;
    <span style="color: #666666; font-style: italic;">// note how we are using the action we are about to redirect to, not the action we are in right now for the message key</span>
    <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">setPersistentMessage</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Resource/manage'</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">'Your resource was cancelled successfully.'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
    <span style="color: #000088;">$this</span><span style="color: #339933;">-></span><span style="color: #004000;">headerRedirect</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'manage'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span></pre></div>
<p>Most, if not all, developers have seen this pattern even if they were not quite aware how to categorize it. Especially with the new setPersistentMessage() helper method this pattern should be easy to implement and facilitates targeted quality controllers that are easy to implement and maintain.</p>
<p>-Tony</p>

