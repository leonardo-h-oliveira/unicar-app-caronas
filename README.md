# UniCar

Protótipo de aplicativo de caronas universitárias desenvolvido como Trabalho de Conclusão de Curso do Bacharelado Interdisciplinar em Ciência e Tecnologia da UNIFAL-MG.

O projeto investigou como organizar a oferta e a solicitação de caronas dentro da comunidade universitária, com regras para cadastro, autenticação, pontos de encontro, vagas disponíveis e comunicação entre motorista e passageiro.

## Escopo do trabalho

O protótipo original foi desenvolvido para Android com MIT App Inventor, Firebase Authentication, Firebase Realtime Database e armazenamento local com TinyDB.

Este repositório preserva a documentação do projeto e uma representação em Python das principais entidades e regras de negócio. O objetivo é registrar a modelagem realizada no TCC, não distribuir um aplicativo para uso em produção.

## Conteúdo do repositório

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

- `docs/`: requisitos, fluxos, regras e decisões técnicas
- `core_python/`: demonstração das entidades, do repositório em memória e dos serviços do domínio

Para executar a demonstração em Python:

```bash
python -m core_python.demo
```

## Principais regras modeladas

- Cadastro e autenticação de usuários
- Oferta e solicitação de caronas
- Seleção de pontos de encontro
- Controle da quantidade de vagas
- Persistência de informações locais e remotas
- Comunicação entre motorista e passageiro após a confirmação

## Continuidade

Os requisitos e aprendizados do UniCar deram origem ao [Smart Carpool](https://github.com/leonardo-h-oliveira/smart-carpool), uma implementação web com banco relacional, API, testes automatizados e demonstração publicada.

## Autoria

Trabalho desenvolvido por Leonardo Henrique Oliveira e Bruna Helena Antonialli Gomes, sob orientação do Prof. Dr. Luiz Felipe Ramos Turci.
