# Each Warface region has it's own set of servers. This allows multiple people
# to have the same username as long as they are playing diffrent servers.
# This file contains the common interface for all servers in the world across
# both "normal" Warface, and Russian Warface.

import requests
from .region import Region
from .userclass import Class
from .user import User


@dataclass
class Server(object):
    """This class contains mappings from the my.com server codenames to their server numbers"""

    # Known servers
    RU_ALPHA: Server = Server(1, "Alpha", Region.RUSSIA)
    RU_BRAVO: Server = Server(2, "Bravo", Region.RUSSIA)
    RU_CHARLIE: Server = Server(3, "Charlie", Region.RUSSIA)
    RU_DELTA: Server = Server(4, "Delta", Region.RUSSIA)
    ALPHA: Server = Server(1, "Alpha", Region.WORLD)
    BRAVO: Server = Server(2, "Bravo", Region.WORLD)
    CHARLIE: Server = Server(3, "Charlie", Region.WORLD)
    DELTA: Server = Server(4, "Delta", Region.WORLD)

    # Server data
    server_id: int
    server_codename: str
    region: Region

    @staticmethod
    def asList() -> list:
        """Get a list of all known servers"""
        return[Server.RU_ALPHA, Server.RU_BRAVO, Server.RU_CHARLIE, Server.RU_DELTA, Server.ALPHA, Server.BRAVO, Server.CHARLIE, Server.DELTA]

    def getTop100(self, class_sort: Class = None) -> list:

        # Build request
        req = {
            "server": self.server_id,
            "class": ""
        }

        # Determine the class parameter
        if class_sort:
            req["class"] = str(class_sort.class_type)

        # Make request to server
        resp = requests.get(
            f"http://api.{self.region.ip_addr}/rating/top100", params=req).json()

        return resp

    def getUser(self, username: str) -> User:
        pass
