from model.creature import Creature

# fake data, until we use a real database and SQL
_creatures = [
    Creature(name="yeti", description="Abominable Snowman", location="Himalayas"),
    Creature(
        name="bigfoot",
        description="AKA Sasquatch, the New World " "Cousin Eddie of the yeti",
        location="North America",
    ),
]


def get_all() -> list[Creature]:
    """Return all creatures"""
    return _creatures


def get_one(name: str) -> Creature | None:
    """Return one creature"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


# The following are non-functional for now,
# so they just act like they work, without modifying
# the actual fake _creatures list:
def create(creature: Creature) -> Creature:
    """Add a creature"""
    return creature


def modify(creature: Creature) -> Creature:
    """Partially modify a creature"""
    return creature


def replace(creature: Creature) -> Creature:
    """Completely replace a creature"""
    return creature


def delete(name: str):
    """Delete a creature; return None if it existed"""
    return None
