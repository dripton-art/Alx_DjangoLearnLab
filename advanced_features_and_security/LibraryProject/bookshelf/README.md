# Django Books App – Group & Permission Setup

## User Groups

We use Django’s `Group` and `Permission` system to control access.

### Groups:

| Group Name | Permissions Assigned |
|------------|----------------------|
| **Viewers** | `can_view`          |
| **Editors** | `can_create`, `can_edit`, `can_view` |
| **Admins**  | `can_create`, `can_edit`, `can_delete`, `can_view` |

---

## Custom Permissions (Defined in `Book` model)

| Codename      | Purpose             | Used In               |
|---------------|---------------------|------------------------|
| `can_create`  | Add new books       | `add_book` view       |
| `can_edit`    | Edit existing books | `edit_book` view      |
| `can_delete`  | Delete books        | `delete_book` view    |
| `can_view`    | View book list      | `list_books` view     |

---

## How to Test Access

1. Create users in Django admin.
2. Assign them to one of the groups: `Viewers`, `Editors`, or `Admins`.
3. Log in and try accessing:
   - `/books/` → list all books
   - `/books/add/` → add new book
   - `/books/<id>/edit/` → edit a book
   - `/books/<id>/delete/` → delete a book

Each route checks permissions with `@permission_required` decorators.

---

## Developer Notes

- Permissions are enforced in both views and templates.
- Use `user.has_perm('bookshelf.can_edit')` in custom logic if needed.
- In templates: `{% if perms.bookshelf.can_edit %}`

