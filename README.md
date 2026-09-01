# UniCar

A university carpooling application prototype developed as the final project for the Interdisciplinary Bachelor's Degree in Science and Technology at UNIFAL-MG.

The project explored how to organize ride offers and requests within a university community, including account registration, authentication, boarding points, seat availability and communication between drivers and passengers.

## Project scope

The original Android prototype was built with MIT App Inventor, Firebase Authentication, Firebase Realtime Database and TinyDB local storage.

This repository preserves the project documentation and a Python representation of its main entities and business rules. Its purpose is to document the work completed for the undergraduate project, not to distribute a production application.

## Repository contents

```text
unicar-app-caronas/
├── core_python/
│   ├── demo.py
│   ├── models.py
│   ├── repository.py
│   └── services.py
├── docs/
└── README.md
```

- `docs/`: requirements, workflows, business rules and technical decisions
- `core_python/`: a runnable representation of the domain entities, in-memory repository and services

Run the Python demonstration with:

```bash
python -m core_python.demo
```

## Main business rules

- User registration and authentication
- Publishing and requesting rides
- Boarding point selection
- Seat availability control
- Local and remote data persistence
- Driver and passenger communication after confirmation

## Continuation

The requirements and lessons from UniCar led to [Smart Carpool](https://github.com/leonardo-h-oliveira/smart-carpool), a web implementation with a relational database, API, automated tests and a published demonstration.

## Authors

Developed by Leonardo Henrique Oliveira and Bruna Helena Antonialli Gomes under the supervision of Professor Luiz Felipe Ramos Turci.
