import requests
from .region import Region


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

    def getTop100(self) -> list:
        pass
