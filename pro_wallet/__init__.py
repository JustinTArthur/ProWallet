from electrum.i18n import _

fullname = _('Pro Wallet')
description = ''.join([
    _("This plugin adds a wallet for power users."), '<br/>',
    _("For more information, visit"),
    " <a href=\"https://github.com/JustinTArthur/ProWallet\">https://github.com/JustinTArthur/ProWallet</a>"
])
requires_wallet_type = ('pro',)
registers_wallet_type = 'pro'
available_for = ('qt',)
