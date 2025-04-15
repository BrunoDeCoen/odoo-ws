{
    "name":"Test",
    "summary": "owl Test module",
    "author": "Bruno De Coen",
    "version": "0.0.1",
    "license": "LGPL-3",
    "category": "bdc-ws",
    "depends": ["base", "web"],
    "data": [
        #VIEWS
        "views/templates.xml",
    ],
    "assets": {
        "mp_owl.assets_playground": [
            ("include", "web._assets_helpers"),
            "web/static/src/scss/pre_variables.scss",
            "web/static/lib/bootstrap/scss/_variables.scss",
            "web/static/lib/bootstrap/scss/_maps.scss",
            ("include", "web._assets_bootstrap"),
            ("include", "web._assets_core"),
            "web/static/src/libs/fontawesome/css/font-awesome.css",
            "mp_owl/static/src/**/*",
        ],
    },
    "application": True,
    "installable": True,
    "auto_install": False
}