---
title: "How to Contribute to the Glossary"
tags:
- help
weight: -9
---

If you want to deploy direct, skip this and go directly to your preferred Deployment Methods:
* Web edits through GitHub
* Creating an Issue and we'll do the rest
* Or cloning and running it locally

## General Info
[Quartz](https://quartz.jzhao.xyz) runs on top of [Hugo](https://gohugo.io/) so all notes are written in [Markdown](https://www.markdownguide.org/getting-started/) and can be edited through any editor.

### Folder Structure
The content of the Glossary is in `content/term` folder. The rest outside of `content/` is the website/framework.

To edit the main home page, open `/content/_index.md`.
### Links
To create a link between terms in the glossary, just create a normal link using Markdown pointing to the document in question. Please note that **all links should be relative to the root `/content` path**.
```markdown
For example, I want to link this current document to `term/config.md`.
[A link to the config page](term/config.md)
```

Similarly, you can put local images anywhere in the `/content` folder.
```markdown
Example image (source is in content/images/example.png)
![Example Image](/content/images/example.png)
```

### Lower Case
Terms are lower case that links are also lowercase. When we create a link to a term, I usually capitalize the beginning of each word to make it look nice. E.g `[Apache Arrow](term/apache%20arrow.md)`. Other such as YAML I write all in capitals.

We didn't activate wikilinks, but that would be an option as well. See more on [editing](https://quartz.jzhao.xyz/notes/editing/).
### Metatag with Front Matter
Hugo is picky when it comes to metadata for files. Make sure that your title is double-quoted and that you have a title defined at the top of your file like so. You can also add tags here as well.
```yaml
---
title: "What is a Glossary?"
tags:
- example-tag
- here i can add more we keep it lower case
url: "term/my-other-domain"
aliases:
- Digital Garden
- Second Brain
---

Rest of your content here.
```

- `url`: this is not needed, only if the default link (name of the note) is not sufficient
	- all spaces will be replaced with `-` (dash).
- `aliases`: Are like tags, you can add multiple and they will be linkable same as a adding a new term would be.


## Web Edit with GitHub
You can either click on `Edit Source` on each page and directly edit on GitHub or you can create a [New Issue](https://github.com/airbytehq/glossary/issues).

## Create an Issue
If you are unsure, you can always [create an issue](https://github.com/airbytehq/glossary/issues) on our GitHub repo and we will make sure to add the new entry.

## Changing a lot? Clone locally
### Clone it locally with git
Clone the [repo](https://github.com/airbytehq/glossary) with:
```sh
git clone https://github.com/airbytehq/glossary.git
```

### Editors
#### Obsidian as an Editor (Recommended)
If you want to use [Obsidian](https://obsidian.md/), which I recommend as it will handle all links when renaming terms, adding a nice Markdown view with lots of features (even if you don't need them) and showing backlinks and [graph](term/about%20this%20glossary.md#interactive-graph). Just open the Obsidian in the folder `content/`, there is a hidden folder called `.obsidian` which does the rest.

1. ![](images/Pasted%20image%2020220908082431.png)
2. ![](images/Pasted%20image%2020220908082439.png)

More details and step-by-step manual you see on [Quartz Setup](https://quartz.jzhao.xyz/notes/setup/), how to [Edit Notes ](https://quartz.jzhao.xyz/notes/editing/) and [How to set up Obsidian](https://quartz.jzhao.xyz/notes/obsidian/) (although the settings are already done when you open the `.obsidian` folder as described above).

#### Use any other Editor
Of course, as everything is Markdown, you can edit each file under `content/term` as a normal markdown file and publish (see below) changes to GitHub. Keep in mind, ethat very new term you create will automatically be created as a page in dthe eployment process or when you run it locally.

### Preview Locally
#### Setup
Quartz runs on top of [Hugo](https://gohugo.io/) so all notes are written in [Markdown](https://www.markdownguide.org/getting-started/).

We need to install golang, hugo-obsidian and hugo. Follow the instructions on [Preview Changes on Quartz](https://quartz.jzhao.xyz/notes/preview-changes/).

> [!info]
> 
> If you are running into an error saying that `command not found: hugo-obsidian`, make sure you set your `GOPATH` correctly! This will allow your terminal to correctly recognize hugo-obsidian as an executable.

I added to my `~/.zshrc` (or `~/.bashrc`):
 ```sh
#go path
export GOPATH=$HOME/go
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
```
#### Run it!
All you need to do it goint to your root directory of you cloned repo and start `make serve`:
```sh
# Navigate to your local Quartz folder
cd <location-of-your-local-quartz>

# Start local server
make serve

# View your site in a browser at http://localhost:1313/
```
That's it, from now on that's how you run it. All changes you make will be automatically published, you do not need to stop and restart when you add terms, etc. (only the graph view will only be updated after stopping and serving again).

## How to Publish
Commit and Push to branch `hugo` and wait a couple of minutes until [GitHub Actions](https://github.com/airbytehq/glossary/actions) will deploy it automatically. At the moment we do not need to create PR's to make the updates as easy as possible. 

If we encounter problems in the future, we might change that. If you are unsure, you can always [create an issue](https://github.com/airbytehq/glossary/issues) and we will make sure to add the new entry.
