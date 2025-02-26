# -*- coding: utf-8 -*-
"""sysdescrparser.cisco_fxos."""

import re
from sysdescr import SysDescr


class CiscoFXOS(SysDescr):
    """Clase para extraer información de sysDescr en dispositivos Cisco FXOS.

    Se espera que el sysDescr tenga un formato similar a:
    "Cisco FirePOWER FPR-2130 Security Appliance, System Version 2.3(1.131)"
    """

    def __init__(self, raw):
        """Constructor."""
        super(CiscoFXOS, self).__init__(raw)
        self.vendor = 'CISCO'
        self.model = self.UNKNOWN
        self.os = 'FXOS'
        self.version = self.UNKNOWN

    def parse(self):
        """Parseo del valor de sysDescr para extraer modelo y versión."""
        regex = (r"Cisco\s+FirePOWER\s+(\S+)\s+Security Appliance,\s+System Version\s+(\S+)")
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self
        return False
