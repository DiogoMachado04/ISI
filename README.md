# Projeto ISI - Integração de Sistemas de Informação

Este repositório contém o código e documentação do projecto desenvolvido no âmbito da unidade curricular *Integração de Sistemas de Informação (ISI)*. O objetivo é implementar um fluxo completo de tratamento de dados — geração, processamento e visualização — utilizando ferramentas como Pentaho Data Integration (PDI) e Node-RED.

## Estrutura do Repositório

- `data/` - Contém os ficheiros de dados gerados ou utilizados (ex: hotéis, clientes, reservas).  
- `dataint/` - Scripts ou transformações PDI utilizadas para integração e preparação dos dados.  
- `graficos/` - Ficheiros de output relacionados com a visualização de dados (gráficos, dashboards).  
- `node-red/` - Fluxos Node-RED exportados que realizam automação, leitura/escrita de ficheiros e geração de gráficos.  
- `scripts/` - Scripts auxiliares (por exemplo em Python) usados durante o projecto.  
- `README.md` - Este documento.  
- `requirements.txt` - Lista de dependências ou pacotes externos necessários.

## Funcionalidades Principais

1. **Geração de dados aleatórios** — Um dos fluxos Node-RED gera ficheiros com dados fictícios de hotéis, clientes e reservas.  
2. **Processamento e limpeza de dados** — Utilização de PDI para importar, transformar e validar os dados antes da análise.  
3. **Geração de gráficos e relatórios** — A partir dos dados processados, cria-se visualizações que permitem observar métricas como total gasto por cliente ou receitas por hotel.  
4. **Exportação de resultados** — Os dados finais e os gráficos são exportados para ficheiros (ex: CSV, JSON) prontos para utilização ou partilha.

## Como configurar e executar

### Pré-requisitos  
- Instalar o Node-RED.  
- Instalar o Pentaho Data Integration (ou o ambiente equivalente).  
- Garantir que os caminhos (paths) nos nós de leitura e escrita de ficheiros estão corretamente configurados para o teu sistema (ver *Atenções para Execução em Outros Computadores*, abaixo).  
- Instalar as dependências listadas em `requirements.txt`, se aplicável.

### Passos de execução  
1. Importar os fluxos para o Node-RED a partir da pasta `node-red/`.  
2. Adaptar os paths nos nós de ficheiro conforme o local onde colocaste o projecto.  
3. Executar o fluxo de geração de dados (hotéis, clientes, reservas).  
4. Executar o fluxo que gera os gráficos a partir dos dados produzidos.  
5. Consultar os ficheiros exportados em `data/output/` ou local equivalente.

## Atenções para execução em outros computadores  
Nos nós de entrada e saída de ficheiros do Node-RED foram definidos caminhos absolutos. Por exemplo:

C:\Users\Diogo Machado\Documents\GitHub\ISI\data\output\hoteis_totais.csv

Para garantir que o programa funciona correctamente noutro dispositivo, **deves alterar estes caminhos para corresponderem à estrutura de pastas do teu computador** ou preferencialmente usar caminhos relativos. A não adaptação destes paths impedirá o Node-RED de ler ou gravar os ficheiros adequadamente.