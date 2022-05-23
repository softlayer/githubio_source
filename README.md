# SoftLayer Code Examples

This is the source to build [SLDN](https://sldn.softlayer.com) with [hugo](https://github.com/spf13/hugo/)

## Building SLDN

This repository has a copy of the Hugo binaries in the `bin` directory, and those should be used to build the site, as newer versions of Hugo might not build it properly.
Just use the right binary for your OS.

- Linux is `bin/hugo`
- Windows is `bin/hugo.exe`
- Mac is `bin/hugo_mac`

### Updating `/content/reference`
This section is updated by the `bin/generateSLDN.py` python script (requires Python 3.8+)

`python bin/generateSLDN.py --download`

This script will do the following:
1. Download and parse the SLDN metadata from https://api.softlayer.com/metadata/v3.1
2. Create any needed service/method/datatype stub files
3. Generate any of the needed magic ORM methods that don't technically exist in the metadata.

Running `python bin/generateSLDN.py` without the `--download` option will simply re-parse the `data/sldn_metadata.json` file, creating and updating template fies as needed. This is useful if you want to test out changes that don't exist in the real metadata, or build the internal API documentation.

If services/datatypes are REMOVED from the metadata, this might cause issues with the hugo site generation. To fix this, simply remove the reference content and regenerate from the metadata.

`rm -rf content/reference/datatypes content/reference/services; python bin/generateSLDN.py`


### Testing Changes Locally
To view any changes you made without publishing the content, run the following:

`./bin/hugo server -d html`
This will create a local webserver available at http://localhost:1313/ and keep the generated HTML in the `html` directory, which is useful if you need to inspect the raw files for whatever reason.

### Publishing

By default https://sldn.softlayer.com ( source is on https://github.com/softlayer/softlayer.github.io) is updated by a GitHub action ([Publish Action](https://github.com/softlayer/githubio_source/actions/workflows/publish.yml)), which still requires a merged pull request on the softlayer.github.io repo, but is otherwise automated.

If you want to do this manually, you will need to checkout a copy of https://github.com/softlayer/softlayer.github.io (lets say to `../softlayer.github.io`) and run the following command:

```bash
./bin/hugo -d ../softlayer.github.io -v
```

Commit and push your changes, merge to master, and wait a few minutes.

## Directory Structure

- `.github/` All the Github actions and other github related data
- `bin/` Binaries and scripts needed for the site
- `content/` Content files that represent pages and other content on the site
    + `reference/` The auto generated documentation reference material. *Do not manually edit these files*
    + `release_notes/` Release Note blog posts, sorted into directories by year, titled by date published.
    + `*/` Everything is is grouped into language specific example blog posts.
- `data/` Contains the formatted metdata from SLDN. *Do not manually edit this file*
- `layouts/` The hugo templates that drive how pages are rendered into HTML
    + `reference/` These layouts are specific to the `reference` content
    + `partials/` These pare bit of pages that go in different sections, like Headers and Footers.
    + `_default` Layouts to use when no other is specified
    + `release_notes` Layouts specific to the release notes
- `static/` Javascript and CSS type files, other static content
- `config.toml` The main config for Hugo


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

