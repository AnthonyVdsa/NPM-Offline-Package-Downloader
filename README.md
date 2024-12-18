# NPM Offline Package Downloader

This project enables you to download all NPM packages and their dependencies specified in a `package.json` file. The downloaded packages can be stored locally / or in an offline package repository for offline use.

## Features

- Automatically fetches and downloads NPM packages along with all dependencies.
- Uses a simple Docker-based setup for ease of use and portability.
- Saves downloaded packages to a specified location for offline use.

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

Follow these steps to use the NPM Offline Package Downloader:

### 1. Clone the Repository

```bash
git clone https://github.com/AnthonyVdsa/NPM-Offline-Package-Downloader.git
cd NPM-Offline-Package-Downloader/
```

### 2. Prepare Your `package.json`

Ensure you have a valid `package.json` file with all the dependencies you want to download in the root directory.

### 3. Build and Run the Docker Container

Build the Docker image:

```bash
docker compose build
```

Run the container:

```bash
docker compose up
```

### 4. Access the Downloaded Packages

Once the process completes, the downloaded packages will be available in the `./npm_packages_downloaded` directory specified in your Docker Compose file.

## Project Structure

```
.
├── Dockerfile                # Docker configuration file
├── docker-compose.yml        # Docker Compose configuration
├── script_dependencies.py    # Script to download packages
├── package.json              # Your input file containing dependencies
└── npm_packages_downloaded/  # Directory where downloaded packages are stored
```

## Dockerfile Overview

The Dockerfile is set up to:

1. Copy your `package.json` file into the container.
2. Run a script that installs all dependencies listed in the `package.json` file using NPM.
3. Save the downloaded packages into the specified directory.

## Notes

- Ensure the `package.json` file is valid and contains all required dependencies before running the container.
- The output directory (`npm_packages_downloaded`) will be created automatically if it doesn't already exist.
- This setup is ideal for environments with limited or no internet access, as it allows you to prefetch dependencies in advance.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have improvements or bug fixes.
