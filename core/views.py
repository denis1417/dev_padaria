from django.shortcuts import render
from datetime import date
from .models import Produto  

def index(request):
    produtos = Produto.objects.all()

    # Contadores para o gráfico
    total_produtos = produtos.count()
    alerta_3 = 0  
    alerta_1 = 0  
    prontos = 0   

    hoje = date.today()

    for produto in produtos:
        dias_para_vencer = (produto.validade - hoje).days
        produto.dias_para_vencer = dias_para_vencer  # Adiciona um atributo extra para o template

        if dias_para_vencer >= 4:
            prontos += 1
        elif 2 <= dias_para_vencer <= 3:
            alerta_3 += 1  # Amarelo (2 ou 3 dias restantes)
        else:  # 1 dia ou vencido
            alerta_1 += 1  # Vermelho

    # Passa os valores para o template
    return render(request, 'index.html', {
        'produtos': produtos,
        'prontos': prontos,
        'alerta_3': alerta_3,
        'alerta_1': alerta_1,
        'total_produtos': total_produtos
    })

