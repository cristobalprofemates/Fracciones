# Crear estructura básica de datos para el juego de fracciones
import json

# Datos para diferentes tipos de operaciones con fracciones
operaciones_fracciones = {
    "suma_mismo_denominador": [
        {
            "pregunta": "¿Cuál es el resultado de 2/5 + 1/5?",
            "opciones": ["3/5", "3/10", "2/10", "1/5"],
            "respuesta_correcta": 0,
            "explicacion": "Al tener el mismo denominador, sumamos los numeradores: 2 + 1 = 3, y mantenemos el denominador 5"
        },
        {
            "pregunta": "¿Cuál es el resultado de 4/7 + 2/7?",
            "opciones": ["6/7", "6/14", "2/7", "4/14"],
            "respuesta_correcta": 0,
            "explicacion": "Sumamos los numeradores: 4 + 2 = 6, y mantenemos el denominador 7"
        },
        {
            "pregunta": "¿Cuál es el resultado de 3/8 - 1/8?",
            "opciones": ["2/8", "1/4", "4/16", "2/16"],
            "respuesta_correcta": 0,
            "explicacion": "Restamos los numeradores: 3 - 1 = 2, y mantenemos el denominador 8. (También se puede simplificar a 1/4)"
        }
    ],
    "suma_diferente_denominador": [
        {
            "pregunta": "¿Cuál es el resultado de 1/2 + 1/3?",
            "opciones": ["5/6", "2/5", "1/6", "3/6"],
            "respuesta_correcta": 0,
            "explicacion": "Método mariposa: (1×3)+(1×2) = 5 en el numerador, 2×3 = 6 en el denominador"
        },
        {
            "pregunta": "¿Cuál es el resultado de 1/4 + 1/6?",
            "opciones": ["5/12", "2/10", "1/10", "5/24"],
            "respuesta_correcta": 0,
            "explicacion": "Método mariposa: (1×6)+(1×4) = 10, denominador: 4×6 = 24, simplificando: 10/24 = 5/12"
        },
        {
            "pregunta": "¿Cuál es el resultado de 2/3 - 1/4?",
            "opciones": ["5/12", "1/7", "3/12", "8/12"],
            "respuesta_correcta": 0,
            "explicacion": "Método mariposa: (2×4)-(1×3) = 8-3 = 5 en el numerador, 3×4 = 12 en el denominador"
        }
    ],
    "multiplicacion": [
        {
            "pregunta": "¿Cuál es el resultado de 2/3 × 1/4?",
            "opciones": ["2/12", "1/6", "3/7", "2/7"],
            "respuesta_correcta": 0,
            "explicacion": "Multiplicamos numerador por numerador (2×1=2) y denominador por denominador (3×4=12). Se puede simplificar a 1/6"
        },
        {
            "pregunta": "¿Cuál es el resultado de 3/5 × 2/7?",
            "opciones": ["6/35", "5/12", "6/12", "1/35"],
            "respuesta_correcta": 0,
            "explicacion": "Multiplicamos: 3×2 = 6 (numerador), 5×7 = 35 (denominador)"
        },
        {
            "pregunta": "¿Cuál es el resultado de 1/2 × 4/5?",
            "opciones": ["4/10", "2/5", "5/6", "1/10"],
            "respuesta_correcta": 0,
            "explicacion": "Multiplicamos: 1×4 = 4 (numerador), 2×5 = 10 (denominador). Se puede simplificar a 2/5"
        }
    ],
    "division": [
        {
            "pregunta": "¿Cuál es el resultado de 1/2 ÷ 1/3?",
            "opciones": ["3/2", "1/6", "2/3", "6/1"],
            "respuesta_correcta": 0,
            "explicacion": "Multiplicación cruzada: 1×3 = 3 (numerador), 2×1 = 2 (denominador)"
        },
        {
            "pregunta": "¿Cuál es el resultado de 2/5 ÷ 3/4?",
            "opciones": ["8/15", "6/20", "15/8", "5/12"],
            "respuesta_correcta": 0,
            "explicacion": "Multiplicación cruzada: 2×4 = 8 (numerador), 5×3 = 15 (denominador)"
        },
        {
            "pregunta": "¿Cuál es el resultado de 3/7 ÷ 2/3?",
            "opciones": ["9/14", "6/21", "14/9", "21/6"],
            "respuesta_correcta": 0,
            "explicacion": "Multiplicación cruzada: 3×3 = 9 (numerador), 7×2 = 14 (denominador)"
        }
    ]
}

# Crear datos para el sistema de puntuación y gamificación
sistema_gamificacion = {
    "niveles": [
        {"nivel": 1, "nombre": "Aprendiz de Fracciones", "puntos_minimos": 0, "descripcion": "¡Empiezas tu aventura con las fracciones!"},
        {"nivel": 2, "nombre": "Explorador Matemático", "puntos_minimos": 100, "descripcion": "Ya dominas las operaciones básicas"},
        {"nivel": 3, "nombre": "Maestro de Números", "puntos_minimos": 300, "descripcion": "Eres experto en todas las operaciones"},
        {"nivel": 4, "nombre": "Campeón de Fracciones", "puntos_minimos": 500, "descripcion": "¡Eres un verdadero campeón!"}
    ],
    "logros": [
        {"id": "primera_suma", "nombre": "Primera Suma", "descripcion": "Completaste tu primera suma de fracciones", "puntos": 10},
        {"id": "primera_resta", "nombre": "Primera Resta", "descripcion": "Completaste tu primera resta de fracciones", "puntos": 10},
        {"id": "primera_multiplicacion", "nombre": "Primera Multiplicación", "descripcion": "Completaste tu primera multiplicación", "puntos": 15},
        {"id": "primera_division", "nombre": "Primera División", "descripcion": "Completaste tu primera división", "puntos": 20},
        {"id": "racha_5", "nombre": "Racha de 5", "descripcion": "Respondiste 5 preguntas seguidas correctamente", "puntos": 50},
        {"id": "perfeccionista", "nombre": "Perfeccionista", "descripcion": "Completaste un nivel sin errores", "puntos": 100}
    ],
    "puntuacion": {
        "respuesta_correcta": 10,
        "respuesta_incorrecta": -2,
        "bonus_velocidad": 5,
        "bonus_racha": 2
    }
}

print("Datos creados exitosamente:")
print(f"Total de preguntas: {sum(len(categoria) for categoria in operaciones_fracciones.values())}")
print(f"Categorías: {list(operaciones_fracciones.keys())}")
print(f"Niveles de gamificación: {len(sistema_gamificacion['niveles'])}")
print(f"Logros disponibles: {len(sistema_gamificacion['logros'])}")

# Guardar los datos en formato JSON para usar en la aplicación
with open('datos_fracciones.json', 'w', encoding='utf-8') as f:
    json.dump({
        'operaciones': operaciones_fracciones,
        'gamificacion': sistema_gamificacion
    }, f, ensure_ascii=False, indent=2)

print("Archivo JSON creado: datos_fracciones.json")