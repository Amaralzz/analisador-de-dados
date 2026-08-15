from django.shortcuts import render, redirect
from .forms import CSVUploadForm
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

def receber_arquivo(request):
    resultado = None
    descricao = None
    nulos = None
    imagem_base64 = None
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            conteudo = pd.read_csv(arquivo)
            resultado = conteudo.head().to_html()
            descricao = conteudo.describe().to_html()
            nulos = conteudo.isnull().sum().to_frame().to_html()
            colunas_numericas = conteudo.select_dtypes(include='number')
            primeira_coluna = colunas_numericas.columns[0]

            fig, ax = plt.subplots()
            ax.hist(conteudo[primeira_coluna])

            buffer = io.BytesIO()
            fig.savefig(buffer, format='png')
            buffer.seek(0)
            imagem_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            plt.close(fig)


    else:
        form = CSVUploadForm()
    return render(request, 'dados/receber_arquivo.html', {
        'form': form, 
        'resultado': resultado,
        'descricao': descricao,
        'nulos': nulos,
        'imagem': imagem_base64
        })