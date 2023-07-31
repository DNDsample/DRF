# Project Name 
Book Collection API
Description
Project Name is a Django REST framework API for managing a collection of books.

Table of Contents

- Requirements #requirements
- Installation #installation
- Usage #usage
- API Endpoints #api-endpoints
- License #license

Requirements

- Python (3.6 or higher)
- Django (3.0 or higher)
- Django REST framework (3.11 or higher)
- drf-yasg (1.20 or higher)

Installation

1. Clone the repository or download the project files:

git clone https://github.com/your_username/project_name.git

2. Navigate to the project directory:
cd project_name

3. Create a virtual environment (optional but recommended):
python -m venv venv

4. Activate the virtual environment:
   
For Windows:
venv\Scripts\activate

For macOS/Linux:
source venv/bin/activate

5. Install the required dependencies:
pip install -r requirements.txt

## Usage

1. Run database migrations:
python manage.py migrate

2. Create a superuser to access the Django admin interface:
python manage.py createsuperuser

3. Start the development server:
python manage.py runserver

4. Open your web browser and go to `http://localhost:8000/admin/` to access the Django admin interface and log in using the superuser credentials.

5. To view the Swagger/OpenAPI documentation for the API, go to `http://localhost:8000/swagger/

# End points
1.http://127.0.0.1:8000/books/ - This URL corresponds to the BookListCreateView view and 
allows you to list all books and create a new book using HTTP methods like GET and POST.

2.http://127.0.0.1:8000/books/<int:pk>/ - This URL corresponds to the BookRetrieveUpdateDeleteView view and
allows you to retrieve, update, or delete a specific book by providing its primary key (ID) in the URL. You can use HTTP methods like GET, PUT, and DELETE.

3.http://127.0.0.1:8000/books/<int:pk>/partial/ - This URL corresponds to the BookPartialUpdateView view and 
allows you to partially update a specific book by providing its primary key (ID) in the URL. You can use the HTTP method PATCH for this.
   
4.http://127.0.0.1:8000/swagger/ -  This URL provides access to the Swagger documentation for your Django REST framework API. 
The Swagger documentation allows you to explore your API's endpoints, view available schemas, and test the API interactively.

