# Arquitetura do Sistema

O UniCar foi desenvolvido utilizando o MIT App Inventor como plataforma
de desenvolvimento e o Firebase como backend em nuvem, responsável pelo
armazenamento e autenticação de dados.

## Visão Arquitetural

O sistema segue uma arquitetura em três camadas:

### Camada de Apresentação
- Desenvolvida no MIT App Inventor
- Responsável pela interface e interação com o usuário

### Camada de Lógica de Negócio
- Implementada por meio de blocos de programação
- Controle de autenticação, validações e regras de carona

### Camada de Dados
- Firebase Authentication para login e registro
- Firebase Realtime Database para armazenamento de usuários e ofertas
- TinyDB para persistência local de dados temporários
