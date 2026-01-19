# Regras de Negócio – UniCar

## Perfis e acesso
- O cadastro é único: o mesmo usuário pode atuar como motorista ou passageiro.
- No momento de uso, o usuário escolhe entre oferecer carona ou buscar carona.

## Oferta de carona
- Ao ofertar uma carona, o motorista informa:
  - origem, destino
  - data/horário
  - número de vagas disponíveis
  - (opcional) valor sugerido / observações
- A oferta só pode ser considerada ativa se houver pelo menos 1 vaga disponível.

## Gestão de vagas
- Cada vez que um passageiro entra na carona, o número de vagas diminui.
- Ao remover um passageiro, o número de vagas aumenta.
- Quando vagas = 0, a carona fica indisponível para novas entradas.

## Entrada e saída de passageiros
- Passageiros podem solicitar/entrar em uma oferta disponível.
- O sistema deve impedir entrada se não houver vagas.
- O motorista pode remover passageiros (ex.: cancelamento).
- O passageiro pode sair da carona (desistência).

## Cancelamento
- O motorista pode cancelar uma oferta.
- Ao cancelar, a oferta deixa de aparecer em buscas.
