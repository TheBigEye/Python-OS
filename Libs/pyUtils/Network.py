"""
    Module Name:
        Network

    Module Description:
        This module provides functions to interact with the network.
"""

import psutil
import urllib.request

class Network:
    """
    This class implements the network functions.
    """

    def getStatus() -> bool:
        """ Checks if the network is connected. """

        try:
            request = urllib.request.urlopen("https://www.google.com/")
            if request.getcode() == 200:
                return True
            else:
                return False
        except:
            return False

    def getIP() -> str:
        """ Returns the IP address of the computer. """

        return psutil.net_if_addrs()['Ethernet'][0].address

    def getHTTPStatus(URL: str) -> bool:
        """ Returns the HTTP status of a URL. """

        try:
            request = urllib.request.urlopen(URL)
            if request.getcode() == 200:
                return True
            else:
                return False
        except:
            return False
