Python Blog with Flask and Bootstrap

This is a blog project made with Python and Flask, using a PostgreSQL database to store data. The graphical interface was built using Bootstrap, allowing the website to have a modern and responsive design.

Requirements:

Python 3.x
Flask
PostgreSQL
Bootstrap

Installation:

Clone the repository:
bash
Copy code
git clone https://github.com/byterbluu/Project-Blog-Flask.git

Install the dependencies:

bash

Copy code

pip install -r requirements.txt

Create the PostgreSQL database:
bash
Copy code
createdb blog_db
Initialize the database:
bash
Copy code
flask db init
flask db migrate
flask db upgrade
Run the server locally:
bash
Copy code
flask run
Usage:
The website allows users to register, log in, create posts, and view other users' posts. Additionally, users can edit and delete their own posts.

