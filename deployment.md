# Deployment Details
There are two GitHub Actions. First [Deploy to GitHub Pages](https://github.com/airbytehq/glossary/actions/workflows/deploy.yaml) that package branch `hugo` and run the deployment (e.g. running GoHugo), essentially rendering the webpage to a static webpage. It will build and publish the static website to [master](https://github.com/airbyteglossary/airbyteglossary.github.io/tree/master) branch on the publishing repo.

The `master` branch is also what you see on [glossary.airbyte.com](https://glossary.airbyte.com). So whenever you push changes to the `hugo` branch, it will automatically be merged and deployed.

The `hugo` branch is not protected and everyone can add. Maybe will change that later. For now, we want a fast update cycle.

