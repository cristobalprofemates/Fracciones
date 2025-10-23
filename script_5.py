
# Crear la segunda parte del archivo JavaScript
app_js_part2 = '''
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
    const pointsEarned = gameState.totalPoints - (loadGameProgress()?.totalPoints || 0);
    
    document.getElementById('correct-answers').textContent = correct;
    document.getElementById('incorrect-answers').textContent = incorrect;
    document.getElementById('points-earned').textContent = pointsEarned;
    document.getElementById('accuracy').textContent = accuracy + '%';
    
    // Calcular puntuación SCORM (0-100)
    const scormScore = accuracy;
    setSCORMScore(scormScore);
    
    // Establecer estado en SCORM
    if (scormScore >= 70) {
        setSCORMStatus('passed');
    } else {
        setSCORMStatus('completed');
    }
    
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
            checkAnswer(-1); // Respuesta incorrecta por tiempo
        }
    }, 1000);
}

function updateTimerDisplay() {
    document.getElementById('timer').textContent = `⏱️ ${gameState.timeRemaining}`;
}

// Actualizar nivel
function updateLevel() {
    for (let i = GAME_DATA.niveles.length - 1; i >= 0; i--) {
        if (gameState.totalPoints >= GAME_DATA.niveles[i].puntos_minimos) {
            if (gameState.currentLevel !== GAME_DATA.niveles[i].nivel) {
                gameState.currentLevel = GAME_DATA.niveles[i].nivel;
                showNotification(`¡Subiste a nivel ${gameState.currentLevel}!`);
            }
            break;
        }
    }
}

// Verificar logros
function checkAchievements(question) {
    // Primera suma
    if (question.pregunta.includes('+') && !gameState.achievements.includes('primera_suma')) {
        unlockAchievement('primera_suma');
    }
    
    // Primera multiplicación
    if (question.pregunta.includes('×') && !gameState.achievements.includes('primera_multiplicacion')) {
        unlockAchievement('primera_multiplicacion');
    }
    
    // Primera división
    if (question.pregunta.includes('÷') && !gameState.achievements.includes('primera_division')) {
        unlockAchievement('primera_division');
    }
    
    // Racha de 5
    if (gameState.streak === 5 && !gameState.achievements.includes('racha_5')) {
        unlockAchievement('racha_5');
    }
    
    // Perfeccionista
    if (gameState.incorrectAnswers === 0 && 
        gameState.currentQuestionIndex === gameState.currentQuestions.length - 1 &&
        !gameState.achievements.includes('perfeccionista')) {
        unlockAchievement('perfeccionista');
    }
}

// Desbloquear logro
function unlockAchievement(achievementId) {
    gameState.achievements.push(achievementId);
    const achievement = GAME_DATA.logros.find(a => a.id === achievementId);
    
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
    
    GAME_DATA.logros.forEach(logro => {
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
    
    const currentLevelData = GAME_DATA.niveles.find(n => n.nivel === gameState.currentLevel);
    const nextLevelData = GAME_DATA.niveles.find(n => n.nivel === gameState.currentLevel + 1);
    
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
    
    setTimeout(() => {
        notification.classList.add('hidden');
    }, 3000);
}

// Cambiar pantalla
function showScreen(screenId) {
    document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
    });
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
    
    // También actualizar la puntuación en tiempo real
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

# Combinar ambas partes
with open('app_js_temp.txt', 'r', encoding='utf-8') as f:
    part1 = f.read()

full_app_js = part1 + app_js_part2

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(full_app_js)

print("✓ app.js completo creado")
print("\n=== ARCHIVOS DEL PAQUETE SCORM CREADOS ===")
print("1. imsmanifest.xml - Manifiesto SCORM")
print("2. scorm-api.js - API de comunicación con Moodle")
print("3. app.js - Lógica del juego")
print("4. index.html - Interfaz principal")
print("5. styles.css - Estilos visuales")
