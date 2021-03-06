from ops.charm import EventBase, CharmEvents, EventSource


class UnitEvent(EventBase):
    """ Base Class for Unit related Governor Events. """

    def __init__(self, handle, unit_name):
        super().__init__(handle)

        self.unit_name = unit_name

    def snapshot(self):
        """ Store unit name to operator storage. """
        return {"unit_name": self.unit_name}

    def restore(self, snapshot):
        """ Restore unit name from operator storage. """
        self.unit_name = snapshot["unit_name"]


class UnitAddedEvent(UnitEvent):
    """ Unit Added Event. """


class UnitRemovedEvent(UnitEvent):
    """ Unit Removed Event. """


class UnitBlockedEvent(UnitEvent):
    """ Unit Blocked Event. """


class UnitErrorEvent(UnitEvent):
    """ Unit Error Event. """


class GovernorEvents(CharmEvents):
    """ Object Events class for all GovernorEvents. """

    unit_added = EventSource(UnitAddedEvent)
    unit_removed = EventSource(UnitRemovedEvent)
    unit_blocked = EventSource(UnitBlockedEvent)
    unit_error = EventSource(UnitErrorEvent)
