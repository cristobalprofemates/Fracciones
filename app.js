// Datos del juego
const GAME_DATA = {
  "operaciones": {
    "suma": [
      {
        "pregunta": "¿Cuál es el resultado de 2/5 + 1/5?",
        "opciones": [
          "3/5",
          "3/10",
          "2/10",
          "1/5"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Al tener el mismo denominador, sumamos los numeradores: 2 + 1 = 3, y mantenemos el denominador 5"
      },
      {
        "pregunta": "¿Cuál es el resultado de 4/7 + 2/7?",
        "opciones": [
          "6/7",
          "6/14",
          "2/7",
          "4/14"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Sumamos los numeradores: 4 + 2 = 6 y mantenemos el denominador 7"
      },
      {
        "pregunta": "¿Cuál es el resultado de 1/2 + 1/3?",
        "opciones": [
          "5/6",
          "2/5",
          "1/6",
          "3/6"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Buscamos un denominador común (6): 1/2 = 3/6 y 1/3 = 2/6, luego sumamos 3 + 2 = 5"
      },
      {
        "pregunta": "¿Cuál es el resultado de 1/4 + 1/6?",
        "opciones": [
          "5/12",
          "2/10",
          "1/10",
          "5/24"
        ],
        "respuesta_correcta": 0,
        "explicacion": "El mínimo común múltiplo de 4 y 6 es 12: 1/4 = 3/12 y 1/6 = 2/12, 3 + 2 = 5/12"
      },
      {
        "pregunta": "¿Cuál es el resultado de 3/10 + 2/5?",
        "opciones": [
          "7/10",
          "5/15",
          "5/10",
          "6/10"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Convertimos 2/5 a décimos: 2/5 = 4/10, luego 3/10 + 4/10 = 7/10"
      },
      {
        "pregunta": "¿Cuál es el resultado de 5/8 + 3/16?",
        "opciones": [
          "13/16",
          "8/24",
          "15/24",
          "1/2"
        ],
        "respuesta_correcta": 0,
        "explicacion": "El denominador común es 16: 5/8 = 10/16, luego 10/16 + 3/16 = 13/16"
      }
    ],
    "resta": [
      {
        "pregunta": "¿Cuál es el resultado de 3/8 - 1/8?",
        "opciones": [
          "2/8",
          "1/4",
          "4/16",
          "2/16"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Restamos los numeradores: 3 - 1 = 2 y mantenemos el denominador 8"
      },
      {
        "pregunta": "¿Cuál es el resultado de 5/6 - 1/3?",
        "opciones": [
          "1/2",
          "4/18",
          "4/6",
          "2/9"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Usamos denominador común 6: 1/3 = 2/6, 5/6 - 2/6 = 3/6 = 1/2"
      },
      {
        "pregunta": "¿Cuál es el resultado de 7/9 - 2/3?",
        "opciones": [
          "1/9",
          "5/6",
          "5/9",
          "2/6"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Convertimos 2/3 a novenos: 2/3 = 6/9, luego 7/9 - 6/9 = 1/9"
      },
      {
        "pregunta": "¿Cuál es el resultado de 4/5 - 1/10?",
        "opciones": [
          "7/10",
          "3/5",
          "6/10",
          "5/10"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Convertimos 4/5 a décimos: 4/5 = 8/10 y 8/10 - 1/10 = 7/10"
      },
      {
        "pregunta": "¿Cuál es el resultado de 3/4 - 1/6?",
        "opciones": [
          "7/12",
          "2/24",
          "1/2",
          "5/12"
        ],
        "respuesta_correcta": 0,
        "explicacion": "El mínimo común múltiplo de 4 y 6 es 12: 3/4 = 9/12 y 1/6 = 2/12, 9/12 - 2/12 = 7/12"
      },
      {
        "pregunta": "¿Cuál es el resultado de 5/8 - 1/4?",
        "opciones": [
          "3/8",
          "1/8",
          "1/2",
          "5/16"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Llevamos 1/4 a octavos: 1/4 = 2/8 y 5/8 - 2/8 = 3/8"
      }
    ],
    "multiplicacion": [
      {
        "pregunta": "¿Cuál es el resultado de 2/3 × 1/4?",
        "opciones": [
          "2/12",
          "1/6",
          "3/7",
          "2/7"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicamos numerador por numerador (2×1=2) y denominador por denominador (3×4=12)"
      },
      {
        "pregunta": "¿Cuál es el resultado de 3/5 × 2/7?",
        "opciones": [
          "6/35",
          "5/12",
          "6/12",
          "1/35"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicamos: 3×2 = 6 (numerador), 5×7 = 35 (denominador)"
      },
      {
        "pregunta": "¿Cuál es el resultado de 1/2 × 4/5?",
        "opciones": [
          "4/10",
          "2/5",
          "5/6",
          "1/10"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicamos: 1×4 = 4 (numerador), 2×5 = 10 (denominador)"
      },
      {
        "pregunta": "¿Cuál es el resultado de 2/5 × 3/4?",
        "opciones": [
          "3/10",
          "5/9",
          "5/12",
          "6/9"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicamos numeradores 2×3 = 6 y denominadores 5×4 = 20; 6/20 se simplifica a 3/10"
      },
      {
        "pregunta": "¿Cuál es el resultado de 5/6 × 3/5?",
        "opciones": [
          "1/2",
          "2/3",
          "4/9",
          "3/5"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicamos numeradores 5×3 = 15 y denominadores 6×5 = 30; 15/30 se simplifica a 1/2"
      },
      {
        "pregunta": "¿Cuál es el resultado de 7/8 × 2/3?",
        "opciones": [
          "7/12",
          "14/24",
          "9/16",
          "5/12"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicamos numeradores 7×2 = 14 y denominadores 8×3 = 24; 14/24 se simplifica a 7/12"
      }
    ],
    "division": [
      {
        "pregunta": "¿Cuál es el resultado de 1/2 ÷ 1/3?",
        "opciones": [
          "3/2",
          "1/6",
          "2/3",
          "6/1"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicación cruzada: 1×3 = 3 (numerador), 2×1 = 2 (denominador)"
      },
      {
        "pregunta": "¿Cuál es el resultado de 2/5 ÷ 3/4?",
        "opciones": [
          "8/15",
          "6/20",
          "15/8",
          "5/12"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicación cruzada: 2×4 = 8 (numerador), 5×3 = 15 (denominador)"
      },
      {
        "pregunta": "¿Cuál es el resultado de 3/7 ÷ 2/3?",
        "opciones": [
          "9/14",
          "6/21",
          "14/9",
          "21/6"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicación cruzada: 3×3 = 9 (numerador), 7×2 = 14 (denominador)"
      },
      {
        "pregunta": "¿Cuál es el resultado de 4/5 ÷ 2/3?",
        "opciones": [
          "6/5",
          "8/15",
          "6/7",
          "10/12"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicamos 4/5 por el inverso de 2/3: 4×3 = 12 y 5×2 = 10; 12/10 se simplifica a 6/5"
      },
      {
        "pregunta": "¿Cuál es el resultado de 5/8 ÷ 1/4?",
        "opciones": [
          "5/2",
          "5/32",
          "4/5",
          "8/20"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicamos 5/8 por el inverso de 1/4: 5×4 = 20 y 8×1 = 8; 20/8 se simplifica a 5/2"
      },
      {
        "pregunta": "¿Cuál es el resultado de 7/10 ÷ 7/5?",
        "opciones": [
          "1/2",
          "14/50",
          "5/10",
          "10/7"
        ],
        "respuesta_correcta": 0,
        "explicacion": "Multiplicamos 7/10 por el inverso de 7/5: 7×5 = 35 y 10×7 = 70; 35/70 se simplifica a 1/2"
      }
    ]
  },
  "gamificacion": {
    "niveles": [
      {
        "nivel": 1,
        "nombre": "Aprendiz de Fracciones",
        "puntos_minimos": 0
      },
      {
        "nivel": 2,
        "nombre": "Explorador Matemático",
        "puntos_minimos": 100
      },
      {
        "nivel": 3,
        "nombre": "Maestro de Números",
        "puntos_minimos": 300
      },
      {
        "nivel": 4,
        "nombre": "Campeón de Fracciones",
        "puntos_minimos": 500
      }
    ],
    "logros": [
      {
        "id": "primera_suma",
        "nombre": "Primera Suma",
        "descripcion": "Completaste tu primera suma",
        "puntos": 10
      },
      {
        "id": "primera_multiplicacion",
        "nombre": "Primera Multiplicación",
        "descripcion": "Completaste tu primera multiplicación",
        "puntos": 15
      },
      {
        "id": "primera_division",
        "nombre": "Primera División",
        "descripcion": "Completaste tu primera división",
        "puntos": 20
      },
      {
        "id": "racha_5",
        "nombre": "Racha de 5",
        "descripcion": "5 respuestas seguidas correctas",
        "puntos": 50
      },
      {
        "id": "perfeccionista",
        "nombre": "Perfeccionista",
        "descripcion": "Nivel sin errores",
        "puntos": 100
      }
    ],
    "puntuacion": {
      "respuesta_correcta": 10,
      "respuesta_incorrecta": -2,
      "bonus_velocidad": 5,
      "bonus_racha": 2
    }
  }
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
    initializeSCORM();
    loadGameProgress();
    setupEventListeners();
    updateUI();
    setInterval(saveGameProgress, 10000);
});

function setupEventListeners() {
    document.querySelectorAll('.category-card').forEach(card => {
        card.addEventListener('click', function() {
            startGame(this.dataset.category);
            closeSidebarOnMobile();
        });
    });
    document.getElementById('mixed-mode-btn').addEventListener('click', () => {
        startGame('mixed');
        closeSidebarOnMobile();
    });
    document.getElementById('back-btn').addEventListener('click', returnToMenu);
    document.getElementById('next-btn').addEventListener('click', nextQuestion);
    document.getElementById('play-again-btn').addEventListener('click', () => startGame(gameState.currentCategory));
    document.getElementById('change-category-btn').addEventListener('click', returnToMenu);

    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebarOverlay = document.getElementById('sidebar-overlay');

    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', () => toggleSidebar());
    }

    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', () => toggleSidebar(false));
    }

    document.addEventListener('keydown', event => {
        if (event.key === 'Escape' && document.body.classList.contains('sidebar-open')) {
            toggleSidebar(false);
        }
    });

    window.addEventListener('resize', handleSidebarResize);
    handleSidebarResize();
}

function toggleSidebar(forceState) {
    const body = document.body;
    const isOpen = body.classList.contains('sidebar-open');
    const shouldOpen = typeof forceState === 'boolean' ? forceState : !isOpen;
    body.classList.toggle('sidebar-open', shouldOpen);

    const toggleButton = document.getElementById('sidebar-toggle');
    if (toggleButton) {
        toggleButton.setAttribute('aria-expanded', shouldOpen ? 'true' : 'false');
    }
}

function closeSidebarOnMobile() {
    if (window.innerWidth <= 1024) {
        toggleSidebar(false);
    }
}

function handleSidebarResize() {
    if (window.innerWidth > 1024) {
        toggleSidebar(false);
    }
}

function startGame(category) {
    closeSidebarOnMobile();
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

function checkAnswer(selectedIndex) {
    const question = gameState.currentQuestions[gameState.currentQuestionIndex];
    const isCorrect = selectedIndex === question.respuesta_correcta;

    document.querySelectorAll('.option-btn').forEach((btn, idx) => {
        btn.classList.add('disabled');
        if (idx === question.respuesta_correcta) btn.classList.add('correct');
        else if (idx === selectedIndex && !isCorrect) btn.classList.add('incorrect');
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

function nextQuestion() {
    gameState.currentQuestionIndex++;
    if (gameState.currentQuestionIndex < gameState.currentQuestions.length) {
        showQuestion();
    } else {
        showResults();
    }
}

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

function unlockAchievement(achievementId) {
    gameState.achievements.push(achievementId);
    const achievement = GAME_DATA.gamificacion.logros.find(a => a.id === achievementId);
    if (achievement) {
        gameState.totalPoints += achievement.puntos;
        showNotification(`¡Logro desbloqueado! ${achievement.nombre} (+${achievement.puntos} puntos)`);
    }
    updateAchievementsDisplay();
}

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

function showNotification(message) {
    const notification = document.getElementById('notification');
    const content = notification.querySelector('.notification-content');
    content.textContent = message;
    notification.classList.remove('hidden');
    setTimeout(() => notification.classList.add('hidden'), 3000);
}

function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(screen => screen.classList.remove('active'));
    document.getElementById(screenId).classList.add('active');
}

function returnToMenu() {
    clearInterval(gameState.timerInterval);
    showScreen('welcome-screen');
    closeSidebarOnMobile();
}

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

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

console.log('Aplicación de fracciones cargada correctamente');
