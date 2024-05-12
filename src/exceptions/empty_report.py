class EmptyReportsException(Exception):
    def __init__(self, message: str = "Empty Report Exception!"):
        self.message = message
        