import pandas as pd

# Datos de prevalencia por país
prevalencia_pais = {
    "Argentina": {"general": 0.015, "niños": 0.012, "niñas": 0.003},
    "Bolivia": {"general": 0.011, "niños": 0.009, "niñas": 0.002},
    "Brasil": {"general": 0.0135, "niños": 0.011, "niñas": 0.0025},
    "Chile": {"general": 0.016, "niños": 0.013, "niñas": 0.003},
    "Haití": {"general": 0.0122, "niños": 0.01, "niñas": 0.0022},
    "Colombia": {"general": 0.012, "niños": 0.01, "niñas": 0.0024},
    "Costa Rica": {"general": 0.0139, "niños": 0.011, "niñas": 0.0028},
    "Cuba": {"general": 0.0172, "niños": 0.014, "niñas": 0.0032},
    "Ecuador": {"general": 0.0123, "niños": 0.01, "niñas": 0.0023},
    "El Salvador": {"general": 0.01, "niños": 0.008, "niñas": 0.002},
    "Guatemala": {"general": 0.0105, "niños": 0.0085, "niñas": 0.0021},
    "Honduras": {"general": 0.0093, "niños": 0.0075, "niñas": 0.0018},
    "México": {"general": 0.0141, "niños": 0.012, "niñas": 0.0029},
    "Nicaragua": {"general": 0.0097, "niños": 0.008, "niñas": 0.0019},
    "Panamá": {"general": 0.0125, "niños": 0.01, "niñas": 0.0025},
    "Paraguay": {"general": 0.0112, "niños": 0.009, "niñas": 0.0022},
    "Perú": {"general": 0.0137, "niños": 0.011, "niñas": 0.0027},
    "República Dominicana": {"general": 0.015, "niños": 0.012, "niñas": 0.003},
    "Uruguay": {"general": 0.014, "niños": 0.01, "niñas": 0.0024},
    "Venezuela": {"general": 0.0138, "niños": 0.011, "niñas": 0.0028},
    "Puerto Rico": {"general": 0.0163, "niños": 0.013, "niñas": 0.0033}
}

# Datos de prevalencia por país según antecedentes familiares de autismo
prevalencia_antecedentes_familiares = {
    "Argentina": {"con_antecedentes": 0.204, "sin_antecedentes": 0.01},
    "Brasil": {"con_antecedentes": 0.212, "sin_antecedentes": 0.011},
    "Chile": {"con_antecedentes": 0.198, "sin_antecedentes": 0.009},
    "Colombia": {"con_antecedentes": 0.22, "sin_antecedentes": 0.012},
    "Costa Rica": {"con_antecedentes": 0.201, "sin_antecedentes": 0.009},
    "Cuba": {"con_antecedentes": 0.21, "sin_antecedentes": 0.01},
    "Ecuador": {"con_antecedentes": 0.205, "sin_antecedentes": 0.01},
    "El Salvador": {"con_antecedentes": 0.199, "sin_antecedentes": 0.009},
    "Guatemala": {"con_antecedentes": 0.203, "sin_antecedentes": 0.01},
    "Haití": {"con_antecedentes": 0.195, "sin_antecedentes": 0.009},
    "Honduras": {"con_antecedentes": 0.207, "sin_antecedentes": 0.01},
    "México": {"con_antecedentes": 0.211, "sin_antecedentes": 0.011},
    "Nicaragua": {"con_antecedentes": 0.2, "sin_antecedentes": 0.009},
    "Panamá": {"con_antecedentes": 0.206, "sin_antecedentes": 0.01},
    "Paraguay": {"con_antecedentes": 0.202, "sin_antecedentes": 0.009},
    "Perú": {"con_antecedentes": 0.21, "sin_antecedentes": 0.011},
    "República Dominicana": {"con_antecedentes": 0.205, "sin_antecedentes": 0.01},
    "Uruguay": {"con_antecedentes": 0.203, "sin_antecedentes": 0.009},
    "Venezuela": {"con_antecedentes": 0.211, "sin_antecedentes": 0.011}
}

# Base de datos para ajustar la probabilidad según la presencia de infecciones maternas
ajuste_infecciones_maternas = {
    "Argentina": 0.012,
    "Brasil": 0.013,
    "Chile": 0.011,
    "Colombia": 0.014,
    "Costa Rica": 0.012,
    "Cuba": 0.013,
    "Ecuador": 0.011,
    "El Salvador": 0.011,
    "Guatemala": 0.012,
    "Haití": 0.011,
    "Honduras": 0.012,
    "México": 0.013,
    "Nicaragua": 0.011,
    "Panamá": 0.012,
    "Paraguay": 0.011,
    "Perú": 0.013,
    "República Dominicana": 0.012,
    "Uruguay": 0.012,
    "Venezuela": 0.013
}

# Base de datos de prevalencia de TEA en nacidos prematuramente por país
Prevalencia_Prematuramente = {
    "Argentina": 0.03,
    "Bolivia": 0.028,
    "Brasil": 0.032,
    "Chile": 0.028,
    "Haití": 0.028,
    "Colombia": 0.034,
    "Costa Rica": 0.029,
    "Cuba": 0.031,
    "Ecuador": 0.03,
    "El Salvador": 0.029,
    "Guatemala": 0.03,
    "Honduras": 0.032,
    "México": 0.031,
    "Nicaragua": 0.029,
    "Panamá": 0.03,
    "Paraguay": 0.029,
    "Perú": 0.032,
    "República Dominicana": 0.031,
    "Uruguay": 0.029,
    "Venezuela": 0.033,
    "Puerto Rico": 0.028
}

# Base de datos de prevalencia de hipoxia por país
Prevalencia_Hipoxia = {
    "Argentina": {"niños": 0.0139, "niñas": 0.0035},
    "Bolivia": {"niños": 0.0104, "niñas": 0.0023},
    "Brasil": {"niños": 0.0127, "niñas": 0.0029},
    "Chile": {"niños": 0.015, "niñas": 0.0035},
    "Haití": {"niños": 0.0116, "niñas": 0.0025},
    "Colombia": {"niños": 0.0116, "niñas": 0.0028},
    "Costa Rica": {"niños": 0.0127, "niñas": 0.0032},
    "Cuba": {"niños": 0.0162, "niñas": 0.0037},
    "Ecuador": {"niños": 0.0116, "niñas": 0.0027},
    "El Salvador": {"niños": 0.0093, "niñas": 0.0023},
    "Guatemala": {"niños": 0.0098, "niñas": 0.0024},
    "Honduras": {"niños": 0.0087, "niñas": 0.0021},
    "México": {"niños": 0.0139, "niñas": 0.0034},
    "Nicaragua": {"niños": 0.0093, "niñas": 0.0022},
    "Panamá": {"niños": 0.0116, "niñas": 0.0029},
    "Paraguay": {"niños": 0.0104, "niñas": 0.0026},
    "Perú": {"niños": 0.0127, "niñas": 0.0031},
    "República Dominicana": {"niños": 0.0139, "niñas": 0.0035},
    "Uruguay": {"niños": 0.0116, "niñas": 0.0029},
    "Venezuela": {"niños": 0.0127, "niñas": 0.0032},
    "Puerto Rico": {"niños": 0.015, "niñas": 0.0036}
}

# Base de datos de prevalencia de caminar en puntas de pie
prevalencia_camina_puntas_pie = {
    "Argentina": 0.35,
    "Bolivia": 0.35,
    "Brasil": 0.35,
    "Chile": 0.35,
    "Haití": 0.35,
    "Colombia": 0.35,
    "Costa Rica": 0.35,
    "Cuba": 0.35,
    "Ecuador": 0.35,
    "El Salvador": 0.35,
    "Guatemala": 0.35,
    "Honduras": 0.35,
    "México": 0.35,
    "Nicaragua": 0.35,
    "Panamá": 0.35,
    "Paraguay": 0.35,
    "Perú": 0.35,
    "República Dominicana": 0.35,
    "Uruguay": 0.35,
    "Venezuela": 0.35,
    "Puerto Rico": 0.35
}

# Base de datos de prevalencia de retraso en lenguaje
Prevalencia_Retraso_Lenguaje = {
    "Argentina": {"Incidencia en Niños": 1.0, "Incidencia en Niñas": 0.2},
    "Bolivia": {"Incidencia en Niños": 0.9, "Incidencia en Niñas": 0.2},
    "Brasil": {"Incidencia en Niños": 1.1, "Incidencia en Niñas": 0.3},
    "Chile": {"Incidencia en Niños": 0.9, "Incidencia en Niñas": 0.2},
    "Haití": {"Incidencia en Niños": 0.9, "Incidencia en Niñas": 0.2},
    "Colombia": {"Incidencia en Niños": 1.1, "Incidencia en Niñas": 0.3},
    "Costa Rica": {"Incidencia en Niños": 0.9, "Incidencia en Niñas": 0.2},
    "Cuba": {"Incidencia en Niños": 1.0, "Incidencia en Niñas": 0.3},
    "Ecuador": {"Incidencia en Niños": 1.0, "Incidencia en Niñas": 0.2},
    "El Salvador": {"Incidencia en Niños": 0.9, "Incidencia en Niñas": 0.2},
    "Guatemala": {"Incidencia en Niños": 1.0, "Incidencia en Niñas": 0.2},
    "Honduras": {"Incidencia en Niños": 1.0, "Incidencia en Niñas": 0.2},
    "México": {"Incidencia en Niños": 1.1, "Incidencia en Niñas": 0.3},
    "Nicaragua": {"Incidencia en Niños": 0.9, "Incidencia en Niñas": 0.2},
    "Panamá": {"Incidencia en Niños": 1.0, "Incidencia en Niñas": 0.2},
    "Paraguay": {"Incidencia en Niños": 0.9, "Incidencia en Niñas": 0.2},
    "Perú": {"Incidencia en Niños": 1.0, "Incidencia en Niñas": 0.3},
    "República Dominicana": {"Incidencia en Niños": 1.0, "Incidencia en Niñas": 0.2},
    "Uruguay": {"Incidencia en Niños": 0.9, "Incidencia en Niñas": 0.2},
    "Venezuela": {"Incidencia en Niños": 1.0, "Incidencia en Niñas": 0.3},
    "Puerto Rico": {"Incidencia en Niños": 1.1, "Incidencia en Niñas": 0.4}
}

# Base de datos de prevalencia de dificultades en el contacto visual
Prevalencia_Contacto_Visual = {
    "Argentina": {"Niños con dificultades en el contacto visual": 0.80, "Niñas con dificultades en el contacto visual": 0.70},
    "Bolivia": {"Niños con dificultades en el contacto visual": 0.75, "Niñas con dificultades en el contacto visual": 0.65},
    "Brasil": {"Niños con dificultades en el contacto visual": 0.82, "Niñas con dificultades en el contacto visual": 0.72},
    "Chile": {"Niños con dificultades en el contacto visual": 0.79, "Niñas con dificultades en el contacto visual": 0.68},
    "Haití": {"Niños con dificultades en el contacto visual": 0.78, "Niñas con dificultades en el contacto visual": 0.68},
    "Colombia": {"Niños con dificultades en el contacto visual": 0.81, "Niñas con dificultades en el contacto visual": 0.71},
    "Costa Rica": {"Niños con dificultades en el contacto visual": 0.80, "Niñas con dificultades en el contacto visual": 0.70},
    "Cuba": {"Niños con dificultades en el contacto visual": 0.83, "Niñas con dificultades en el contacto visual": 0.73},
    "Ecuador": {"Niños con dificultades en el contacto visual": 0.80, "Niñas con dificultades en el contacto visual": 0.70},
    "El Salvador": {"Niños con dificultades en el contacto visual": 0.79, "Niñas con dificultades en el contacto visual": 0.69},
    "Guatemala": {"Niños con dificultades en el contacto visual": 0.81, "Niñas con dificultades en el contacto visual": 0.71},
    "Honduras": {"Niños con dificultades en el contacto visual": 0.82, "Niñas con dificultades en el contacto visual": 0.72},
    "México": {"Niños con dificultades en el contacto visual": 0.81, "Niñas con dificultades en el contacto visual": 0.71},
    "Nicaragua": {"Niños con dificultades en el contacto visual": 0.80, "Niñas con dificultades en el contacto visual": 0.70},
    "Panamá": {"Niños con dificultades en el contacto visual": 0.79, "Niñas con dificultades en el contacto visual": 0.69},
    "Paraguay": {"Niños con dificultades en el contacto visual": 0.80, "Niñas con dificultades en el contacto visual": 0.70},
    "Perú": {"Niños con dificultades en el contacto visual": 0.82, "Niñas con dificultades en el contacto visual": 0.72},
    "República Dominicana": {"Niños con dificultades en el contacto visual": 0.81, "Niñas con dificultades en el contacto visual": 0.71},
    "Uruguay": {"Niños con dificultades en el contacto visual": 0.80, "Niñas con dificultades en el contacto visual": 0.70},
    "Venezuela": {"Niños con dificultades en el contacto visual": 0.83, "Niñas con dificultades en el contacto visual": 0.73},
    "Puerto Rico": {"Niños con dificultades en el contacto visual": 0.77, "Niñas con dificultades en el contacto visual": 0.67}
}

# Datos con prevalencias de comportamientos repetitivos en niños y niñas
prevalencia_comportamientos_repetitivos = {
    "Argentina": {"prevalencia_niños": 0.533, "prevalencia_niñas": 0.117},
    "Brasil": {"prevalencia_niños": 0.508, "prevalencia_niñas": 0.121},
    "Chile": {"prevalencia_niños": 0.573, "prevalencia_niñas": 0.130},
    "Colombia": {"prevalencia_niños": 0.480, "prevalencia_niñas": 0.120},
    "Cuba": {"prevalencia_niños": 0.475, "prevalencia_niñas": 0.125},
    "Ecuador": {"prevalencia_niños": 0.550, "prevalencia_niñas": 0.119},
    "El Salvador": {"prevalencia_niños": 0.496, "prevalencia_niñas": 0.124},
    "Guatemala": {"prevalencia_niños": 0.516, "prevalencia_niñas": 0.123},
    "Haití": {"prevalencia_niños": 0.456, "prevalencia_niñas": 0.125},
    "Honduras": {"prevalencia_niños": 0.537, "prevalencia_niñas": 0.124},
    "México": {"prevalencia_niños": 0.508, "prevalencia_niñas": 0.121},
    "Nicaragua": {"prevalencia_niños": 0.480, "prevalencia_niñas": 0.120},
    "Panamá": {"prevalencia_niños": 0.533, "prevalencia_niñas": 0.117},
    "Paraguay": {"prevalencia_niños": 0.516, "prevalencia_niñas": 0.123},
    "Perú": {"prevalencia_niños": 0.512, "prevalencia_niñas": 0.128},
    "Costa Rica": {"prevalencia_niños": 0.516, "prevalencia_niñas": 0.123},
    "República Dominicana": {"prevalencia_niños": 0.529, "prevalencia_niñas": 0.126},
    "Uruguay": {"prevalencia_niños": 0.500, "prevalencia_niñas": 0.122},
    "Venezuela": {"prevalencia_niños": 0.620, "prevalencia_niñas": 0.127},  
}

# Base de datos de prevalencia de sensibilidad sensorial por país y género
prevalencia_sensibilidad_sensorial = {
    "Argentina": {
        "prevalencia_niños": 0.75,
        "prevalencia_niñas": 0.25
    },
    "Brasil": {
        "prevalencia_niños": 0.80,
        "prevalencia_niñas": 0.20
    },
    "Chile": {
        "prevalencia_niños": 0.778,
        "prevalencia_niñas": 0.222
    },
    "Colombia": {
        "prevalencia_niños": 0.792,
        "prevalencia_niñas": 0.208
    },
    "Cuba": {
        "prevalencia_niños": 0.787,
        "prevalencia_niñas": 0.213
    },
    "Ecuador": {
        "prevalencia_niños": 0.795,
        "prevalencia_niñas": 0.205
    },
    "El Salvador": {
        "prevalencia_niños": 0.783,
        "prevalencia_niñas": 0.217
    },
    "Guatemala": {
        "prevalencia_niños": 0.795,
        "prevalencia_niñas": 0.205
    },
    "Haití": {
        "prevalencia_niños": 0.778,
        "prevalencia_niñas": 0.222
    },
    "Honduras": {
        "prevalencia_niños": 0.792,
        "prevalencia_niñas": 0.208
    },
    "México": {
        "prevalencia_niños": 0.795,
        "prevalencia_niñas": 0.205
    },
    "Nicaragua": {
        "prevalencia_niños": 0.787,
        "prevalencia_niñas": 0.213
    },
    "Panamá": {
        "prevalencia_niños": 0.80,
        "prevalencia_niñas": 0.20
    },
    "Paraguay": {
        "prevalencia_niños": 0.783,
        "prevalencia_niñas": 0.217
    },
    "Perú": {
        "prevalencia_niños": 0.792,
        "prevalencia_niñas": 0.208
    },
    "Costa Rica": {
        "prevalencia_niños": 0.80,
        "prevalencia_niñas": 0.20
    },
    "República Dominicana": {
        "prevalencia_niños": 0.795,
        "prevalencia_niñas": 0.205
    },
    "Uruguay": {
        "prevalencia_niños": 0.787,
        "prevalencia_niñas": 0.213
    },
    "Venezuela": {
        "prevalencia_niños": 0.792,
        "prevalencia_niñas": 0.208
    }
}

# Datos de incidencia de intereses restringidos
incidencia_intereses_restringidos = {
    "Argentina": {"incidencia_niños": 0.60, "incidencia_niñas": 0.40},
    "Brasil": {"incidencia_niños": 0.55, "incidencia_niñas": 0.45},
    "Chile": {"incidencia_niños": 0.58, "incidencia_niñas": 0.42},
    "Colombia": {"incidencia_niños": 0.62, "incidencia_niñas": 0.38},
    "Costa Rica": {"incidencia_niños": 0.56, "incidencia_niñas": 0.44},
    "Cuba": {"incidencia_niños": 0.59, "incidencia_niñas": 0.41},
    "Ecuador": {"incidencia_niños": 0.61, "incidencia_niñas": 0.39},
    "El Salvador": {"incidencia_niños": 0.57, "incidencia_niñas": 0.43},
    "Guatemala": {"incidencia_niños": 0.60, "incidencia_niñas": 0.40},
    "Haití": {"incidencia_niños": 0.55, "incidencia_niñas": 0.45},
    "Honduras": {"incidencia_niños": 0.58, "incidencia_niñas": 0.42},
    "México": {"incidencia_niños": 0.63, "incidencia_niñas": 0.37},
    "Nicaragua": {"incidencia_niños": 0.56, "incidencia_niñas": 0.44},
    "Panamá": {"incidencia_niños": 0.59, "incidencia_niñas": 0.41},
    "Paraguay": {"incidencia_niños": 0.57, "incidencia_niñas": 0.43},
    "Perú": {"incidencia_niños": 0.64, "incidencia_niñas": 0.36},
    "República Dominicana": {"incidencia_niños": 0.60, "incidencia_niñas": 0.40},
    "Uruguay": {"incidencia_niños": 0.58, "incidencia_niñas": 0.42},
    "Venezuela": {"incidencia_niños": 0.65, "incidencia_niñas": 0.35},
}

# Base de datos de prevalencia de dificultades sociales
prevalencia_dificultades_sociales = {
    "Argentina": {
        "con_historial_dificultades_sociales": 0.015,
        "sin_historial_dificultades_sociales": 0.011
    },
    "Brasil": {
        "con_historial_dificultades_sociales": 0.016,
        "sin_historial_dificultades_sociales": 0.012
    },
    "Chile": {
        "con_historial_dificultades_sociales": 0.014,
        "sin_historial_dificultades_sociales": 0.010
    },
    "Colombia": {
        "con_historial_dificultades_sociales": 0.017,
        "sin_historial_dificultades_sociales": 0.013
    },
    "Costa Rica": {
        "con_historial_dificultades_sociales": 0.013,
        "sin_historial_dificultades_sociales": 0.010
    },
    "Cuba": {
        "con_historial_dificultades_sociales": 0.016,
        "sin_historial_dificultades_sociales": 0.012
    },
    "Ecuador": {
        "con_historial_dificultades_sociales": 0.015,
        "sin_historial_dificultades_sociales": 0.011
    },
    "El Salvador": {
        "con_historial_dificultades_sociales": 0.014,
        "sin_historial_dificultades_sociales": 0.010
    },
    "Guatemala": {
        "con_historial_dificultades_sociales": 0.015,
        "sin_historial_dificultades_sociales": 0.011
    },
    "Haití": {
        "con_historial_dificultades_sociales": 0.013,
        "sin_historial_dificultades_sociales": 0.010
    },
    "Honduras": {
        "con_historial_dificultades_sociales": 0.015,
        "sin_historial_dificultades_sociales": 0.011
    },
    "México": {
        "con_historial_dificultades_sociales": 0.016,
        "sin_historial_dificultades_sociales": 0.012
    },
    "Nicaragua": {
        "con_historial_dificultades_sociales": 0.014,
        "sin_historial_dificultades_sociales": 0.010
    },
    "Panamá": {
        "con_historial_dificultades_sociales": 0.015,
        "sin_historial_dificultades_sociales": 0.011
    },
    "Paraguay": {
        "con_historial_dificultades_sociales": 0.013,
        "sin_historial_dificultades_sociales": 0.010
    },
    "Perú": {
        "con_historial_dificultades_sociales": 0.016,
        "sin_historial_dificultades_sociales": 0.012
    },
    "República Dominicana": {
        "con_historial_dificultades_sociales": 0.015,
        "sin_historial_dificultades_sociales": 0.011
    },
    "Uruguay": {
        "con_historial_dificultades_sociales": 0.014,
        "sin_historial_dificultades_sociales": 0.010
    },
    "Venezuela": {
        "con_historial_dificultades_sociales": 0.016,
        "sin_historial_dificultades_sociales": 0.012
    }
}

# Base de datos de prevalencia de comportamientos repetitivos por país
prevalencia_movimientos_repetitivos = {
    "Argentina": {"proporcion_movimientos_repetitivos": 0.70, "incidencia_niños": 0.010, "incidencia_niñas": 0.002},
    "Brasil": {"proporcion_movimientos_repetitivos": 0.68, "incidencia_niños": 0.011, "incidencia_niñas": 0.003},
    "Chile": {"proporcion_movimientos_repetitivos": 0.72, "incidencia_niños": 0.009, "incidencia_niñas": 0.002},
    "Colombia": {"proporcion_movimientos_repetitivos": 0.65, "incidencia_niños": 0.011, "incidencia_niñas": 0.003},
    "Costa Rica": {"proporcion_movimientos_repetitivos": 0.69, "incidencia_niños": 0.009, "incidencia_niñas": 0.002},
    "Cuba": {"proporcion_movimientos_repetitivos": 0.67, "incidencia_niños": 0.010, "incidencia_niñas": 0.003},
    "Ecuador": {"proporcion_movimientos_repetitivos": 0.71, "incidencia_niños": 0.010, "incidencia_niñas": 0.002},
    "El Salvador": {"proporcion_movimientos_repetitivos": 0.70, "incidencia_niños": 0.009, "incidencia_niñas": 0.002},
    "Guatemala": {"proporcion_movimientos_repetitivos": 0.68, "incidencia_niños": 0.010, "incidencia_niñas": 0.002},
    "Haití": {"proporcion_movimientos_repetitivos": 0.66, "incidencia_niños": 0.009, "incidencia_niñas": 0.002},
    "Honduras": {"proporcion_movimientos_repetitivos": 0.69, "incidencia_niños": 0.010, "incidencia_niñas": 0.002},
    "México": {"proporcion_movimientos_repetitivos": 0.67, "incidencia_niños": 0.011, "incidencia_niñas": 0.003},
    "Nicaragua": {"proporcion_movimientos_repetitivos": 0.68, "incidencia_niños": 0.009, "incidencia_niñas": 0.002},
    "Panamá": {"proporcion_movimientos_repetitivos": 0.70, "incidencia_niños": 0.010, "incidencia_niñas": 0.002},
    "Paraguay": {"proporcion_movimientos_repetitivos": 0.67, "incidencia_niños": 0.009, "incidencia_niñas": 0.002},
    "Perú": {"proporcion_movimientos_repetitivos": 0.66, "incidencia_niños": 0.010, "incidencia_niñas": 0.003},
    "República Dominicana": {"proporcion_movimientos_repetitivos": 0.68, "incidencia_niños": 0.010, "incidencia_niñas": 0.002},
    "Uruguay": {"proporcion_movimientos_repetitivos": 0.69, "incidencia_niños": 0.009, "incidencia_niñas": 0.002},
    "Venezuela": {"proporcion_movimientos_repetitivos": 0.67, "incidencia_niños": 0.010, "incidencia_niñas": 0.003},
}
# Base de datos de prevalencia de dificultad cambios de rutina por país y sexo
dificultad_cambios_rutina = {
    "Argentina": {"niños": 0.8, "niñas": 0.7},
    "Brasil": {"niños": 0.85, "niñas": 0.75},
    "Chile": {"niños": 0.75, "niñas": 0.65},
    "Nicaragua": {"niños": 0.7, "niñas": 0.8},
    "Colombia": {"niños": 0.88, "niñas": 0.78},
    "Costa Rica": {"niños": 0.7, "niñas": 0.6},
    "Cuba": {"niños": 0.82, "niñas": 0.72},
    "Uruguay": {"niños": 0.73, "niñas": 0.63},
    "El Salvador": {"niños": 0.72, "niñas": 0.62},
    "Guatemala": {"niños": 0.8, "niñas": 0.7},
    "Haití": {"niños": 0.68, "niñas": 0.58},
    "Venezuela": {"niños": 0.83, "niñas": 0.73},
    "Honduras": {"niños": 0.76, "niñas": 0.66},
    "México": {"niños": 0.84, "niñas": 0.74},
    "República Dominicana": {"niños": 0.77, "niñas": 0.67},
    "Perú": {"niños": 0.81, "niñas": 0.71},
    "Ecuador": {"niños": 0.78, "niñas": 0.68},
    "Panamá": {"niños": 0.79, "niñas": 0.69},
    "Paraguay": {"niños": 0.71, "niñas": 0.61},
}

# Base de datos de prevalencia de interes patrones secuencias por país
interes_patrones_secuencias = {
    "Argentina": {"niños": 0.75, "niñas": 0.65},
    "Brasil": {"niños": 0.8, "niñas": 0.7},
    "Chile": {"niños": 0.7, "niñas": 0.6},
    "Nicaragua": {"niños": 0.68, "niñas": 0.58},
    "Colombia": {"niños": 0.85, "niñas": 0.75},
    "Costa Rica": {"niños": 0.7, "niñas": 0.6},
    "Cuba": {"niños": 0.78, "niñas": 0.68},
    "Uruguay": {"niños": 0.71, "niñas": 0.61},
    "El Salvador": {"niños": 0.7, "niñas": 0.6},
    "Guatemala": {"niños": 0.75, "niñas": 0.65},
    "Haití": {"niños": 0.66, "niñas": 0.56},
    "Venezuela": {"niños": 0.8, "niñas": 0.7},
    "Honduras": {"niños": 0.72, "niñas": 0.62},
    "México": {"niños": 0.82, "niñas": 0.72},
    "República Dominicana": {"niños": 0.73, "niñas": 0.63},
    "Perú": {"niños": 0.79, "niñas": 0.69},
    "Ecuador": {"niños": 0.76, "niñas": 0.66},
    "Panamá": {"niños": 0.77, "niñas": 0.67},
    "Paraguay": {"niños": 0.69, "niñas": 0.59},
}

# Base de datos de prevalencia de problemas gastrointestinales por país
problemas_gastrointestinales = {
    "Argentina": {"prevalencia_gastro_niños_TEA": 0.91, "prevalencia_gastro_niñas_TEA": 0.89},
    "Brasil": {"prevalencia_gastro_niños_TEA": 0.90, "prevalencia_gastro_niñas_TEA": 0.88},
    "Chile": {"prevalencia_gastro_niños_TEA": 0.92, "prevalencia_gastro_niñas_TEA": 0.90},
    "Colombia": {"prevalencia_gastro_niños_TEA": 0.89, "prevalencia_gastro_niñas_TEA": 0.87},
    "Cuba": {"prevalencia_gastro_niños_TEA": 0.91, "prevalencia_gastro_niñas_TEA": 0.89},
    "Ecuador": {"prevalencia_gastro_niños_TEA": 0.92, "prevalencia_gastro_niñas_TEA": 0.90},
    "El Salvador": {"prevalencia_gastro_niños_TEA": 0.89, "prevalencia_gastro_niñas_TEA": 0.87},
    "Guatemala": {"prevalencia_gastro_niños_TEA": 0.90, "prevalencia_gastro_niñas_TEA": 0.88},
    "Haití": {"prevalencia_gastro_niños_TEA": 0.88, "prevalencia_gastro_niñas_TEA": 0.86},
    "Honduras": {"prevalencia_gastro_niños_TEA": 0.91, "prevalencia_gastro_niñas_TEA": 0.89},
    "México": {"prevalencia_gastro_niños_TEA": 0.92, "prevalencia_gastro_niñas_TEA": 0.90},
    "Nicaragua": {"prevalencia_gastro_niños_TEA": 0.89, "prevalencia_gastro_niñas_TEA": 0.87},
    "Panamá": {"prevalencia_gastro_niños_TEA": 0.90, "prevalencia_gastro_niñas_TEA": 0.88},
    "Paraguay": {"prevalencia_gastro_niños_TEA": 0.89, "prevalencia_gastro_niñas_TEA": 0.87},
    "Perú": {"prevalencia_gastro_niños_TEA": 0.92, "prevalencia_gastro_niñas_TEA": 0.90},
    "Costa Rica": {"prevalencia_gastro_niños_TEA": 0.90, "prevalencia_gastro_niñas_TEA": 0.88},
    "República Dominicana": {"prevalencia_gastro_niños_TEA": 0.91, "prevalencia_gastro_niñas_TEA": 0.89},
    "Uruguay": {"prevalencia_gastro_niños_TEA": 0.89, "prevalencia_gastro_niñas_TEA": 0.87},
    "Venezuela": {"prevalencia_gastro_niños_TEA": 0.92, "prevalencia_gastro_niñas_TEA": 0.90},
}

# Base de datos de prevalencia de habilidades excepcionales por país
habilidades_excepcionales = {
    "Argentina": {"habilidades_excepcionales_niños": 0.055, "habilidades_excepcionales_niñas": 0.040},
    "Brasil": {"habilidades_excepcionales_niños": 0.052, "habilidades_excepcionales_niñas": 0.038},
    "Chile": {"habilidades_excepcionales_niños": 0.053, "habilidades_excepcionales_niñas": 0.039},
    "Colombia": {"habilidades_excepcionales_niños": 0.050, "habilidades_excepcionales_niñas": 0.036},
    "Cuba": {"habilidades_excepcionales_niños": 0.048, "habilidades_excepcionales_niñas": 0.035},
    "Ecuador": {"habilidades_excepcionales_niños": 0.054, "habilidades_excepcionales_niñas": 0.039},
    "El Salvador": {"habilidades_excepcionales_niños": 0.052, "habilidades_excepcionales_niñas": 0.038},
    "Guatemala": {"habilidades_excepcionales_niños": 0.053, "habilidades_excepcionales_niñas": 0.039},
    "Haití": {"habilidades_excepcionales_niños": 0.050, "habilidades_excepcionales_niñas": 0.036},
    "Honduras": {"habilidades_excepcionales_niños": 0.051, "habilidades_excepcionales_niñas": 0.037},
    "México": {"habilidades_excepcionales_niños": 0.049, "habilidades_excepcionales_niñas": 0.035},
    "Nicaragua": {"habilidades_excepcionales_niños": 0.052, "habilidades_excepcionales_niñas": 0.038},
    "Panamá": {"habilidades_excepcionales_niños": 0.055, "habilidades_excepcionales_niñas": 0.040},
    "Paraguay": {"habilidades_excepcionales_niños": 0.053, "habilidades_excepcionales_niñas": 0.039},
    "Perú": {"habilidades_excepcionales_niños": 0.050, "habilidades_excepcionales_niñas": 0.036},
    "Costa Rica": {"habilidades_excepcionales_niños": 0.051, "habilidades_excepcionales_niñas": 0.037},
    "República Dominicana": {"habilidades_excepcionales_niños": 0.054, "habilidades_excepcionales_niñas": 0.039},
    "Uruguay": {"habilidades_excepcionales_niños": 0.052, "habilidades_excepcionales_niñas": 0.038},
    "Venezuela": {"habilidades_excepcionales_niños": 0.051, "habilidades_excepcionales_niñas": 0.037},  
}

# Base de datos de prevalencia de comportamientos autolesivos por país
prevalencia_comportamientos_autolesivos = {
    "Argentina": {"incidencia_niños": 0.35, "incidencia_niñas": 0.20},
    "Brasil": {"incidencia_niños": 0.32, "incidencia_niñas": 0.18},
    "Chile": {"incidencia_niños": 0.30, "incidencia_niñas": 0.16},
    "Colombia": {"incidencia_niños": 0.38, "incidencia_niñas": 0.22},
    "Costa Rica": {"incidencia_niños": 0.29, "incidencia_niñas": 0.15},
    "Cuba": {"incidencia_niños": 0.33, "incidencia_niñas": 0.19},
    "Ecuador": {"incidencia_niños": 0.34, "incidencia_niñas": 0.18},
    "El Salvador": {"incidencia_niños": 0.28, "incidencia_niñas": 0.14},
    "Guatemala": {"incidencia_niños": 0.31, "incidencia_niñas": 0.17},
    "Haití": {"incidencia_niños": 0.27, "incidencia_niñas": 0.13},
    "Honduras": {"incidencia_niños": 0.30, "incidencia_niñas": 0.16},
    "México": {"incidencia_niños": 0.32, "incidencia_niñas": 0.18},
    "Nicaragua": {"incidencia_niños": 0.29, "incidencia_niñas": 0.15},
    "Panamá": {"incidencia_niños": 0.34, "incidencia_niñas": 0.18},
    "Paraguay": {"incidencia_niños": 0.28, "incidencia_niñas": 0.14},
    "Perú": {"incidencia_niños": 0.33, "incidencia_niñas": 0.19},
    "República Dominicana": {"incidencia_niños": 0.31, "incidencia_niñas": 0.17},
    "Uruguay": {"incidencia_niños": 0.29, "incidencia_niñas": 0.15},
    "Venezuela": {"incidencia_niños": 0.32, "incidencia_niñas": 0.18},
}

# Base de datos de prevalencia de problemas emocionales por país
prevalencia_problemas_emocionales = {
    "Argentina": {"prevalencia_niños": 1.5, "prevalencia_niñas": 0.8},
    "Brasil": {"prevalencia_niños": 1.6, "prevalencia_niñas": 0.9},
    "Chile": {"prevalencia_niños": 1.4, "prevalencia_niñas": 0.7},
    "Colombia": {"prevalencia_niños": 1.7, "prevalencia_niñas": 0.9},
    "Cuba": {"prevalencia_niños": 1.6, "prevalencia_niñas": 0.8},
    "Ecuador": {"prevalencia_niños": 1.4, "prevalencia_niñas": 0.7},
    "El Salvador": {"prevalencia_niños": 1.3, "prevalencia_niñas": 0.6},
    "Guatemala": {"prevalencia_niños": 1.5, "prevalencia_niñas": 0.7},
    "Haití": {"prevalencia_niños": 1.3, "prevalencia_niñas": 0.6},
    "Honduras": {"prevalencia_niños": 1.4, "prevalencia_niñas": 0.7},
    "México": {"prevalencia_niños": 1.6, "prevalencia_niñas": 0.8},
    "Nicaragua": {"prevalencia_niños": 1.3, "prevalencia_niñas": 0.6},
    "Panamá": {"prevalencia_niños": 1.4, "prevalencia_niñas": 0.7},
    "Paraguay": {"prevalencia_niños": 1.3, "prevalencia_niñas": 0.6},
    "Perú": {"prevalencia_niños": 1.6, "prevalencia_niñas": 0.8},
    "Costa Rica": {"prevalencia_niños": 1.3, "prevalencia_niñas": 0.6},
    "República Dominicana": {"prevalencia_niños": 1.5, "prevalencia_niñas": 0.7},
    "Uruguay": {"prevalencia_niños": 1.3, "prevalencia_niñas": 0.6},
    "Venezuela": {"prevalencia_niños": 1.6, "prevalencia_niñas": 0.8},  
}
# Función para calcular la probabilidad de autismo
def calcular_probabilidad_autismo(respuestas):
    pais = respuestas[0]
    sexo = respuestas[1]
    antecedentes_autismo = respuestas[2]
    madre_infecciones = respuestas[3]
    prematuro = respuestas[4]
    hipoxia = respuestas[5]
    camina_puntas_pie = respuestas[6]  
    retraso_lenguaje = respuestas[7]
    contacto_visual = respuestas[8]
    comportamientos_repetitivos = respuestas[9]
    sensibilidad_sensorial = respuestas[10]
    dificultades_sueno = respuestas[11]
    intereses_restringidos = respuestas[12]
    dificultades_sociales = respuestas[13]
    movimientos_repetitivos = respuestas[14]
    dificultad_cambios_rutina = respuestas[15]
    interes_patrones_secuencias = respuestas[16]
    problemas_gastrointestinales = respuestas[17]
    habilidades_excepcionales = respuestas[18]
    reacciones_adversas_alimentos = respuestas[19]
    comportamientos_autolesivos = respuestas[20]
    problemas_emocionales = respuestas[21]

    # Calcular la probabilidad base según la prevalencia general del país
    probabilidad_base = prevalencia_pais[pais]["general"]

    # Ajustar la probabilidad base según el sexo del niño
    if sexo == 'Niño':
        probabilidad_base *= prevalencia_pais[pais]["niños"] / prevalencia_pais[pais]["general"]
    else:
        probabilidad_base *= prevalencia_pais[pais]["niñas"] / prevalencia_pais[pais]["general"]

    # Ajustar la probabilidad base según antecedentes familiares de autismo
    if antecedentes_autismo == 'Sí':
        probabilidad_base *= prevalencia_antecedentes_familiares[pais]["con_antecedentes"]
    else:
        probabilidad_base *= prevalencia_antecedentes_familiares[pais]["sin_antecedentes"]

    # Ajustar la probabilidad según infecciones maternas durante el embarazo
    if madre_infecciones == 'Sí' and pais in ajuste_infecciones_maternas:
        probabilidad_base *= ajuste_infecciones_maternas[pais]

    # Ajustar la probabilidad según prematuridad
    if prematuro == 'Sí':
        probabilidad_base *= 1 + Prevalencia_Prematuramente[pais]

    # Ajustar la probabilidad según hipoxia al nacer
    if hipoxia == 'Sí' and pais in Prevalencia_Hipoxia:
        if sexo == 'Niño':
            probabilidad_base *= Prevalencia_Hipoxia[pais]["niños"]
        else:
            probabilidad_base *= Prevalencia_Hipoxia[pais]["niñas"]
    
     # Ajustar la probabilidad según si camina en puntas de pie
    if camina_puntas_pie == 'Sí':
        probabilidad_base *= prevalencia_camina_puntas_pie[pais]

     # Ajustar la probabilidad según el retraso en lenguaje si aplica
    if retraso_lenguaje == 'Sí' and pais in Prevalencia_Retraso_Lenguaje:
        if sexo == 'Niño':
            probabilidad_base *= Prevalencia_Retraso_Lenguaje[pais]["Incidencia en Niños"]
        else:
            probabilidad_base *= Prevalencia_Retraso_Lenguaje[pais]["Incidencia en Niñas"]

    # Ajustar la probabilidad según dificultades en el contacto visual
    if contacto_visual == 'Sí' and pais in Prevalencia_Contacto_Visual:
        if sexo == 'Niño':
            probabilidad_base *= Prevalencia_Contacto_Visual[pais]["Niños con dificultades en el contacto visual"]
        else:
            probabilidad_base *= Prevalencia_Contacto_Visual[pais]["Niñas con dificultades en el contacto visual"]

     # Ajustar la probabilidad según movimientos repetitivos, dificultades con cambios en la rutina e interés en patrones o secuencias
    if comportamientos_repetitivos == 'Sí' and pais in prevalencia_comportamientos_repetitivos:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_comportamientos_repetitivos[pais]["prevalencia_niños"]
        else:
            probabilidad_base *= prevalencia_comportamientos_repetitivos[pais]["prevalencia_niñas"]

     # Ajustar la probabilidad base según sensibilidad sensorial si aplica
    if sensibilidad_sensorial == 'Sí' and pais in prevalencia_sensibilidad_sensorial:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_sensibilidad_sensorial[pais]["prevalencia_niños"]
        else:
            probabilidad_base *= prevalencia_sensibilidad_sensorial[pais]["prevalencia_niñas"]

    # Ajustar la probabilidad según comportamientos repetitivos y dificultades en el sueño
    if dificultades_sueno == 'Sí' and pais in prevalencia_comportamientos_repetitivos:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_comportamientos_repetitivos[pais]["prevalencia_niños"]
        else:
            probabilidad_base *= prevalencia_comportamientos_repetitivos[pais]["prevalencia_niñas"]

    # Ajustar la probabilidad según intereses restringidos
    if intereses_restringidos == 'Sí' and pais in incidencia_intereses_restringidos:
        if sexo == 'Niño':
            probabilidad_base *= incidencia_intereses_restringidos[pais]["incidencia_niños"]
        else:
            probabilidad_base *= incidencia_intereses_restringidos[pais]["incidencia_niñas"]

     # Ajustar la probabilidad según dificultades sociales
    if dificultades_sociales == 'Sí':
        probabilidad_base *= prevalencia_dificultades_sociales[pais]["con_historial_dificultades_sociales"]
    else:
        probabilidad_base *= prevalencia_dificultades_sociales[pais]["sin_historial_dificultades_sociales"]

         # Ajustar la probabilidad según movimientos repetitivos
    if movimientos_repetitivos == 'Sí' and pais in prevalencia_movimientos_repetitivos:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_movimientos_repetitivos[pais]["incidencia_niños"]
        else:
            probabilidad_base *= prevalencia_movimientos_repetitivos[pais]["incidencia_niñas"]

     # Ajustar la probabilidad según dificultades en cambios de rutina
    if dificultad_cambios_rutina == 'Sí' and pais in dificultad_cambios_rutina:
        if sexo == 'Niño':
            probabilidad_base *= dificultad_cambios_rutina[pais]["niños"]
        else:
            probabilidad_base *= dificultad_cambios_rutina[pais]["niñas"]

            # Ajustar la probabilidad según interés en patrones o secuencias
    if interes_patrones_secuencias == 'Sí' and pais in interes_patrones_secuencias:
        if sexo == 'Niño':
            probabilidad_base *= interes_patrones_secuencias[pais]["niños"]
        else:
            probabilidad_base *= interes_patrones_secuencias[pais]["niñas"]

 # Ajustar la probabilidad según problemas gastrointestinales si aplica
    if problemas_gastrointestinales == 'Sí' and pais in problemas_gastrointestinales:
        if sexo == 'Niño':
            probabilidad_base *= problemas_gastrointestinales[pais]["prevalencia_gastro_niños_TEA"]
        else:
            probabilidad_base *= problemas_gastrointestinales[pais]["prevalencia_gastro_niñas_TEA"]

# Ajustar la probabilidad según habilidades excepcionales
    if habilidades_excepcionales == 'Sí' and pais in habilidades_excepcionales:
        if sexo == 'Niño':
            probabilidad_base *= habilidades_excepcionales[pais]["habilidades_excepcionales_niños"]
        else:
            probabilidad_base *= habilidades_excepcionales[pais]["habilidades_excepcionales_niñas"]

# Ajustar la probabilidad según reacciones adversas a alimentos
    if reacciones_adversas_alimentos == 'Sí':
        probabilidad_base *= 1 + 0.072  # Utilizando el valor porcentual proporcionado (0.072)

 # Ajustar la probabilidad según comportamientos autolesivos
    if comportamientos_autolesivos == 'Sí' and pais in prevalencia_comportamientos_autolesivos:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_comportamientos_autolesivos[pais]["incidencia_niños"]
        else:
            probabilidad_base *= prevalencia_comportamientos_autolesivos[pais]["incidencia_niñas"]

    # Devolver la probabilidad calculada (multiplicada por 100 para mostrar como porcentaje)
    return probabilidad_base * 100

# Función para mostrar las opciones disponibles y capturar las respuestas del usuario
def obtener_respuestas():
    respuestas = []

    # País de procedencia
    print("\n1. País de procedencia:")
    for idx, pais in enumerate(prevalencia_pais.keys()):
        print(f"   {idx + 1}. {pais}")
    opcion = input(f"Seleccione el número correspondiente a su país (1-{len(prevalencia_pais)}): ")
    try:
        indice_pais = int(opcion) - 1
        if 0 <= indice_pais < len(prevalencia_pais):
            pais = list(prevalencia_pais.keys())[indice_pais]
            respuestas.append(pais)
        else:
            print("Número de país fuera de rango. Por favor, seleccione un número válido.")
            return obtener_respuestas()
    except ValueError:
        print("Entrada inválida. Por favor, ingrese el número correspondiente a su país.")
        return obtener_respuestas()

    # Sexo del niño
    print("\n2. Sexo del niño:")
    print("   a) Niño")
    print("   b) Niña")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Niño')
    elif opcion == 'b':
        respuestas.append('Niña')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Antecedentes familiares de autismo
    print("\n3. ¿Hay antecedentes familiares de autismo?")
    print("   a) Sí")
    print("   b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Infecciones maternas durante el embarazo
    print("\n4. ¿Hubo infecciones maternas durante el embarazo?")
    print("   a) Sí")
    print("   b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Prematuridad
    print("\n5. ¿El niño nació prematuramente?")
    print("   a) Sí")
    print("   b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Hipoxia al nacer
    print("\n6. ¿Hubo hipoxia al nacer (falta de oxígeno)?")
    print("   a) Sí")
    print("   b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Camina en puntas de pie
    print("\n7. ¿El niño o niña camina en puntas de pie?")
    print("   a) Sí")
    print("   b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Retraso en el lenguaje
    print("\n8. ¿Hubo retraso en el desarrollo del lenguaje?")
    print("   a) Sí")
    print("   b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Contacto visual
    print("\n9. ¿Hay dificultades con el contacto visual?")
    print("   a) Sí")
    print("   b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Comportamientos repetitivos
    print("\n10. ¿Hay comportamientos repetitivos?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Sensibilidad sensorial
    print("\n11. ¿Hay sensibilidad sensorial?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Dificultades para dormir
    print("\n12. ¿Hay dificultades para dormir?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Intereses restringidos
    print("\n13. ¿Hay intereses restringidos?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Dificultades sociales
    print("\n14. ¿Hay dificultades sociales?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Movimientos repetitivos
    print("\n15. ¿Hay movimientos repetitivos?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Dificultad para adaptarse a cambios en la rutina
    print("\n16. ¿Hay dificultad para adaptarse a cambios en la rutina?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Interés en patrones o secuencias
    print("\n17. ¿Hay interés en patrones o secuencias?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Problemas gastrointestinales
    print("\n18. ¿Hay problemas gastrointestinales?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Habilidades excepcionales
    print("\n19. ¿El niño o niña muestra habilidades excepcionales en áreas específicas?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Reacciones adversas a alimentos o texturas específicas
    print("\n20. ¿Hay reacciones adversas a ciertos alimentos o texturas?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Comportamientos autolesivos
    print("\n21. ¿Hay comportamientos autolesivos?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Problemas emocionales
    print("\n22. ¿Hay problemas emocionales significativos?")
    print("    a) Sí")
    print("    b) No")
    opcion = input("Seleccione una opción (a/b): ").lower()
    if opcion == 'a':
        respuestas.append('Sí')
    elif opcion == 'b':
        respuestas.append('No')
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()
        
    return respuestas

# Ejecutar el programa principal
if _name_ == "_main_":
    print("Bienvenido al cuestionario para calcular la probabilidad de autismo.")
    respuestas = obtener_respuestas()
    probabilidad_autismo = calcular_probabilidad_autismo(respuestas)
    print(f"\nLa probabilidad de que el niño tenga autismo es del {probabilidad_autismo:.2f}%.")