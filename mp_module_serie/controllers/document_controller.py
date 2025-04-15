from odoo import http
from odoo.http import request
import base64

class DocumentController(http.Controller):

    @http.route('/document/download', type='http', auth="user")
    def download_document(self, id, **kw):
        record = request.env["mp.document"].browse(int(id))         # => model name
        filecontent = base64.b64decode(record["document"] or '')    # => field name
        if not filecontent:
            return request.not_found()

        return request.make_response(filecontent,
                                     headers=[
                                         ('Content-Type', 'application/octet-stream'),
                                         ('Content-Disposition', 'attachment; filename=document.pdf'),
                                     ])