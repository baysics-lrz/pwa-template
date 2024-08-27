from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class ObservationsApphook(CMSApp):
    app_name = "Observations"
    name = "Observations App"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["observations.urls"]