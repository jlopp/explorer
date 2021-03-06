from django import template

from blockcypher.utils import satoshis_to_btc, satoshis_to_btc_rounded
from blockcypher.api import _get_websocket_url
from blockcypher.constants import COIN_SYMBOL_MAPPINGS


register = template.Library()


@register.filter(name='satoshis_to_btc_rounding')
def satoshis_to_btc_rounding(satoshis):
    return satoshis_to_btc_rounded(satoshis=satoshis, decimals=4)


@register.filter(name='satoshis_to_btc_full')
def satoshis_to_btc_full(satoshis):
    return satoshis_to_btc(satoshis=satoshis)


@register.filter(name='coin_symbol_to_display_name')
def coin_symbol_to_display_name(coin_symbol):
    return COIN_SYMBOL_MAPPINGS[coin_symbol]['display_name']


@register.filter(name='coin_symbol_to_display_shortname')
def coin_symbol_to_display_shortname(coin_symbol):
    return COIN_SYMBOL_MAPPINGS[coin_symbol]['display_shortname']


@register.filter(name='coin_symbol_to_currency_name')
def coin_symbol_to_currency_name(coin_symbol):
    return COIN_SYMBOL_MAPPINGS[coin_symbol]['currency_abbrev']


@register.filter(name='coin_symbol_to_wss')
def coin_symbol_to_wss(coin_symbol):
    return _get_websocket_url(coin_symbol)
