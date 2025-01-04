def calcular_metricas(vp, vn, fp, fn):
    """
    Calcula as métricas de avaliação com base nos valores da matriz de confusão.
    
    Args:
        vp (int): Verdadeiros Positivos
        vn (int): Verdadeiros Negativos
        fp (int): Falsos Positivos
        fn (int): Falsos Negativos
    
    Returns:
        dict: Dicionário contendo as métricas calculadas.
    """
    # Acurácia
    acuracia = (vp + vn) / (vp + vn + fp + fn)

    # Sensibilidade (Recall)
    recall = vp / (vp + fn) if (vp + fn) != 0 else 0

    # Especificidade
    especificidade = vn / (vn + fp) if (vn + fp) != 0 else 0

    # Precisão
    precisao = vp / (vp + fp) if (vp + fp) != 0 else 0

    # F-score
    f_score = (2 * precisao * recall) / (precisao + recall) if (precisao + recall) != 0 else 0

    # Retornar as métricas em um dicionário
    return {
        "Acurácia": acuracia,
        "Recall (Sensibilidade)": recall,
        "Especificidade": especificidade,
        "Precisão": precisao,
        "F-score": f_score
    }

# Exemplo de uso
# Definindo os valores arbitrários para a matriz de confusão
vp = 50  # Verdadeiros Positivos
vn = 40  # Verdadeiros Negativos
fp = 10  # Falsos Positivos
fn = 5   # Falsos Negativos

# Calculando as métricas
metricas = calcular_metricas(vp, vn, fp, fn)

# Exibindo as métricas
for metrica, valor in metricas.items():
    print(f"{metrica}: {valor:.2f}")
