# Deployment Details
There are two GitHub Actions:
- [Deploy to GitHub Pages](https://github.com/airbytehq/glossary/actions/workflows/deploy.yaml) - this action packages `master` branch and runs the deployment (e.g. running GoHugo), essentially rendering the webpage to a static webpage. It will build and publish the static website to [gh-pages](https://github.com/airbytehq/glossary/tree/gh-pages) branch in the same repo.
- [pages-build-deployment](https://github.com/airbytehq/glossary/actions/workflows/pages/pages-build-deployment) - this action configures hosting of [glossary.airbyte.com](https://glossary.airbyte.com) from static webpage assets which are stored in `gh-pages` branch.

The `master` branch is what you see on [glossary.airbyte.com](https://glossary.airbyte.com). So whenever you push changes to the `master` branch, it will automatically be merged and deployed.

The `master` branch is not protected and everyone can add. Maybe will change that later. For now, we want a fast update cycle.

