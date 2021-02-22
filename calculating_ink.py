print ("Bem vindos a loja de tintas!!!")
print ()
metros = float(input("Qual o tamanho da área que será pintada em metros quadrados? "))
litros = metros/6
print ("Litros: ", litros)

    # 1L de tinta pinta 6m*2
    # Latas 18L custa 80.00
    # Galões 3.6L custa 25.00

    # Comprando apenas latas de 18L, serão XXX latas e pagará R$
    # Comprando apenas galões de 3.6L, serão XXX galões e pagará R$
print ()

latas = round((litros/18)+0.5)
#print ("Latas:", latas)
preco_lata = latas*80
#print ("Preço lata:", preco_lata)

galoes = round((litros/3.6)+0.5)
#print ("Galões:", galoes)
preco_galao = galoes*25
#print ("Preço galão:", preco_galao)
#print ()

print (f"Para {metros}m², considerando apenas latas, serão necessárias {latas} lata(s). Sendo assim o valor final será de R${preco_lata}")
print ()

print (f"Para {metros}m², considerando apenas galões, serão necessárias {galoes} galão(ões). Sendo assim o valor final será de R${preco_galao}")
print()

if litros >= 18:
    latas = int(litros/18)
    sobra = litros % 18
    galoes = round(sobra/3.6 + 0.5)

else:
    latas = 0
    galoes = round(litros/3.6 + 0.5)

preco_lata = latas*80
preco_galao = galoes*25
preco_total = preco_galao + preco_lata

print (f"Se for considerar a menor quantidade de tinta desperdiçada, serão necessárias {latas} lata(s) e {galoes} galão(ões), totalizando um valor de {preco_total} reais")