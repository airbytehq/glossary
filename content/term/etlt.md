---
title: "What is EtLT?"
tags:
- data engineering
- concept
---
EtLT refers to Extract, “tweak”, Load, [Transform](term/data%20transformation.md), and can be thought of an extension to the [ELT](term/elt.md) approach to data integration. 

When compared to ELT, the EtLT approach incorporates an additional light “tweak” (small “t”) transformation, which is done on the data after it is extracted from the source and before it is loaded into the destination. This is demonstrated in the following image:

![](images/etlt-extract-tweak-load-transform.png)

For a more detailed explanation of EtLT see: [EtLT for improved GDPR compliance](https://airbyte.com/blog/etlt-gdpr-compliance).
