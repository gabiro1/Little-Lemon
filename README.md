# Little Lemon Web Application

## Project Description
The Little Lemon web application is a Django-based system designed to provide an online presence for Little Lemon, a neighborhood bistro. The platform allows users to explore the restaurant’s menu and detailed descriptions of individual menu items. The system supports a multi-page structure and integrates dynamic content powered by the Django framework.

## Features
- **Home Page**: Displays the introduction and highlights of the restaurant.
- **About Page**: Provides detailed information about Little Lemon.
- **Booking Page**: Allows customers to make reservations.
- **Menu Page**: Displays all available menu items along with their prices.
- **Menu Item Page**: Provides detailed descriptions of individual menu items.

## System Workflow

1. **Database Design**:
   - The project includes a `Menu` model in `models.py` with the following attributes:
     - `name` (CharField): Name of the menu item.
     - `price` (IntegerField): Price of the menu item.
     - `menu_item_description` (TextField): Detailed description of the menu item.
   - A `Booking` model is also pre-configured to manage customer reservations.

2. **Admin Panel Configuration**:
   - The `Menu` model is registered in the admin panel.
   - Data for menu items can be added or updated using the admin panel.

3. **Dynamic Pages**:
   - **Menu Page**:
     - Uses a `menu()` view function to retrieve all menu items from the database and display them.
     - The template includes Django Template Language (DTL) to iterate through menu items and render their names and prices.
   - **Menu Item Page**:
     - Each menu item on the menu page links to its detailed view using dynamic URLs.
     - The `display_menu_items()` view function retrieves details of a specific menu item using its primary key (PK).

4. **Routing**:
   - Project-level `urls.py` includes routes for the admin panel and app-level URLs.
   - App-level `urls.py` includes paths for the following pages:
     - Home (`/`)
     - About (`/about/`)
     - Booking (`/book/`)
     - Menu (`/menu/`)
     - Menu Item (`/menu_item/<int:pk>/`)

5. **Templates**:
   - Each page has its own HTML file in the `templates` directory.
   - Pages extend a common `base.html` layout for consistent styling.
   - Static files, including CSS and images, are included for improved UI/UX.

6. **Commands**:
   - Run the development server:
     ```bash
     python manage.py runserver
     ```
   - Create and apply migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```
   - Create a superuser:
     ```bash
     python manage.py createsuperuser
     ```

7. **Testing**:
   - After starting the server, visit the following URLs to test the application:
     - Home: `http://127.0.0.1:8000/`
     - Menu: `http://127.0.0.1:8000/menu/`
     - Menu Item: `http://127.0.0.1:8000/menu_item/<int:pk>/`
   - Test CRUD operations for menu items using the admin panel at `http://127.0.0.1:8000/admin/`.

## Prerequisites
- Python 3.x
- Django 4.x
- A code editor (e.g., VS Code)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd littlelemon
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the application in your browser at `http://127.0.0.1:8000/`.

## File Structure
```
littlelemon/
├── littlelemon/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── restaurant/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── menu.html
│   │   ├── menu_item.html
│   │   ├── index.html
│   │   ├── about.html
│   │   └── book.html
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
└── manage.py
```

## Future Enhancements
- Add user authentication for secure bookings.
- Implement a search feature for menu items.
- Enhance the UI with additional styling and animations.
- Add a contact form for customer inquiries.

## Acknowledgments
This project was developed as part of the Django course to provide practical experience in building web applications.
