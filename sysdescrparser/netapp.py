# -*- coding: utf-8 -*-
"""sysdescrparser.netapp."""

import re
from sysdescr import SysDescr


class NetApp(SysDescr):
    """Clase para parsear el sysDescr de dispositivos NetApp Data ONTAP.

    Ejemplo de sysDescr:
      "NetApp Release 8.2.5P1 7-Mode: Thu Dec 21 21:09:11 PST 2017"
    """

    def __init__(self, raw):
        """Constructor."""
        super(NetApp, self).__init__(raw)
        self.vendor = 'NETAPP'
        self.os = 'Data ONTAP'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Extrae la versión y, opcionalmente, el modelo desde el sysDescr."""
        # La expresión regular contempla que pueda aparecer o no un modelo
        # antes de la palabra "Release".
        regex = r"NetApp(?:\s+(?P<model>\S+))?\s+Release\s+(?P<version>[\d\.A-Za-z]+)"
        pat = re.compile(regex, re.IGNORECASE)
        res = pat.search(self.raw)
        if res:
            if res.group("model"):
                self.model = res.group("model")
            self.version = res.group("version")
            return self
        return False
