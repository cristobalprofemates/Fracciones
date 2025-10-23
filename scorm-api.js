// SCORM 1.2 API Implementation
var API = null;
var apiHandle = null;
var findAPITries = 0;

// Función para encontrar el API de SCORM
function findAPI(win) {
    findAPITries++;
    if (findAPITries > 500) {
        console.error("Error al encontrar API - Demasiados intentos");
        return null;
    }

    // Buscar en la ventana actual
    if (win.API != null) {
        return win.API;
    } 
    // Buscar en el padre
    else if (win.parent != null && win.parent != win) {
        return findAPI(win.parent);
    }
    // Buscar en el opener
    else if (win.opener != null && typeof(win.opener) != "undefined") {
        return findAPI(win.opener);
    }

    return null;
}

// Inicializar SCORM API
function initializeSCORM() {
    apiHandle = findAPI(window);

    if (apiHandle == null) {
        console.warn("No se encontró API SCORM - Modo de prueba activado");
        // Crear API simulada para pruebas locales
        createMockAPI();
        return false;
    }

    var result = apiHandle.LMSInitialize("");

    if (result == "true") {
        // Establecer valores iniciales
        var lessonStatus = apiHandle.LMSGetValue("cmi.core.lesson_status");

        if (lessonStatus == "not attempted") {
            apiHandle.LMSSetValue("cmi.core.lesson_status", "incomplete");
        }

        console.log("SCORM inicializado correctamente");
        return true;
    } else {
        console.error("Error al inicializar SCORM");
        return false;
    }
}

// Finalizar SCORM
function finalizeSCORM() {
    if (apiHandle != null) {
        apiHandle.LMSFinish("");
    }
}

// Establecer valor en SCORM
function setSCORMValue(element, value) {
    if (apiHandle != null) {
        return apiHandle.LMSSetValue(element, value);
    }
    return "false";
}

// Obtener valor de SCORM
function getSCORMValue(element) {
    if (apiHandle != null) {
        return apiHandle.LMSGetValue(element);
    }
    return "";
}

// Commit datos a SCORM
function commitSCORM() {
    if (apiHandle != null) {
        return apiHandle.LMSCommit("");
    }
    return "false";
}

// Establecer puntuación
function setSCORMScore(score) {
    // Score debe estar entre 0 y 100
    score = Math.max(0, Math.min(100, score));
    setSCORMValue("cmi.core.score.raw", score);
    setSCORMValue("cmi.core.score.min", "0");
    setSCORMValue("cmi.core.score.max", "100");
    commitSCORM();
}

// Establecer estado de finalización
function setSCORMStatus(status) {
    // status puede ser: "passed", "completed", "failed", "incomplete", "browsed", "not attempted"
    setSCORMValue("cmi.core.lesson_status", status);
    commitSCORM();
}

// Guardar datos de suspensión (progreso del estudiante)
function saveSuspendData(data) {
    var jsonData = JSON.stringify(data);
    setSCORMValue("cmi.suspend_data", jsonData);
    commitSCORM();
}

// Recuperar datos de suspensión
function loadSuspendData() {
    var jsonData = getSCORMValue("cmi.suspend_data");
    if (jsonData && jsonData !== "") {
        try {
            return JSON.parse(jsonData);
        } catch (e) {
            console.error("Error al parsear suspend_data", e);
            return null;
        }
    }
    return null;
}

// API simulada para pruebas locales
function createMockAPI() {
    var mockData = {
        "cmi.core.lesson_status": "not attempted",
        "cmi.core.score.raw": "",
        "cmi.suspend_data": ""
    };

    apiHandle = {
        LMSInitialize: function(param) {
            console.log("Mock API: LMSInitialize");
            return "true";
        },
        LMSFinish: function(param) {
            console.log("Mock API: LMSFinish");
            return "true";
        },
        LMSGetValue: function(element) {
            console.log("Mock API: LMSGetValue -", element, ":", mockData[element]);
            return mockData[element] || "";
        },
        LMSSetValue: function(element, value) {
            console.log("Mock API: LMSSetValue -", element, ":", value);
            mockData[element] = value;
            return "true";
        },
        LMSCommit: function(param) {
            console.log("Mock API: LMSCommit -", mockData);
            return "true";
        },
        LMSGetLastError: function() {
            return "0";
        },
        LMSGetErrorString: function(errorCode) {
            return "No error";
        },
        LMSGetDiagnostic: function(errorCode) {
            return "";
        }
    };
}

// Evento de descarga de página - finalizar SCORM
window.addEventListener('beforeunload', function(e) {
    finalizeSCORM();
});
