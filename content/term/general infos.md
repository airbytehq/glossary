---
title: "General Infos (Folder Structure, Links)"
tags:
- help
weight: -9
---
[Quartz](https://quartz.jzhao.xyz) runs on top of [Hugo](https://gohugo.io/) so all notes are written in [Markdown](https://www.markdownguide.org/getting-started/) and can be edited through any editor.

## Folder Structure
The content of the Glossary is in `content/term` folder. The rest outside of `content/` is the website/framework.

To edit the main home page, open `/content/_index.md`.
## Links
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

## Lower Case
Terms are lower case that links are also lowercase. When we create a link to a term, I usually capitalize the beginning of each word to make it look nice. E.g `[Apache Arrow](term/apache%20arrow.md)`. Other such as YAML I write all in capitals.

We didn't activate wikilinks, but that would be an option as well. See more on [editing](https://quartz.jzhao.xyz/notes/editing/).
## Metatag with Front Matter
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

