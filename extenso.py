import num2words
from babel.numbers import format_currency

def numero_para_extenso(valor):
    reais = int(valor)
    centavos = int(round((valor - reais) * 100))
    extenso_reais = num2words.num2words(reais, lang='pt_BR')
    # Remove pontos da string gerada pelo num2words
    extenso_reais = extenso_reais.replace('.', '')
    extenso_centavos = num2words.num2words(centavos, lang='pt_BR')
    valor_formatado = format_currency(valor, 'BRL', locale='pt_BR')
    return f'{extenso_reais.upper()} REAIS E {extenso_centavos.upper()} CENTAVOS.'

continuar = True

while continuar:
    valor_str = input("Digite o valor em números: ")
    valor_float = float(valor_str.replace('.', '').replace(',', '.'))
    print(numero_para_extenso(valor_float))
    opcao = input("Deseja continuar? (S/N) ").upper()
    continuar = opcao == 'S'
