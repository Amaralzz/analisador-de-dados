# Analisador de Dados

Aplicação web em Django que recebe um arquivo CSV via upload e gera automaticamente uma análise exploratória (EDA): prévia dos dados, estatísticas descritivas, contagem de valores ausentes e um histograma da primeira coluna numérica — tudo processado em memória, sem salvar arquivos em disco.

## Funcionalidades

- Upload de arquivo CSV
- Prévia dos dados (`.head()`)
- Estatísticas descritivas (`.describe()`)
- Contagem de valores ausentes por coluna
- Histograma gerado dinamicamente com Matplotlib e exibido direto na página (imagem em base64, sem salvar em disco)

## Tecnologias

- Python / Django
- Pandas
- Matplotlib
- HTML / CSS

## Como rodar localmente

```bash
git clone <url-do-repositorio>
cd analisador

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

pip install django pandas matplotlib

python manage.py migrate
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/dados/` e envie um arquivo `.csv`.

## Decisões técnicas e aprendizados

- **Processamento em memória, sem persistência**: o CSV enviado nunca é salvo no servidor — é lido diretamente do objeto de upload (`request.FILES`) pelo Pandas e descartado após a resposta, evitando acúmulo de arquivos e problemas de espaço em disco.
- **Geração de gráficos sem interface gráfica**: como o servidor não tem "tela", o Matplotlib é configurado com o backend `Agg` (`matplotlib.use('Agg')`) para renderizar imagens apenas em memória.
- **Imagem embutida via base64**: o gráfico é salvo num buffer (`io.BytesIO`) em vez de um arquivo `.png`, convertido para uma string base64 e embutido diretamente no HTML (`<img src="data:image/png;base64,...">`) — evitando escrever e gerenciar arquivos estáticos temporários.

## Possíveis melhorias futuras

- Permitir escolher qual coluna plotar
- Suporte a outros tipos de gráfico (dispersão, boxplot)
- Validação de arquivos não-CSV com mensagem de erro amigável
- Exportar o relatório de análise em PDF