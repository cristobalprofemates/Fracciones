
# Crear el archivo JavaScript principal con toda la lógica del juego (Parte 1)
app_js_part1 = '''// Datos del juego
const GAME_DATA = {
    operaciones: {
        suma_mismo_denominador: [
            {
                pregunta: "¿Cuál es el resultado de 2/5 + 1/5?",
                opciones: ["3/5", "3/10", "2/10", "1/5"],
                respuesta_correcta: 0,
                explicacion: "Al tener el mismo denominador, sumamos los numeradores: 2 + 1 = 3, y mantenemos el denominador 5"
            },
            {
                pregunta: "¿Cuál es el resultado de 4/7 + 2/7?",
                opciones: ["6/7", "6/14", "2/7", "4/14"],
                respuesta_correcta: 0,
                explicacion: "Sumamos los numeradores: 4 + 2 = 6, y mantenemos el denominador 7"
            },
            {
                pregunta: "¿Cuál es el resultado de 3/8 - 1/8?",
                opciones: ["2/8", "1/4", "4/16", "2/16"],
                respuesta_correcta: 0,
                explicacion: "Restamos los numeradores: 3 - 1 = 2, y mantenemos el denominador 8"
            }
        ],
        suma_diferente_denominador: [
            {
                pregunta: "¿Cuál es el resultado de 1/2 + 1/3?",
                opciones: ["5/6", "2/5", "1/6", "3/6"],
                respuesta_correcta: 0,
                explicacion: "Método mariposa: (1×3)+(1×2) = 5 en el numerador, 2×3 = 6 en el denominador"
            },
            {
                pregunta: "¿Cuál es el resultado de 1/4 + 1/6?",
                opciones: ["5/12", "2/10", "1/10", "5/24"],
                respuesta_correcta: 0,
                explicacion: "Método mariposa: (1×6)+(1×4) = 10, denominador: 4×6 = 24, simplificando: 10/24 = 5/12"
            },
            {
                pregunta: "¿Cuál es el resultado de 2/3 - 1/4?",
                opciones: ["5/12", "1/7", "3/12", "8/12"],
                respuesta_correcta: 0,
                explicacion: "Método mariposa: (2×4)-(1×3) = 8-3 = 5 en el numerador, 3×4 = 12 en el denominador"
            }
        ],
        multiplicacion: [
            {
                pregunta: "¿Cuál es el resultado de 2/3 × 1/4?",
                opciones: ["2/12", "1/6", "3/7", "2/7"],
                respuesta_correcta: 0,
                explicacion: "Multiplicamos numerador por numerador (2×1=2) y denominador por denominador (3×4=12)"
            },
            {
                pregunta: "¿Cuál es el resultado de 3/5 × 2/7?",
                opciones: ["6/35", "5/12", "6/12", "1/35"],
                respuesta_correcta: 0,
                explicacion: "Multiplicamos: 3×2 = 6 (numerador), 5×7 = 35 (denominador)"
            },
            {
                pregunta: "¿Cuál es el resultado de 1/2 × 4/5?",
                opciones: ["4/10", "2/5", "5/6", "1/10"],
                respuesta_correcta: 0,
                explicacion: "Multiplicamos: 1×4 = 4 (numerador), 2×5 = 10 (denominador)"
            }
        ],
        division: [
            {
                pregunta: "¿Cuál es el resultado de 1/2 ÷ 1/3?",
                opciones: ["3/2", "1/6", "2/3", "6/1"],
                respuesta_correcta: 0,
                explicacion: "Multiplicación cruzada: 1×3 = 3 (numerador), 2×1 = 2 (denominador)"
            },
            {
                pregunta: "¿Cuál es el resultado de 2/5 ÷ 3/4?",
                opciones: ["8/15", "6/20", "15/8", "5/12"],
                respuesta_correcta: 0,
                explicacion: "Multiplicación cruzada: 2×4 = 8 (numerador), 5×3 = 15 (denominador)"
            },
            {
                pregunta: "¿Cuál es el resultado de 3/7 ÷ 2/3?",
                opciones: ["9/14", "6/21", "14/9", "21/6"],
                respuesta_correcta: 0,
                explicacion: "Multiplicación cruzada: 3×3 = 9 (numerador), 7×2 = 14 (denominador)"
            }
        ]
    },
    niveles: [
        { nivel: 1, nombre: "Aprendiz de Fracciones", puntos_minimos: 0 },
        { nivel: 2, nombre: "Explorador Matemático", puntos_minimos: 100 },
        { nivel: 3, nombre: "Maestro de Números", puntos_minimos: 300 },
        { nivel: 4, nombre: "Campeón de Fracciones", puntos_minimos: 500 }
    ],
    logros: [
        { id: "primera_suma", nombre: "Primera Suma", descripcion: "Completaste tu primera suma", puntos: 10 },
        { id: "primera_multiplicacion", nombre: "Primera Multiplicación", descripcion: "Completaste tu primera multiplicación", puntos: 15 },
        { id: "primera_division", nombre: "Primera División", descripcion: "Completaste tu primera división", puntos: 20 },
        { id: "racha_5", nombre: "Racha de 5", descripcion: "5 respuestas seguidas correctas", puntos: 50 },
        { id: "perfeccionista", nombre: "Perfeccionista", descripcion: "Nivel sin errores", puntos: 100 }
    ]
};

// Estado del juego
let gameState = {
    totalPoints: 0,
    currentLevel: 1,
    streak: 0,
    maxStreak: 0,
    achievements: [],
    currentCategory: null,
    currentQuestions: [],
    currentQuestionIndex: 0,
    correctAnswers: 0,
    incorrectAnswers: 0,
    sessionStartTime: null,
    timerInterval: null,
    timeRemaining: 30
};

// Inicializar aplicación
document.addEventListener('DOMContentLoaded', function() {
    console.log('Iniciando aplicación de fracciones...');
    
    // Inicializar SCORM
    initializeSCORM();
    
    // Cargar progreso previo
    loadGameProgress();
    
    // Configurar event listeners
    setupEventListeners();
    
    // Actualizar UI
    updateUI();
    
    // Iniciar guardado automático
    setInterval(saveGameProgress, 10000); // Guardar cada 10 segundos
});

// Configurar event listeners
function setupEventListeners() {
    // Categorías
    document.querySelectorAll('.category-card').forEach(card => {
        card.addEventListener('click', function() {
            const category = this.dataset.category;
            startGame(category);
        });
    });
    
    // Modo mixto
    document.getElementById('mixed-mode-btn').addEventListener('click', function() {
        startGame('mixed');
    });
    
    // Botones de navegación
    document.getElementById('back-btn').addEventListener('click', returnToMenu);
    document.getElementById('next-btn').addEventListener('click', nextQuestion);
    document.getElementById('play-again-btn').addEventListener('click', function() {
        startGame(gameState.currentCategory);
    });
    document.getElementById('change-category-btn').addEventListener('click', returnToMenu);
}

// Iniciar juego
function startGame(category) {
    gameState.currentCategory = category;
    gameState.currentQuestionIndex = 0;
    gameState.correctAnswers = 0;
    gameState.incorrectAnswers = 0;
    gameState.sessionStartTime = Date.now();
    
    // Obtener preguntas
    if (category === 'mixed') {
        gameState.currentQuestions = [];
        Object.values(GAME_DATA.operaciones).forEach(cat => {
            gameState.currentQuestions = gameState.currentQuestions.concat(cat);
        });
        shuffleArray(gameState.currentQuestions);
    } else {
        gameState.currentQuestions = [...GAME_DATA.operaciones[category]];
        shuffleArray(gameState.currentQuestions);
    }
    
    // Limitar a 10 preguntas
    gameState.currentQuestions = gameState.currentQuestions.slice(0, 10);
    
    showScreen('game-screen');
    showQuestion();
}

// Mostrar pregunta
function showQuestion() {
    const question = gameState.currentQuestions[gameState.currentQuestionIndex];
    
    // Actualizar contador
    document.getElementById('question-counter').textContent = 
        `Pregunta ${gameState.currentQuestionIndex + 1}/${gameState.currentQuestions.length}`;
    
    // Mostrar pregunta
    document.getElementById('question-text').textContent = question.pregunta;
    
    // Mostrar opciones
    const optionsContainer = document.getElementById('options-container');
    optionsContainer.innerHTML = '';
    
    question.opciones.forEach((opcion, index) => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.textContent = opcion;
        btn.addEventListener('click', () => checkAnswer(index));
        optionsContainer.appendChild(btn);
    });
    
    // Ocultar feedback
    document.getElementById('feedback').classList.add('hidden');
    
    // Reiniciar timer
    resetTimer();
}

// Verificar respuesta
function checkAnswer(selectedIndex) {
    const question = gameState.currentQuestions[gameState.currentQuestionIndex];
    const isCorrect = selectedIndex === question.respuesta_correcta;
    
    // Deshabilitar botones
    document.querySelectorAll('.option-btn').forEach((btn, idx) => {
        btn.classList.add('disabled');
        if (idx === question.respuesta_correcta) {
            btn.classList.add('correct');
        } else if (idx === selectedIndex && !isCorrect) {
            btn.classList.add('incorrect');
        }
    });
    
    // Detener timer
    clearInterval(gameState.timerInterval);
    
    // Actualizar estadísticas
    if (isCorrect) {
        gameState.correctAnswers++;
        gameState.streak++;
        gameState.maxStreak = Math.max(gameState.maxStreak, gameState.streak);
        
        // Calcular puntos
        let points = 10;
        if (gameState.timeRemaining > 20) points += 5; // Bonus velocidad
        if (gameState.streak >= 3) points += 2; // Bonus racha
        
        gameState.totalPoints += points;
        
        // Mostrar feedback positivo
        showFeedback(true, question.explicacion, points);
        
        // Verificar logros
        checkAchievements(question);
    } else {
        gameState.incorrectAnswers++;
        gameState.streak = 0;
        gameState.totalPoints = Math.max(0, gameState.totalPoints - 2);
        
        // Mostrar feedback negativo
        showFeedback(false, question.explicacion);
    }
    
    // Actualizar nivel
    updateLevel();
    updateUI();
    saveGameProgress();
}'''

print("Creando archivo JavaScript principal (app.js)...")
with open('app_js_temp.txt', 'w', encoding='utf-8') as f:
    f.write(app_js_part1)
print("✓ Parte 1 de app.js creada")
