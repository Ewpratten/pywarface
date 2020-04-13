class Region(object):
    """This class contains info for each region"""

    # Known regions
    RUSSIA: Region = Region("warface.ru", "Russia")
    WORLD: Region = Region("wf.my.com", "World")

    # Class data
    ip_addr: str
    name: str

    def __init___(self, master_server_addr, region_name):
        self.ip_addr = master_server_addr
        self.name = region_name

    def asList(self) -> list:
        """Get a list of all regions"""
        return [self.WORLD, self.RUSSIA]