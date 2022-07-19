from csv import DictReader, DictWriter
import json
import os.path

ss = "ss\ndd"

descricao = """Código Ref.: 65044A

Material: Napa Croco na cor Preto;

Enfeites: Zíper na Cor Preto;

Palmilha: 8 mm de Espessura, Espuma em EVA, e Taloneira Napa Preto;

Forro: Cacharrel, material espumado para maior conforto, na cor Preto;

Salto: 10 cm de Altura e Revestido em Napa Croco na cor Preto;

Solado de TR na cor Preto."
Dimensões da Caixa: 31,5 x 30 x 9,5 cm
Peso do Produto na Caixa: 1000 gramas (aproximadamente)"""



estoque = {'34': '17', '35': '39', '36': '56', '37': '60', '38': '38', '39': '12'}
marca = "Torricella"
referencia = "65044A"
titulo = "Bota Bico Fino Feminina"
categoria = "Calçados Femininos Botas"
preco = "R$ 179,90"

obj = {

'referencia':referencia,
'titulo':titulo,
'categoria':categoria,
'preco': preco,
'descricao': descricao,
'estoque': estoque
}

# print(obj)

headers = ['referencia', 'titulo', 'categoria', 'preco', 'descricao', 'variacao', 'estoque']
if not os.path.isfile('data.csv'):
    with open('data.csv', "a+") as f:
        writer = DictWriter(f, fieldnames=headers)
        writer.writeheader()
        f.close()

for i in range(len(estoque)):
    with open('data.csv', "r+") as f:
        open_file = f.readlines()
        
        print(list(estoque.keys())[i])
        # ss = list(estoque.keys())[i]
        obj['variacao'] = list(estoque.keys())[i]

        obj['estoque'] = list(estoque.values())[i]
        # estoque = list(estoque.values())[i]
        
        # estoque = list(estoque.keys())[i]
        # variacao = list(estoque.values()[i])
        # print(estoque)
        # obj['variacao'] = 'variacao'
        # obj['estoque'] = 'estoque'
       
        kwargs = [{**obj}]
        writer = DictWriter(f, fieldnames=headers)
        writer.writerows(kwargs)
        f.close()

# frase = ['1','2','minha frase','33', '33']
# frase = [valor for valor in frase if 'minha' not in valor ]

# marca = "Marca: Torricella teste s s s"
# marca = " ".join(marca.split()[1:])
# print(marca)

# numero_de_variacoes = len(frase) / 2

# metade = int((str(len(frase) / 2)).split('.')[0])
# # print(metade)

# numero = frase[:metade]
# estoque = frase[metade:]


# dict_from_list = dict(zip(numero, estoque))
# print(dict_from_list)

# key_list = ['name', 'age', 'address']
# value_list = ['Johnny', '27', 'New York']

# dict_from_list = dict(zip(key_list, value_list))
# print(dict_from_list)