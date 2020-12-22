# SoftLayer Code Examples

This is the source to build [SLDN](https://sldn.softlayer.com) with [hugo](https://github.com/spf13/hugo/)



 ## Making Changes.
Files in the /content/reference section are automatically generated and shouldn't be modified by hand. Otherwise, simply creating a pull request for changes is usually sufficient.

### Content Template
Below is a template to use when making new content.

```
---
title: "Your Title"
description: "This will show up in the list view, and should contain a few keywords for easy searching.."
date: "YYYY-MM-DD"
classes:
    - "SoftLayer_Account"
tags:
    - "users"
    - "permissions"
---


# Markdown From here on out](#title-one-link) {#title-one-link .anchor-link}
Your content goes here
```

### Tips

#### Heading Links / Anchor Links
To add a link to a heading use a heading like this:
```
[Title One](#title-one-link) {#title-one-link .anchor-link}
```
The `.anchor-link` bit adds a css class to the title, so that the link goes to the right location on the page, with a offset for the header.

#### Tags
Always a good idea to check [softlayer.github.io/tags](https://github.com/softlayer/softlayer.github.io/tree/master/tags) for existing tags and add onto those instead of making new ones where possible.

#### Classes
Any main classes your examples uses should be included. Helpful in searching.

#### Code Blocks
Code blocks should have the style added so hugo renders it properly, otherwise it will just use a generic brown/white style.
````
```<syntax>
 {"Code Example": "Goes Here"}
```
````



 
 ## Requesting Examples
 If you ever find yourself wishing there was an example of how to do something in the SoftLayer API, please make a github issue on the [githubio_source](https://github.com/softlayer/githubio_source/issues) repository.
