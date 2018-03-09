---
title: "Ember-cli-defeatureify Addon: Feature Flag Support and Stripping of Debug Statements "
description: "If you have ever used a canary build of the Ember.js framework, you are likely familiar with feature flags. Used to bund"
date: "2015-06-03"
author: "jbrown"
tags:
    - "blog"
---

If you have ever used a canary build of the Ember.js framework, you are likely familiar with feature flags. Used to bundle functionality and make it available in an application, it also allows for its use to be turned on or off via an entry in the application’s configuration file. While used by the Ember.js community to allow for an easy way to test new, and sometimes experimental, features in upcoming releases of Ember.js, there are times when such capabilities can be useful in your own applications. And thanks to the [ember-cli-defeatureify](https://github.com/jkarsrud/ember-cli-defeatureify) addon, you can use and test it out too!

#####Feature Flags
To have features of your codebase removed from a production build of your application but remain during development, you simply need to identify the sections of code to be managed by a feature flag. To do this, utilize the <code>isEnabled()</code> method:

<center><code>if ( <namespace>.FEATURES.isEnabled('<flagName>') ) {...}</code></center>

In this example, <code>**<namespace>**</code> refers to either the name of your application from the <code>package.json</code> file or to the value set in the namespace property in the configuration. <code>**<flagName>**</code> refers to the name of the flag used to enable and disable the code features.

Now that you have used this configuration to identify which features should be affected by feature flags, you need to configure your application to use them by adding the following to your application's <code>Brocfile.js</code>:

<javascript>var app = new EmberApp({
    defeatureify: {
        features: {
            'highlightMissingToken': true
        }
    }
});
</javascript>

Set each specified flag's value to *true* if you desire to have it enabled in a production build.

#####Strip Debug Statements

Ember-cli-defeatureify addon can strip debug statements out of your codebase during a production build—another use not discussed or demonstrated as prominently in its documentation. Any console statements inadvertently left in the code during development will not affect the user experience in your deployed application.

To enable this feature of the addon, set the <code>enableStripDebug</code> property to true, and then provide an array of statements to strip out in the <code>debugStatements</code> property.  You can leverage both the stripping of debug statements and the use of feature flags within the same codebase and configuration. If you are not employing any feature flags, be certain to set the <code>features</code> property to an empty object so you will not encounter build errors.

While you can reference the console namespace directly in the array of statements set on the <code>debugStatements</code> property, you will need to reference any Ember ones using <code>Ember.default</code> rather than just <code>Ember</code>. Below is an example configuration that SoftLayer uses to build its production Ember applications:

<javascript>var app = new EmberApp({
    defeatureify: {
        'enableStripDebug': true,
        'debugStatements': [
            'Ember.default.warn',
            'Ember.default.assert',
            'Ember.default.deprecate',
            'Ember.default.debug',
            'Ember.default.Logger.assert',
            'Ember.default.Logger.debug',
            'Ember.default.Logger.error',
            'Ember.default.Logger.info',
            'Ember.default.Logger.log',
            'Ember.default.Logger.warn',
            'console.assert',
            'console.clear',
            'console.count',
            'console.debug',
            'console.dir',
            'console.dirxml',
            'console.error',
            'console.group',
            'console.groupCollapsed',
            'console.groupEnd',
            'console.info',
            'console.log',
            'console.profile',
            'console.profileEnd',
            'console.select',
            'console.table',
            'console.time',
            'console.timeEnd',
            'console.trace',
            'console.warn'
        ],
        'features': {}
    }
});
</javascript>

For questions, comments, or for more information, visit [github.com](https://github.com/jkarsrud/ember-cli-defeatureify). 

-Jeremy


