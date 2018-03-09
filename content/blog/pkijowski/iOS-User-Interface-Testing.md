---
title: "iOS User Interface Testing"
description: "<p>Automate, automate, automate...</p>\n<p><a href=http://blog.softlayer.com/2012/what-does-automation-look-like/>Auto"
date: "2012-09-14"
author: "pkijowski"
tags:
    - "blog"
---

<p>Automate, automate, automate...</p>
<p><a href="http://blog.softlayer.com/2012/what-does-automation-look-like/">Automation</a> is part of our SoftLayer DNA. We automate not only our external processes and procedures, such as server provisioning and operating system reloads, but also internal processes such as our iOS mobile products testing.</p>
<p>Our mobile applications have short, 2-3 week release cycles, and growing feature sets. Regression tests on the applications can take several days to complete. In order to maintain high release quality standards with the small mobile teams, we decided to implement both User Interface and code level tests to exercise our daily builds.  Failing test cases alert us when the product potentially becomes unstable. This article focuses on SoftLayer’s iOS products UI testing automation.</p>
<p>Apple’s developer tools include a product known as Instruments.  Instruments, in turn, has a number modules that help when developing mobile device software. One of these modules is the <a href="http://developer.apple.com/library/ios/documentation/AnalysisTools/Reference/Instruments_User_Reference/AutomationInstrument/AutomationInstrument.html#http://developer.apple.com/library/ios/documentation/AnalysisTools/Reference/Instruments_User_Re">Automation Instrument</a>, a tool that enables user interface testing.</p>
<p>[inline:automate1.png]<br />
<em>UI Automation Instrument In Action</em></p>
<p>The team enthusiastically started creating UI test scenarios using the Automation Instrument but quickly learned its limitations. The tool works well when it is run manually from the Mac OS X user interface environment, however running it from the command line script on a build machine inside the context of a Jenkins Continuous Integration process isn’t quite as effortless.</p>
<p>We would not be worthy of calling ourselves “SLayers” if we weren’t able to find solutions for several “minor” issues, right? So here’s how we got it working…</p>
<p>First we extended our build script so it accepts additional parameters that trigger execution of the automated test.</p>
<div class="geshifilter">
<pre class="ruby geshifilter-ruby" style="font-family:monospace;"><span style="color:#008000; font-style:italic;"># Run the build script.</span>
&nbsp;
<span style="color:#006600; font-weight:bold;">/</span>usr<span style="color:#006600; font-weight:bold;">/</span>bin<span style="color:#006600; font-weight:bold;">/</span>ruby Scripts<span style="color:#006600; font-weight:bold;">/</span>build_script.<span style="color:#9900CC;">rb</span> <span style="color:#006600; font-weight:bold;">--</span>build_number $<span style="color:#006600; font-weight:bold;">&#123;</span>BUILD_NUMBER<span style="color:#006600; font-weight:bold;">&#125;</span> <span style="color:#006600; font-weight:bold;">--</span>run_automated_tests <span style="color:#006600; font-weight:bold;">--</span>run_unit_tests
&nbsp;
BUILD_RESULT=$<span style="color:#006600; font-weight:bold;">&#123;</span>?<span style="color:#006600; font-weight:bold;">&#125;</span></pre></div>
<p>When the test arguments are present, the following method gets called inside of the “build_script.rb”.</p>
<div class="geshifilter">
<pre class="ruby geshifilter-ruby" style="font-family:monospace;"><span style="color:#008000; font-style:italic;"># ---------------------------------------------------------------</span>
<span style="color:#008000; font-style:italic;"># Run UI Automation test suite</span>
<span style="color:#008000; font-style:italic;"># ---------------------------------------------------------------</span>
<span style="color:#9966CC; font-weight:bold;">def</span> run_test_suite<span style="color:#006600; font-weight:bold;">&#40;</span>build_products_dir<span style="color:#006600; font-weight:bold;">&#41;</span>
&nbsp;
    unlock_login_keychain_command = <span style="color:#996600;">"security -v unlock-keychain -p PasswordHere <span style="color:#000099;">\\"</span>${HOME}/Library/Keychains/login.keychain<span style="color:#000099;">\\"</span>"</span>
    <span style="color:#9966CC; font-weight:bold;">if</span> <span style="color:#006600; font-weight:bold;">&#40;</span>!<span style="color:#006600; font-weight:bold;">&#40;</span>system_debug<span style="color:#006600; font-weight:bold;">&#40;</span>unlock_login_keychain_command<span style="color:#006600; font-weight:bold;">&#41;</span><span style="color:#006600; font-weight:bold;">&#41;</span><span style="color:#006600; font-weight:bold;">&#41;</span>
        <span style="color:#CC0066; font-weight:bold;">raise</span> <span style="color:#996600;">"Error unlocking login keychain."</span>
    <span style="color:#9966CC; font-weight:bold;">end</span>
    instruments_command = <span style="color:#996600;">"/bin/sh ./Scripts/UIAutomationTestSuite/run_instruments.sh"</span>
    <span style="color:#9966CC; font-weight:bold;">if</span> <span style="color:#006600; font-weight:bold;">&#40;</span>!<span style="color:#006600; font-weight:bold;">&#40;</span>system_debug<span style="color:#006600; font-weight:bold;">&#40;</span>instruments_command<span style="color:#006600; font-weight:bold;">&#41;</span><span style="color:#006600; font-weight:bold;">&#41;</span><span style="color:#006600; font-weight:bold;">&#41;</span>
        <span style="color:#CC0066; font-weight:bold;">raise</span> <span style="color:#996600;">"Error running instruments."</span>
    <span style="color:#9966CC; font-weight:bold;">end</span>
<span style="color:#9966CC; font-weight:bold;">end</span></pre></div>
<p>Unfortunately, when starting Instruments from the command line, the user still must give Instruments permission to start and monitor processes. The method above executes a shell script on the build machine that then uses another command line tool, expect, to interact with Instruments on the users behalf.</p>
<div class="geshifilter">
<pre class="bash geshifilter-bash" style="font-family:monospace;"><span style="color: #666666; font-style: italic;">#/bin/sh</span>
<span style="color: #000000; font-weight: bold;">/</span>usr<span style="color: #000000; font-weight: bold;">/</span>bin<span style="color: #000000; font-weight: bold;">/</span>expect .<span style="color: #000000; font-weight: bold;">/</span>Scripts<span style="color: #000000; font-weight: bold;">/</span>UIAutomationTestSuite<span style="color: #000000; font-weight: bold;">/</span>interact_with_instruments.sh
<span style="color: #7a0874; font-weight: bold;">wait</span>
<span style="color: #7a0874; font-weight: bold;">exit</span> <span style="color: #000000;">0</span></pre></div>
<p>"Expect" script:</p>
<div class="geshifilter">
<pre class="bash geshifilter-bash" style="font-family:monospace;"><span style="color: #666666; font-style: italic;">#!/usr/bin/expect</span>
&nbsp;
<span style="color: #000000; font-weight: bold;">set</span> timeout <span style="color: #660033;">-1</span>
&nbsp;
spawn instruments <span style="color: #660033;">-t</span> .<span style="color: #000000; font-weight: bold;">/</span>Scripts<span style="color: #000000; font-weight: bold;">/</span>UIAutomationTestSuite<span style="color: #000000; font-weight: bold;">/</span>Automation.tracetemplate <span style="color: #000000; font-weight: bold;">/</span>Users<span style="color: #000000; font-weight: bold;">/</span>build<span style="color: #000000; font-weight: bold;">/</span>workspace<span style="color: #000000; font-weight: bold;">/</span>MobileApplication_iPhone<span style="color: #000000; font-weight: bold;">/</span>SLMobileClient<span style="color: #000000; font-weight: bold;">/</span>TestProducts<span style="color: #000000; font-weight: bold;">/</span>Debug-iphonesimulator<span style="color: #000000; font-weight: bold;">/</span>SoftLayerMobile.app <span style="color: #660033;">-e</span> UIASCRIPT .<span style="color: #000000; font-weight: bold;">/</span>Scripts<span style="color: #000000; font-weight: bold;">/</span>UIAutomationTestSuite<span style="color: #000000; font-weight: bold;">/</span>iPhone_testSuite.js <span style="color: #660033;">-e</span> UIARESULTPATH <span style="color: #000000; font-weight: bold;">/</span>Users<span style="color: #000000; font-weight: bold;">/</span>build<span style="color: #000000; font-weight: bold;">/</span>workspace<span style="color: #000000; font-weight: bold;">/</span>MobileApplication_iPhone<span style="color: #000000; font-weight: bold;">/</span>SLMobileClient<span style="color: #000000; font-weight: bold;">/</span>TestProduct
&nbsp;
expect <span style="color: #ff0000;">"Name (build):"</span>
send <span style="color: #ff0000;">"<span style="color: #000099; font-weight: bold;">\\r</span>"</span>
expect <span style="color: #ff0000;">"Password:"</span>
send <span style="color: #ff0000;">"PasswordHere<span style="color: #000099; font-weight: bold;">\\r</span>"</span>
interact
expect eof
catch <span style="color: #7a0874; font-weight: bold;">wait</span> result
<span style="color: #7a0874; font-weight: bold;">exit</span> <span style="color: #7a0874; font-weight: bold;">&#91;</span>lindex <span style="color: #007800;">$result</span> <span style="color: #000000;">3</span><span style="color: #7a0874; font-weight: bold;">&#93;</span></pre></div>
<p>When the credentials are provided, instruments start running test cases as defined in the UI Automation script. </p>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #008080;">#import "./iPhone_loginAndLogout.js"</span>
<span style="color: #008080;">#import "./iPhone_launchAndNavigateBandwidthInfo.js"</span>
<span style="color: #008080;">#import "./iPhone_launchAndNavigateTickets.js"</span>
<span style="color: #008080;">#import "./iPhone_launchAndNavigateDevices.js"</span>
<span style="color: #008080;">#import "./iPhone_launchAndNavigateAbout.js"</span>
<span style="color: #008080;">#import "./iPhone_launchAndNavigateStorage.js"</span>
<span style="color: #008080;">#import "./iPhone_launchAndNavigateAccounting.js"</span>
<span style="color: #008080;">#import "./iPhone_launchAndNavigateNotifications.js"</span>
<span style="color: #008080;">#import "./iPhone_launchAndNavigateSupport.js"</span>
&nbsp;
var target <span style="color: #008000;">=</span> UIATarget.<span style="color: #0000FF;">localTarget</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
var host <span style="color: #008000;">=</span> target.<span style="color: #0000FF;">host</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
&nbsp;
UIALogger.<span style="color: #0000FF;">logMessage</span><span style="color: #000000;">&#40;</span><span style="color: #666666;">"Cleaning old tests results..."</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
host.<span style="color: #0000FF;">performTaskWithPathArgumentsTimeout</span><span style="color: #000000;">&#40;</span><span style="color: #666666;">"/bin/sh"</span>, <span style="color: #000000;">&#91;</span><span style="color: #666666;">"Scripts/UIAutomationTestSuite/clean_tests.sh"</span><span style="color: #000000;">&#93;</span>, <span style="color: #FF0000;">10</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
&nbsp;
UIALogger.<span style="color: #0000FF;">logStart</span><span style="color: #000000;">&#40;</span><span style="color: #666666;">"Running iPhone UI test suite..."</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
&nbsp;
run_testLaunchAndNavigateAbout<span style="color: #000000;">&#40;</span>target<span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
run_testLoginAndLogout<span style="color: #000000;">&#40;</span>target<span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
run_testLaunchAndNavigateTickets<span style="color: #000000;">&#40;</span>target<span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
run_testLaunchAndNavigateDevices<span style="color: #000000;">&#40;</span>target<span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
run_testLaunchAndNavigateBandwidthInfo<span style="color: #000000;">&#40;</span>target<span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
run_testLaunchAndNavigateStorage<span style="color: #000000;">&#40;</span>target<span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
run_testLaunchAndNavigateAccounting<span style="color: #000000;">&#40;</span>target<span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
run_testLaunchAndNavigateNotifications<span style="color: #000000;">&#40;</span>target<span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
run_testLaunchAndNavigateSupport<span style="color: #000000;">&#40;</span>target<span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
&nbsp;
UIALogger.<span style="color: #0000FF;">logMessage</span><span style="color: #000000;">&#40;</span><span style="color: #666666;">"Stopped running iPhone UI test suite..."</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
&nbsp;
var result <span style="color: #008000;">=</span> host.<span style="color: #0000FF;">performTaskWithPathArgumentsTimeout</span><span style="color: #000000;">&#40;</span><span style="color: #666666;">"/bin/sh"</span>, <span style="color: #000000;">&#91;</span><span style="color: #666666;">"Scripts/UIAutomationTestSuite/prepare_junit_test_report.sh"</span><span style="color: #000000;">&#93;</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span>
logTaskResults<span style="color: #000000;">&#40;</span>result, <span style="color: #666666;">"false"</span><span style="color: #000000;">&#41;</span><span style="color: #008000;">;</span></pre></div>
<div style="margin: 0 auto; text-align:center;">
Automation test cases running on the simulator<br />
<iframe width="420" height="315" src="http://www.youtube.com/embed/YGbPFNbzwp8" frameborder="0" allowfullscreen></iframe></div>
<p>When the instruments application finishes running the tests, their results are saved into a JUnit style XML file in a location where Jenkins can find them.</p>
<p>[inline:automate2.png]<br />
<em>Test results reported by Jenkins</em></p>
<p>Jenkins also makes the test case results a part of the build artifacts.</p>
<p>Stay tuned for part 2: Automate, automate, automate… - How to automate Unit Testing on iOS</p>
<p>Pawel</p>

