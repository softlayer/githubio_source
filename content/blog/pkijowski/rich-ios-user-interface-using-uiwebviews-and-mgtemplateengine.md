---
title: "Rich iOS User Interface using UIWebViews and MGTemplateEngine"
description: "<p>SoftLayer Mobile Team is part of the Interface Development group that is dedicated to providing access to <a href=ht"
date: "2013-01-08"
author: "pkijowski"
tags:
    - "blog"
---

<p>SoftLayer Mobile Team is part of the Interface Development group that is dedicated to providing access to <a href="http://www.softlayer.com/about/">SoftLayer global platform</a>. Our goal is to bring an outstanding user experience by clear presentation of data and friendly navigation through resources right in the palms of our customers.</p>
<p>Our mobile application users are very often interested in not only browsing tickets or devices – data that can efficiently be presented using native iOS UI controls like table views – but also in seeing resources health and usage info like bandwidth billing data, monitoring alarms updates and maintenance events – data sets that are more complex and not easily presentable using native controls. The greatest challenge is how to display this kind of information on a small screen.</p>
<p>To solve our dilemma, we came up with several options:</p>
<p>1. Use native controls like labels, text and scroll views and dynamically create complex data views.<br />
2. Use collection views introduced in iOS 6.X.<br />
3. Use “hybrid views” i.e.: wrap HTML content in the native web views. </p>
<p>We decided to dynamically generate HTML content and present it in the iOS web views. The results speak for themselves – take a look at the bellow screenshots.</p>
<h4>iPhone scheduled event details view:</h4>
<p>[inline:blog1.png]</p>
<h4>iPad bandwidth data set view:</h4>
<p>[inline:blog2.png]</p>
<p>Let’s dive deeper into the implementation of the Scheduled Events Details view that was shown earlier. There are two main components needed to make the “hybrid view” work:</p>
<p>1. View controller that owns a web view: <span class="geshifilter"><code class="csharp geshifilter-csharp">SLScheduledEventDetailsViewController</code></span><br />
2. Scheduled Events HTML web page template: <span class="geshifilter"><code class="csharp geshifilter-csharp">ScheduledEventDetails.<span style="color: #0000FF;">mghtml</span></code></span></p>
<p>The view controller makes use of the <a href="http://mattgemmell.com/2008/05/20/mgtemplateengine-templates-with-cocoa/">MGTemplateEngine</a> to load the template and perform necessary template substitutions based on the actual Scheduled Event item being viewed. </p>
<h4>SLScheduledEventDetailsViewController declaration:</h4>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #008080;">#import <UIKit/UIKit.h></span>
&nbsp;
@<span style="color: #FF0000;">interface</span> SLScheduledEventDetailsViewController <span style="color: #008000;">:</span> UIViewController <span style="color: #008000;"><</span> UIWebViewDelegate<span style="color: #008000;">></span>
&nbsp;
@end</pre></div>
<h4>SLScheduledEventDetailsViewController declaration:</h4>
<div class="geshifilter">
<pre class="csharp geshifilter-csharp" style="font-family:monospace;"><span style="color: #008080;">#import <MGTemplateEngine/MGTemplateEngine.h></span>
<span style="color: #008080;">#import <MGTemplateEngine/ICUTemplateMatcher.h></span>
<span style="color: #008080;">#import <SLPortalAPI/SLPortalAPI.h></span>
<span style="color: #008080;">#import " SLScheduledEventDetailsViewController.h"</span>
&nbsp;
<span style="color: #0600FF;">static</span> <span style="color: #0600FF;">const</span> CGFloat kUpdatesTableViewMargin <span style="color: #008000;">=</span> <span style="color: #FF0000;">8.0</span><span style="color: #008000;">;</span>
&nbsp;
@<span style="color: #FF0000;">interface</span> SLScheduledEventDetailsViewController <span style="color: #000000;">&#40;</span><span style="color: #000000;">&#41;</span>
@property <span style="color: #000000;">&#40;</span>strong, nonatomic<span style="color: #000000;">&#41;</span> SLSecheduledEvent <span style="color: #008000;">*</span>eventItem<span style="color: #008000;">;</span>
@end
&nbsp;
@implementation SLScheduledEventDetailsViewController
&nbsp;
<span style="color: #008000;">-</span> <span style="color: #000000;">&#40;</span>id<span style="color: #000000;">&#41;</span>initWithScheduledEventItem<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span>SLSecheduledEvent <span style="color: #008000;">*</span><span style="color: #000000;">&#41;</span> item
<span style="color: #000000;">&#123;</span>
    self <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>super init<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
    <span style="color: #0600FF;">if</span> <span style="color: #000000;">&#40;</span>self<span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
        self.<span style="color: #0000FF;">eventItem</span> <span style="color: #008000;">=</span> item<span style="color: #008000;">;</span>
    <span style="color: #000000;">&#125;</span>
    <span style="color: #0600FF;">return</span> self<span style="color: #008000;">;</span>
<span style="color: #000000;">&#125;</span>
&nbsp;
<span style="color: #008000;">-</span> <span style="color: #000000;">&#40;</span><span style="color: #0600FF;">void</span><span style="color: #000000;">&#41;</span> viewWillAppear<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span><span style="color: #FF0000;">BOOL</span><span style="color: #000000;">&#41;</span> animated
<span style="color: #000000;">&#123;</span>
\t<span style="color: #000000;">&#91;</span>super viewWillAppear<span style="color: #008000;">:</span> animated<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
\t<span style="color: #000000;">&#91;</span>self reloadWebContent<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
<span style="color: #000000;">&#125;</span>
&nbsp;
<span style="color: #008000;">-</span> <span style="color: #000000;">&#40;</span><span style="color: #0600FF;">void</span><span style="color: #000000;">&#41;</span> reloadWebContent
<span style="color: #000000;">&#123;</span>
\tNSString <span style="color: #008000;">*</span>templatePath <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span><span style="color: #000000;">&#91;</span>NSBundle mainBundle<span style="color: #000000;">&#93;</span> pathForResource<span style="color: #008000;">:</span> <span style="color: #666666;">@"ScheduledEventDetails"</span> 
                                                                ofType<span style="color: #008000;">:</span> <span style="color: #666666;">@"mghtml"</span> 
                                                           inDirectory<span style="color: #008000;">:</span> nil<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
\tMGTemplateEngine <span style="color: #008000;">*</span>templateEngine <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>MGTemplateEngine templateEngine<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
\t<span style="color: #000000;">&#91;</span>templateEngine setMatcher<span style="color: #008000;">:</span> <span style="color: #000000;">&#91;</span>ICUTemplateMatcher matcherWithTemplateEngine<span style="color: #008000;">:</span> templateEngine<span style="color: #000000;">&#93;</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
\tNSMutableString <span style="color: #008000;">*</span>descriptionHTMLized <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">eventItem</span>.<span style="color: #0000FF;">summary</span> mutableCopy<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
\tNSError <span style="color: #008000;">*</span>regularExpressionError <span style="color: #008000;">=</span> nil<span style="color: #008000;">;</span>
\tNSRegularExpression <span style="color: #008000;">*</span>eachLineExpression <span style="color: #008000;">=</span> 
                                           <span style="color: #000000;">&#91;</span>NSRegularExpression regularExpressionWithPattern<span style="color: #008000;">:</span><span style="color: #666666;">@"^(.*)$"</span> 
                                           options<span style="color: #008000;">:</span> NSRegularExpressionAnchorsMatchLines 
                                             error<span style="color: #008000;">:</span> <span style="color: #008000;">&</span>regularExpressionError<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
\t<span style="color: #000000;">&#91;</span>eachLineExpression replaceMatchesInString<span style="color: #008000;">:</span> descriptionHTMLized
\t\t\t\t\t        options<span style="color: #008000;">:</span> <span style="color: #FF0000;">0</span>
\t\t\t\t\t          range<span style="color: #008000;">:</span> NSMakeRange<span style="color: #000000;">&#40;</span><span style="color: #FF0000;">0</span>, <span style="color: #000000;">&#91;</span>descriptionHTMLized length<span style="color: #000000;">&#93;</span><span style="color: #000000;">&#41;</span> 
                                     withTemplate<span style="color: #008000;">:</span> <span style="color: #666666;">@"<p>$1</p>"</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
    NSArray <span style="color: #008000;">*</span>updateItems <span style="color: #008000;">=</span> self.<span style="color: #0000FF;">eventItem</span>.<span style="color: #0000FF;">updates</span><span style="color: #008000;">;</span>
   <span style="color: #000000;">&#91;</span>NSMutableArray arrayWithCapacity<span style="color: #008000;">:</span> <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">eventItem</span>.<span style="color: #0000FF;">EventUpdates</span> count<span style="color: #000000;">&#93;</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
    NSArray <span style="color: #008000;">*</span>sortedEvents <span style="color: #008000;">=</span><span style="color: #000000;">&#91;</span> sortedArrayUsingComparator<span style="color: #008000;">:</span>
                    <span style="color: #008000;">^</span>NSComparisonResult<span style="color: #000000;">&#40;</span>SLScheduledEventUpdate <span style="color: #008000;">*</span>lhs, SLScheduledEventUpdate <span style="color: #008000;">*</span>rhs<span style="color: #000000;">&#41;</span> <span style="color: #000000;">&#123;</span>
        <span style="color: #0600FF;">return</span> <span style="color: #000000;">&#91;</span>lhs.<span style="color: #0000FF;">createDate</span> compare<span style="color: #008000;">:</span> rhs.<span style="color: #0000FF;">createDate</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
    <span style="color: #000000;">&#125;</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
    <span style="color: #0600FF;">for</span> <span style="color: #000000;">&#40;</span><span style="color: #FF0000;">int</span> i <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>sortedEvents count<span style="color: #000000;">&#93;</span> <span style="color: #008000;">-</span> <span style="color: #FF0000;">1</span><span style="color: #008000;">;</span> i <span style="color: #008000;">>=</span> <span style="color: #FF0000;">0</span><span style="color: #008000;">;</span> <span style="color: #008000;">--</span>i<span style="color: #000000;">&#41;</span>
    <span style="color: #000000;">&#123;</span>
        SLScheduledEventUpdate <span style="color: #008000;">*</span>update <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>sortedEvents objectAtIndex<span style="color: #008000;">:</span> i<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
        NSMutableString <span style="color: #008000;">*</span>contentHTMLized <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>update.<span style="color: #0000FF;">contents</span> mutableCopy<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
        NSRegularExpression <span style="color: #008000;">*</span>eachLineContentExpression <span style="color: #008000;">=</span> 
                                  <span style="color: #000000;">&#91;</span>NSRegularExpressionregularExpressionWithPattern<span style="color: #008000;">:</span> <span style="color: #666666;">@"^(.*)$"</span> 
                                                        options<span style="color: #008000;">:</span> NSRegularExpressionAnchorsMatchLines  
                                                          error<span style="color: #008000;">:</span> <span style="color: #008000;">&</span>regularExpressionError<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
        <span style="color: #000000;">&#91;</span>eachLineContentExpression replaceMatchesInString<span style="color: #008000;">:</span> contentHTMLized
                                                  options<span style="color: #008000;">:</span> <span style="color: #FF0000;">0</span>
                                                    range<span style="color: #008000;">:</span> NSMakeRange<span style="color: #000000;">&#40;</span><span style="color: #FF0000;">0</span>, <span style="color: #000000;">&#91;</span>contentHTMLized length<span style="color: #000000;">&#93;</span><span style="color: #000000;">&#41;</span> 
                                             withTemplate<span style="color: #008000;">:</span> <span style="color: #666666;">@"<p>$1</p>"</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
&nbsp;
        NSDictionary <span style="color: #008000;">*</span>updateItem <span style="color: #008000;">=</span> @<span style="color: #000000;">&#123;</span><span style="color: #666666;">@"formattedDate"</span> <span style="color: #008000;">:</span> <span style="color: #000000;">&#91;</span>update createDateString<span style="color: #000000;">&#93;</span>,
        <span style="color: #666666;">@"contents"</span> <span style="color: #008000;">:</span> contentHTMLized<span style="color: #000000;">&#125;</span><span style="color: #008000;">;</span>
&nbsp;
        <span style="color: #000000;">&#91;</span>updateItems addObject<span style="color: #008000;">:</span> updateItem<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
    <span style="color: #000000;">&#125;</span>
&nbsp;
    NSDictionary <span style="color: #008000;">*</span>substitutions <span style="color: #008000;">=</span> @<span style="color: #000000;">&#123;</span><span style="color: #666666;">@"ScheduledEventDescription"</span><span style="color: #008000;">:</span> descriptionHTMLized,
                                    <span style="color: #666666;">@"updateItems"</span> <span style="color: #008000;">:</span> updateItems<span style="color: #000000;">&#125;</span><span style="color: #008000;">;</span>
    NSString <span style="color: #008000;">*</span>newHTMLString <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span>templateEngine processTemplateInFileAtPath<span style="color: #008000;">:</span> templatePath 
                                                               withVariables<span style="color: #008000;">:</span> substitutions<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
    <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">webView</span> loadHTMLString<span style="color: #008000;">:</span> newHTMLString baseURL<span style="color: #008000;">:</span> <span style="color: #000000;">&#91;</span>NSURL fileURLWithPath<span style="color: #008000;">:</span> <span style="color: #000000;">&#91;</span><span style="color: #000000;">&#91;</span>NSBundle 
                                                   mainBundle<span style="color: #000000;">&#93;</span> resourcePath<span style="color: #000000;">&#93;</span> 
                                               isDirectory<span style="color: #008000;">:</span> YES<span style="color: #000000;">&#93;</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
<span style="color: #000000;">&#125;</span>
&nbsp;
<span style="color: #008000;">-</span> <span style="color: #000000;">&#40;</span><span style="color: #0600FF;">void</span><span style="color: #000000;">&#41;</span> loadView
<span style="color: #000000;">&#123;</span>
\tself.<span style="color: #0000FF;">view</span> <span style="color: #008000;">=</span> <span style="color: #000000;">&#91;</span><span style="color: #000000;">&#91;</span>UIWebView alloc<span style="color: #000000;">&#93;</span> init<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
\tself.<span style="color: #0000FF;">webView</span>.<span style="color: #0000FF;">dataDetectorTypes</span> <span style="color: #008000;">=</span> UIDataDetectorTypeNone<span style="color: #008000;">;</span>
<span style="color: #000000;">&#125;</span>
&nbsp;
<span style="color: #008000;">-</span> <span style="color: #000000;">&#40;</span><span style="color: #0600FF;">void</span><span style="color: #000000;">&#41;</span> performURLCommand<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span>NSString <span style="color: #008000;">*</span><span style="color: #000000;">&#41;</span> urlCommand
<span style="color: #000000;">&#123;</span>
\t<span style="color: #0600FF;">if</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#91;</span>urlCommand isEqualToString<span style="color: #008000;">:</span> <span style="color: #666666;">@"showDevices"</span><span style="color: #000000;">&#93;</span><span style="color: #000000;">&#41;</span>
\t<span style="color: #000000;">&#123;</span>
\t\t<span style="color: #000000;">&#91;</span>self performSelector<span style="color: #008000;">:</span>@selector<span style="color: #000000;">&#40;</span>showDevices<span style="color: #008000;">:</span><span style="color: #000000;">&#41;</span> withObject<span style="color: #008000;">:</span> self<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
\t<span style="color: #000000;">&#125;</span>
<span style="color: #000000;">&#125;</span>
&nbsp;
<span style="color: #008000;">-</span> <span style="color: #000000;">&#40;</span>IBAction<span style="color: #000000;">&#41;</span> showDevices<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span>id<span style="color: #000000;">&#41;</span> sender
<span style="color: #000000;">&#123;</span>
    SLImpactedResourcesViewController <span style="color: #008000;">*</span>impactedResourcesController <span style="color: #008000;">=</span> 
                               <span style="color: #000000;">&#91;</span><span style="color: #000000;">&#91;</span>SLImpactedResourcesViewController alloc<span style="color: #000000;">&#93;</span> initWithImpactedResources<span style="color: #008000;">:</span>  
                                                                          <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">eventItem</span> resources<span style="color: #000000;">&#93;</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
    <span style="color: #000000;">&#91;</span>self.<span style="color: #0000FF;">navigationController</span> pushViewController<span style="color: #008000;">:</span> impactedResourcesController animated<span style="color: #008000;">:</span> YES<span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
<span style="color: #000000;">&#125;</span>
&nbsp;
<span style="color: #008080;">#pragma mark -</span>
<span style="color: #008080;">#pragma mark UIWebKitDelegate</span>
&nbsp;
<span style="color: #008000;">-</span> <span style="color: #000000;">&#40;</span><span style="color: #FF0000;">BOOL</span><span style="color: #000000;">&#41;</span>           webView<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span>UIWebView <span style="color: #008000;">*</span><span style="color: #000000;">&#41;</span> webView
shouldStartLoadWithRequest<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span>NSURLRequest <span style="color: #008000;">*</span><span style="color: #000000;">&#41;</span>request
\t        navigationType<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span>UIWebViewNavigationType<span style="color: #000000;">&#41;</span>navigationType
<span style="color: #000000;">&#123;</span>
\t<span style="color: #FF0000;">BOOL</span> shouldLoad <span style="color: #008000;">=</span> YES<span style="color: #008000;">;</span>
&nbsp;
\t<span style="color: #0600FF;">if</span><span style="color: #000000;">&#40;</span>navigationType <span style="color: #008000;">=</span> <span style="color: #008000;">=</span> UIWebViewNavigationTypeLinkClicked<span style="color: #000000;">&#41;</span>
\t<span style="color: #000000;">&#123;</span>
\t\tNSURL <span style="color: #008000;">*</span>requestURL <span style="color: #008000;">=</span> request.<span style="color: #0000FF;">URL</span><span style="color: #008000;">;</span>
\t\t<span style="color: #0600FF;">if</span><span style="color: #000000;">&#40;</span>requestURL<span style="color: #000000;">&#41;</span>
\t\t<span style="color: #000000;">&#123;</span>
\t\t\t<span style="color: #0600FF;">if</span><span style="color: #000000;">&#40;</span><span style="color: #000000;">&#91;</span><span style="color: #000000;">&#91;</span>requestURL scheme<span style="color: #000000;">&#93;</span> isEqualToString<span style="color: #008000;">:</span> <span style="color: #666666;">@"slmc-cmd"</span><span style="color: #000000;">&#93;</span><span style="color: #000000;">&#41;</span>
\t\t\t<span style="color: #000000;">&#123;</span>
\t\t\t\t<span style="color: #000000;">&#91;</span>self performURLCommand<span style="color: #008000;">:</span> <span style="color: #000000;">&#91;</span>requestURL resourceSpecifier<span style="color: #000000;">&#93;</span><span style="color: #000000;">&#93;</span><span style="color: #008000;">;</span>
\t\t\t<span style="color: #000000;">&#125;</span>
\t\t<span style="color: #000000;">&#125;</span>
&nbsp;
\t\tshouldLoad <span style="color: #008000;">=</span> NO<span style="color: #008000;">;</span>
\t<span style="color: #000000;">&#125;</span>
&nbsp;
\t<span style="color: #0600FF;">return</span> shouldLoad<span style="color: #008000;">;</span>
<span style="color: #000000;">&#125;</span>
&nbsp;
@end</pre></div>
<p>The key method is <span class="geshifilter"><code class="csharp geshifilter-csharp"><span style="color: #000000;">&#40;</span><span style="color: #0600FF;">void</span><span style="color: #000000;">&#41;</span>reloadWebContent</code></span>, where the template substitutions take place. Another method that is worth taking a closer look at is the <span class="geshifilter"><code class="csharp geshifilter-csharp"><span style="color: #000000;">&#40;</span><span style="color: #FF0000;">BOOL</span><span style="color: #000000;">&#41;</span> webView<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span>UIWebView <span style="color: #008000;">*</span><span style="color: #000000;">&#41;</span> webView shouldStartLoadWithRequest<span style="color: #008000;">:</span> <span style="color: #000000;">&#40;</span>NSURLRequest <span style="color: #008000;">*</span><span style="color: #000000;">&#41;</span>request</code></span> that allows us to react to user events i.e.: link/buttons taps.</p>
<h4>ScheduledEventsDetails.mghtml template file:</h4>
<div class="geshifilter">
<pre class="bash geshifilter-bash" style="font-family:monospace;"><span style="color: #000000; font-weight: bold;"><!</span>DOCTYPE HTML<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"><</span>html<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"><</span><span style="color: #c20cb9; font-weight: bold;">head</span><span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"><</span>title<span style="color: #000000; font-weight: bold;">></span>SoftLayer Scheduled Events<span style="color: #000000; font-weight: bold;"></</span>title<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"><</span>meta name =<span style="color: #ff0000;">''</span> <span style="color: #ff0000;">"viewport"</span> content =<span style="color: #ff0000;">''</span> <span style="color: #ff0000;">"initial-scale ='' 1.0,user-scalable ='' no"</span><span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"><</span><span style="color: #c20cb9; font-weight: bold;">link</span> <span style="color: #007800;">rel</span>=<span style="color: #ff0000;">"stylesheet"</span> <span style="color: #007800;">href</span>=<span style="color: #ff0000;">"ScheduledEventDetails.css"</span> <span style="color: #007800;"><span style="color: #7a0874; font-weight: bold;">type</span></span>=<span style="color: #ff0000;">"text/css"</span> <span style="color: #007800;">media</span>=<span style="color: #ff0000;">"screen"</span> <span style="color: #007800;">title</span>=<span style="color: #ff0000;">"no title"</span> <span style="color: #007800;">charset</span>=<span style="color: #ff0000;">"utf-8"</span><span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"></</span><span style="color: #c20cb9; font-weight: bold;">head</span><span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"><</span>body<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"><</span>div <span style="color: #007800;"><span style="color: #c20cb9; font-weight: bold;">id</span></span>=<span style="color: #ff0000;">"title"</span><span style="color: #000000; font-weight: bold;">></span>
\t<span style="color: #000000; font-weight: bold;"><</span>table<span style="color: #000000; font-weight: bold;">></span>
\t<span style="color: #000000; font-weight: bold;"><</span><span style="color: #c20cb9; font-weight: bold;">tr</span><span style="color: #000000; font-weight: bold;">></span>
\t\t<span style="color: #000000; font-weight: bold;"><</span>td<span style="color: #000000; font-weight: bold;">></span>
\t\t\t<span style="color: #000000; font-weight: bold;"><</span>img <span style="color: #007800;"><span style="color: #c20cb9; font-weight: bold;">id</span></span>=<span style="color: #ff0000;">"toolboxIcon"</span> <span style="color: #007800;">src</span>=<span style="color: #ff0000;">"EventsIcon.pdf"</span><span style="color: #000000; font-weight: bold;">/></span>
\t\t<span style="color: #000000; font-weight: bold;"></</span>td<span style="color: #000000; font-weight: bold;">></span>
\t\t<span style="color: #000000; font-weight: bold;"><</span>td<span style="color: #000000; font-weight: bold;">></span>
\t\t\t<span style="color: #000000; font-weight: bold;"><</span>h1<span style="color: #000000; font-weight: bold;">></span>Scheduled Event<span style="color: #000000; font-weight: bold;"></</span>h1<span style="color: #000000; font-weight: bold;">></span>
\t\t<span style="color: #000000; font-weight: bold;"></</span>td<span style="color: #000000; font-weight: bold;">></span>
\t<span style="color: #000000; font-weight: bold;"></</span><span style="color: #c20cb9; font-weight: bold;">tr</span><span style="color: #000000; font-weight: bold;">></span>
\t<span style="color: #000000; font-weight: bold;"></</span>table<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"></</span>div<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"><</span>div <span style="color: #007800;"><span style="color: #c20cb9; font-weight: bold;">id</span></span>=<span style="color: #ff0000;">"summary"</span><span style="color: #000000; font-weight: bold;">></span>
&nbsp;
<span style="color: #000000; font-weight: bold;"></</span>div<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"><</span>div <span style="color: #007800;">class</span>=<span style="color: #ff0000;">"updateTable"</span><span style="color: #000000; font-weight: bold;">></span>
\t<span style="color: #000000; font-weight: bold;"><</span>table <span style="color: #007800;"><span style="color: #c20cb9; font-weight: bold;">id</span></span>=<span style="color: #ff0000;">"UpdateTable"</span> <span style="color: #007800;">width</span>=<span style="color: #ff0000;">"100%"</span><span style="color: #000000; font-weight: bold;">></span>
\t<span style="color: #000000; font-weight: bold;"><</span><span style="color: #c20cb9; font-weight: bold;">tr</span><span style="color: #000000; font-weight: bold;">></span>
\t\t<span style="color: #000000; font-weight: bold;"><</span>th <span style="color: #007800;">class</span>=<span style="color: #ff0000;">"value_header"</span><span style="color: #000000; font-weight: bold;">></span>
\t\t\tDate
\t\t<span style="color: #000000; font-weight: bold;"></</span>th<span style="color: #000000; font-weight: bold;">></span>
\t\t<span style="color: #000000; font-weight: bold;"><</span>th <span style="color: #007800;">class</span>=<span style="color: #ff0000;">"value_header"</span><span style="color: #000000; font-weight: bold;">></span>
\t\t\tUpdate
\t\t<span style="color: #000000; font-weight: bold;"></</span>th<span style="color: #000000; font-weight: bold;">></span>
\t<span style="color: #000000; font-weight: bold;"></</span><span style="color: #c20cb9; font-weight: bold;">tr</span><span style="color: #000000; font-weight: bold;">></span>
\t <span style="color: #7a0874; font-weight: bold;">&#123;</span><span style="color: #000000; font-weight: bold;">%</span> <span style="color: #000000; font-weight: bold;">for</span> updateItem <span style="color: #000000; font-weight: bold;">in</span> updateItems <span style="color: #000000; font-weight: bold;">%</span><span style="color: #7a0874; font-weight: bold;">&#125;</span>
\t<span style="color: #000000; font-weight: bold;"><</span><span style="color: #c20cb9; font-weight: bold;">tr</span><span style="color: #000000; font-weight: bold;">></span>
\t\t<span style="color: #000000; font-weight: bold;"><</span>td <span style="color: #007800;">class</span>=<span style="color: #ff0000;">"key"</span><span style="color: #000000; font-weight: bold;">></span>
&nbsp;
\t\t<span style="color: #000000; font-weight: bold;"></</span>td<span style="color: #000000; font-weight: bold;">></span>
\t\t<span style="color: #000000; font-weight: bold;"><</span>td <span style="color: #007800;">class</span>=<span style="color: #ff0000;">"value"</span><span style="color: #000000; font-weight: bold;">></span>
&nbsp;
\t\t<span style="color: #000000; font-weight: bold;"></</span>td<span style="color: #000000; font-weight: bold;">></span>
\t<span style="color: #000000; font-weight: bold;"></</span><span style="color: #c20cb9; font-weight: bold;">tr</span><span style="color: #000000; font-weight: bold;">></span>
\t <span style="color: #7a0874; font-weight: bold;">&#123;</span><span style="color: #000000; font-weight: bold;">%</span> <span style="color: #000000; font-weight: bold;">/</span><span style="color: #000000; font-weight: bold;">for</span> <span style="color: #000000; font-weight: bold;">%</span><span style="color: #7a0874; font-weight: bold;">&#125;</span>
\t<span style="color: #000000; font-weight: bold;"><</span>table<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"></</span>div<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"><</span>br<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"><</span>center<span style="color: #000000; font-weight: bold;">><</span>a <span style="color: #007800;">href</span>=<span style="color: #ff0000;">"slmc-cmd:showDevices"</span> <span style="color: #007800;">class</span>=<span style="color: #ff0000;">"buttonLookingLink"</span><span style="color: #000000; font-weight: bold;">/><</span>img <span style="color: #007800;">src</span>=<span style="color: #ff0000;">"ServerIconSmallWhite.png"</span> <span style="color: #007800;">height</span>=<span style="color: #ff0000;">"26"</span> <span style="color: #007800;">width</span>=<span style="color: #ff0000;">"26"</span> <span style="color: #007800;">align</span>=<span style="color: #ff0000;">"center"</span> <span style="color: #007800;">style</span>=<span style="color: #ff0000;">"padding:2px;"</span><span style="color: #000000; font-weight: bold;">/></span>Associated Devices<span style="color: #000000; font-weight: bold;"></</span>a<span style="color: #000000; font-weight: bold;">></</span>center<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"></</span>body<span style="color: #000000; font-weight: bold;">></span>
<span style="color: #000000; font-weight: bold;"></</span>html<span style="color: #000000; font-weight: bold;">></span></pre></div>
<p>The technique of using “hybrid views” has proven not only to be quite robust and maintainable, but also that it can be seamlessly integrated with the native iOS UI components. It is also worth pointing out that the “hybrid views” allow for easy rich text formatting, which is limited on pre iOS 6.X versions of the Apple OS.</p>
<p><a href="https://itunes.apple.com/us/app/softlayer-mobile/id373786244?mt=8">Check out the “hybrid views” in action today!</a></p>
<p>Pawel</p>

