{
    'name': 'Digizilla Module',
    'version': '1.0',
    'depends': ['base', 'mail'],
    'author': 'Mahmoud Mohamed',
    'category': 'Custom',
    'description': 'Custom module for Digizilla',
    'data': [
        'views/digizilla_list.xml',
        'views/digizilla_kanban.xml',
        'views/digizilla_form.xml',
        'views/digizilla_report_template.xml',
    ],
    'installable': True,
    'application': True,
}
