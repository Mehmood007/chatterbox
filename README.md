# ChatterBox

## Description

**This project introduces the development of a real-time chat application using Django REST Framework (DRF) for the backend and React for the frontend. It focuses on building a robust API that facilitates real-time communication, leveraging Django Channels for handling WebSocket connections. The backend is designed to manage user authentication, message storage, and real-time event broadcasting, allowing users to send and receive messages instantly. It integrates DRF to create a RESTful API that communicates with the React frontend, ensuring a seamless user experience. On the frontend, React is utilized to build a dynamic user interface that connects to the backend via WebSockets and RESTful API calls. Users can engage in real-time conversations, with features such as targeted messaging and group chats.**

## Features

- Realtime Chats
- Group Chat  
- Authentication


### Technologies Used

| Python | Django | Rest Framework | SQLite | React |
|--------|--------|----------------|--------|--------|
| <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="50"> | <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Django_logo.svg" width="50"> | <img src="https://www.django-rest-framework.org/img/logo.png" width="100"> | <img src="https://www.sqlite.org/images/sqlite370_banner.gif" width="100"> | <img src="https://www.svgrepo.com/show/327388/logo-react.svg" width="50"> |



## Setup Locally
- **First clone repo locally**  
  **Run below command in terminal**  
  `git clone https://github.com/Mehmood007/chatterbox.git`  

-  **ADD SECRET_KEY TO ENV**  
  Rename `.env-example` to `env` and Assign value to `SECRET_KEY`  

- **Install Dependencies**  
  First make sure virtual environment is activated  
  `pip install -r requirements.txt`

- **Run Migrations in app directory**   
  `python manage.py migrate`

- **Run Server**  
  `python manage.py runserver`