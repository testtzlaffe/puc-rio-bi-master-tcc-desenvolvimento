[< VOLTAR PARA README](/README.md)

### Exemplo do formato de um processo/despacho no XML:

```xml
<processo numero="920493416" data-deposito="19/08/2020">
    <despachos>
      <despacho codigo="IPAS421" nome="Republicação de pedido">
        <texto-complementar>Republicado o pedido, tendo em vista alteração da classe internacional reivindicada para fins de adequação da mesma à especificação apresentada.</texto-complementar>
      </despacho>
    </despachos>
    <titulares>
      <titular nome-razao-social="PABLO SILVA NEVES" pais="BR" uf="MG"/>
    </titulares>
    <marca apresentacao="Mista" natureza="Produtos e/ou Serviço">
      <nome>ESTUDIO CAR DETALHAMENTO</nome>
    </marca>
    <classes-vienna>
      <classe-vienna codigo="18.1.9" edicao="4"/>
    </classes-vienna>
    <lista-classe-nice>
      <classe-nice codigo="37">
        <especificacao>Lavagem de Veículos, Limpeza de Veículos e Polimento de Veículos. Lavador e Polidor&#xd;
de carro independente, serviço de Lavagem, lubrificação e polimento de veículos&#xd;
automotores. Detalhamento em veículos automotroes.; </especificacao>
        <status>Pendente (com especificação livre)</status>
      </classe-nice>
    </lista-classe-nice>
  </processo>

```
