---
title: "PHP Memory Management in Foreach"
description: "<style type=text/css>code { display: block; background:#dddddd; border: 1px solid #999999; padding: 5px; }</style><p>M"
date: "2009-01-15"
author: "dmcaloon"
tags:
    - "blog"
---

<style type="text/css">code { display: block; background:#dddddd; border: 1px solid #999999; padding: 5px; }</style><p>Many developers, even experienced ones, are confused by the way PHP handles arrays in <a href="http://us3.php.net/foreach">foreach loops</a>.  In the standard foreach loop, PHP makes a copy of the array that is used in the loop.  The copy is discarded immediately after the loop finishes.  This is transparent in the operation of a simple foreach loop.  For example:</p>
<div class="geshifilter">
<pre class="php geshifilter-php" style="font-family:monospace;"><span style="color: #000088;">$set</span> <span style="color: #339933;">=</span> <a href="http://www.php.net/array"><span style="color: #990000;">array</span></a><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">"apple"</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">"banana"</span><span style="color: #339933;">,</span> <span style="color: #0000ff;">"coconut"</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span>
<span style="color: #b1b100;">foreach</span> <span style="color: #009900;">&#40;</span> <span style="color: #000088;">$set</span> <span style="color: #b1b100;">AS</span> <span style="color: #000088;">$item</span> <span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span>
    <a href="http://www.php.net/echo"><span style="color: #990000;">echo</span></a> <span style="color: #0000ff;">"<span style="color: #006699; font-weight: bold;">{$item}</span><span style="color: #000099; font-weight: bold;">\
</span>"</span><span style="color: #339933;">;</span>
<span style="color: #009900;">&#125;</span></pre></div>
<p>This outputs:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">apple
banana
coconut</pre></div>
<p>Even though the copy is created, the developer doesn’t notice, because the original array isn’t referenced within the loop or after the loop finishes.  However, when you attempt to modify the items in a loop, you find that they are unmodified when you finish:</p>
<p><span style="color: #000000"><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">);<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">AS&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">strrev&nbsp;</span><span style="color: #007700">(</span><span style="color: #0000BB">$item</span><span style="color: #007700">);<br />}<br /></span><span style="color: #0000BB">print_r</span><span style="color: #007700">(</span><span style="color: #0000BB">$set</span><span style="color: #007700">);</span></span></p>
<p>This outputs:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">Array
(
    [0] => apple
    [1] => banana
    [2] => coconut
)</pre></div>
<p>There are no changes from the original, even though you clearly assigned a value to $item.  This is because you are operating on $item as it appears in the copy of $set being worked on.  You can override this by grabbing $item by reference, like so:</p>
<p><span style="color: #000000"><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">);<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">AS&nbsp;&</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">strrev</span><span style="color: #007700">(</span><span style="color: #0000BB">$item</span><span style="color: #007700">);<br />}<br /></span><span style="color: #0000BB">print_r</span><span style="color: #007700">(</span><span style="color: #0000BB">$set</span><span style="color: #007700">);</span></span></p>
<p>This outputs:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">Array
(
    [0] => elppa
    [1] => ananab
    [2] => tunococ
)</pre></div>
<p>As you can see, when $item is operated on by-reference, the changes made to $item are made to the members of the original $set.  Using $item by reference also prevents PHP from creating the array copy.  To test this, first we’ll show a quick script demonstrating the copy:</p>
<p><span style="color: #000000"><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">);<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">AS&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$set</span><span style="color: #007700">[]&nbsp;=&nbsp;</span><span style="color: #0000BB">ucfirst</span><span style="color: #007700">(</span><span style="color: #0000BB">$item</span><span style="color: #007700">);<br />}<br /></span><span style="color: #0000BB">print_r</span><span style="color: #007700">(</span><span style="color: #0000BB">$set</span><span style="color: #007700">);</span></span></p>
<p>This outputs:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">Array
(
    [0] => apple
    [1] => banana
    [2] => coconut
    [3] => Apple
    [4] => Banana
    [5] => Coconut
)</pre></div>
<p>In this example, PHP copied $set and used it to loop over, but when $set was used inside the loop, PHP added the variables to the original array, not the copied array.  Basically, PHP is only using the copied array for the execution of the loop and the assignment of $item.  Because of this, the loop above only executes 3 times, and each time it appends another value to the end of the original $set, leaving the original $set with 6 elements, but never entering an infinite loop.</p>
<p>However, what if we had used $item by reference, as I mentioned before?  A single character added to the above test:</p>
<p><span style="color: #000000"><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">);<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">AS&nbsp;&</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$set</span><span style="color: #007700">[]&nbsp;=&nbsp;</span><span style="color: #0000BB">ucfirst</span><span style="color: #007700">(</span><span style="color: #0000BB">$item</span><span style="color: #007700">);<br />}<br /></span><span style="color: #0000BB">print_r</span><span style="color: #007700">(</span><span style="color: #0000BB">$set</span><span style="color: #007700">);</span></span></p>
<p>Results in an infinite loop.  Note this actually is an infinite loop, you’ll have to either kill the script yourself or wait for your OS to run out of memory.  I added the following line to my script so PHP would run out of memory very quickly, I suggest you do the same if you’re going to be running these infinite loop tests:</p>
<p><span style="color: #000000"><span style="color: #0000BB">ini_set</span><span style="color: #007700">(</span><span style="color: #DD0000">"memory_limit"</span><span style="color: #007700">,</span><span style="color: #DD0000">"1M"</span><span style="color: #007700">);</span></span></p>
<p>So in this previous example with the infinite loop, we see the reason why PHP was written to create a copy of the array to loop over.  When a copy is created and used only by the structure of the loop construct itself, the array stays static throughout the execution of the loop, so you’ll never run into issues.</p>
<p>But wait, there’s more.  PHP fails to create a copy of the array if a reference is used at all.  We know that referencing $item will cause the infinite loop scenario above, but if $set is referenced anywhere else in the script, even the non-referencing foreach format will break:</p>
<p><span style="color: #000000"><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">);<br /></span><span style="color: #0000BB">$a&nbsp;</span><span style="color: #007700">=&nbsp;&</span><span style="color: #0000BB">$set</span><span style="color: #007700">;<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">AS&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$set</span><span style="color: #007700">[]&nbsp;=&nbsp;</span><span style="color: #0000BB">ucfirst</span><span style="color: #007700">(</span><span style="color: #0000BB">$item</span><span style="color: #007700">);<br />}</span></span></p>
<p>Results in an infinite loop, even though $item isn’t by reference.  Using $a instead of $set gives identical results.  </p>
<p>This is not to say that $item is implicitly used by reference if $set is referenced.  See this example:</p>
<p><span style="color: #000000"><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">);<br /></span><span style="color: #0000BB">$a&nbsp;</span><span style="color: #007700">=&nbsp;&</span><span style="color: #0000BB">$set</span><span style="color: #007700">;<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$a&nbsp;</span><span style="color: #007700">AS&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">ucfirst</span><span style="color: #007700">(</span><span style="color: #0000BB">$item</span><span style="color: #007700">);<br />}<br /></span><span style="color: #0000BB">print_r</span><span style="color: #007700">(</span><span style="color: #0000BB">$set</span><span style="color: #007700">);</span></span></p>
<p>This outputs:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">Array
(
    [0] => apple
    [1] => banana
    [2] => coconut
)</pre></div>
<p>$set is unchanged from the original values, because even though $set is referenced by $a, and $set has not been copied, $item is still given only lexical scope in relation to the loop, and will not pass modifications back to $set.  You will still have to assign it by reference to make changes to the original array:</p>
<p><span style="color: #000000"><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">,&nbsp;</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">);<br /></span><span style="color: #0000BB">$a&nbsp;</span><span style="color: #007700">=&nbsp;&</span><span style="color: #0000BB">$set</span><span style="color: #007700">;<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$a&nbsp;</span><span style="color: #007700">AS&nbsp;&</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">strrev</span><span style="color: #007700">(</span><span style="color: #0000BB">$item</span><span style="color: #007700">);<br />}<br /></span><span style="color: #0000BB">print_r</span><span style="color: #007700">(</span><span style="color: #0000BB">$set</span><span style="color: #007700">);</span></span></p>
<p>This outputs:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">Array
(
    [0] => elppa
    [1] => ananab
    [2] => tunococ
)</pre></div>
<p>All of these examples also work in associative arrays using the foreach ( $set AS $key => $item ) syntax.  $key can never be used by-reference it always comes from the array the loop construct is using, and cannot be modified.  So the tricks used to modify array items in-position won’t work for modifying the keys.  You can create new keys in the array, however, and unset the existing ones, like so:</p>
<p><span style="color: #000000"><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">=></span><span style="color: #DD0000">"red"</span><span style="color: #007700">,</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">=></span><span style="color: #DD0000">"yellow"</span><span style="color: #007700">,</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">=></span><span style="color: #DD0000">"brown"</span><span style="color: #007700">);<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">AS&nbsp;</span><span style="color: #0000BB">$key&nbsp;</span><span style="color: #007700">=>&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$set</span><span style="color: #007700">[</span><span style="color: #0000BB">ucfirst</span><span style="color: #007700">(</span><span style="color: #0000BB">$key</span><span style="color: #007700">)]&nbsp;=&nbsp;</span><span style="color: #0000BB">$item</span><span style="color: #007700">;<br />&nbsp;&nbsp;&nbsp;&nbsp;unset(</span><span style="color: #0000BB">$set</span><span style="color: #007700">[</span><span style="color: #0000BB">$key</span><span style="color: #007700">]);<br />}<br /></span><span style="color: #0000BB">print_r</span><span style="color: #007700">(</span><span style="color: #0000BB">$set</span><span style="color: #007700">);</span></span></p>
<p>This outputs:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">Array
(
    [Apple] => red
    [Banana] => yellow
    [Coconut] => brown
)</pre></div>
<p>However, as you may have already noticed, this array was copied before the loop began.  If you were using the array in a situation where it couldn’t be copied, you will run into errors:</p>
<p><span style="color: #000000"><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">=></span><span style="color: #DD0000">"red"</span><span style="color: #007700">,</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">=></span><span style="color: #DD0000">"yellow"</span><span style="color: #007700">,</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">=></span><span style="color: #DD0000">"brown"</span><span style="color: #007700">);<br /></span><span style="color: #0000BB">$a&nbsp;</span><span style="color: #007700">=&nbsp;&</span><span style="color: #0000BB">$set</span><span style="color: #007700">;<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">AS&nbsp;</span><span style="color: #0000BB">$key&nbsp;</span><span style="color: #007700">=>&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$set</span><span style="color: #007700">[</span><span style="color: #0000BB">ucfirst</span><span style="color: #007700">(</span><span style="color: #0000BB">$key</span><span style="color: #007700">)]&nbsp;=&nbsp;</span><span style="color: #0000BB">$item</span><span style="color: #007700">;<br />&nbsp;&nbsp;&nbsp;&nbsp;unset(</span><span style="color: #0000BB">$set</span><span style="color: #007700">[</span><span style="color: #0000BB">$key</span><span style="color: #007700">]);<br />}<br /></span><span style="color: #0000BB">print_r</span><span style="color: #007700">(</span><span style="color: #0000BB">$set</span><span style="color: #007700">);</span></span></p>
<p>This outputs:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">Array
(
)</pre></div>
<p>Because the array was referenced and not copied, you get vastly unpredictable results when attempting to alter the physical structure of the array, especially using unset().  Without the unset() call in this example, you operate on the original array and loop through the original array, so you get the same infinite-loop generating code as before, but since we’re specifying the key for $set it doesn’t continue forever:</p>
<p><span style="color: #000000"><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">=></span><span style="color: #DD0000">"red"</span><span style="color: #007700">,</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">=></span><span style="color: #DD0000">"yellow"</span><span style="color: #007700">,</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">=></span><span style="color: #DD0000">"brown"</span><span style="color: #007700">);<br /></span><span style="color: #0000BB">$a&nbsp;</span><span style="color: #007700">=&nbsp;&</span><span style="color: #0000BB">$set</span><span style="color: #007700">;<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">AS&nbsp;</span><span style="color: #0000BB">$key&nbsp;</span><span style="color: #007700">=>&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$set</span><span style="color: #007700">[</span><span style="color: #0000BB">ucfirst</span><span style="color: #007700">(</span><span style="color: #0000BB">$key</span><span style="color: #007700">)]&nbsp;=&nbsp;</span><span style="color: #0000BB">$item</span><span style="color: #007700">;<br />}<br /></span><span style="color: #0000BB">print_r</span><span style="color: #007700">(</span><span style="color: #0000BB">$set</span><span style="color: #007700">);</span></span></p>
<p>This outputs:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">Array
(
    [apple] => red
    [banana] => yellow
    [coconut] => brown
    [Apple] => red
    [Banana] => yellow
    [Coconut] => brown
)</pre></div>
<p>You can prove that it’s still possible to enter an infinite loop by adding a $set[] inside your loop:</p>
<p><span style="color: #000000"><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">=></span><span style="color: #DD0000">"red"</span><span style="color: #007700">,</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">=></span><span style="color: #DD0000">"yellow"</span><span style="color: #007700">,</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">=></span><span style="color: #DD0000">"brown"</span><span style="color: #007700">);<br /></span><span style="color: #0000BB">$a&nbsp;</span><span style="color: #007700">=&nbsp;&</span><span style="color: #0000BB">$set</span><span style="color: #007700">;<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">AS&nbsp;</span><span style="color: #0000BB">$key&nbsp;</span><span style="color: #007700">=>&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$set</span><span style="color: #007700">[</span><span style="color: #0000BB">ucfirst</span><span style="color: #007700">(</span><span style="color: #0000BB">$key</span><span style="color: #007700">)]&nbsp;=&nbsp;</span><span style="color: #0000BB">$item</span><span style="color: #007700">;<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$set</span><span style="color: #007700">[]&nbsp;=&nbsp;</span><span style="color: #0000BB">$item</span><span style="color: #007700">;<br />}<br /></span><span style="color: #0000BB">print_r</span><span style="color: #007700">(</span><span style="color: #0000BB">$set</span><span style="color: #007700">);</span></span></p>
<p>This results in an infinite loop.</p>
<p>One interesting thing you can do with the $key => $item syntax when the array is copied is modify the original array structure without fear of causing loop issues:</p>
<p><span style="color: #000000"><span style="color: #0000BB"><?php<br />$set&nbsp;</span><span style="color: #007700">=&nbsp;array(</span><span style="color: #DD0000">"apple"</span><span style="color: #007700">=></span><span style="color: #DD0000">"red"</span><span style="color: #007700">,</span><span style="color: #DD0000">"banana"</span><span style="color: #007700">=></span><span style="color: #DD0000">"yellow"</span><span style="color: #007700">,</span><span style="color: #DD0000">"coconut"</span><span style="color: #007700">=></span><span style="color: #DD0000">"brown"</span><span style="color: #007700">);<br />foreach&nbsp;(&nbsp;</span><span style="color: #0000BB">$set&nbsp;</span><span style="color: #007700">AS&nbsp;</span><span style="color: #0000BB">$key&nbsp;</span><span style="color: #007700">=>&nbsp;</span><span style="color: #0000BB">$item&nbsp;</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$set</span><span style="color: #007700">[]&nbsp;=&nbsp;</span><span style="color: #0000BB">ucfirst</span><span style="color: #007700">(</span><span style="color: #0000BB">$item</span><span style="color: #007700">);<br />&nbsp;&nbsp;&nbsp;&nbsp;unset(</span><span style="color: #0000BB">$set</span><span style="color: #007700">[</span><span style="color: #0000BB">$key</span><span style="color: #007700">]);<br />}<br /></span><span style="color: #0000BB">print_r</span><span style="color: #007700">(</span><span style="color: #0000BB">$set</span><span style="color: #007700">); </span></span></p>
<p>This outputs:</p>
<div class="geshifilter">
<pre class="text geshifilter-text" style="font-family:monospace;">Array
(
    [0] => Red
    [1] => Yellow
    [2] => Brown
)</pre></div>
<p>As you can see from this example, the array was copied for use in the loop construct.  References to $set within the loop still refer to the outer version of $set, so the unset() call and the $set[] addition work on the original, leaving us with a nicely upper-cased version of the original, without keys.  </p>
<p>This knowledge is useful for developers who are trying to plug memory holes in PHP applications.  If you foreach through an array of objects that can be 50MB in size, you create an entire copy of the structure in memory for no reason other than to power the loop.  If your loop doesn’t modify the structure of the array or add to it at all, it would be vastly more efficient to add the “cheat” of $a = &$array; right before your array to prevent PHP from making a copy.  </p>
<p>This knowledge is also hopefully useful for programmers who cannot figure out why arrays are behaving like they are.  Basically, if you don’t use references, the loop executes once for each member in the original array, regardless of what you do to the original.  </p>
<p>NOTE:  These tests were performed on PHP version 5.2.5.  5.2.0 and earlier perform differently.  Run these tests yourself under controlled circumstances before relying on PHP to behave in any particular way.</p>

