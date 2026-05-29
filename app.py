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

st.markdown(
    """
    <style>

    .main {
        background-color: #0E1117;
    }

    h1, h2, h3 {
        color: #FAFAFA;
    }

    </style>
    """,
    unsafe_allow_html=True
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

with col1:
    st.success(
        f"Total Buses: {total_buses}"
    )

with col2:
    st.info(
        f"Total Wait Time: {total_wait} mins"
    )

with col3:
    st.warning(
        f"Average Wait: {average_wait:.2f} mins"
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

st.subheader("Wait Time Analysis")

chart_data = operator_df.set_index(
    "Operator"
)

st.bar_chart(
    chart_data["Total Wait"]
)

st.subheader("Station Queues")

timeline_data = []

for station in stations:

    for entry in station.queue:

        timeline_data.append({

            "Station":
                station.name,

            "Bus":
                entry["Bus ID"],

            "Start":
                entry["Charging Start"],

            "End":
                entry["Charging End"]
        })

timeline_df = pd.DataFrame(
    timeline_data
)

st.subheader(
    "Charging Timeline"
)

st.dataframe(
    timeline_df,
    use_container_width=True
)

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