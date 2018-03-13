---
title: "Introduction: Deploying Drupal on SoftLayer with Chef"
description: "<p>DevOps adoption rate has substantially increased in the last couple of years across all organization sizes due to the"
date: "2014-03-05"
author: "phil"
tags:
    - "blog"
---

<p>DevOps adoption rate has substantially increased in the last couple of years across all organization sizes due to the real business value that DevOps provides in terms of agility. Automation of application installation in the cloud is an important aspect in DevOps. Traditionally, automation has been achieved via writing shell scripts. These were sufficient to manage smaller applications, but more complex runtimes required the scripts to be written in higher-level programming languages like Perl, Python and Ruby. To manage these complexities better, several automation frameworks have been developed. Chef and Puppet are examples of two such automation and configuration management frameworks.</p>
<p>This three-part series will show you how to use the Chef IT automation framework to automate the installation and configuration of Drupal on the SoftLayer infrastructure.</p>
<ol>
<li>The first installment will give you an overview of the technologies we’ll use.</li>
<li>The second installment will walk you through the setup of the Chef server and Chef workstation, then performing a manual install of Drupal on SoftLayer using the Knife command.</li>
<li>The final installment will use the SoftLayer API Client for Ruby to provision a CCI and use the Ridley Gem to manage Chef through Ruby code. This will give you an end-to-end script for provisioning and configuring an instance.<br />
<img src="http://dev-sldn151.softlayer.local/sites/default/files/drupal.png" width=700 /><br />
Core Drupal running on SoftLayer using Chef</li>
</ol>
<p>We will use three CCIs (cloud computing instances) hosted on SoftLayer: one for the Chef server, one for the Chef workstation and one for the Drupal client node. At the end of this series, you should be able to complete your own installation of Drupal in a matter of minutes.</p>
<h2>Tools and technologies used</h2>
<p><em>SoftLayer Python CLI:</em> A command line to manage and interact with the SoftLayer APIs<br />
<em>Ruby:</em> Open source programming language<br />
<em>Chef:</em> A configuration management framework written in Ruby<br />
<em>Ridley:</em> A Ruby Chef API client gem to manage your Chef server<br />
<em>Drupal:</em> An open source content management system</p>
<h2>Chef automation framework overview</h2>
<p>Chef is a systems and cloud infrastructure automation framework that makes it easy to deploy servers and applications to any physical, virtual, or cloud location, irrespective of the size of the infrastructure that is being built. It is written in Ruby programming languages. As of this writing, Chef Version 11 is the current release. Opscode, a privately held company based in Seattle, Washington, maintains and enhances the Chef tooling today. Chef uses cooking metaphors in its naming.</p>
<p>Chef is an open source tool supported by an active community. It is released under the Apache license which allows you to safely integrate Chef into your organization and to extend it to match your organization’s unique complexity, requirements, and scale. Chef is used by a large number of companies across the world, ranging from small startups to large enterprises.<br />
Once automated, Chef allows you to build or rebuild the infrastructure automatically in minutes and hours instead of weeks and months. Once the service is live, Chef gives you endless flexibility to quickly adapt on the fly.<br />
<img src="http://dev-sldn151.softlayer.local/sites/default/files/chef.png" width=700 /><br />
There are three main components in Chef:<br />
1. <em>The workstation:</em> a computer with a local Chef repository that is configured with Knife. Knife is a utility to manage the Chef server configuration and to communicate with nodes over SSH. As a developer, you can develop or download cookbooks (a collection of configuration recipes and resource definitions) on the workstation and upload them to the Chef server when ready.<br />
2. <em>The Chef server:</em> a server that acts as a hub for all the infrastructure configuration information, such as the list of clients, nodes, and corresponding configurations.<br />
3. <em>The Chef node:</em> a node is a host that runs the Chef client – a Chef agent that communicates to the Chef server using the APIs, in order to retrieve the configuration information needed for that particular node. A node is identified with its runlist (a list of recipes executed in the right order) and attributes (default settings that can be overridden).</p>
<h2>Chef components and terminology</h2>
<ul>
<li>Workstation<br />
A computer mainly used to develop and synchronize cookbooks with the Chef server. This workstation is configured to run the Knife command. </li>
<li>Knife<br />
A command line tool that helps users manage the Chef server and allows them to synchronize the workstation repository (chef-repo) with the Chef server.</li>
<li>Chef-repo<br />
A location on the workstation where cookbooks, roles, and other resources are stored. The repo is usually synchronized with a version control system.</li>
<li>Cookbook<br />
Contains all the resources needed to configure the infrastructure and distribute policies. Usually a cookbook consists of multiple recipes.</li>
<li>Recipes<br />
The most fundamental configuration in Chef. </li>
<li>Chef-client<br />
An agent that runs on every node registered with the server. The agent is responsible for performing all the steps and actions to configure the node.</li>
<li>Node<br />
A host that runs the Chef client. Roles and recipes are applied to nodes based on the defined runlist and attributes. Nodes can have one or more roles.</li>
<li>Runlist<br />
A list of recipes in each node that are applied in the exact order they are defined.</li>
<li>Chef server<br />
The centralized location where all objects needed by Chef are stored.</li>
</ul>
<h2>Drupal overview</h2>
<p>Drupal is an open source content management system (CMS) written in PHP that is used in many websites worldwide. The standard release of Drupal, known as Drupal core, contains many basic common features like user account registration, maintenance, and menu management. It is also flexible and extensible with many community add-ons, known as modules. Drupal runs on any platform that supports a web server and a database. In this series, we will use Apache2 and MySQL as defined in the default Chef cookbook.</p>
<p>In the next installment, I will show you how to set up and configure the Chef server and Chef workstation, then perform a manual installation of Drupal on SoftLayer using the Knife command.<br />
?</p>

