from odoo import api, fields, models

class MpDocument(models.Model):
    _name = "mp.document"
    _description = "MP document"

    naam = fields.Char(string="Naam", required=True)
    omschrijving = fields.Char(string="Omschrijving", required=True)
    document = fields.Binary(string="Document", attachment=True)
    type=fields.Selection(string="Type",
                            selection=[
                                ("particulier","Particulier"),
                                ("professional","Professional"),
                                ("architect","Architect")
                            ],
                            copy=False)
    serie_id = fields.Many2one('mp.serie')