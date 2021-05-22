### Tabela de mapeamento de tags e atributos do XML:


<table>
<tr><th>TAG</th><th style="width: 50px;">CAMINHO</th><th>ATRIBUTOS</th><th>CONTÉM TEXTO INTERNO?</th></tr>
<tr><td>revista</td><td>/revista</td><td>numero, data</td><td></td></tr>
<tr><td>processo</td><td>/revista/processo</td><td>numero, data-deposito, data-concessao, data-vigencia</td><td></td></tr>
<tr><td>despachos</td><td>/revista/processo/despachos</td><td></td><td></td></tr>
<tr><td>despacho</td><td>/revista/processo/despachos/despacho</td><td>codigo, nome</td><td></td></tr>
<tr><td>texto-complementar</td><td>/revista/processo/despachos/despacho/texto-complementar</td><td></td><td>Sim</td></tr>
<tr><td>texto-sobrestamento</td><td>/revista/processo/despachos/despacho/texto-sobrestamento</td><td></td><td>Sim</td></tr>
<tr><td>protocolo</td><td>/revista/processo/despachos/despacho/protocolo</td><td>numero, data, codigoServico</td><td></td></tr>
<tr><td>requerente</td><td>/revista/processo/despachos/despacho/protocolo/requerente</td><td>nome-razao-social, pais, uf</td><td></td></tr>
<tr><td>procurador</td><td>/revista/processo/despachos/despacho/protocolo/procurador</td><td></td><td>Sim</td></tr>
<tr><td>cedentes</td><td>/revista/processo/despachos/despacho/protocolo/cedentes</td><td></td><td></td></tr>
<tr><td>cedente</td><td>/revista/processo/despachos/despacho/protocolo/cedentes/cedente</td><td>nome-razao-social, pais, uf</td><td></td></tr>
<tr><td>cessionarios</td><td>/revista/processo/despachos/despacho/protocolo/cessionarios</td><td></td><td></td></tr>
<tr><td>cessionario</td><td>/revista/processo/despachos/despacho/protocolo/cessionarios/cessionario</td><td>nome-razao-social</td><td></td></tr>
<tr><td>marca</td><td>/revista/processo/marca</td><td>apresentacao, natureza</td><td></td></tr>
<tr><td>nome</td><td>/revista/processo/marca/nome</td><td></td><td>Sim</td></tr>
<tr><td>titulares</td><td>/revista/processo/titulares</td><td></td><td></td></tr>
<tr><td>titular</td><td>/revista/processo/titulares/titular</td><td>nome-razao-social, pais, uf</td><td></td></tr>
<tr><td>procurador</td><td>/revista/processo/procurador</td><td></td><td>Sim</td></tr>
<tr><td>sobrestadores</td><td>/revista/processo/sobrestadores</td><td></td><td></td></tr>
<tr><td>sobrestador</td><td>/revista/processo/sobrestadores/sobrestador</td><td>processo, marca</td><td></td></tr>
<tr><td>lista-classe-nice</td><td>/revista/processo/lista-classe-nice</td><td></td><td></td></tr>
<tr><td>classe-nice</td><td>/revista/processo/lista-classe-nice/classe-nice</td><td>codigo</td><td></td></tr>
<tr><td>especificacao</td><td>/revista/processo/lista-classe-nice/classe-nice/especificacao</td><td></td><td>Sim</td></tr>
<tr><td>traducao-especificacao</td><td>/revista/processo/lista-classe-nice/classe-nice/traducao-especificacao</td><td></td><td>Sim</td></tr>
<tr><td>status</td><td>/revista/processo/lista-classe-nice/classe-nice/status</td><td></td><td>Sim</td></tr>
<tr><td>classes-vienna</td><td>/revista/processo/classes-vienna</td><td></td><td></td></tr>
<tr><td>classe-vienna</td><td>/revista/processo/classes-vienna/classe-viena</td><td>codigo, edicao</td><td></td></tr>
<tr><td>classe-nacional</td><td>/revista/processo/classe-nacional</td><td>codigo</td><td></td></tr>
<tr><td>especificacao</td><td>/revista/processo/classe-nacional/especificacao</td><td></td><td>Sim</td></tr>
<tr><td>sub-classes-nacional</td><td>/revista/processo/classe-nacional/sub-classes-nacional</td><td></td><td></td></tr>
<tr><td>sub-classe-nacional</td><td>/revista/processo/classe-nacional/sub-classes-nacional/sub-classe-nacional</td><td>codigo</td><td></td></tr>
<tr><td>dados-de-madri</td><td>/revista/processo/dados-de-madri</td><td>numero-inscricao-internacional, data-recebimento-inpi</td><td></td></tr>
<tr><td>apostila</td><td>/revista/processo/apostila</td><td></td><td>Sim</td></tr>
<tr><td>prioridade-unionista</td><td>/revista/processo/prioridade-unionista</td><td></td><td></td></tr>
<tr><td>prioridade</td><td>/revista/processo/prioridade-unionista/prioridade</td><td>data, numero, pais</td><td></td></tr>
</table>
