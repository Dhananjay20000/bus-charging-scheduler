# 🏗️ Architecture Overview

## System Design

The Bus Charging Scheduler is designed using a modular and configuration-driven architecture.

The system separates:

* Data Loading
* Scheduling Logic
* Scoring Logic
* Utility Functions
* User Interface

This separation improves:

* Maintainability
* Scalability
* Testability
* Extensibility

The application is entirely driven by scenario JSON files, allowing new scenarios and configurations to be added without modifying application code.

---

# 🎯 Scheduler Framework / Approach

## Approach Chosen

The scheduler uses a queue-based charging allocation strategy.

Each charging station maintains its own charging queue and charger availability timeline.

When a bus reaches a charging station:

1. The arrival time is calculated.
2. The station checks charger availability.
3. If a charger is available, charging begins immediately.
4. Otherwise, the bus enters the queue.
5. Waiting time is calculated.
6. The charging slot is allocated.

---

## Why This Approach?

This problem is fundamentally a resource allocation and scheduling problem.

A queue-based scheduler was chosen because it is:

* Deterministic
* Easy to explain
* Easy to debug
* Efficient for the assignment scope
* Extensible for future optimization algorithms

The design also allows advanced schedulers to replace the current implementation without affecting the UI or data model.

---

# 📂 Module Responsibilities

## 1. app.py

Responsible for:

* Streamlit UI
* Scenario Selection
* Metrics Display
* Table Rendering
* Analytics Visualization

---

## 2. data/

Contains all scenario configurations.

Examples:

* scenario1.json
* scenario2.json
* scenario3.json
* scenario4.json
* scenario5.json

Each scenario defines:

* Route
* Stations
* Buses
* Weights

The application dynamically loads scenarios at runtime.

---

## 3. models/

Contains domain models.

### bus.py

Represents:

* Bus ID
* Operator
* Direction
* Departure Time

### station.py

Represents:

* Station Name
* Distance
* Charging Queue

### route.py

Route abstraction layer.

### schedule.py

Schedule abstraction layer.

---

## 4. scheduler/

Contains scheduling logic.

### engine.py

Responsible for:

* Travel simulation
* Charger allocation
* Queue management
* Wait-time calculation

### scoring.py

Responsible for:

* Scenario evaluation
* Score calculation

### rules.py

Responsible for:

* Scheduling constraints
* Future rule extensions

---

## 5. utils/

Reusable helper functions.

### scenario_loader.py

Loads scenario JSON files.

### time_utils.py

Handles:

* Time conversion
* Formatting
* Calculations

---

# 🧱 Data Structure Design

## Bus Structure

```python
{
    "id": "bus-BK-01",
    "operator": "KPN",
    "direction": "Bangalore-Kochi",
    "departure": "19:00"
}
```

Stores all information related to a bus.

---

## Station Structure

```python
{
    "name": "A",
    "distance": 100
}
```

Represents a charging station.

Queue information is maintained internally by the scheduler.

---

## Scenario Structure

```python
{
    "name": "Scenario 1",
    "weights": {},
    "route": {},
    "buses": []
}
```

Acts as the top-level configuration object.

All scenarios follow the same structure.

---

# ⚙️ Scheduling Workflow

1. Load scenario from JSON
2. Create station objects
3. Create bus objects
4. Simulate travel
5. Calculate station arrivals
6. Allocate charging slots
7. Calculate waiting time
8. Update station queues
9. Generate schedules
10. Display results in Streamlit

---

# 📈 Scalability Considerations

The architecture supports future enhancements such as:

* Multiple chargers per station
* Real-time traffic data
* Dynamic charging durations
* Priority charging
* Battery health monitoring
* AI-based optimization
* Live charger availability

The modular architecture allows these features to be added without affecting unrelated components.

---

# 🔄 Future Changes Anticipated

The data model was intentionally designed to support future requirements through configuration rather than code changes.

## Multiple Chargers Per Station

Future JSON:

```json
{
  "name": "A",
  "distance": 100,
  "chargers": 4
}
```

No structural redesign required.

---

## Battery Percentage Tracking

Future JSON:

```json
{
  "id": "bus-BK-01",
  "battery": 35
}
```

Can be added without affecting existing scenarios.

---

## Priority Charging

Future JSON:

```json
{
  "id": "bus-BK-01",
  "priority": true
}
```

Allows implementation of priority-based scheduling.

---

## Dynamic Charging Duration

Future JSON:

```json
{
  "id": "bus-BK-01",
  "charge_time": 40
}
```

Allows charger usage to vary per bus.

---

## Traffic Conditions

Future JSON:

```json
{
  "traffic_multiplier": 1.2
}
```

Can influence travel time calculations.

---

# 🎯 Design Decisions

## Why JSON-Based Scenarios?

JSON was chosen because it provides:

* Configuration-driven architecture
* Easy scenario creation
* Simple maintenance
* Extensibility without code changes

---

## Why Modular Scheduler Design?

Separating scheduler logic from the UI improves:

* Maintainability
* Scalability
* Testing
* Readability

---

## Why Streamlit?

Streamlit enables:

* Rapid development
* Clean dashboards
* Minimal frontend complexity
* Easy deployment

---

# ⚖️ How to Change a Weight

Weights are defined inside scenario files.

Example:

```json
"weights": {
  "individual": 2,
  "operator": 3,
  "overall": 4
}
```

To modify scoring behavior:

1. Open the desired scenario JSON file.
2. Update the weight values.
3. Save the file.
4. Reload the application.

No code changes are required.

---

# 🛠️ How to Add a New Rule

Scheduling rules are maintained in:

```text
scheduler/rules.py
```

Example:

```python
def low_battery_priority(bus):
    return bus.battery < 20
```

Integration example:

```python
if low_battery_priority(bus):
    schedule_priority_bus(bus)
else:
    schedule_normal_bus(bus)
```

This allows new scheduling constraints to be introduced without affecting unrelated modules.

Example future rules:

* Low battery priority
* Operator priority
* Peak-hour restrictions
* Maintenance windows
* Emergency charging

---

# 📌 Assumptions Made

The following assumptions were used during implementation:

1. Each station contains one charger.
2. Charging duration is fixed at 25 minutes.
3. Travel speed is approximated as 1 km = 1 minute.
4. Charging stations are always operational.
5. All buses follow predefined routes.
6. Queue processing follows first-come-first-served scheduling.
7. Departure times are valid.
8. Charging starts immediately when a charger becomes available.
9. No battery degradation effects are considered.
10. Scenario configuration is fully driven by JSON files.

---

# 🔮 Future Enhancements

* Multiple chargers per station
* AI-based optimization
* Genetic algorithm scheduling
* Reinforcement learning scheduler
* Dynamic route balancing
* Real-time traffic integration
* Battery percentage simulation
* Live charger monitoring
* Interactive analytics dashboards
* Graph-based route optimization

```
```
