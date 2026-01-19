# Modelo de Dados (Firebase) – UniCar

Abaixo está uma representação conceitual dos dados do sistema.
A estrutura exata pode variar conforme a implementação no Firebase.

## Entidade: Usuário
Campos sugeridos:
- userId (chave)
- nome
- email
- telefone (opcional)
- tipo (motorista/passageiro no momento do uso)

## Entidade: Carona (Oferta)
Campos sugeridos:
- caronaId (chave)
- motoristaId (referência ao usuário)
- origem
- destino
- dataHora
- vagasTotais
- vagasDisponiveis
- status (ativa/cancelada/finalizada)
- observacoes (opcional)

## Entidade: Participação (Passageiros em uma Carona)
Campos sugeridos:
- caronaId
- passageiros[] (lista de userId)
ou, alternativamente:
- participacoes/{caronaId}/{userId}: true
