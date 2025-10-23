
# Leer el código JavaScript parte 1 desde los archivos creados
with open('datos_fracciones.json', 'r', encoding='utf-8') as f:
    import json
    datos = json.load(f)

# Crear el archivo JavaScript completo
app_js_completo = '''// Datos del juego
const GAME_DATA = ''' + json.dumps(datos, ensure_ascii=False, indent=2) + ''';

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
    initializeSCORM();
    loadGameProgress();
    setupEventListeners();
    updateUI();
    setInterval(saveGameProgress, 10000);
});

// Configurar event listeners
function setupEventListeners() {
    document.querySelectorAll('.category-card').forEach(card => {
        card.addEventListener('click', function() {
            startGame(this.dataset.category);
        });
    });
    document.getElementById('mixed-mode-btn').addEventListener('click', () => startGame('mixed'));
    document.getElementById('back-btn').addEventListener('click', returnToMenu);
    document.getElementById('next-btn').addEventListener('click', nextQuestion);
    document.getElementById('play-again-btn').addEventListener('click', () => startGame(gameState.currentCategory));
    document.getElementById('change-category-btn').addEventListener('click', returnToMenu);
}

// Iniciar juego
function startGame(category) {
    gameState.currentCategory = category;
    gameState.currentQuestionIndex = 0;
    gameState.correctAnswers = 0;
    gameState.incorrectAnswers = 0;
    gameState.sessionStartTime = Date.now();
    
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
    
    gameState.currentQuestions = gameState.currentQuestions.slice(0, 10);
    showScreen('game-screen');
    showQuestion();
}

// Mostrar pregunta
function showQuestion() {
    const question = gameState.currentQuestions[gameState.currentQuestionIndex];
    document.getElementById('question-counter').textContent = 
        `Pregunta ${gameState.currentQuestionIndex + 1}/${gameState.currentQuestions.length}`;
    document.getElementById('question-text').textContent = question.pregunta;
    
    const optionsContainer = document.getElementById('options-container');
    optionsContainer.innerHTML = '';
    
    question.opciones.forEach((opcion, index) => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.textContent = opcion;
        btn.addEventListener('click', () => checkAnswer(index));
        optionsContainer.appendChild(btn);
    });
    
    document.getElementById('feedback').classList.add('hidden');
    resetTimer();
}

// Verificar respuesta
function checkAnswer(selectedIndex) {
    const question = gameState.currentQuestions[gameState.currentQuestionIndex];
    const isCorrect = selectedIndex === question.respuesta_correcta;
    
    document.querySelectorAll('.option-btn').forEach((btn, idx) => {
        btn.classList.add('disabled');
        if (idx === question.respuesta_correcta) {
            btn.classList.add('correct');
        } else if (idx === selectedIndex && !isCorrect) {
            btn.classList.add('incorrect');
        }
    });
    
    clearInterval(gameState.timerInterval);
    
    if (isCorrect) {
        gameState.correctAnswers++;
        gameState.streak++;
        gameState.maxStreak = Math.max(gameState.maxStreak, gameState.streak);
        
        let points = 10;
        if (gameState.timeRemaining > 20) points += 5;
        if (gameState.streak >= 3) points += 2;
        
        gameState.totalPoints += points;
        showFeedback(true, question.explicacion, points);
        checkAchievements(question);
    } else {
        gameState.incorrectAnswers++;
        gameState.streak = 0;
        gameState.totalPoints = Math.max(0, gameState.totalPoints - 2);
        showFeedback(false, question.explicacion);
    }
    
    updateLevel();
    updateUI();
    saveGameProgress();
}

// Mostrar feedback
function showFeedback(isCorrect, explanation, points = 0) {
    const feedback = document.getElementById('feedback');
    const icon = feedback.querySelector('.feedback-icon');
    const text = feedback.querySelector('.feedback-text');
    const explanationDiv = feedback.querySelector('.feedback-explanation');
    
    if (isCorrect) {
        icon.textContent = '🎉';
        text.textContent = `¡Correcto! +${points} puntos`;
        text.style.color = '#51cf66';
    } else {
        icon.textContent = '❌';
        text.textContent = '¡Incorrecto!';
        text.style.color = '#ff6b6b';
    }
    
    explanationDiv.textContent = explanation;
    feedback.classList.remove('hidden');
}

// Siguiente pregunta
function nextQuestion() {
    gameState.currentQuestionIndex++;
    if (gameState.currentQuestionIndex < gameState.currentQuestions.length) {
        showQuestion();
    } else {
        showResults();
    }
}

// Mostrar resultados
function showResults() {
    const total = gameState.currentQuestions.length;
    const correct = gameState.correctAnswers;
    const incorrect = gameState.incorrectAnswers;
    const accuracy = Math.round((correct / total) * 100);
    
    document.getElementById('correct-answers').textContent = correct;
    document.getElementById('incorrect-answers').textContent = incorrect;
    document.getElementById('points-earned').textContent = correct * 10;
    document.getElementById('accuracy').textContent = accuracy + '%';
    
    setSCORMScore(accuracy);
    setSCORMStatus(accuracy >= 70 ? 'passed' : 'completed');
    
    showScreen('results-screen');
    saveGameProgress();
}

// Timer
function resetTimer() {
    clearInterval(gameState.timerInterval);
    gameState.timeRemaining = 30;
    updateTimerDisplay();
    
    gameState.timerInterval = setInterval(() => {
        gameState.timeRemaining--;
        updateTimerDisplay();
        
        if (gameState.timeRemaining <= 5) {
            document.getElementById('timer').classList.add('warning');
        }
        
        if (gameState.timeRemaining <= 0) {
            clearInterval(gameState.timerInterval);
            checkAnswer(-1);
        }
    }, 1000);
}

function updateTimerDisplay() {
    document.getElementById('timer').textContent = `⏱️ ${gameState.timeRemaining}`;
}

// Actualizar nivel
function updateLevel() {
    for (let i = GAME_DATA.gamificacion.niveles.length - 1; i >= 0; i--) {
        if (gameState.totalPoints >= GAME_DATA.gamificacion.niveles[i].puntos_minimos) {
            if (gameState.currentLevel !== GAME_DATA.gamificacion.niveles[i].nivel) {
                gameState.currentLevel = GAME_DATA.gamificacion.niveles[i].nivel;
                showNotification(`¡Subiste a nivel ${gameState.currentLevel}!`);
            }
            break;
        }
    }
}

// Verificar logros
function checkAchievements(question) {
    if (question.pregunta.includes('+') && !gameState.achievements.includes('primera_suma')) {
        unlockAchievement('primera_suma');
    }
    if (question.pregunta.includes('×') && !gameState.achievements.includes('primera_multiplicacion')) {
        unlockAchievement('primera_multiplicacion');
    }
    if (question.pregunta.includes('÷') && !gameState.achievements.includes('primera_division')) {
        unlockAchievement('primera_division');
    }
    if (gameState.streak === 5 && !gameState.achievements.includes('racha_5')) {
        unlockAchievement('racha_5');
    }
    if (gameState.incorrectAnswers === 0 && 
        gameState.currentQuestionIndex === gameState.currentQuestions.length - 1 &&
        !gameState.achievements.includes('perfeccionista')) {
        unlockAchievement('perfeccionista');
    }
}

// Desbloquear logro
function unlockAchievement(achievementId) {
    gameState.achievements.push(achievementId);
    const achievement = GAME_DATA.gamificacion.logros.find(a => a.id === achievementId);
    
    if (achievement) {
        gameState.totalPoints += achievement.puntos;
        showNotification(`¡Logro desbloqueado! ${achievement.nombre} (+${achievement.puntos} puntos)`);
    }
    
    updateAchievementsDisplay();
}

// Actualizar visualización de logros
function updateAchievementsDisplay() {
    const achievementsList = document.getElementById('achievements-list');
    achievementsList.innerHTML = '';
    
    GAME_DATA.gamificacion.logros.forEach(logro => {
        const div = document.createElement('div');
        div.className = 'achievement-item';
        if (gameState.achievements.includes(logro.id)) {
            div.classList.add('unlocked');
        }
        div.textContent = `🏆 ${logro.nombre}`;
        achievementsList.appendChild(div);
    });
}

// Actualizar UI
function updateUI() {
    document.getElementById('total-points').textContent = gameState.totalPoints;
    document.getElementById('current-level').textContent = gameState.currentLevel;
    document.getElementById('streak').textContent = gameState.streak;
    
    const currentLevelData = GAME_DATA.gamificacion.niveles.find(n => n.nivel === gameState.currentLevel);
    const nextLevelData = GAME_DATA.gamificacion.niveles.find(n => n.nivel === gameState.currentLevel + 1);
    
    document.getElementById('level-name').textContent = currentLevelData.nombre;
    
    if (nextLevelData) {
        const progress = gameState.totalPoints - currentLevelData.puntos_minimos;
        const needed = nextLevelData.puntos_minimos - currentLevelData.puntos_minimos;
        const percentage = Math.min(100, (progress / needed) * 100);
        
        document.getElementById('progress-fill').style.width = percentage + '%';
        document.getElementById('progress-text').textContent = 
            `${gameState.totalPoints} / ${nextLevelData.puntos_minimos}`;
    } else {
        document.getElementById('progress-fill').style.width = '100%';
        document.getElementById('progress-text').textContent = '¡Nivel máximo!';
    }
    
    updateAchievementsDisplay();
}

// Mostrar notificación
function showNotification(message) {
    const notification = document.getElementById('notification');
    const content = notification.querySelector('.notification-content');
    content.textContent = message;
    notification.classList.remove('hidden');
    setTimeout(() => notification.classList.add('hidden'), 3000);
}

// Cambiar pantalla
function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(screen => screen.classList.remove('active'));
    document.getElementById(screenId).classList.add('active');
}

// Volver al menú
function returnToMenu() {
    clearInterval(gameState.timerInterval);
    showScreen('welcome-screen');
}

// Guardar progreso
function saveGameProgress() {
    const progressData = {
        totalPoints: gameState.totalPoints,
        currentLevel: gameState.currentLevel,
        maxStreak: gameState.maxStreak,
        achievements: gameState.achievements,
        lastPlayed: Date.now()
    };
    saveSuspendData(progressData);
    const percentage = Math.min(100, Math.round((gameState.totalPoints / 500) * 100));
    setSCORMScore(percentage);
}

// Cargar progreso
function loadGameProgress() {
    const savedData = loadSuspendData();
    if (savedData) {
        gameState.totalPoints = savedData.totalPoints || 0;
        gameState.currentLevel = savedData.currentLevel || 1;
        gameState.maxStreak = savedData.maxStreak || 0;
        gameState.achievements = savedData.achievements || [];
        console.log('Progreso cargado:', savedData);
        return savedData;
    }
    return null;
}

// Utilidad: mezclar array
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

console.log('Aplicación de fracciones cargada correctamente');
'''

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js_completo)

print("✓ app.js completo creado\n")
print("=== PAQUETE SCORM COMPLETADO ===")
print("\nArchivos creados:")
print("1. ✓ imsmanifest.xml - Manifiesto SCORM 1.2")
print("2. ✓ scorm-api.js - Comunicación con Moodle")
print("3. ✓ app.js - Lógica del juego gamificado")
print("4. ✓ index.html - Interfaz de usuario")
print("5. ✓ styles.css - Estilos visuales modernos")
print("6. ✓ datos_fracciones.json - Datos de preguntas")
