class EventResponse:
    def __init__(self, handled: bool, should_close: bool, values):
        self.should_close = should_close
        self.values = values
        self.handled = handled
