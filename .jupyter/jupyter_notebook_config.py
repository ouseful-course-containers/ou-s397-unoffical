# Traitlet configuration file for jupyter-notebook.
#jupyter_notebook_config.py

c.ServerProxy.servers = {
    'Genie': {
        'command': ['node', 'genie/genie_app.js'],
        'port': 3000,
        'timeout': 120,
        'launcher_entry': {
            'title': 'Genie',
            'icon_path': '/home/jovyan/.jupyter/genie.svg'
        },
    },
}
