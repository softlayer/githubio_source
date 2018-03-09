---
title: "Blocks - A welcome addition to C"
description: "<p>In the programming environment of Mac OS X 10.6 (Snow Leopard), Apple added a programming construct to C (and by exte"
date: "2011-04-18"
author: "sthompson"
tags:
    - "blog"
---

<p>In the programming environment of Mac OS X 10.6 (Snow Leopard), Apple added a programming construct to C (and by extension C++ and Objective-C) known simply as "Blocks". This new construct has been carried to the iOS platform starting with iOS 4.0. Developers familiar with the venerable LISP will smile knowingly at blocks, and wonder what took that young whippersnapper C so long. Likewise, Ruby aficionados will look at blocks and find an old friend. JavaScript developers will see in blocks echoes of anonymous functions. The concepts and behaviors that define Blocks are neither new nor revolutionary, and are implemented in a variety of languages. Seeing those concepts and behaviors implemented in a family of C languages, however, is new and exciting.</p>
<p>Put simply, a block is a chunk of executable code, and a lexical closure of the environment in which it was created, that can be passed around like data and executed when needed. You might think of it as a function that can be passed around like Plain Old Data, however the function carries with it the environment in which it was defined. The idea takes some getting used to, but once understood, Blocks become a powerful tool for solving problems.</p>
<p>Rather than post a lot of code here, I would invite you to explore this new language feature on your own. Apple has a good document which introduces a developer to the syntax and semantics of blocks here:</p>
<p><a href="http://developer.apple.com/library/ios/#featuredarticles/Short_Practical_Guide_Blocks/_index.html">A Short Practical Guide to Blocks</a></p>
<p>An interesting article on the uses of blocks in different contexts can be found here:</p>
<p><a href="http://parmanoir.com/8_ways_to_use_Blocks_in_Snow_Leopard">8 ways to use Blocks in Snow Leopard</a></p>
<p>The developer community will be happy to know that Apple has submitted the specification for blocks (along with a specification for Garbage Collection) to C Standards working group for public consumption, see:</p>
<p><a href="http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1370.pdf">Apple's Extensions to C</a></p>
<p>That means that any C language compiler has the potential to implement blocks in the future. This has great potential to put a powerful new tool into the hands of programmers in any of a number of environments.</p>

