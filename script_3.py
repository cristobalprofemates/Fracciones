
# Crear el archivo CSS con estilos atractivos
styles_css = '''/* Estilos para el Juego de Fracciones SCORM */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #333;
    overflow-x: hidden;
}

#app-container {
    display: flex;
    min-height: 100vh;
}

/* Sidebar */
#sidebar {
    width: 280px;
    background: white;
    box-shadow: 2px 0 10px rgba(0,0,0,0.1);
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.logo h2 {
    color: #667eea;
    text-align: center;
    font-size: 24px;
    margin-bottom: 10px;
}

.stats {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.stat-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px;
    background: #f8f9fa;
    border-radius: 8px;
}

.stat-label {
    font-size: 14px;
    color: #666;
    font-weight: 500;
}

.stat-value {
    font-size: 24px;
    font-weight: bold;
    color: #667eea;
}

.progress-container {
    margin-top: 10px;
}

.progress-label {
    font-size: 14px;
    font-weight: 600;
    color: #333;
    margin-bottom: 8px;
}

.progress-bar {
    width: 100%;
    height: 20px;
    background: #e0e0e0;
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 5px;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    transition: width 0.5s ease;
    width: 0%;
}

.progress-text {
    font-size: 12px;
    color: #666;
    text-align: center;
}

.achievements {
    margin-top: 10px;
}

.achievements h3 {
    font-size: 16px;
    margin-bottom: 10px;
    color: #333;
}

#achievements-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.achievement-item {
    padding: 10px;
    background: #f0f0f0;
    border-radius: 6px;
    font-size: 13px;
    opacity: 0.5;
}

.achievement-item.unlocked {
    background: linear-gradient(135deg, #ffd89b 0%, #19547b 100%);
    color: white;
    opacity: 1;
    animation: unlockAchievement 0.5s ease;
}

@keyframes unlockAchievement {
    0% { transform: scale(0.8); opacity: 0; }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); opacity: 1; }
}

/* Main Content */
#main-content {
    flex: 1;
    padding: 40px;
    overflow-y: auto;
}

.screen {
    display: none;
    animation: fadeIn 0.5s ease;
}

.screen.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Welcome Screen */
#welcome-screen h1 {
    color: white;
    text-align: center;
    font-size: 48px;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.subtitle {
    color: white;
    text-align: center;
    font-size: 20px;
    margin-bottom: 40px;
    opacity: 0.9;
}

.categories {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.category-card {
    background: white;
    border-radius: 15px;
    padding: 30px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.category-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.2);
}

.category-icon {
    font-size: 64px;
    margin-bottom: 15px;
}

.category-card h3 {
    color: #333;
    font-size: 20px;
    margin-bottom: 5px;
}

.category-card p {
    color: #666;
    font-size: 14px;
}

/* Game Screen */
.game-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}

.timer {
    background: white;
    padding: 10px 20px;
    border-radius: 25px;
    font-size: 20px;
    font-weight: bold;
    color: #667eea;
}

.timer.warning {
    background: #ff6b6b;
    color: white;
    animation: pulse 1s infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}

.question-counter {
    background: white;
    padding: 10px 20px;
    border-radius: 25px;
    font-size: 16px;
    color: #666;
}

.question-container {
    background: white;
    border-radius: 20px;
    padding: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

#question-text {
    font-size: 32px;
    color: #333;
    text-align: center;
    margin-bottom: 40px;
}

.options {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin-bottom: 20px;
}

.option-btn {
    background: #f8f9fa;
    border: 3px solid transparent;
    border-radius: 15px;
    padding: 30px;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
    color: #333;
}

.option-btn:hover:not(.disabled) {
    background: #e9ecef;
    border-color: #667eea;
    transform: scale(1.05);
}

.option-btn.correct {
    background: #51cf66;
    color: white;
    border-color: #51cf66;
    animation: correctAnswer 0.5s ease;
}

.option-btn.incorrect {
    background: #ff6b6b;
    color: white;
    border-color: #ff6b6b;
    animation: shake 0.5s ease;
}

.option-btn.disabled {
    cursor: not-allowed;
    opacity: 0.6;
}

@keyframes correctAnswer {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-10px); }
    75% { transform: translateX(10px); }
}

.feedback {
    margin-top: 30px;
    text-align: center;
}

.feedback.hidden {
    display: none;
}

.feedback-icon {
    font-size: 64px;
    margin-bottom: 15px;
}

.feedback-text {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 15px;
}

.feedback-explanation {
    font-size: 16px;
    color: #666;
    margin-bottom: 20px;
    padding: 15px;
    background: #f8f9fa;
    border-radius: 10px;
}

/* Results Screen */
#results-screen h1 {
    color: white;
    text-align: center;
    font-size: 48px;
    margin-bottom: 30px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.results-summary {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.result-card {
    background: white;
    border-radius: 15px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.result-icon {
    font-size: 48px;
    margin-bottom: 10px;
}

.result-label {
    font-size: 14px;
    color: #666;
    margin-bottom: 10px;
}

.result-value {
    font-size: 36px;
    font-weight: bold;
    color: #667eea;
}

.new-achievements {
    background: white;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 20px;
}

.results-buttons {
    display: flex;
    gap: 20px;
    justify-content: center;
}

/* Buttons */
.btn {
    padding: 15px 30px;
    border: none;
    border-radius: 25px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
    background: white;
    color: #667eea;
    border: 2px solid #667eea;
}

.btn-secondary:hover {
    background: #667eea;
    color: white;
}

#mixed-mode-btn {
    display: block;
    margin: 0 auto;
    font-size: 20px;
}

/* Notification */
.notification {
    position: fixed;
    top: 20px;
    right: 20px;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.3);
    z-index: 1000;
    animation: slideIn 0.3s ease;
}

.notification.hidden {
    display: none;
}

@keyframes slideIn {
    from { transform: translateX(400px); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}

.notification-content {
    font-size: 16px;
    color: #333;
}

/* Responsive */
@media (max-width: 768px) {
    #app-container {
        flex-direction: column;
    }
    
    #sidebar {
        width: 100%;
    }
    
    .categories {
        grid-template-columns: 1fr;
    }
    
    .options {
        grid-template-columns: 1fr;
    }
    
    #question-text {
        font-size: 24px;
    }
}'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(styles_css)

print("✓ styles.css creado")
