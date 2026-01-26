
# Technical Decisions

This document describes the main technical decisions made during the development of the UniCar prototype and the rationale behind each choice. The goal was to balance simplicity, clarity, and functional completeness within an academic context.

---

## 1. MIT App Inventor as Development Platform

### Decision
Use MIT App Inventor as the primary development environment.

### Rationale
- Enables rapid prototyping using block-based programming.
- Reduces entry barriers for mobile application development.
- Allows focus on business logic, data flow, and system modeling rather than UI boilerplate.
- Well-suited for academic projects and concept validation.

### Trade-offs
- Limited flexibility compared to native frameworks.
- Visual complexity for large projects.
- Mitigated through modular procedures and clear documentation.

---

## 2. Firebase Realtime Database for Cloud Persistence

### Decision
Use Firebase Realtime Database as the centralized data store.

### Rationale
- Provides real-time synchronization across users.
- Simplifies backend infrastructure requirements.
- Supports hierarchical data structures aligned with the application logic.
- Seamless integration with MIT App Inventor components.

### Trade-offs
- Limited relational modeling.
- Requires careful structuring of keys and consistency rules.
- Addressed through clear data modeling and documented constraints.

---

## 3. TinyDB for Local State Management

### Decision
Use TinyDB for local, temporary data persistence.

### Rationale
- Enables state preservation between screens.
- Reduces repeated cloud queries.
- Improves navigation continuity and perceived performance.
- Supports offline-tolerant behavior during user interaction.

### Trade-offs
- Data is device-local and session-oriented.
- Not suitable for long-term persistence.
- Used strictly for transient context, not authoritative data.

---

## 4. Hybrid Persistence Strategy (Firebase + TinyDB)

### Decision
Adopt a hybrid persistence model combining cloud and local storage.

### Rationale
- Firebase maintains global shared state.
- TinyDB maintains local navigation context.
- This separation simplifies logic and improves responsiveness.
- Prevents unnecessary coupling between screens and cloud operations.

---

## 5. Seat Availability Control Logic

### Decision
Implement explicit seat availability control at the offer level.

### Rationale
- Ensures that carpool capacity is never exceeded.
- Reflects real-world constraints of shared rides.
- Simplifies offer validation and filtering.

### Implementation Detail
- Seat availability is decremented only after explicit passenger confirmation.
- Updated values are immediately written back to Firebase.
- Offers with zero seats are hidden or marked as unavailable.

---

## 6. Daily Offer Reset Mechanism

### Decision
Implement a daily reset mechanism using `dia_ultima_oferta`.

### Rationale
- Prevents accumulation of outdated offers.
- Keeps available carpools relevant to the current day.
- Simplifies lifecycle management in an academic prototype.

### Trade-offs
- Uses a simplified day-based control instead of timestamps.
- Acceptable within the prototype scope.
- Can be replaced by full date-time logic in future versions.

---

## 7. WhatsApp Integration for Communication

### Decision
Use WhatsApp as the communication channel between passengers and drivers.

### Rationale
- Widely adopted messaging platform.
- Eliminates the need to implement in-app messaging.
- Reduces system complexity while maintaining usability.

### Implementation Detail
- Messages are generated programmatically with contextual information.
- WhatsApp is launched via Android intents with pre-filled text.
- Final message sending remains user-controlled.

---

## 8. Confirmation-Based User Actions

### Decision
Require explicit user confirmation for critical actions.

### Rationale
- Prevents accidental operations.
- Improves user awareness and control.
- Ensures data consistency in cloud updates.

### Examples
- Confirming carpool selection
- Reducing seat availability
- Initiating external communication

---

## 9. Academic Scope and Design Constraints

### Decision
Limit system scope to a functional academic prototype.

### Rationale
- Focus on validating logic and architecture.
- Avoid premature optimization.
- Prioritize clarity and learning outcomes.

### Result
- A robust conceptual model.
- Clear pathways for future expansion.
- Documentation suitable for technical evaluation and portfolio presentation.

---

## Summary

The technical decisions in UniCar prioritize clarity, modularity, and consistency.
All choices were made considering the academic context while maintaining alignment
with real-world software engineering principles.
