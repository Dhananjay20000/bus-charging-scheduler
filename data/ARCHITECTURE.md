# 🏗️ Architecture Overview

## System Design

The project is designed using a modular architecture to improve scalability, maintainability, and extensibility.

The system separates:

* data loading,
* scheduling logic,
* scoring logic,
* utility functions,
* and UI rendering.

This separation allows new features and scheduling strategies to be added easily without affecting existing components.

---

# 📂 Module Responsibilities

## 1. app.py

Responsible for:

* Streamlit UI
* Scenario selection
* Rendering tables and metrics
* Displaying scheduler results

---

## 2. data/

Contains all scenario configurations in JSON format.

Each scenario defines:

* buses,
* routes,
* stations,
* weights,
* and scheduling parameters.

The application is fully data-driven and avoids hardcoded scenarios.

---

## 3. models/

Contains core domain models.

### bus.py

Represents bus information and charging plans.

### station.py

Represents charging stations and queue management.

### route.py

Can be extended for route abstraction.

### schedule.py

Can be extended for schedule encapsulation.

---

## 4. scheduler/

Contains the core scheduling engine.

### engine.py

Main scheduler execution logic.

Responsibilities:

* travel simulation,
* charger allocation,
* queue handling,
* wait-time calculation.

### scoring.py

Scenario scoring and evaluation logic.

### rules.py

Reserved for custom scheduling constraints and rule extensions.

---

## 5. utils/

Contains reusable helper utilities.

### scenario_loader.py

Loads JSON scenarios dynamically.

### time_utils.py

Handles time conversion and formatting utilities.

---

# ⚙️ Scheduling Workflow

1. Load scenario from JSON
2. Create station objects
3. Create bus objects
4. Simulate travel between stations
5. Allocate charging slots
6. Calculate wait times
7. Update station queues
8. Generate final schedules
9. Render results in Streamlit UI

---

# 📈 Scalability Considerations

The architecture is designed to support future enhancements such as:

* multiple chargers per station,
* dynamic scheduling algorithms,
* live traffic integration,
* battery health tracking,
* real-time updates,
* AI-based optimization.

---

# 🎯 Design Decisions

## Why JSON-based scenarios?

Using JSON allows:

* dynamic test case creation,
* easy extensibility,
* configuration-driven architecture.

---

## Why modular scheduler design?

Separating scheduler logic from UI improves:

* maintainability,
* testing,
* scalability,
* readability.

---

## Why Streamlit?

Streamlit enables:

* rapid dashboard development,
* quick prototyping,
* clean visualization with minimal frontend overhead.

---

# 🔮 Future Enhancements

* Genetic algorithm optimization
* Reinforcement learning scheduler
* Multi-route balancing
* Real-time charger monitoring
* Graph-based route optimization
* Interactive analytics dashboard
