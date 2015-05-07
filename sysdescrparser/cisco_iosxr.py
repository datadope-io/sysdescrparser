# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_ios."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class CiscoIOSXR(SysDescr):

    """Class CiscoIOSXR.

    SNMP sysDescr for Cisco IOSXR.

    """

    def parse(self):
        """Parse."""
        vendor = 'cisco'
        os = 'iosxr'
        series = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'Cisco\s+IOS\s+XR\s+'
                 r'Software\s+\((.*)\),\s+Version\s+(.*\[.*\])')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)
            return self._store(vendor, os, series, version)

        return False