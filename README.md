# SoftLayer Code Examples

This is the source to build [SLDN](https://sldn.softlayer.com) with [hugo](https://github.com/spf13/hugo/)


## Making Changes.

Files in the /content/reference section are automatically generated and shouldn't be modified by hand. Otherwise, simply creating a pull request for changes is usually sufficient. See the [CONTRIBUTING](https://github.com/softlayer/githubio_source/blob/master/CONTRIBUTING.md) guide for more specific details.

### Content Template
Below is a template to use when making new content.

`````
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

Code examples should have the language explicitly set

```python

def some_function():
    pass
```

`````

This project uses goldmark to parse these files. See [CommonMark](https://spec.commonmark.org/0.29/) project details for support notations.


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


## Requesting Examples

If you ever find yourself wishing there was an example of how to do something in the SoftLayer API, please make a github issue on the [githubio_source](https://github.com/softlayer/githubio_source/issues) repository. We are always on the look out for more content ideas!


## Building the project

To generate the HTML and see what your changes would look like, just run the `hugo` binary included in this repository ( or build the hugo project yourself if you want to test a different version).

```bash
$ ./hugo server ./sldnHtml/
WARN 2021/04/15 15:43:54 [en] REF_NOT_FOUND: Ref "reference/datatypes/SoftLayer_Workload_Citrix_Order": "./githubio_source/content/reference/services/SoftLayer_Workload_Citrix_Workspace_Response/_index.md:21:107": page not found

                   |  EN
-------------------+--------
  Pages            | 10279
  Paginator pages  |    25
  Non-page files   |     2
  Static files     |  1797
  Processed images |     0
  Aliases          |  5649
  Sitemaps         |     1
  Cleaned          |     0

Built in 7417 ms
Watching for changes in ./githubio_source/{content,layouts,static}
Watching for config changes in ./Source/githubio_source/config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

This will start a temporary web server at http://localhost:1313/ to display the content, which was generated locally to the ./sldnHtml folder

You can ignore the `WARN` about `REF_NOT_FOUND` errors, they come from the automtically generated content.