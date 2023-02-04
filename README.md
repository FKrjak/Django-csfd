# Django CSFD prototype

Small Django projects that read and processes top X movies from popular Czech movie website csfd.cz.

# Getting Started

There are multiple options for running this small application. Let's discuss two main options.

## 1. Using Docker

- Install docker
- In the root directory run commands

```
docker build -t django-csfd .
```

- Then start the container with command

```
docker run -dp 8000:8000 django-csfd
```

- Website is accessible on url http://localhost:8000

## 2. Using local Python

- Install all requirements from requirements.txt

```
pip install -r requirements.txt
```

- Then run the command to start the application

```
python3 manage.py runserver
```

- Application is accessible on url http://127.0.0.1:8000/

# Development mode

I personally use development inside containers, with help of Makefile. Provided tutorial to run this application in development mode is gonna focus only on VSCode.

## Running development mode VSCode

- Install VSCode extension [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- Clone and open this repository inside VSCode
- Refresh your VScode window and on the right bottom of the screen notification that says "Open in the container should appear
- Click on it and wait, till the container is installed
- When done, open the terminal, and with a simple `make dev` command application can be started up