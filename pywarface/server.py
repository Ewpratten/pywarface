import requests


class Server(object):
    """This class contains mappings from the my.com server codenames to their server numbers"""

    # Known servers
    ALPHA: Server = Server(1, "Alpha")
    BRAVO: Server = Server(2, "Bravo")
    CHARLIE: Server = Server(3, "Charlie")
    DELTA: Server = Server(4, "Delta")

    # Server data
    server_id: int
    server_codename: str

    def __init__(self, server_id, server_codename):
        self.server_id = server_id
        self.server_codename = server_codename

    @staticmethod
    def asList() -> list:
        """Get a list of all known servers"""
        return[Server.ALPHA, Server.BRAVO, Server.CHARLIE, Server.DELTA]
