# Little Lemon 

### Base URL: http://127.0.0.1:8000/auth/

### Data Format: JSON

## Role 
### `Admin - 1` `Manager - 2` `Employee - 3` `Delivery Crew - 4` `Customer - 5` 
###
# Registration:

> `Register (POST /register)`

```json
{
    "username": "username",
    "email": "user@email.com",
    "password": "strong_password"
}
```

> `Register Admin (POST /register-admin): (Potentially Restricted)`

```json
{
    "username": "username",
    "email": "admin@email.com",
    "password": "strong_password"
}
```

> `Login (POST /login)`

```json
{
    "email": "user@email.com",
    "password": "user_password"
}
```

> `Change Password (POST /change-password):`

```json
{
    "email": "user@email.com",
    "old_password": "current_password",
    "new_password": "new_strong_password"
}
```

> `Update Role (POST /update-role): (Requires Authentication) [Only Admin can chnage roles.]`

```json
{
    "uid" : "efa691fef3b84a5c8e414275a439ce0b",
    "role": "3"
}
```

# Menu:


> `Fetch Categories (GET /menu/categories/all)`

> `Add Category (POST /menu/add-category/)`

```json
{
    "name": "Chinese"
}
```

> `Update Category (POST /menu/update-category/category_id)`

```json
{
    "name": "Chinese"
}
```

> `Delete Category (DELETE /menu/delete-category/category_id)`
#
> `Fetch Items (GET /menu/items/all)`

> `Add Item (POST /menu/add-item/)`

```json
{
    "name": "Fried Rice",
    "category_uid": "66d8cebcca7c43e6bfe402e3d86913de"
}
```

> `Update Item (POST /menu/update-item/item_id)`

```json
{
    "name": "Fried Rice",
    "category_uid": "66d8cebcca7c43e6bfe402e3d86913de"
}
```

> `Delete Item (DELETE /menu/delete-item/item_id)`
#
#
### `Roles:`

    Admin
    Manager
    Employee
    Customer
    Delivery Crew

### `Admin:`

    CRUD Category
    CRUD Item
    Update Roles
    Add Manager
    Add Employee

### `Manager:`

    Add Item of the Day
    Assign Employee
    Assign Delivery Crew to Customer
    Assign Orders to Delivery Crew

### `Delivery Crew:`

    See Orders
    Delivery Orders
    Update Orders

### `Customer:`

    Browse Categories
    Browse All Items
    Browse Items by Category
    Paginated Items
    Sort Items by Price
    Add Item to Cart
    Place Order
    View Order List
    View Past Order List

