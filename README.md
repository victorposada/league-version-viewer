# League of Legends Version Viewer

Welcome to the League of Legends Version Viewer repository! This project is designed to display the current version of League of Legends on a webpage. The page is automatically updated using GitHub Actions whenever there is a new version release.

## Live Demo

Visit the live demo: [League of Legends Version Viewer](https://yourusername.github.io/league-version-viewer)

## How It Works

The project uses GitHub Pages to host the webpage and GitHub Actions to automate the process of updating the page whenever there is a new League of Legends version.

### GitHub Actions Workflow

The workflow is triggered on a schedule (e.g., daily) and performs the following steps:

1. Fetches the latest League of Legends version from data dragon
2. Updates the webpage with the current version.
3. Commits the changes and pushes them to the `main` branch.
4. GitHub Pages automatically reflects the changes on the live webpage.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests. Your feedback and contributions are highly appreciated!

