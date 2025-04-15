from odoo import http
from odoo.http import request

class SeriesController(http.Controller):
    
    @http.route('/series', type='http', auth='public', website=True)
    def series_list(self, **kwargs):
        series = request.env['mp.serie'].sudo().search([])
        return request.render('mp_module_serie.series_list_template', {'series': series})
    
    @http.route('/series/<int:series_id>', type='http', auth='public', website=True)
    def series_detail(self, series_id, **kwargs):
        series = request.env['mp.serie'].sudo().browse(series_id)
        return request.render('mp_module_serie.series_detail_template', {'series': series})

    @http.route('/series/data', type='json', auth='public', website=True)
    def load_snippet(self):
        series = request.env['mp.serie'].sudo().search([])
        data = [{'id': rec.id, 'titel': rec.titel, 'omschrijving': rec.omschrijving, 'tag': rec.tag, 'afbeelding': rec.afbeelding} for rec in series]
        return data