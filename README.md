<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">.</h1>
</p>
<p align="center">
    <em>Reflex App with deployment, logging and user management.</em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. -->
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

Video Walkthrough: https://www.youtube.com/watch?v=VYPsVksAqOM (Edit 29th May 2024: the video is slightly outdatet since we use the reflex-clerk pypi package instead of manually wrapping the clerk react component)

This Reflex Template facilitates the seamless creation and deployment of Reflex web applications with robust production environment setups. Leveraging Docker Compose and Caddy for orchestration and web content delivery, the project streamlines service configurations, database management, and secure routing. Automating deployment through GitHub Actions, the project offers an end-to-end solution for building feature-rich web apps with Clerk and Betterstack integrations. Its core functionalities span environment configuration, component creation, authentication handling, and logging customization, empowering developers to focus on crafting engaging user experiences.

---

##  Features

<code>► User Management via Clerk (clerk.com) using the reflex-clerk pypi package (https://github.com/kroo/reflex-clerk)</code>

<code>► Log Management via Betterstack (logs.betterstack.com)</code>

<code>► Production deployment of reflex app taken from: https://github.com/reflex-dev/reflex/blob/main/docker-example/README.md and https://www.youtube.com/watch?v=1iuefsBCHQc</code>

<code>► Github Action workflow adapted from https://github.com/masenf/rx_shout/blob/main/.github/workflows/deploy.yml</code>

---

##  Repository Structure

```sh
└── ./
    ├── .github
    │   └── workflows
    ├── Caddy.Dockerfile
    ├── Caddyfile
    ├── LICENSE
    ├── assets
    │   ├── dentro_logo.svg
    │   └── favicon.ico
    ├── compose.prod.yaml
    ├── compose.yaml
    ├── prod.Dockerfile
    ├── reflex_template
    │   ├── __init__.py
    │   ├── components
    │   ├── reflex_template.py
    │   └── utils
    ├── requirements.txt
    └── rxconfig.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                   | Summary                                                                                                                                                                                                                                                                                                        |
| ---                                    | ---                                                                                                                                                                                                                                                                                                            |
| [compose.prod.yaml](compose.prod.yaml) | Enables running the app in production mode with Postgres and Redis. Defines services for database and caching, configures environment variables, and sets up dependencies. Utilizes Docker Compose to orchestrate the app components.                                                                          |
| [prod.Dockerfile](prod.Dockerfile)     | Generates a production-ready Docker image for a Reflex web app. Initializes, installs dependencies, deploys templates, and exports static frontend files. Copies artifacts into a lightweight container, handles signal handling, ensures database migrations, and runs the backend on production environment. |
| [Caddy.Dockerfile](Caddy.Dockerfile)   | Copies web static files and configures Caddy server in the parent repository for serving web content.                                                                                                                                                                                                          |
| [requirements.txt](requirements.txt)   | Enables Python dependencies management for the project, ensuring seamless integration of critical packages such as logtail, python-dotenv, reflex, and ruff.                                                                                                                                                   |
| [rxconfig.py](rxconfig.py)             | Defines configuration for the reflex_template app using Reflex library and loads environment variables.                                                                                                                                                                                                        |
| [Caddyfile](Caddyfile)                 | Enables dynamic routing and reverse proxying for backend services in the site root based on specified rules to handle incoming requests efficiently.                                                                                                                                                           |
| [compose.yaml](compose.yaml)           | Deploys a production instance of the Reflex app with Caddy webserver for TLS termination and reverse proxying. Defines service configurations, environment variables, and volumes essential for secure and reliable deployment within the repositorys architecture.                                            |

</details>

<details closed><summary>.github.workflows</summary>

| File                                         | Summary                                                                                                                                                                         |
| ---                                          | ---                                                                                                                                                                             |
| [deploy.yaml](.github/workflows/deploy.yaml) | Automates deployment workflows with GitHub Actions for the repository. Manages continuous integration and deployment processes, ensuring seamless delivery of software updates. |

</details>

<details closed><summary>reflex_template</summary>

| File                                                     | Summary                                                                                                                                                                                                                                          |
| ---                                                      | ---                                                                                                                                                                                                                                              |
| [reflex_template.py](reflex_template/reflex_template.py) | Outlines steps to create a basic app, defines app state, and renders app content with user-specific greetings and info. Offers features like Clerk Integration, Betterstack Integration, Docker compose files, and Github Action for deployment. |

</details>

<details closed><summary>reflex_template.components</summary>

| File                                              | Summary                                                                                                                                             |
| ---                                               | ---                                                                                                                                                 |
| [navbar.py](reflex_template/components/navbar.py) | Employs reflex and reflex-clerk to construct a sticky navbar with a logo, user button, and styling attributes for a cohesive front-end experience. |

</details>

<details closed><summary>reflex_template.utils</summary>

| File                                                         | Summary                                                                                                                                                                        |
| ---                                                          | ---                                                                                                                                                                            |

| [logging_config.py](reflex_template/utils/logging_config.py) | Defines custom log formatting for different log levels in the project, enhancing log clarity and readability by applying distinct colors and styles based on log severity.     |

</details>

---

##  Getting Started

**System Requirements:**

* **Python**: `version 3.12`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the . repository:
>
> ```console
> $ git clone https://github.com/dentro-innovation/reflex_template
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd reflex_template
> ```
>
> 3. Create and source a python environment:
> ```console
> $ python3.12 -m venv .venv; source .venv/bin/activate
> ```
>
> 4. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```


###  Usage

<h4>From <code>source</code></h4>

> Create .env and set necessary environment variables (at least define CLERK_PUBLISHABLE_KEY and CLERK_SECRET_KEY):
> ```console
> $ mv cp .example.env .env; nano .env
> ```
>
> Run . using the command below:
> ```console
> $ reflex init; reflex run
> ```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://local//issues)**: Submit bugs found or log feature requests for the `.` project.
- **[Submit Pull Requests](https://local//blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://local//discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your local account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone ../.
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to local**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://local{//}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=">
   </a>
</p>
</details>

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE](reflex_template/LICENCE) file.

---

##  Acknowledgments

- Elliot Kroo for the reflex-clerk pypi package
- Masen for debugging the production deployment
- Alek for the initial Clerk reflex wrapper
- Lendemor for debugging advanced Clerk Setup with Carl
- Carl for providing code for the advanced clerk setup

[**Return**](#-overview)

---
