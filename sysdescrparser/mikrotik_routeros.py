# -*- coding: utf-8 -*-
"""sysdescrparser.mikrotik_routeros."""

import re
from sysdescr import SysDescr


class MikroTikRouterOS(SysDescr):
    """Clase para parsear el sysDescr en dispositivos MikroTik con RouterOS.

    Se contemplan distintos patrones:
      - Patrón antiguo: "RouterOS <version> (<algo>) on <modelo>"
      - Patrón simple: "RouterOS <modelo>" o "RouterOS <modelo> Version <version>"
    """

    def __init__(self, raw):
        """Constructor."""
        super(MikroTikRouterOS, self).__init__(raw)
        self.vendor = 'MikroTik'
        self.os = 'RouterOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsea el sysDescr utilizando varias expresiones regulares."""
        patterns = [
            # Patrón existente: busca "RouterOS <version> (<algo>) on <modelo>"
            r"RouterOS\s+([\d.]+)\s+\(([\w|-]+)\)\s+on\s+([\w\-\+]+)",
            # Nuevo patrón: busca "RouterOS <modelo>" opcionalmente seguido de "Version <version>"
            r"RouterOS\s+(?P<model>\S+)(?:\s+Version\s+(?P<version>[\d.]+))?"
        ]
        for regex in patterns:
            pat = re.compile(regex, re.IGNORECASE)
            res = pat.search(self.raw)
            if res:
                # Si se usa el patrón con grupos con nombre, se extraen dichos grupos.
                if "model" in res.groupdict():
                    self.model = res.group("model")
                    if res.group("version") is not None:
                        self.version = res.group("version")
                else:
                    # Patrón antiguo sin grupos con nombre.
                    self.version = res.group(1)
                    self.model = res.group(3)
                return self

        return False
