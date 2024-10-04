# Inventory CRUD API

This repository contains materials related to the Inventory CRUD API development using Django and Django REST Framework. It covers user authentication, inventory item management, API documentation, unit testing, and logging.

## Table of Contents

1. [Introduction](#introduction)
2. [Folder Structure](#folder-structure)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Contributing](#contributing)

## Introduction

The Inventory CRUD API is a simple application designed to manage inventory items efficiently. This API allows users to perform Create, Read, Update, and Delete operations on inventory items. It includes user authentication using JWT tokens, thorough API documentation, logging for monitoring and debugging, and unit tests for ensuring the functionality of API endpoints.

## Folder Structure

The folder structure of this repository is organized as follows:

- `inventory/`: Contains the Django application with models, views, and serializers.
- `tests/`: Includes unit tests for the API endpoints.
- `requirements.txt`: Lists the necessary packages and dependencies for the project.
- `README.md`: Documentation for the project.

## Getting Started

To get started with this repository, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Datirsayali12/inventory-management.git
    ```

2. Navigate to the cloned repository:

    ```bash
    cd inventory-management
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create the database and add configuration in `settings.py`.

5. Set up Redis on your local machine (optional).

6. Create tables in the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Finally, run the server:

    ```bash
    python manage.py runserver
    ```

## Usage

Feel free to use the materials in this repository for self-learning, academic purposes, or as a reference for your projects. Make sure to adhere to any licensing terms mentioned in individual files or directories.

## Contributing

If you find any issues, errors, or have suggestions for improvement, please feel free to open an issue or submit a pull request. Contributions from the community are highly appreciated!
