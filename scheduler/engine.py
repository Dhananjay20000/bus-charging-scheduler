from models.bus import Bus
from models.station import Station
from utils.time_utils import (
    time_to_minutes,
    minutes_to_time
)


TRAVEL_SPEED = 60
CHARGING_TIME = 25


def run_scheduler(scenario):

    stations = []

    for s in scenario["route"]["stations"]:

        station = Station(
            s["name"],
            s["distance"]
        )

        stations.append(station)

    results = []

    for bus_data in scenario["buses"]:

        bus = Bus(
            bus_data["id"],
            bus_data["operator"],
            bus_data["direction"],
            bus_data["departure"]
        )

        departure_minutes = time_to_minutes(
            bus.departure
        )

        current_time = departure_minutes

        if bus.direction == "Bangalore-Kochi":

           charging_stations = [
               stations[1],
               stations[3]
        ]

        else:

            charging_stations = [
                stations[2],
                stations[0]
        ]

        previous_distance = 0

        for station in charging_stations:

            distance = (
                station.distance
                - previous_distance
            )

            travel_time = distance

            arrival_time = (
                current_time
                + travel_time
            )

            charging_start = max(
                arrival_time,
                station.available_at
            )

            wait_time = (
                charging_start
                - arrival_time
            )

            charging_end = (
                charging_start
                + CHARGING_TIME
            )

            station.available_at = (
                charging_end
            )

            station.queue.append({
                "bus_id": bus.bus_id,
                "start": minutes_to_time(
                    charging_start
                ),
                "end": minutes_to_time(
                    charging_end
                )
            })

            bus.charging_plan.append({
                "station": station.name,
                "arrival": minutes_to_time(
                    arrival_time
                ),
                "charging_start": minutes_to_time(
                    charging_start
                ),
                "charging_end": minutes_to_time(
                    charging_end
                ),
                "wait_time": wait_time
            })

            bus.total_wait_time += (
                wait_time
            )

            current_time = charging_end
            previous_distance = station.distance

        results.append(bus)

    return results, stations