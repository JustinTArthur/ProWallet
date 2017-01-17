from electrum.plugins import BasePlugin
from electrum.wallet import Deterministic_Wallet


class ProWallet(Deterministic_Wallet):
    pass


class ProWalletPlugin(BasePlugin):
    wallet_class = ProWallet
