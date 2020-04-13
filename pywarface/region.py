# There are technically two diffrent versions of Warface.
# One is Russia-only, the other is for the rest of the world.
# As far as I know, the games are mostly the same gameplay-wise,
# but they physically use diffrent sets of servers, and have
# seprate API endpoints (and even account databases)


@dataclass
class Region(object):
    """This class contains info for each region"""

    # Known regions
    RUSSIA: Region = Region("warface.ru", "Russia")
    WORLD: Region = Region("wf.my.com", "World")

    # Class data
    ip_addr: str
    name: str

    @staticmethod
    def asList() -> list:
        """Get a list of all regions"""
        return [Region.WORLD, Region.RUSSIA]
