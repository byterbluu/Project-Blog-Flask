# Python Blog with Flask and Bootstrap
***
This is a blog project made with Python and Flask, using a PostgreSQL database to store data. The graphical interface was built using Bootstrap, allowing the website to have a modern and responsive design.

Requirements:

A list of technologies used within the project:
* [Python 3.x](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [PostgreSQL](https://www.postgresql.org/)
* [Bootstrap](https://getbootstrap.com/)



## Installation:
***

Clone the repository:
```
$ git clone https://github.com/byterbluu/Project-Blog-Flask.git
```
Install the dependencies:
```
$ pip install -r requirements.txt
```
Create the PostgreSQL database:
```
createdb blog_db
```
Initialize the database:
```
flask db init
flask db migrate
flask db upgrade
```
Run the server locally:
```
flask run
```
