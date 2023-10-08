# coffeeshop

Welcome to the coffeeshop repository! This is a brief guide on how to get started with this
project.

# Installation

1. Clone the repository

First, clone the project repository to your local machine. Open your terminal and run:
git clone https://github.com/Art01ur/coffeeshop.git
cd coffeeshop

2. Install dependencies

To install the necessary Python packages, use the `pip` package manager:
pip install Django==4.2.5
pip install django-tastypie==0.14.6


3. Apply migrations

Run the following commands to apply database migrations:
python manage.py makemigrations
python manage.py migrate

4. Start the development server

You can now start the development server:
python manage.py runserver