const test = require('node:test');
const assert = require('node:assert');
const { execSync } = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

const rootDir = path.resolve(__dirname, '..');
const appPath = path.join(rootDir, 'app.js');

test('app.js compila correctamente', () => {
  assert.doesNotThrow(() => {
    execSync(`node --check "${appPath}"`, { stdio: 'pipe' });
  }, 'El archivo app.js debería ser válido para Node.js');
});

test('El temporizador está configurado a 60 segundos', () => {
  const source = fs.readFileSync(appPath, 'utf8');
  assert.match(
    source,
    /timeRemaining\s*:\s*60/,
    'El estado inicial debe fijar el temporizador en 60 segundos'
  );
  assert.match(
    source,
    /gameState\.timeRemaining\s*=\s*60;/,
    'La función resetTimer debe reiniciar el temporizador a 60 segundos'
  );
});
