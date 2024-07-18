# Web Scraping Service

A web scraping service built with Flask, deployed on Heroku.

## Description

This project is a web scraping service that collects data from specified websites and stores the results in a SQLite database.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Gavand1969/web_scraping_service.git
    cd web_scraping_service
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    python test_sqlite.py
    ```

5. Run the application:
    ```sh
    python app.py
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000`.
2. Use the interface to start web scraping tasks.

## Deployment

The application is deployed on Heroku and can be accessed at [https://gja-web-scraper-bf807c2e68d5.herokuapp.com/](https://gja-web-scraper-bf807c2e68d5.herokuapp.com/).

To deploy your own version on Heroku:

1. Create a Heroku app:
    ```sh
    heroku create your-app-name
    ```

2. Push the code to Heroku:
    ```sh
    git push heroku main
    ```

3. Open the app in your browser:
    ```sh
    heroku open
    ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contact

Gavin Anderson - [gavanderson13@gmail.com](mailto:gavanderson13@gmail.com)

Project Link: [https://github.com/Gavand1969/web_scraping_service](https://github.com/Gavand1969/web_scraping_service)
