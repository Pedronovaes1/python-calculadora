import sympy  # type: ignore

#uma função para calcular a integgral
def funcao_calculadora(funcao, limiteSuperior=None, limiteInferior=None):
    #Primeiro crio uma váriavel 
    x = sympy.Symbol('x')
    #converter string em funcao
    funcao_2 = sympy.sympify(funcao)

    #Verificar se tem limite ou é indefinida 
    if limiteSuperior is not None and limiteInferior is not None:
        integral = sympy.integrate(funcao_2,(x, limiteInferior, limiteSuperior))
    else:  
        integral = sympy.integrate(funcao_2, x) 
    
    return integral 

#def comprimeto_arco(funcao, limiteSuperior=None, limiteInferiror=None):

#def area_da_curva(funcao, limiteSuperior=None, limiteInferiror=None):

#def volume_da_curva(funcao, limiteSuperior=None, limiteInferiror=None):

# digitar o algoritmo principal
print("\n==== Calculadora de Integral ====")
print("---------------------------------")

print('OBS: digite a função em relação a x \nExemplo: 2*x**2 + 3*x + 1\n')

funcao = input("Digite a função que deseja calcular a integral: ")
limiteSuperior = input("Digite o limite superior (Ou presione enter para idefinida): ")
limiteInferior = input("Digite o limite inferiror (Ou presione enter para idefinida): ")

# Verificar os limites 
limiteSuperior = float(limiteSuperior) if limiteSuperior else None
limiteInferior = float(limiteInferior) if limiteInferior else None

#Pegar o resultado da função

resultado = funcao_calculadora(funcao, limiteSuperior, limiteInferior)

print("\nO resultado da integral é: ")
print(resultado)
