# UniCar

A university carpooling application prototype developed as the final project for the Interdisciplinary Bachelor's Degree in Science and Technology at UNIFAL-MG.

The project explored how to organize ride offers and requests within a university community, including account registration, authentication, boarding points, seat availability and communication between drivers and passengers.

## Project scope

The original Android prototype was built with MIT App Inventor, Firebase Authentication, Firebase Realtime Database and TinyDB local storage.

This repository is a public record of the academic project. It summarizes the prototype described in the final report and also contains a small Python study of some domain rules. The Python files were added later for learning purposes: they are not the source code of the Android prototype and were not part of the submitted application.

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

- `docs/`: notes based on the academic report, including scope, workflows and limitations
- `core_python/`: a later, independent exercise that represents a subset of the domain in Python

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

## Related portfolio project

[Smart Carpool](https://github.com/leonardo-h-oliveira/smart-carpool) is a separate web portfolio project by Leonardo Henrique Oliveira. It addresses the same broad subject, but it is not a new version of UniCar and does not share its source code, interface or Git history.

## Academic reference

GOMES, Bruna Helena Antonialli; OLIVEIRA, Leonardo Henrique. **UniCar: um aplicativo de caronas compartilhadas para a Universidade Federal de Alfenas**. Trabalho de Conclusão de Curso, Bacharelado Interdisciplinar em Ciência e Tecnologia, Universidade Federal de Alfenas, Poços de Caldas, 2025. Advisor: Professor Luiz Felipe Ramos Turci.

[Read the public TCC copy](docs/UniCar_TCC_public.pdf)

This public copy preserves the complete submitted report, including the authentication explanation, interface screenshots, test account examples and MIT App Inventor programming blocks. Only the Firebase Web API key value shown twice in Figure 5 was obscured; no explanatory content was removed. The original PDF remains preserved by the authors.

## Authors

Developed by Leonardo Henrique Oliveira and Bruna Helena Antonialli Gomes under the supervision of Professor Luiz Felipe Ramos Turci.
