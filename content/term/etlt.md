---
title: "What is EtLT?"
tags:
- data engineering
- concepts
---
EtLT refers to Extract, “tweak”, Load, Transform, and can be thought of an extension of the [ELT](https://glossary.airbyte.com/term/elt/) approach to data integration. The EtLT approach incorporates a very light “tweak” (small “t”) transformation which is done on the data after it is extracted from the source before it is loaded into the destination, as demonstrated in the following image:

![](images/etlt-extract-tweak-load-transform.png)

For a more detailed explanation of EtLT see: [EtLT for improved GDPR compliance](https://airbyte.com/blog/etlt-gdpr-compliance).
