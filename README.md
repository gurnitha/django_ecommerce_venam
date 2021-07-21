## DJANGO STARTER PROJECT

### ------------
### 1. SETUP
### ------------


#### 1.1.1 Setup DONE, refer to README-SETUP.md


### --------------
### 2. DATABASE
### --------------


#### 2.1.2 Create and connect the database

        modified:   .gitignore
        modified:   README.md
        new file:   _sourcecodes
        modified:   apps/core/admin.py
        modified:   apps/core/models.py
        modified:   config/.env


### ----------
### 3. MODEL
### ----------


#### 3.1.3 Create Banner, Category, Brand, Color, Size, Product, ProductAttribute models

        modified:   README.md
        modified:   README.md
        modified:   apps/core/models.py


#### 3.2.4 Run migrations and create superuser

        modified:   README.md
        new file:   apps/core/migrations/0001_initial.py


#### 3.3.5 Register models to admin and define the admin display

        modified:   README.md
        modified:   apps/core/admin.py

### ----------------
### 4. TEMPLATES
### ----------------


#### 4.1.6 Adding and loading static files, create homepage using template inheritance


#### 4.2.7 Creating category page

        new file:   apps/core/templates/core/category_list.html
        modified:   apps/core/templates/core/shared/navbar.html
        modified:   apps/core/urls.py
        modified:   apps/core/views.py
        new file:   media/cat_imgs/4.jpg
        new file:   media/cat_imgs/4_GefSQZE.jpg


#### 4.3.8 Customize Django Admin Part 1 - Adding class Meta

        Note:
        class Meta is about how to display the plural name of
        the model/table in the admin panel.
        It also possible to add siquance number for it. 

        modified:   README.md
        modified:   apps/core/models.py


#### 4.4.8 Customize Django Admin Part 1 - Using mark_safe to showing image thumbnail in admin panel

        modified:   apps/core/admin.py
        modified:   apps/core/models.py


#### 4.5.8 Create brand_list page, Insert and Read data

        modified:   README.md
        new file:   apps/core/templates/core/brand_list.html
        modified:   apps/core/templates/core/shared/navbar.html
        modified:   apps/core/urls.py
        modified:   apps/core/views.py
        new file:   media/brand_imgs/1.jpg
        new file:   media/brand_imgs/5.jpg


#### 4.6.9 Product list Part 1 - Create product_list template, views and urls

        modified:   README.md
        modified:   _sourcecodes
        new file:   apps/core/templates/core/product_list.html
        modified:   apps/core/templates/core/shared/navbar.html
        modified:   apps/core/urls.py
        modified:   apps/core/views.py

#### 4.6.9 Product list Part 1 - Insert and Read data based on (category, brand, color, and size)

        modified:   README.md
        modified:   _sourcecodes
        modified:   apps/core/__pycache__/views.cpython-39.pyc
        modified:   apps/core/templates/core/product_list.html
        modified:   apps/core/views.py
        new file:   media/product_imgs/1.jpg
        new file:   media/product_imgs/5.jpg






























