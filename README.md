# Leave Management App

The app helps employees/ staff's to request leaves from administrators.

There are 3 roles of user:
- None (Does not have permission to the panel, unless accepted by administrator)
- Viewer (Have access to the request and requests list pages, but can't create requests)
- Employee (Allowed to create requests to be reviewed by administrator)
- Manager (Allowed to craete the new request and list all leave requests)

Adminitrator can:
- Manage all users and change their roles (None -> Viewer, Viewer -> Employee, Employee -> None, etc)
- Allow/Reject requests from users changing its status (Waiting -> Rejected, Waiting -> Approved, Rejected -> Approved, Approved -> Cancelled, etc)

Users (Viewer/Employee) can see all their requests and filter them by status and leave type. CalendarView is used to choose dates (Start date and Finish date).

The app was built with Django 4. Bootstrap 5 is used for the Front-End.
- Login/Registration
- SQLite3
- Two apps (Members, Management System)
- Auth system via email
