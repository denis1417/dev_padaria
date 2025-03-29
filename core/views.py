from django.shortcuts import render
from datetime import date
from .models import Produto  

def index(request):
    produtos = Produto.objects.all()

    # Contadores para o gráfico
    total_produtos = produtos.count()
    alerta_3 = 0  # Produtos com 3 dias restantes
    alerta_1 = 0  # Produtos vencendo
    prontos = 0   # Produtos normais

    hoje = date.today()

    for produto in produtos:
        dias_para_vencer = (produto.validade - hoje).days
        produto.dias_para_vencer = dias_para_vencer
        
        if dias_para_vencer == 3:
            alerta_3 += 1
        elif dias_para_vencer <= 1:
            alerta_1 += 1
        else:
            prontos += 1

    # Passa os valores para o template
    return render(request, 'index.html', {
        'produtos': produtos,
        'prontos': prontos,
        'alerta_3': alerta_3,
        'alerta_1': alerta_1,
        'total_produtos': total_produtos
    })
