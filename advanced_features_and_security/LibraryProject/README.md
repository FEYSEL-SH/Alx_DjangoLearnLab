# LibraryProject
## Permissions and Groups Setup

In this project, we have defined custom permissions for the `Post` model, which include:

- `can_view`: Permission to view posts.
- `can_create`: Permission to create posts.
- `can_edit`: Permission to edit posts.
- `can_delete`: Permission to delete posts.

We have also created three user groups:

- **Editors**: Can create and edit posts.
- **Viewers**: Can only view posts.
- **Admins**: Have full access (create, edit, delete, and view).

These permissions are assigned to groups via Django’s admin interface, and the `@permission_required` decorator is used in the views to restrict access.
