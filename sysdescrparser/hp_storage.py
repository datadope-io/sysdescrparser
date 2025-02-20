# -*- coding: utf-8 -*-
"""sysdescrparser.hp_storage."""

import re
from hp import HP


class HPStorage(HP):
    """Clase para parsear el sysDescr en dispositivos HP Storage (P2000).

    Ejemplos de sysDescr:
      - "HP P2000G3 FC/iSCSI"
      - "HP StorageWorks P2000G3 FC/iSCSI"
    """

    def __init__(self, raw):
        """Constructor."""
        super(HPStorage, self).__init__(raw)
        self.os = 'HP Storage'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsea el sysDescr para extraer el modelo.

        Se espera que la cadena siga alguno de los siguientes patrones:
          - "HP P2000G3 FC/iSCSI"
          - "HP StorageWorks P2000G3 FC/iSCSI"
        """
        regex = r"^HP\s+(?P<model>(?:StorageWorks\s+)?P2000\w+)\s+FC/iSCSI"
        pat = re.compile(regex, re.IGNORECASE)
        res = pat.search(self.raw)
        if res:
            self.model = res.group("model")
            return self

        return False
