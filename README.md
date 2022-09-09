# Readme of Glossary 🧠

Please see more about how to edit or publish on [How to Contribute](https://glossary.airbyte.com/term/contribute-to-glossary/). The glossary it live on [glossary.airbyte.com](https://glossary.airbyte.com).

* ✍ Missing a Term or want to fix a typo? Check [How to Contribute](https://glossary.airbyte.com/term/contribute-to-glossary/)
* 👀 Want to discuss or need help, talk to us on [Slack](https://slack.airbyte.com/)

# Technical part
Some technical details of the deployment process.

## Deployment
There are two GitHub Actions. First [Deploy to GitHub Pages](https://github.com/airbytehq/glossary/actions/workflows/deploy.yaml) that package branch `hugo` and run the deployment (e.g. running GoHugo), essentially rendering the webpage to a static webpage. It will build and publish the static website to [master](https://github.com/airbyteglossary/airbyteglossary.github.io/tree/master) branch on publishing repo.

The `master` branch is also what you see on [glossary.airbyte.com](https://glossary.airbyte.com). So whenever you push changes to the `hugo` branch, it will automatically be merged and deployed.

The `hugo` branch is not protected and everyone can add. Maybe will change that later. For now, we want a fast update cycle.

## Special Thanks
This repo is a fork of [Quartz](https://github.com/jackyzha0/quartz) and we thank Jacky for open-sourcing this gem.
