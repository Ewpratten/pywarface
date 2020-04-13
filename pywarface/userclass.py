@dataclass
class Class:

    # Class types
    AIRCRAFT: Class = Class(1, "Aircraft")
    MEDIC: Class = Class(2, "Medic")
    SNIPER: Class = Class(3, "Sniper")
    ENGINEER: Class = Class(4, "Engineer")
    EDMS: Class = Class(4, "EDMS")

    # Class data
    class_type: int
    name: str
