# TCC | BI Master | PUC-Rio

## Processo de BI para acompanhamento de registros de marcas no INPI

Christian Testtzlaffe Alpoim ([Linkedin](https://www.linkedin.com/in/christian-testtzlaffe-alpoim/))

**Orientador:** Anderson Nascimento
<br>
<br>


<hr>

### Objetivo

Este trabalho tem o objetivo de construir um processo de Business Intelligence (BI) com fluxo de coleta, transformação e carga/persistência de dados dos processos de registros de marcas originados pelo Instituto Nacional de Propriedade Industrial (INPI). Antes deste processo de extração, transformação e carga (ETL), será necessário o mapeamento dos dados, a modelagem e a criação do repositório destes registros (banco de dados relacional). Uma vez que o processo esteja configurado e sendo executado periodicamente, este banco de dados permitirá a construção de aplicações para acompanhamento e alerta sobre o avanço nos registros de marcas.

<hr>

### INPI

O Instituto Nacional da Propriedade Industrial (INPI) é uma autarquia federal brasileira, criada em 1970, vinculada ao Ministério do Desenvolvimento, Indústria e Comércio Exterior (MDIC). Localiza-se na cidade do Rio de Janeiro, Brasil. Antecedido pelo Departamento Nacional da Propriedade Industrial.

Conforme art. 2º da Lei nº 5.648/1970, "O INPI tem por finalidade principal executar, no âmbito nacional, as normas que regulam a propriedade industrial, tendo em vista a sua função social, econômica, jurídica e técnica, bem como pronunciar-se quanto à conveniência de assinatura, ratificação e denúncia de convenções, tratados, convênios e acordos sobre propriedade industrial". (Redação dada pela Lei nº 9.279, de 1996).

Entre suas funções, o INPI é responsável pelo registro e concessão de marcas, que é a base para este trabalho.

<hr>

### Origem dos dados
Os dados a serem coletados para o processo de BI são públicos e disponibilizados na Revista da Propriedade Industrial (http://revistas.inpi.gov.br/rpi/). O INPI divulga semanalmente, toda terça-feira, os dados de atualização sobre os processos de registros de marcas, tanto no formato pdf quanto em XML. Neste trabalho, foi avaliado que o arquivo XML contém as principais informações de despachos do INPI, e servirá como origem dos dados para o processo de ETL.

<hr>

### Extração, transformação e carga dos dados
O processo central do trabalho, o ETL, segue algumas etapas importantes para o alcance do objetivo de geração do banco de dados devidamente carregado. Abaixo, um diagrama sobre este fluxo:

Fonte dos dados (XML semanal de marcas da Revista de Propriedade Industrial) → Coleta dos dados → Transformações dos dados (conteúdos das tags do XML para formato tabular) → carga (inserção de registros no banco de dados).

<hr>

### Arquitetura da solução

Para cada etapa do projeto, foram definidas ferramentas que auxiliarão no processo:

- Modelagem dos dados: Power Architect
- ETL: Pentaho Data Integration (PDI)
- SGBD: PostgreSQL
- API: Node.js
- Interface: Página Web (HTML, CSS e JavaScript)

<hr>

### Fonte dos dados

O PDI também auxiliou na listagem de todas as tags e nós do arquivo XML (no exemplo, revista nº 2625). Por meio da etapa "Get data from XML" na ferramenta, na funcionalidade "Get XPath nodes", é possível visualizar todos os nós (tags) presentes no arquivo:

Além das tags, alguns nós do XML têm atributos, por exemplo: na tag "titular", há atributos como nome e país do titular da marca.

As tags mais importantes para este trabalho são:

Revista: cada semana, o INPI disponibiliza uma revista, e esta tag do XML indica o número e a data da divulgação.

Processo: primeira tag após o nó da revista. Há dezenas de milhares de processos por Revista/semana. Tem como atributos o número do processo, e em algumas situações, traz a data de depósito, a data de concessão e a data de vigência de uso da marca.

Marca: em alguns tipos de registros, esta tag aparece indicando o nome da marca, a natureza e a apresentação (nominativa, figurativa ou mista).

Despachos: junto com o processo, os depachos são as principais informações do arquivo. Nos despacho é que está a descrição do que aconteceu naquele processo naquela semana (com código de despacho), e em alguns casos traz observações (texto-complementar ou texto-sobrestamento).

Titulares: lista os nomes, estados e países dos titulares da marca.

Classes Vienna e Nice: são classificações de atividades que aquela marca está atrelada. 

Abaixo, um exemplo de processo no arquivo XML:

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
