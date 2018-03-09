---
title: "Technical Debt"
description: "<p>According to <a href=http://www.merriam-webster.com>Merriam-Webster dictionary</a>, <em>debt</em> is defined as, s"
date: "2013-07-25"
author: "jbrown"
tags:
    - "blog"
---

<p>According to <a href="http://www.merriam-webster.com">Merriam-Webster dictionary</a>, <em>debt</em> is defined as, "something owed, an obligation, to be in a state of owing."  You are likely familiar with this concept as it pertains to financial affairs.  When you take out a loan to purchase a home or vehicle, you have obligated yourself to repay the amount of money you borrowed from a financial institution.  If you do not fulfill your repayment obligation there are consequences, most likely the repossession of the item purchased with the borrowed funds and a decrease in your credit worthiness.  Did you know it is also possible to incur debt during the development of a coding project? This concept is referred to as <em>technical debt</em> and it can have just as damaging of consequences for a project as its financial cousin.</p>
<p>Technical Debt can be incurred a variety of ways including, but not limited to:</p>
<ul>
<li>Business pressures, where meeting a deadline becomes more important that the consideration of the remaining items in this list</li>
<li>Not constructing code into reusable and flexible units, able to be easily adapted to changing business needs </li>
<li>Lack of documentation </li>
<li>Lack of unit tests, which does not catch any breakages in existing code and allows for potential introduction of new problems into the codebase</li>
<li>Lack of the sharing of knowledge amongst other team members </li>
</ul>
<p>The end result of each of these, and others, is that work remains to be completed before the project can every be truly considered finished.</p>
<p>We can break the concept of technical debt down further by dividing it into its two main components: interest owed and payment due dates.  We'll start with interest.</p>
<p>Just like interest is charged on financial debt, so too is interest charged on technical debt.  But instead of owing money on technical debt, outstanding interest is paid by an increase in the maintenance required and missed deadlines.  Every time a developer has to determine what a section of code is doing because there are no comments explaining its function, or because knowledge about its function had not been shared with team members, interest is paid on technical debt.  When there are no unit tests for a project and a bug fix is quickly checked into the project and introduces other bugs, interest is paid on technical debt.  Similar to financial debt, the more technical debt you have, the more interest you owe.  If interest is not paid properly, it begins to pile up and your "payments" toward technical debt become unmanageable.  This brings us to your due date.</p>
<p>The due date when you have technical debt is that point where you keep your head above the water.  You may not be paying down your debt, but you aren't racking up additional charges, either.  Payments are considered "on time" when you have enough time to at least keep up with the interest that is occured on your technical debt.  As a bonus, if you have extra time on your hands and it is dedicated to technical debt, it will be paid off early - and no penalties will be charged for prepayment.  However, when there is more uncompleted work than there is time to complete it, your loan is in default.  When you default on technical debt, bugs, questions and often user and developer frustration begin to pile up.  Just like with financial debt, when a developer's technical debt begins piling up and default occurs, stress levels go from healthy to unbearable.  Unfortunately, the more technical debt a developer has, the more likely default becomes.</p>
<p>So how do you keep your projects from defaulting?  The first way is to never take on debt to begin with.  While this is the best answer, it may not be the most reasonable one in many situations.  If you cannot come out of a project debt free, strive to incur the smallest amount of technical debt at all times.  Take those few extra seconds and comment your code.  Automation comes in handy when you find yourself spending a large amount of time writing repetitive documentation.  Introduce coding standards and unit testing to ensure a quality product is developed and it is checked thoroughly before its release.  Take the amount of time needed for each of these items, and others, into account when developing time estimates so that there are no items that have to be left out as the deadline approaches.  And when you're deciding what technical debt to incur, always consider your options and borrow wisely.</p>
<p>I hope this has helped you realize how each unfinished task in a project has a compounding impact and, if not managed correctly, can result in a difficult time for all involved.  Luckily, through wise borrowing and diligent repayment of your debt through the completion of outstanding tasks, you can become free of its obligation.</p>
<p>-Jeremy</p>

