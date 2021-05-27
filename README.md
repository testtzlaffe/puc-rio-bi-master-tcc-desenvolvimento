# TCC | BI Master | PUC-Rio

## Construção de processo automatizado de extração, transformação e carga de dados para acompanhamento de registros de marcas no INPI

Christian Testtzlaffe Alpoim ([Linkedin](https://www.linkedin.com/in/christian-testtzlaffe-alpoim/))

**Orientador:** Prof. Anderson Nascimento

### [Artigo](/anexos/Artigo.pdf)

<hr>

### Objetivo

Este trabalho tem o objetivo de construir um fluxo automatizado de coleta, transformação e carga/persistência de dados dos processos de registros de marcas originados pelo [Instituto Nacional de Propriedade Industrial (INPI)](https://www.gov.br/inpi/pt-br). Antes deste processo de extração, transformação e carga (ETL), é necessário o mapeamento dos dados, a modelagem e a criação do repositório destes registros (banco de dados relacional). Uma vez que o processo esteja configurado e sendo executado periodicamente, este banco de dados permitirá a construção de aplicações para acompanhamento e alerta sobre o avanço nos registros de marcas.

<hr>

### Etapas, Arquitetura e Tecnologias

O diagrama abaixo resume as etapas do processo, bem como a arquitetura da solução e a indicação das tecnologias:

<img src="/imagens/Arquitetura.png" alt="imagem da arquitetura da solução" />

<details>
  <summary>Resumo das etapas e justificativas para definição das tecnologias</summary>
  <br>
  <ul>
    <li><strong>Fonte dos dados:</strong> arquivos XML do site do INPI.</li>
    <li><strong>Mapeamento dos dados:</strong> estudo das principais tags e atributos do arquivo, bem como suas relações.</li>
    <li><strong>Modelagem dos dados:</strong> desenho do modelo de tabelas e seus relacionamentos, com uso do <a href="http://www.bestofbi.com/page/architect">SQL Power Architect</a>. Por meio do Power Architect, é relativamente simples modelar as entidades e suas relações, sendo uma ferramenta bastante utilizada por profissionais especialistas em banco de dados. Além disso, tem integração com diversos sistemas gerenciadores de BD, inclusive o PostgreSQL, utilizado neste trabalho.</li>
    <li><strong>BD (banco de dados):</strong> criação e atualização das tabelas por meio do <a href="https://www.postgresql.org/">PostgreSQL</a>. O PostgreSQL foi definido como o sistema gerenciador de banco de dados do projeto, por ser de código aberto, com mais de 30 anos de desenvolvimento. Tem uma boa reputação e é amplamente utilizado pelo mercado, com arquitetura comprovada, confiável e com recursos robustos. Além disso, pode ser executado em todos os principais sistemas operacionais.</li>
    <li><strong>ETL:</strong> extrações, transformações e cargas com <a href="https://help.pentaho.com/Documentation/7.1/0D0/Pentaho_Data_Integration">Pentaho Data Integration (PDI)</a>. O PDI tem inúmeras funcionalidade de ETL que facilitam a coleta, a limpeza, as transformações e a persistência dos dados. É intuitivo na utilização, e tem integração com vários formatos de entrada e com diversos sistemas gerenciadores de banco de dados, inclusive PostgreSQL. Permite agendar processos para serem executados automaticamente, bem como gerar alertas de finalização ou falhas. O Pentaho Data Integration é amplamente utilizado por diversos tipos de clientes, como instituições financeiras, indústrias, órgãos dos governos federal, estaduais e prefeituras, entidades de saúde, universidades, entre outros. Para a primeira tarefa do ETL, o download dos arquivos .zip, foi utilizado um script em <a href="https://www.python.org/">Python</a>. Python é uma linguagem de programação de alto nível, lançada em 1991. É de propósito geral, sendo muito utilizada para Ciência de Dados e scripts.</li>
</details>

<hr>

### Fonte dos dados

Os dados a serem coletados para o processo são públicos e disponibilizados na <a href="http://revistas.inpi.gov.br/rpi" target="_blank">Revista da Propriedade Industrial (RPI)</a>. O INPI divulga semanalmente, toda terça-feira, as atualizações sobre os registros de marcas, tanto no formato PDF quanto em XML (compactado/zipado). Para este trabalho, foi avaliado que o arquivo XML contém as principais informações de despachos do INPI, e servirá como base para o processo de ETL. Vale destacar que este arquivo, quando descompactado, tem entre 20 e 30MB, com dezenas de milhares de despachos.

<hr>

### Mapeamento dos dados

Inicialmente, foi necessário o estudo dos dados de registro de marcas no INPI. Foram avaliadas minuciosamente algumas Revistas de Propriedade Industrial, tanto na versão XML quanto em PDF. No XML, há diversos nós (tags) e atributos, alguns sempre presentes, e outros aparecem a depender do tipo de despacho.

Como exemplo, há a tag "titular". Nela estão presentes os atributos nome, país e UF do titular da marca. A UF é preenchida apenas quando o país é BR (Brasil).

[Exemplo de um processo/despacho no XML](/anexos/exemplo-processo-xml.md)

[Tabela de tags e atributos do XML](/anexos/tabela-tags-atributos.md)

<hr>

### Modelagem das tabelas e dos campos

Partindo do mapeamento dos dados da etapa anterior, foi possível identificar quais as entidades mais importantes para o modelo do banco de dados. Basicamente, o escopo envolve: revista, processo, marca, titular, procurador, despacho, classe-nice e classe-vienna.

[Modelo Relacional](/anexos/modelo.md)

<hr>

### Criação do banco de dados

O trabalho utiliza como Sistema Gerenciador de Banco de Dados (SGBD) o PostgreSQL. A criação das tabelas foi originada diretamente do SQL Power Architect, tomando como base o modelo desenhado.

<hr>

### Extração, transformação e carga dos dados

O processo central do trabalho, o ETL, segue algumas etapas importantes para o alcance do objetivo de geração do banco de dados devidamente carregado. 

**Extração:** etapa de coleta / extração dos recursos de dados. Neste trabalho, a extração é responsável pelo download, descompactação dos arquivos zipados, leitura do XML e loop sobre as tags importantes para obtenção dos dados.

**Transformação:** tratamento dos dados brutos, formatações e adequações do conteúdo dos campos. Aqui foram realizadas operações sobre textos (strings), formatações de datas, seleção de valores, mapper, entre outros.

**Carga:** etapa final do ETL, persiste os dados no repositório de destino. No caso deste projeto, o conjunto de dados extraídos e transformados para cada entidade são carregados para o PostgreSQL, de forma que semanalmente os registros de processos de marcas estejam sempre atualizados.

Para que seja executado sem necessidade de ação manual, foi configurado no "Agendador de Tarefas" do Windows, para toda terça-feira, duas execuções: 1) download do arquivo .zip do site do INPI; 2) job configurado no Pentaho Data Integration (executado em background).

Para o download, foi desenvolvido um [script em Python](/script-download-revistas), que verifica qual o número atual da revista e baixa o arquivo para determinada pasta.

No Pentaho Data Integration (PDI), foi implementado um fluxo (job) com etapas de extração dos dados, transformações / formatações / preparação dos campos, e carga para cada tabela no PostgreSQL, conforme [telas do PDI](/anexos/transformacoes.md).

A primeira tarefa do job é "unzip", que extrai o XML do arquivo compactado para o diretório definido. Segue com o job organizando uma sequência de chamadas às "transformations". Cada uma realiza a leitura dos dados importantes do XML, efetua as transformações de alguns campos e preenche as respectivas tabelas no banco de dados. Por fim, move os arquivos compactados para uma pasta auxiliar de histórico e deleta o XML utilizado, limpando a pasta para a carga da semana seguinte.

<hr>

### Resultados e conclusões

A sequência de etapas acima atingiu o objetivo do trabalho de construir um fluxo automatizado, que semanalmente realiza o ETL e que culmina na persistência dos dados no PostgreSQL. 

As tecnologias adotadas foram capazes de garantir esta carga. O SQL Power Architect se mostrou intuitivo e efetivo na modelagem das entidades e na criação das tabelas. O Python atendeu perfeitamente a etapa de download com um código enxuto. O Pentaho Data Integration foi versátil, permitindo diversos tipos de transformações, e relativamente rápido na leitura de arquivos XML de mais de 20 MB, e na carga direta no PostgreSQL. Neste fluxo semanal, uma Revista de Propriedade Industrial é lida e carregada no banco de dados entre 1 e 2 minutos. E o PostgreSQL, conforme esperado, se mostrou robusto para cadastro de milhões de registros e com boa latência nas consultas.

No trabalho, foram carregadas as últimas 53 Revistas, equivalente a um ano de atualizações do INPI. Entre os números do trabalho, foram persistidos mais de 1 milhão de despachos, referentes a mais de 700 mil processos de registro de marca. O banco de dados final contém mais de 1 GB.

Este sucesso no resultado permite que o projeto evolua por exemplo para soluções web ou mobile a fim de disponibilizar serviços de acompanhamento de registros de marca no INPI e de alertas sobre atualizações de despachos, com base nos dados gravados.


