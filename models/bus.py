class Bus:

    def __init__(
        self,
        bus_id,
        operator,
        direction,
        departure
    ):

        self.bus_id = bus_id
        self.operator = operator
        self.direction = direction
        self.departure = departure

        self.charging_plan = []
        self.total_wait_time = 0