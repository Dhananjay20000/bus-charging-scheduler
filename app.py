import streamlit as st
import pandas as pd

from utils.scenario_loader import (
    load_scenario
)

from scheduler.engine import (
    run_scheduler
)

from scheduler.scoring import (
    calculate_score
)
st.set_page_config(
    page_title="Bus Charging Scheduler",
    layout="wide"
)

st.title("🚌 Bus Charging Scheduler")

scenarios = [
    "scenario1.json",
    "scenario2.json",
    "scenario3.json",
    "scenario4.json",
    "scenario5.json"
]

selected_scenario = st.selectbox(
    "Select Scenario",
    scenarios
)

scenario_data = load_scenario(
    f"data/{selected_scenario}"
)

results, stations = run_scheduler(
    scenario_data
)

total_buses = len(results)

total_wait = sum(
    bus.total_wait_time
    for bus in results
)

average_wait = (
    total_wait / total_buses
    if total_buses > 0
    else 0
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Buses",
    total_buses
)

col2.metric(
    "Total Wait Time",
    f"{total_wait} mins"
)

col3.metric(
    "Average Wait",
    f"{average_wait:.2f} mins"
)

scenario_score = calculate_score(
    total_wait,
    scenario_data["weights"]
)

st.metric(
    "Scenario Score",
    round(scenario_score, 2)
)

st.subheader("Bus Schedules")

table_data = []

for bus in results:

    for stop in bus.charging_plan:

        table_data.append({
            "Bus": bus.bus_id,
            "Operator": bus.operator,
            "Station": stop["station"],
            "Arrival": stop["arrival"],
            "Charging Start": stop["charging_start"],
            "Charging End": stop["charging_end"],
            "Wait Time": stop["wait_time"]
        })

df = pd.DataFrame(table_data)

st.dataframe(
    df,
    use_container_width=True
)

st.subheader("Operator Summary")

operator_data = []

operators = set(
    bus.operator
    for bus in results
)

for operator in operators:

    operator_buses = [
        bus for bus in results
        if bus.operator == operator
    ]

    operator_wait = sum(
        bus.total_wait_time
        for bus in operator_buses
    )

    operator_data.append({

        "Operator": operator,

        "Bus Count":
            len(operator_buses),

        "Total Wait":
            operator_wait
    })

operator_df = pd.DataFrame(
    operator_data
)

st.dataframe(
    operator_df,
    use_container_width=True
)

st.subheader("Station Queues")

for station in stations:

    st.markdown(
        f"### Station {station.name}"
    )

    queue_df = pd.DataFrame(
        station.queue
    )

    st.dataframe(
        queue_df,
        use_container_width=True
    )