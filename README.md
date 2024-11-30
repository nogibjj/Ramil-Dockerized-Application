[![CI Pipeline](https://github.com/nogibjj/Ramil-Dockerized-Application/actions/workflows/main.yaml/badge.svg)](https://github.com/nogibjj/Ramil-Dockerized-Application/actions/workflows/main.yaml)

# Quote of the Day Flask Application

This is a simple Flask application that displays a random quote from a JSON file and allows users to add new quotes.

## Features
- **Random Quote Display:** Shows a randomly selected quote on the homepage.
- **Add Quote Page:** Lets users add a new quote to the application.
- **Dockerized Deployment:** Easily deploy the application using Docker.

## Requirements
- Python 3.12 or above
- Flask 2.2.5
- Docker (optional for containerized deployment)

## How to Run the Application

### 1. Clone the Repository
```bash
git clone https://github.com/nogibjj/Ramil-Dockerized-Application.git
cd Ramil-Dockerized-Application
```

### 2. Install Dependencies
If running locally without Docker, install the required Python packages:
```bash
make install
```

### 3. Run the Application
Run the Flask application locally:
```bash
python main.py
```

Visit the application at [http://localhost:2222](http://localhost:2222).

## Deploying with Docker

### 1. Build the Docker Image
```bash
docker build -f .devcontainer/.Dockerfile -t quote-of-the-day .
```

### 2. Run the Docker Container
```bash
docker run -p 2222:2222 quote-of-the-day
```

The application will be available at [http://localhost:2222](http://localhost:2222).

### 3. Access the Application Images
The application serves HTML templates located in the `templates` folder. Static files like CSS are in the `static` folder. These files ensure the application is styled and functional.

## Application Images

### Homepage
The homepage displays a random quote.

![Homepage](https://github.com/nogibjj/Ramil-Dockerized-Application/blob/dfa63bcc47c13f66929ebc0cb091d3eb93a5e79a/images/main_page.png)

### Add Quote Page
The "Add Quote" page allows users to input and save new quotes.

![Add Quote](https://github.com/nogibjj/Ramil-Dockerized-Application/blob/dfa63bcc47c13f66929ebc0cb091d3eb93a5e79a/images/add_page.png)

