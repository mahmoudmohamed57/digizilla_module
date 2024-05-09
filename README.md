# Digizilla model
### Digizilla model is a custom model containing many fields like (Name, Gender, Country, Joining Date, Tags, Customers, Company, Notes, Comments) and has a chatter "Messages and logger" r that tracks any change in the previous fields and hides the Create button from the form by adding create="0" At last it Generates a PDF report for your model that contains all the previous fields excluding the message logger
### Folder structure
```
digizilla_module 
├── models
    ├── __init__.py
    ├── digizilla.py
├── views
    ├── digizilla_form.xml
    ├── digizilla_knaban.xml
    ├── digizilla_list.xml
    ├── digizilla_report_template
├── __init__.py
├── __mainfest__.py
```