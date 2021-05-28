[< VOLTAR](/desenvolvimento.md#extra%C3%A7%C3%A3o-transforma%C3%A7%C3%A3o-e-carga-dos-dados)

## Script python para download das Revistas de Propriedade Industrial

Este código foi desenvolvido para ser executado semanalmente, toda terça-feira, para realizar o download dos arquivos .zip referentes às Revistas de Propriedade Industrial do INPI.

### Execução

1. Baixe o código do arquivo [download.py](/script-download-revistas/download.py).

2. Instale o pacote 'requests':
```
pip install requests
```

3. Preencha o caminho desejado como destino dos arquivos baixados:
```python
path = '<DIGITE O CAMINHO DA PASTA DE DESTINO DOS ARQUIVOS BAIXADOS'
```

4. Execute o script:
```
python download.py
```
