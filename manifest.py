# This file is part of carrier_send_shipments_envialia module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['CarrierManifest']


class CarrierManifest:
    __metaclass__ = PoolMeta
    __name__ = 'carrier.manifest'

    @classmethod
    def __setup__(cls):
        super(CarrierManifest, cls).__setup__()
        cls._error_messages.update({
                'not_envialia_manifest': 'Envialia Manifest service is not available.',
                })

    def get_manifest_envialia(self, api, from_date, to_date):
        self.raise_user_error('not_envialia_manifest')
