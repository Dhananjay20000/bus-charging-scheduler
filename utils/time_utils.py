from datetime import datetime, timedelta


def time_to_minutes(time_str):

    time_obj = datetime.strptime(
        time_str,
        "%H:%M"
    )

    return time_obj.hour * 60 + time_obj.minute


def minutes_to_time(minutes):

    base = datetime(2024, 1, 1)

    final_time = base + timedelta(
        minutes=minutes
    )

    return final_time.strftime("%H:%M")