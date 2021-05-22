# TCC | BI Master | PUC-Rio

## [EM DESENVOLVIMENTO] Construção de processo automatizado de extração, transformação e carga de dados para acompanhamento de registros de marcas no INPI

Christian Testtzlaffe Alpoim ([Linkedin](https://www.linkedin.com/in/christian-testtzlaffe-alpoim/))

**Orientador:** Prof. Anderson Nascimento

<hr>

### Objetivo

Este trabalho tem o objetivo de construir um fluxo automatizado de coleta, transformação e carga/persistência de dados dos processos de registros de marcas originados pelo Instituto Nacional de Propriedade Industrial (INPI). Antes deste processo de extração, transformação e carga (ETL), é necessário o mapeamento dos dados, a modelagem e a criação do repositório destes registros (banco de dados relacional). Uma vez que o processo esteja configurado e sendo executado periodicamente, este banco de dados permitirá a construção de aplicações para acompanhamento e alerta sobre o avanço nos registros de marcas.

<hr>

### INPI

O Instituto Nacional da Propriedade Industrial (INPI) é uma autarquia federal brasileira, criada em 1970, vinculada ao Ministério do Desenvolvimento, Indústria e Comércio Exterior (MDIC).

Conforme art. 2º da Lei nº 5.648/1970, "O INPI tem por finalidade principal executar, no âmbito nacional, as normas que regulam a propriedade industrial, tendo em vista a sua função social, econômica, jurídica e técnica, bem como pronunciar-se quanto à conveniência de assinatura, ratificação e denúncia de convenções, tratados, convênios e acordos sobre propriedade industrial". (Redação dada pela Lei nº 9.279, de 1996).

Entre suas funções, o INPI é responsável pelo registro e concessão de marcas, que é a base para este trabalho.

<hr>

### Etapas, Arquitetura e Tecnologias

O diagrama abaixo resume as etapas do processo, bem como a arquitetura da solução e indicação das tecnologias:

<img src="/imagens/Arquitetura.png" alt="imagem da arquitetura da solução" />

<details>
  <summary>Resumo das etapas e justificativas para definição das tecnologias</summary>
  <br>
  <ul>
    <li><strong>Fonte dos dados:</strong> arquivos XML do site do INPI</li>
    <li><strong>Mapeamento dos dados:</strong> estudo das principais tags e atributos do arquivo, bem como suas relações</li>
    <li><strong>Modelagem dos dados:</strong> desenhar o modelo de tabelas e seus relacionamentos, com uso do [SQL Power Architect](http://www.bestofbi.com/page/architect)</li>
    <li><strong>BD (banco de dados):</strong> criação e atualização das tabelas por meio do <a href="https://www.postgresql.org/">PostgreSQL</a>. O PostgreSQL foi definido como o sistema gerenciador de banco de dados relacional do projeto, por ser de código aberto, com mais de 30 anos de desenvolvimento. Tem uma boa reputação e é amplamente utilizada pelo mercado, com arquitetura comprovada, confiável, com recursos robustos. Além disso, pode ser executado em todos os principais sistemas operacionais.</li>
    <li><strong>ETL:</strong> extrações, transformações e cargas com <a href="https://help.pentaho.com/Documentation/7.1/0D0/Pentaho_Data_Integration">Pentaho Data Integration (PDI)</a>. O PDI inúmeras funcionalidade de ETL que facilitam a coleta, limpeza, transformações e persistência dos dados. É intuitivo na utilização, e tem integração com vários formatos de entrada (se mostrou capaz de carregar milhares de registros de um arquivo XML) e com vários sistemas gerenciadores de banco de dados, inclusive PostgreSQL. Apesar dos tamanhos dos arquivos deste trabalho, atendeu bem a conclusão de ETL semanal em poucos minutos. Permite agendar processos para executarem automaticamente, bem como gerar alertas de finalização ou falhas. Pentaho Data Integration é amplamente utilizada por diversos tipos de empresas, entre elas: instituições financeiras, indústrias, órgãos dos governos federal, estaduais e prefeituras, entidades de saúde, universidades, entre outras.</li>
</details>

<hr>

### Fonte dos dados
Os dados a serem coletados para o processo de BI são públicos e disponibilizados na <a href="http://revistas.inpi.gov.br/rpi" target="_blank">Revista da Propriedade Industrial</a>. O INPI divulga semanalmente, toda terça-feira, os dados de atualização sobre os processos de registros de marcas, tanto no formato pdf quanto em XML. Neste trabalho, foi avaliado que o arquivo XML contém as principais informações de despachos do INPI, e servirá como origem dos dados para o processo de ETL.

Vale destacar que o arquivo XML tem dezenas de milhares de despachos, cada um em torno de 20 a 30 MB.

<hr>

### Mapeamento dos dados

O PDI também auxiliou na listagem de todas as tags e nós do arquivo XML (no exemplo, revista nº 2625). Por meio da etapa "Get data from XML" na ferramenta, na funcionalidade "Get XPath nodes", é possível visualizar todos os nós (tags) presentes no arquivo:

Além das tags, alguns nós do XML têm atributos, por exemplo: na tag "titular", há atributos como nome, país e UF do titular da marca.

[Exemplo de um processo/despacho no XML](/anexos/exemplo-processo-xml.md)

[Tabela de tags e atributos do XML](/anexos/tabela-tags-atributos.md)

<hr>

### Modelagem das tabelas e campos

Partindo do mapeamento dos dados da etapa anterior, foi possível identificar quais as entidades mais importantes para o modelo do banco de dados. Basicamente, o escopo envolverá as seguintes entidades: revistas, despachos, processos, titulares e marcas (com auxílio das tabelas natureza_marca e apresentacao_marca) e classes-nice (com tabela auxiliar de tipos de classe).

[Modelo Relacional](/anexos/modelo.md)

<hr>

### Criação do banco de dados

O banco de dados utiliza com sistema gerenciador (SGBD) o PostgreSQL. A criação das tabelas foi originada diretamente do SQL Power Architect, tomando como base o modelo desenhado.

<hr>

### Extração, transformação e carga dos dados
O processo central do trabalho, o ETL, segue algumas etapas importantes para o alcance do objetivo de geração do banco de dados devidamente carregado. 

Extração: etapa de coleta / extração dos recursos de dados. Neste trabalho, a extração é responsável pelo download, descompactação dos arquivos zipados, leitura do XML e loop sobre as tags importantes para obtenção dos dados.

Transformação: tratamento dos dados brutos, formatações e adequações do conteúdo dos campos. Aqui foram realizadas operações sobre textos (strings), formatações de datas, seleção de valores, entre outros.

Carga: etapa final do ETL, persiste os dados no repositório de destino. No caso deste projeto, cada conjunto de dados extraídos e transformados para cada entidade, são carregados para o PostgreSQL de forma que semanalmente os registros de processos de marcas estejam sempre atualizados.

No Pentaho Data Integration (PDI) foi implementado um fluxo (job) de etapas de extração dos dados, transformações / formatações / preparação dos campos, e a carga para cada tabela no PostgreSQL, conforme tela abaixo.

O processo foi agendado no "Agendador de Tarefas" do Windows, para executar toda terça-feira às 11h. São duas execuções agendadas: 1) download do arquivo .zip do site do INPI; 2) job configurado no PDI.

Para o download, foi desenvolvido um [script em python](/script-download-revistas), que define qual o número atual da revista e baixa o arquivo para determinada pasta.

Já para a fase do job no PDI, a primeira etapa é "unzip file", que extrai o xml do arquivo compactado no diretório definido. Segue com o job organizando uma sequência de chamadas às "transformations" desenvolvidas para cada tabela do banco de dados. Por fim, move os arquivos zipados para uma pasta auxiliar de histórico, deleta o xml utilizado, limpando a pasta para a carga da semana seguinte.

[Telas do job e das transformações](/anexos/transformacoes.md)

Foram efetuadas cargas com sucesso de 54 revistas sobre marcas, equivalente a 1 ano de acompanhamento. Estas cargas persistiram mais de 1 milhão de despachos e mais de 700 mil processos. Em torno de 940MB.

<hr>

### Resultados e conclusões

A sequência de etapas acima atingiu o objetivo do trabalho de construir um fluxo automatizado, que semanalmente realiza o ETL, que culmina na persistência dos dados no Postgres. 

O arsenal de tecnologias utilizadas se mostrou capaz de garantir esta carga, mesmo com a quantidade de mais de 1 milhão de despachos por ano.

Este resultado permite que o projeto evolua por exemplo para a conexão de uma API e uma interface web a fim de disponibilizar serviços de acompanhamento de processos de registros de marca no INPI e de alertas sobre atualizações de despachos.


