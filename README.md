# Django Tree Menu Project

This Django project implements a dynamic tree menu system using custom template tags and a flexible data model for hierarchical menu structures. The tree menu is designed to display multi-level nested items with active state tracking and automatic parent expansion. It's a practical solution for websites requiring complex navigational structures.

## Features

- **Dynamic Tree Menu**: The menu is generated dynamically from the database, supporting unlimited levels of nesting.
- **Parent-Child Relationships**: Each menu item can have child items. The active item’s parent and ancestor items are automatically expanded.
- **Custom Template Tags**: The menu is rendered using a custom template tag (`draw_menu`), which can be reused across different templates.
- **URL Matching**: The active state of a menu item is determined based on the current URL, and parent items are expanded accordingly.

## Project Structure

The project is divided into two main apps:

### 1. **`tree_menu` App**

This app contains the core logic of the tree menu, including the models, template tags, and templates required to generate the menu.

- **Models**: 
  - `Menu`: Represents the overall menu.
  - `MenuItem`: Represents individual menu items with parent-child relationships.

- **Template Tags**:
  - A custom template tag `draw_menu` is used to render the menu based on the current URL and active state.

- **Menu Template**: 
  - The `menu.html` template is responsible for rendering the menu, including recursive rendering for nested items.

### 2. **`tree_menu_test` App**

This app is a simple test application that demonstrates the tree menu in action. It includes a basic set of pages that can be accessed through the tree menu to see how the active item and parent expansion work.

- **Test Pages**: 
  - The test app includes pages like "Home", "About Us", "Our Team", "Contact Us", and various sub-pages for services and technologies such as Flask, Django, and FastAPI.

## How to Use

1. **Setup**: 
   - Clone the repository and set up the project with `pip`.
```bash
pip install -r requirements.txt
```

2. **Running the Test App**:
   - Start the development server and navigate through the test pages to see the tree menu in action.
```bash
python manage.py runserver
```
