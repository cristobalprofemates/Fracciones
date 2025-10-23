
# Crear guía de implementación y uso
guia_implementacion = '''# GUÍA DE IMPLEMENTACIÓN DEL PAQUETE SCORM
# Juego Gamificado de Operaciones con Fracciones

## 1. ARCHIVOS INCLUIDOS EN EL PAQUETE

- imsmanifest.xml: Define la estructura del paquete SCORM
- scorm-api.js: Gestiona la comunicación con Moodle
- app.js: Contiene toda la lógica del juego
- index.html: Interfaz principal del usuario
- styles.css: Estilos y animaciones

## 2. CÓMO CREAR EL PAQUETE .ZIP

Paso 1: Reunir todos los archivos en una carpeta
Paso 2: Seleccionar TODOS los archivos (no la carpeta)
Paso 3: Comprimir en formato .zip
Paso 4: Nombrar el archivo: fracciones-scorm.zip

IMPORTANTE: Los archivos deben estar en la raíz del .zip, 
no dentro de una subcarpeta.

## 3. CÓMO SUBIR A MOODLE

1. Acceder a tu curso en Moodle
2. Activar modo de edición
3. Hacer clic en "Añadir una actividad o recurso"
4. Seleccionar "Paquete SCORM"
5. Completar los campos:
   - Nombre: "Juego de Operaciones con Fracciones"
   - Descripción: Breve descripción del juego
6. En "Archivo del paquete", subir fracciones-scorm.zip
7. Configurar opciones de calificación:
   - Método de calificación: Calificación más alta
   - Calificación máxima: 100
8. En "Finalización de actividad":
   - Requerir calificación: Sí
   - Puntuación mínima requerida: 70 (para aprobar)
9. Guardar y mostrar

## 4. CARACTERÍSTICAS DEL JUEGO

### Sistema de Gamificación:
- 4 niveles progresivos
- Sistema de puntos con bonificaciones
- 5 logros desbloqueables
- Racha de respuestas correctas
- Barra de progreso visual

### Tipos de Operaciones:
1. Suma/Resta con mismo denominador
2. Suma/Resta con diferente denominador (método mariposa)
3. Multiplicación de fracciones
4. División de fracciones
5. Modo mixto (todas las operaciones)

### Mecánicas de Juego:
- 10 preguntas por sesión
- Timer de 30 segundos por pregunta
- Feedback inmediato con explicaciones
- Puntuación: +10 base, +5 bonus velocidad, +2 bonus racha
- Penalización: -2 por respuesta incorrecta

## 5. TRACKING EN MOODLE

El paquete SCORM envía a Moodle:
- cmi.core.score.raw: Puntuación de 0-100
- cmi.core.lesson_status: "passed" (≥70%) o "completed" (<70%)
- cmi.suspend_data: Progreso del estudiante (puntos, nivel, logros)
- cmi.core.session_time: Tiempo invertido

## 6. INFORMACIÓN PARA ESTUDIANTES

Los estudiantes verán:
- Puntuación total acumulada
- Nivel actual y progreso
- Racha de respuestas correctas
- Logros desbloqueados
- Estadísticas por sesión
- Explicaciones detalladas de cada respuesta

El progreso se guarda automáticamente cada 10 segundos
y cuando el estudiante cambia de pregunta.

## 7. PRUEBAS RECOMENDADAS

Antes de usar con estudiantes, probar:
1. Subir el paquete a Moodle
2. Completar una sesión de prueba
3. Verificar que se registra la puntuación
4. Cerrar y volver a abrir (verificar que se mantiene el progreso)
5. Probar desde diferentes dispositivos (PC, tablet, móvil)

## 8. SOLUCIÓN DE PROBLEMAS

Problema: No se registra la puntuación en Moodle
Solución: Verificar que el archivo imsmanifest.xml está en la raíz del .zip

Problema: El juego no carga
Solución: Limpiar caché del navegador o probar en modo incógnito

Problema: No se guarda el progreso
Solución: Verificar que las configuraciones de SCORM en Moodle 
permiten el guardado de datos (cmi.suspend_data)

## 9. PERSONALIZACIÓN

Para modificar preguntas, editar el archivo app.js en la sección GAME_DATA
Para cambiar estilos, editar styles.css
Para modificar la lógica de puntuación, editar las funciones en app.js

## 10. REQUISITOS TÉCNICOS

- Navegadores soportados: Chrome, Firefox, Safari, Edge (últimas versiones)
- Moodle 3.x o superior
- JavaScript debe estar habilitado
- Conexión a internet para subir el paquete
- El paquete funciona offline una vez cargado
'''

with open('GUIA_IMPLEMENTACION.txt', 'w', encoding='utf-8') as f:
    f.write(guia_implementacion)

print("✓ Guía de implementación creada\n")
print("=== 📚 DOCUMENTACIÓN COMPLETA ===\n")
print("Se ha creado la guía completa de implementación")
print("que explica paso a paso cómo usar el paquete SCORM")
