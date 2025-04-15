{
    "name": "Series",
    "summary": "Module to manage series",
    "author": "Bruno De Coen",
    "version": "0.0.1",
    "license": "LGPL-3",
    "category": "bdc-ws",
    "depends": ["base","website","web","crm"],
    "data": [
        # SECURITY
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        # VIEWS
        "views/serie_menuitems.xml",
        "views/serie_views.xml",
        "views/document_views.xml",
        "views/website_series_templates.xml",
        "views/snippets/s_serie_snippet.xml",
        "views/snippets/options.xml",
        #REPORTS
        "reports/mp_serie_report_action.xml",
        "reports/mp_serie_report_template.xml",
        #ACTION MENU
        "views/mp_serie_action_menu.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False
    #"data_dir": "/files", #Specify file storage location
}

