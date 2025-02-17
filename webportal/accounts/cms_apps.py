from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class AccountsApphook(CMSApp):
    app_name = "accounts"
    name = "Accounts App"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["accounts.urls"]
