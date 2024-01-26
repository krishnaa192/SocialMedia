# Social Media Platform using Django Rest Framework

This project is a simple social media platform built using Django Rest Framework. It allows users to create posts, follow other users, like posts, and comment on posts.

## Features

- **User Authentication**: Users can sign up, log in, and log out securely.
- **Profile Management**: Users can update their profiles, including profile picture and bio.
- **Posts**: Users can create, view, update, and delete their own posts.
- **Following**: Users can follow other users to see their posts on their feed.
- **Likes**: Users can like and unlike posts.
- **Comments**: Users can comment on posts.

## Requirements

- Python 3.x
- Django
- Django Rest Framework


## Installation


1. Clone the repository:

```bash
git clone https://github.com/yourusername/SocialMedia.git
cd SocialMedia
```

1-Create a virtual environment:
```bash
python3 -m venv env
```
2-Activate the virtual environment:
```bash
source env/bin/activate
```
3-Install the dependencies:
```bash
pip install -r requirements.txt

```
4-Run migrations:
```bash
python manage.py migrate
```
5-Create a superuser:
```bash
python manage.py createsuperuser
```
6-Run the development server:
```bash
python manage.py runserver
```
7-Access the application at http://localhost:8000.

## 8-Usage
Create a new account or log in with an existing account.
Create posts, update profile, follow other users, like posts, and comment on posts.
Explore the API endpoints provided by Django Rest Framework.
## API Endpoints
Users: /api/users/
Posts: /api/posts/
Comments: /api/comments/
Likes: /api/likes/

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.




