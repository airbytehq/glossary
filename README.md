# Readme of Glossary 🧠
You can read about the Glossary on [glossary.airbyte.com](https://glossary.airbyte.com/).


## Lower Case
Terms are lower case that links are also lower case. When we create a link to a term, I usually capitalize beginning of each word to make it look nice. E.g `[Apache Arrow](term/apache%20arrow.md). Other such as YAML I write all in capitals.


## Deployment
Some technical details of the deployment process.

There are two GitHub Actions. First [Deploy to GitHub Pages](https://github.com/airbytehq/glossary/actions/workflows/deploy.yaml) that package branch `hugo` and run the deployment (e.g. running GoHugo), essentially rendering the webpage to a static webpage. The second action [pages-build-deployment](https://github.com/airbyteglossary/airbyteglossary.github.io/actions/workflows/pages/pages-build-deployment) is taking the `public` folder from branch `hugo` and deploying it to `master`.

The `master` branch is also what you see on [glossary.airbyte.com](https://glossary.airbyte.com). So whenever you push changes to the `hugo` branch omergeerging PRs, the GitHub actions will automatically deploy everything.

The `hugo` branch is not protected and everyone can add. Maybe will change that later. For now, we want a fast update cycle.

## Special Thanks
This repo is a fork of [Quartz](https://github.com/jackyzha0/quartz) and we thank Jacky for open-sourcing this gem.
