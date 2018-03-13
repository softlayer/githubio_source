---
title: "View Controller Containment in SoftLayer Mobile HD"
description: "<p>SoftLayer Mobile HD version 1.2 introduced dual-pane browser functionality to provide a superior experience while int"
date: "2012-06-19"
author: "pkijowski"
tags:
    - "blog"
---

<p>SoftLayer Mobile HD version 1.2 introduced dual-pane browser functionality to provide a superior experience while interacting with our highly scalable cloud storage system, <a href="http://www.softlayer.com/cloudlayer/storage">Object Storage</a>. The browser takes advantage of a new feature in Apple’s iOS 5: view controller containment.</p>
<p>The iPad Object Storage browser incorporates functionality similar to that found in the Mac OS X Finder’s file browser that should be familiar to Mac OS X users. The metaphor has been reworked slightly so that it fits well on a mobile device screen. Like the Finder, the SoftLayer Mobile HD Object Storage browser has multiple panes representing the object hierarchy of Object Storage’s virtual file system. In order to fit this multi-pane navigation to the iPad’s smaller screen, the SoftLayer design team uses only two panes to represent the Object Storage structure.<br />
<img src="/sites/default/files/1.png" style="height: 75%; width: 75%; margin: auto;" /><br />
<strong>Figure 1 Dual-pane Object Storage browser</strong></p>
<p>The user navigates through the Object Storage hierarchy by tapping on files and folders. Tapping storage container or folder allows the user to navigate through the Object Storage hierarchy. As the user moves deeper, the panes shift to the right revealing the deeper levels of the hierarchy. Tapping a file, or selecting the accessory button next to a container or folder, presents additional information about the object. A browser-like back button, located in the left upper corner of the screen, allows for navigation back toward the root of the storage system.</p>
<p>Operations such as creating new containers, uploading files and refreshing folder content are readily available through a context sensitive action menu. (Figure 2)</p>
<p><img src="/sites/default/files/2.png" style="height: 70%; width: 70%" /><br />
<strong>Figure 2 Context sensitive action menu</strong></p>
<p>The user can switch between storage clusters at any time while browsing by tapping on the button with globe icon located in the right upper corner of the screen and selecting desired cluster. (Figure 3)</p>
<p><img src="/sites/default/files/3.png" style="height: 70%; width: 70%" /><br />
<strong>Figure 3 Storage cluster selection</strong></p>
<p>Large Object Storage data sets require a quick and reliable way to find the right objects quickly; therefore the Object Storage module provides search functionality. This is accessed using the search bar immediately above the browser, right at the users fingertips. When a search term is entered into the search bar, the dual-pane browser will context switch to search mode and display any objects found which meet the search terms provided. When done searching, a user can either navigate back from search results or simply clear the search bar field to return the browser to its normal operation. (Figure 4)</p>
<p><img src="/sites/default/files/4.png" style="height: 70%; width: 70%" /><br />
<strong>Figure 4 Account search</strong></p>
<p><img src="/sites/default/files/5.png" style="height: 70%; width: 70%" /><br />
<strong>Figure 5 Object Storage Module High Level Design</strong></p>
<p>Object Storage Module was designed to have an <span class="geshifilter"><code class="text geshifilter-text">SLStorageModule</code></span> class acting as a container for browser panes. Its only purpose is to manage browser panes i.e.: adding, removing and transitioning between the panes. The <span class="geshifilter"><code class="text geshifilter-text">SLStorageModule</code></span> takes advantage of iOS feature called: view controller containment; since iOS 5.0 subclasses of <span class="geshifilter"><code class="text geshifilter-text">UIViewController</code></span> can act as containers for other view controllers. This means that the container view controller can easily manage the presentation and interaction behavior of other view controllers. The following methods of the <span class="geshifilter"><code class="text geshifilter-text">UIViewController</code></span> class provide the convenient child view controller functionality:<br />
*addChildViewController:<br />
*removeFromParentViewController<br />
*transitionFromViewController:toViewController:duration:options:animations:completion:<br />
*willMoveToParentViewController:<br />
*didMoveToParentViewController:<br />
*automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers</p>
<p>The logic that controls what view controllers the dual-pane browser is supposed to display for the next level is left to sub-view controllers, called Browser Panes, which know about the Object Storage content and have enough knowledge to make that decision.</p>
<p>The <span class="geshifilter"><code class="text geshifilter-text">SLStorageModule</code></span> exposes pane operations for its child view controllers through push:from:animated and pop:animated methods. (Figure 6 and Figure 7)</p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #008000;">-</span> <span style="color: #000000;">&#40;</span><span style="color: #0600FF;">void</span><span style="color: #000000;">&#41;</span> push<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span>UIViewController <span style="color: #008000;">*</span><span style="color: #000000;">&#41;</span> newViewController from<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span>UIViewController <span style="color: #008000;">*</span><span style="color: #000000;">&#41;</span> existingViewController animated<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span><span style="color: #FF0000;">BOOL</span><span style="color: #000000;">&#41;</span> animated
<span style="color: #000000;">&#123;</span>
    <span style="color: #000000;">&#91;</span>self addChildViewController<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
    <span style="color: #FF0000;">float</span> animationDuration <span style="color: #008000;">=</span> <span style="color: #FF0000;">0.0</span><span style="color: #008000;">;</span>
    <span style="color: #0600FF;">if</span> <span style="color: #000000;">&#40;</span>animated<span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
        animationDuration <span style="color: #008000;">=</span> <span style="color: #FF0000;">0.5</span><span style="color: #008000;">;</span>
    <span style="color: #000000;">&#125;</span>
&nbsp;
    <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">view</span> addSubview<span style="color: #008000;">:</span> newViewController.<span style="color: #0000FF;">view</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
    <span style="color: #000000;">&#91;</span>newViewController willMoveToParentViewController<span style="color: #008000;">:</span> self<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
    <span style="color: #0600FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> count<span style="color: #000000;">&#93;</span> <span style="color: #008000;"><</span>h2<span style="color: #008000;">></span> <span style="color: #FF0000;">1</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
        <span style="color: #000000;">&#91;</span>newViewController viewWillAppear<span style="color: #008000;">:</span> YES<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#91;</span>self notifyViewWillMoveToLeftPane<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#91;</span>self moveOffScreenLeft<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#91;</span>UIView animateWithDuration<span style="color: #008000;">:</span>animationDuration animations<span style="color: #008000;">:^</span><span style="color: #000000;">&#123;</span>
            <span style="color: #000000;">&#91;</span>self moveToLeftPane<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#125;</span> completion<span style="color: #008000;">:^</span><span style="color: #000000;">&#40;</span><span style="color: #FF0000;">BOOL</span> finished<span style="color: #000000;">&#41;</span> <span style="color: #000000;">&#123;</span>
            <span style="color: #000000;">&#91;</span>self notifyViewDidMoveToLeftPane<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
            <span style="color: #000000;">&#91;</span>newViewController didMoveToParentViewController<span style="color: #008000;">:</span> self<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
            <span style="color: #000000;">&#91;</span>newViewController viewDidAppear<span style="color: #008000;">:</span> YES<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#125;</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
    <span style="color: #000000;">&#125;</span>
    <span style="color: #0600FF;">else</span> <span style="color: #0600FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> count<span style="color: #000000;">&#93;</span> <span style="color: #008000;"></</span>h2<span style="color: #008000;">></span> <span style="color: #FF0000;">2</span><span style="color: #000000;">&#41;</span> 
    <span style="color: #000000;">&#123;</span>
        <span style="color: #000000;">&#91;</span>newViewController viewWillAppear<span style="color: #008000;">:</span> YES<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#91;</span>self notifyViewWillMoveToRightPane<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#91;</span>self moveOffScreenRight<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#91;</span>UIView animateWithDuration<span style="color: #008000;">:</span> animationDuration animations<span style="color: #008000;">:^</span><span style="color: #000000;">&#123;</span>
            <span style="color: #000000;">&#91;</span>self moveToRightPane<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#125;</span> completion<span style="color: #008000;">:</span> <span style="color: #008000;">^</span><span style="color: #000000;">&#40;</span><span style="color: #FF0000;">BOOL</span> finished<span style="color: #000000;">&#41;</span> <span style="color: #000000;">&#123;</span>
            <span style="color: #000000;">&#91;</span>self notifyViewDidMoveToRightPane<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
            <span style="color: #000000;">&#91;</span>newViewController didMoveToParentViewController<span style="color: #008000;">:</span> self<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span> 
            <span style="color: #000000;">&#91;</span>newViewController viewDidAppear<span style="color: #008000;">:</span> YES<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#125;</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
    <span style="color: #000000;">&#125;</span>
    <span style="color: #0600FF;">else</span> 
    <span style="color: #000000;">&#123;</span>
        <span style="color: #0600FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #000000;">&#91;</span>self isLeftPaneController<span style="color: #008000;">:</span> existingViewController<span style="color: #000000;">&#93;</span><span style="color: #000000;">&#41;</span>
        <span style="color: #000000;">&#123;</span>            
            NSUInteger newViewControllerIndex <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> count<span style="color: #000000;">&#93;</span> <span style="color: #008000;">-</span> <span style="color: #FF0000;">1</span><span style="color: #008000;">;</span>
            UIViewController <span style="color: #008000;">*</span>currentRightViewController <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> objectAtIndex<span style="color: #008000;">:</span> newViewControllerIndex <span style="color: #008000;">-</span> <span style="color: #FF0000;">1</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
            <span style="color: #000000;">&#91;</span>self moveToRightPane<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
            <span style="color: #000000;">&#91;</span>currentRightViewController willMoveToParentViewController<span style="color: #008000;">:</span> self<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
            <span style="color: #000000;">&#91;</span>self transitionFromViewController<span style="color: #008000;">:</span> currentRightViewController 
                              toViewController<span style="color: #008000;">:</span> newViewController
                                      duration<span style="color: #008000;">:</span> animationDuration
                                       options<span style="color: #008000;">:</span> UIViewAnimationOptionTransitionCrossDissolve
                                    animations<span style="color: #008000;">:</span> <span style="color: #008000;">^</span><span style="color: #000000;">&#123;</span>
                                    <span style="color: #000000;">&#125;</span> 
                                    completion<span style="color: #008000;">:</span> <span style="color: #008000;">^</span><span style="color: #000000;">&#40;</span><span style="color: #FF0000;">BOOL</span> finshed<span style="color: #000000;">&#41;</span> <span style="color: #000000;">&#123;</span>
&nbsp;
                                        <span style="color: #000000;">&#91;</span>self notifyViewDidMoveToRightPane<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
                                        <span style="color: #000000;">&#91;</span>currentRightViewController removeFromParentViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
                                        <span style="color: #000000;">&#91;</span>newViewController didMoveToParentViewController<span style="color: #008000;">:</span> self<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
                                    <span style="color: #000000;">&#125;</span>
             <span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
            <span style="color: #000000;">&#91;</span>currentRightViewController removeFromParentViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#125;</span>
        <span style="color: #0600FF;">else</span>
        <span style="color: #000000;">&#123;</span>
            self.<span style="color: #0000FF;">backButton</span>.<span style="color: #0000FF;">enabled</span> <span style="color: #008000;">=</span> YES<span style="color: #008000;">;</span>
&nbsp;
            <span style="color: #000000;">&#91;</span>self moveOffScreenRight<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
            NSUInteger newViewControllerIndex <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> count<span style="color: #000000;">&#93;</span> <span style="color: #008000;">-</span> <span style="color: #FF0000;">1</span><span style="color: #008000;">;</span>
            UIViewController <span style="color: #008000;">*</span>currentLeftViewController <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> objectAtIndex<span style="color: #008000;">:</span> newViewControllerIndex <span style="color: #008000;">-</span> <span style="color: #FF0000;">2</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
            UIViewController <span style="color: #008000;">*</span>currentRightViewController <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> objectAtIndex<span style="color: #008000;">:</span> newViewControllerIndex <span style="color: #008000;">-</span> <span style="color: #FF0000;">1</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
            <span style="color: #000000;">&#91;</span>self transitionFromViewController<span style="color: #008000;">:</span> currentLeftViewController 
                              toViewController<span style="color: #008000;">:</span> newViewController
                                      duration<span style="color: #008000;">:</span> animationDuration
                                       options<span style="color: #008000;">:</span> <span style="color: #FF0000;">0</span> 
                                    animations<span style="color: #008000;">:</span> <span style="color: #008000;">^</span><span style="color: #000000;">&#123;</span>
                                        <span style="color: #000000;">&#91;</span>self moveOffScreenLeft<span style="color: #008000;">:</span> currentLeftViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
                                        <span style="color: #000000;">&#91;</span>self moveToLeftPane<span style="color: #008000;">:</span> currentRightViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
                                        <span style="color: #000000;">&#91;</span>self moveToRightPane<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
                                    <span style="color: #000000;">&#125;</span> 
                                    completion<span style="color: #008000;">:</span> <span style="color: #008000;">^</span><span style="color: #000000;">&#40;</span><span style="color: #FF0000;">BOOL</span> finished<span style="color: #000000;">&#41;</span> <span style="color: #000000;">&#123;</span>
&nbsp;
                                        <span style="color: #000000;">&#91;</span>self notifyViewDidMoveToLeftPane<span style="color: #008000;">:</span> currentRightViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
                                        <span style="color: #000000;">&#91;</span>self notifyViewDidMoveToRightPane<span style="color: #008000;">:</span> newViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
                                        <span style="color: #000000;">&#91;</span>newViewController didMoveToParentViewController<span style="color: #008000;">:</span> self<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
                                    <span style="color: #000000;">&#125;</span>
             <span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        <span style="color: #000000;">&#125;</span>
    <span style="color: #000000;">&#125;</span>
<span style="color: #000000;">&#125;</span></pre></div>
<p><strong>Figure 6 Push method</strong></p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #008000;">-</span> <span style="color: #000000;">&#40;</span><span style="color: #0600FF;">void</span><span style="color: #000000;">&#41;</span> pop<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span><span style="color: #FF0000;">BOOL</span><span style="color: #000000;">&#41;</span> collapseFolderHierarchy animated<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span><span style="color: #FF0000;">BOOL</span><span style="color: #000000;">&#41;</span> animated
<span style="color: #000000;">&#123;</span>
    <span style="color: #FF0000;">float</span> animationDuration <span style="color: #008000;">=</span> <span style="color: #FF0000;">0.0</span><span style="color: #008000;">;</span>
    <span style="color: #0600FF;">if</span> <span style="color: #000000;">&#40;</span>animated<span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
        animationDuration <span style="color: #008000;">=</span> <span style="color: #FF0000;">0.5</span><span style="color: #008000;">;</span>
    <span style="color: #000000;">&#125;</span>
&nbsp;
    <span style="color: #0600FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #000000;">&#91;</span>self shouldExitSearch<span style="color: #000000;">&#93;</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
        <span style="color: #000000;">&#91;</span>self exitSearch<span style="color: #008000;">:</span> self<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
    <span style="color: #000000;">&#125;</span>
    <span style="color: #0600FF;">else</span> <span style="color: #0600FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> count<span style="color: #000000;">&#93;</span> <span style="color: #008000;">></span> <span style="color: #FF0000;">2</span><span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
        NSUInteger rightViewControllerIndex <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> count<span style="color: #000000;">&#93;</span> <span style="color: #008000;">-</span> <span style="color: #FF0000;">1</span><span style="color: #008000;">;</span>
        UIViewController <span style="color: #008000;">*</span>currentRightViewController <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> objectAtIndex<span style="color: #008000;">:</span> rightViewControllerIndex<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        UIViewController <span style="color: #008000;">*</span>currentLeftViewController <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> objectAtIndex<span style="color: #008000;">:</span> rightViewControllerIndex <span style="color: #008000;">-</span> <span style="color: #FF0000;">1</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        UIViewController <span style="color: #008000;">*</span>prevLevelViewController <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> objectAtIndex<span style="color: #008000;">:</span> rightViewControllerIndex <span style="color: #008000;">-</span> <span style="color: #FF0000;">2</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
        <span style="color: #000000;">&#91;</span>self applyDualPaneViewControllerLook<span style="color: #008000;">:</span> prevLevelViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
\t\t<span style="color: #000000;">&#91;</span>self moveOffScreenLeft<span style="color: #008000;">:</span> prevLevelViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
        <span style="color: #000000;">&#91;</span>currentRightViewController willMoveToParentViewController<span style="color: #008000;">:</span> self<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
        <span style="color: #000000;">&#91;</span>self transitionFromViewController<span style="color: #008000;">:</span> currentRightViewController
                          toViewController<span style="color: #008000;">:</span> prevLevelViewController
                                  duration<span style="color: #008000;">:</span> animationDuration
                                   options<span style="color: #008000;">:</span> <span style="color: #FF0000;">0</span>
                                animations<span style="color: #008000;">:</span> <span style="color: #008000;">^</span><span style="color: #000000;">&#123;</span>
                                    <span style="color: #000000;">&#91;</span>self moveOffScreenRight<span style="color: #008000;">:</span> currentRightViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
                                    <span style="color: #000000;">&#91;</span>self moveToRightPane<span style="color: #008000;">:</span> currentLeftViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
                                    <span style="color: #000000;">&#91;</span>self moveToLeftPane<span style="color: #008000;">:</span> prevLevelViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
                                <span style="color: #000000;">&#125;</span>
                                completion<span style="color: #008000;">:</span> <span style="color: #008000;">^</span><span style="color: #000000;">&#40;</span><span style="color: #FF0000;">BOOL</span> finshed<span style="color: #000000;">&#41;</span> <span style="color: #000000;">&#123;</span>
                                    <span style="color: #000000;">&#91;</span>self notifyViewDidMoveToLeftPane<span style="color: #008000;">:</span> prevLevelViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
                                    <span style="color: #000000;">&#91;</span>self notifyViewDidMoveToRightPane<span style="color: #008000;">:</span> currentLeftViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
                                    <span style="color: #000000;">&#91;</span>currentRightViewController removeFromParentViewController<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
                                    <span style="color: #0600FF;">if</span> <span style="color: #000000;">&#40;</span>collapseFolderHierarchy<span style="color: #000000;">&#41;</span>
                                    <span style="color: #000000;">&#123;</span>   
                                        <span style="color: #000000;">&#91;</span>self popUntilEntireHierarchyIsCollapsed<span style="color: #008000;">:</span> collapseFolderHierarchy animated<span style="color: #008000;">:</span> animated<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
                                    <span style="color: #000000;">&#125;</span>
                                    <span style="color: #0600FF;">if</span> <span style="color: #000000;">&#40;</span><span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">childViewControllers</span> count<span style="color: #000000;">&#93;</span> <span style="color: #008000;"><=</span> <span style="color: #FF0000;">2</span> <span style="color: #008000;">&&</span>
                                        <span style="color: #008000;">!</span><span style="color: #000000;">&#91;</span>self isInSearchMode<span style="color: #000000;">&#93;</span><span style="color: #000000;">&#41;</span>
                                    <span style="color: #000000;">&#123;</span>
                                        self.<span style="color: #0000FF;">backButton</span>.<span style="color: #0000FF;">enabled</span> <span style="color: #008000;">=</span> NO<span style="color: #008000;">;</span>
                                    <span style="color: #000000;">&#125;</span>
                                <span style="color: #000000;">&#125;</span>
         <span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>   
    <span style="color: #000000;">&#125;</span>
<span style="color: #000000;">&#125;</span></pre></div>
<p><strong>Figure 7 Pop method</strong></p>
<p>The Objective-C Protocols <span class="geshifilter"><code class="text geshifilter-text">SLStorageModuleDelegate</code></span> and <span class="geshifilter"><code class="text geshifilter-text">SLSubViewControllerDelegate</code></span> allow for loose coupling, and formalized communication, between <span class="geshifilter"><code class="text geshifilter-text">SLStorageModule</code></span> and its children.</p>
<p>As you can see, the SoftLayer dual-pane browser with its friendly user interface and robust design makes a perfect tool for SoftLayer Object Storage exploration. </p>
<p>Hope you enjoy using SoftLayer Mobile HD application, available from the Apple App Store.</p>
<p><a href="http://itunes.apple.com/us/app/softlayer-mobile-hd/id460377057?mt=8">Check it out today!</a></p>
<p>Pawel</p>

