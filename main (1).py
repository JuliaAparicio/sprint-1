
from graphviz import Digraph
from IPython.display import Image
import os

# Criando o diagrama de fluxo
fluxo = Digraph(comment='Etapa 1 - Coleta e Integração de Dados')

fluxo.attr(rankdir='LR', size='10')

# Nós (etapas)
fluxo.node('A', 'Coleta de Dados via API\n(Energia solar, consumo, sensores)', shape='box', style='filled', fillcolor='lightblue')
fluxo.node('B', 'Envio de Dados via JSON\n(New API - Transmissão dos dados)', shape='box', style='filled', fillcolor='lightgreen')
fluxo.node('C', 'Monitoramento com AWS Cloudwatch\n(Métricas, alertas, eventos)', shape='box', style='filled', fillcolor='orange')
fluxo.node('D', 'Armazenamento no AWS S3\n(Dados não vão para o Redshift)', shape='box', style='filled', fillcolor='lightgrey')
fluxo.node('E', 'Dados disponíveis para análise\n(IA, relatórios, previsões)', shape='box', style='filled', fillcolor='khaki')

# Conexões (arestas)
fluxo.edge('A', 'B', label='Envio em tempo real')
fluxo.edge('B', 'C', label='Monitoramento contínuo')
fluxo.edge('C', 'D', label='Armazenamento seguro')
fluxo.edge('D', 'E', label='Disponibilização para análise')

# Gera a imagem
fluxo.render(filename='etapa1_fluxograma', format='png', cleanup=True)

# Exibe a imagem no notebook
Image(filename='etapa1_fluxograma.png')