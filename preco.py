
class preco():
    def precifica(preco):
        COMISSAO_SHOPEE = 0.12
        COMISSAO_FABRICANTE = 0.10

        custo_produto = preco * COMISSAO_SHOPEE

        valor_anunciado = preco * COMISSAO_FABRICANTE

        total = int(round(custo_produto + valor_anunciado + preco,0))


        match total:
            case total if total < 60:
                print('menos 60')
            case total if total >= 60 and total < 100:
                print('mais 60')
            case total if total >= 100:                
                print('mais que 100')


teste1 = 37.90
teste2 = 59.90
teste3 = 99.90
teste4 = 129.90
teste5 = 149.90
teste6 = 179.90

preco.precifica(teste3)

# add comissao shope
# multiplica 2

# arredonda para *9,90

# até 60 R$ 10
# 60,01 até 100 R$ 20
# 101,01  R$ 30