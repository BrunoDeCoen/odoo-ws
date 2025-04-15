from odoo import api, fields, models
from odoo.exceptions import UserError

class MpSerie(models.Model):
    _name = "mp.serie"
    _description = "MP serie"

    titel = fields.Char(string="Titel", required=True)
    omschrijving = fields.Text(string="Omschrijving")
    tag = fields.Text(string="Tag")
    afbeelding = fields.Binary(string="Afbeelding")

    document_ids = fields.One2many(comodel_name='mp.document', inverse_name="serie_id", string='Document')

    def action_display_error(self):
        raise UserError("This is a message from the button!")

    def action_print_report(self):
        return self.env.ref('mp_module_serie.mp_serie_report_action').report_action(self)