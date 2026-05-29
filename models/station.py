class Station:

    def __init__(
        self,
        name,
        distance
    ):

        self.name = name
        self.distance = distance

        self.available_at = 0
        self.queue = []