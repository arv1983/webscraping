
class Preco():
    def precifica(preco):
        preco = preco.replace("R$ ", "")
        preco = float(preco.replace(",", "."))
        COMISSAO_SHOPEE = 0.12
        COMISSAO_FABRICANTE = 0.10

        custo_produto = preco * COMISSAO_SHOPEE

        valor_anunciado = preco * COMISSAO_FABRICANTE

        total = int(round(custo_produto + valor_anunciado + preco,0))

        total = str(total)
        total = [char for char in total]
        total[-1] = "9.90"
        
        total = float(''.join(total))
        

        match total:
            case total if total < 60:
                total += 10
            case total if total >= 60 and total < 100:
                total += 20
            case total if total >= 100:                
                total += 30
        
        total = str(total) + "0"

        return total.replace(".", ",")
                


# print(Preco.precifica("R$ 46,90"))