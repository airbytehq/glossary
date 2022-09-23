---
title: "What is a Semantic Warehouse"
tags:
- data engineering
---
It incorporates best practices espoused by [Bill Inmon](Bill%20Inmon) for robust, scalable warehouse design built for the cloud as an abstraction of the [[Modern Data Stack]] with [[term/ata modeling]] at its core. 

![](images/semantic-warehouse.png)
Illustrating the Semantic Warehouse from [Chad Sanderson on LinkedIn](https://www.linkedin.com/posts/chad-sanderson_im-very-happy-to-unveil-the-semantic-warehouse-activity-6958091220157964288-JSXj/)

Chad Sanders first introduced the term in this [LinkedIn post](https://www.linkedin.com/posts/chad-sanderson_im-very-happy-to-unveil-the-semantic-warehouse-activity-6958091220157964288-JSXj/). Some defining features:
- Data as a product and capturing the natural world through events instead of batch processing with a clear defined schema
- [Data Contract](term/data%20contract.md) as a foundation to introduce contracts to its underlying source tables.
- Collaborative, peer-reviewed data modeling.
- Centralized metrics with a [Metrics/Locical Layer](term/metrics%20layer.md) allow collaborative data modeling between the business and the (data) engineers and abstract away the complexity of the data stack.
- Built-in incentives with semantics and modeling are required to generate good [Data Products](term/data%20product.md).

The semantic warehouse tries to solve the following problems:
1. The [Modern Data Stack](term/modern%20data%20stack.md) (MDS) is a good set of tools for building things, but they do not help ensure that what is being built is high quality.  
2. Most data architectures and data foundations are not scalable. The first version of data infrastructure (typically set up by engineers or junior data devs) is never refactored because it is tough to do so  
3. Producers do not (but should) own data quality. Data Engineers should not be middle-men caught in the cross-fire of consumers  
4. Semantics and context are missing. Data devs spend days to weeks just trying to understand what data we have, what it means, how it maps to services, and whether data can be trusted  
5. Data modeling was not a first-class citizen. Modeling was challenging to do (because of #4) and, in some cases, impossible, thanks to data simply being missing.  
6. Our [Data Warehouse](term/data%20warehouse.md) did not reflect the real world. Instead, it was a dumping ground for production services and 3rd party APIs.  
7. A lack of interoperability due to tools not 'speaking the same language.' We have multiple products which each require their distinct modeling environment and no shared understanding of business concepts  
8. [Data Governance](term/data%20governance.md) is critical, but businesses will reject it if it becomes a bottleneck. We cannot scale our data team horizontally with the complexity  
  
See also [[Metrics Layer|Semantic Layer]] and [[Data Contract]].