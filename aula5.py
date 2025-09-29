import pandas as pd
import numpy as np
#Criando um DataFrame ficiticio 
np.random.seed(41)
dados = pd.DataFrame({
    "Variavel_A": np.random.rand(10) * 10, #Valores aleatorios entre 0 e 10
    "Variavel_B": np.random.rand(10) * 10, 
    "Variavel_C": np.random.rand(10) * 10
    
})

print(dados)

#O t tempo sempre precisa ser no eixo x 
#Regressão linear é quando o gráfico varia e traçamos uma reta no meio dessas variações, ou seja, a reta média 
# y = ax + b
# y = a + out + b //Para descobrirmos o valor do mes de outubro, o próximo mes eu tenho certeza que é outubro // Isso se chama análise preditiva
#Quando eu acho meu valor médio da reta, eu também acho os dois pontos, o que está para cima e o que está para baixo, os cenários positivo e negativo
#O valor de r mostra a correlação linear entre o x e o y //Ele diz o quão reta é a minha reta média 
#O inverso do r2 é o erro, ou seja, o que eu encontro do r2, o oposto é o erro 
#O r é a % dos numeros que estão passando por cima da reta 

# Calculando o Coeficiente de correlação de pearson entre A e B 
correlacao_A_B = dados["Variavel_A"].corr(dados["Variavel_B"])
print(f"Coeficiente de correlação entre A e B: {correlacao_A_B}")

# Calculando a Matriz de correlação para todas as variáveis 
matriz_correlacao = dados.corr()
print("Matriz de correlação:")
print(matriz_correlacao)

# Para ver o gráfico 

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 5))
sns.heatmap(matriz_correlacao, annot=True, cmap="coolwarm", fmt=".2f", linewidths= 0.5)
plt.title("Matriz de Correlação")
plt.show()

