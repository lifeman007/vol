"""v2 style enhanced works"""

import web

from infogami.utils import delegate
from infogami.utils.view import render_template, public
from infogami.plugins.api.code import add_hook

class work_edition(delegate.page):
    path = "(/works/OL\d+W)/[^/]+/editions/([^/])"

    def GET(self, work_key, edition_key):
        raise web.seeother('/books/%s' % edition_key)

add_hook("work_edition", work_edition)

class work_editions(delegate.page):
    path = "(/works/OL\d+W)/[^/]+/editions"

    def GET(self, work_key):
        page = web.ctx.site.get(work_key)
        return render_template("work/editions", page)

add_hook("work_editions", work_editions)

def setup():
    pass
