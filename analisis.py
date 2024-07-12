import pandas as pd

# Base de datos para calcular la probabilidad de 
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
base_datos_autismo = {
    "prevalencia_pais": {
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
    },
    "prevalencia_antecedentes_familiares": {
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
    },
    "ajuste_infecciones_maternas": {
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
    },
    "prevalencia_prematuro": {
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
    },
    "prevalencia_hipoxia": {
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
        "Guatemala": {"niños": 0.0105, "niñas": 0.0021},
        "Honduras": {"niños": 0.0093, "niñas": 0.002},
        "México": {"niños": 0.0141, "niñas": 0.0031},
        "Nicaragua": {"niños": 0.0093, "niñas": 0.0022},
        "Panamá": {"niños": 0.0125, "niñas": 0.0026},
        "Paraguay": {"niños": 0.0112, "niñas": 0.0021},
        "Perú": {"niños": 0.0137, "niñas": 0.0028},
        "República Dominicana": {"niños": 0.015, "niñas": 0.003},
        "Uruguay": {"niños": 0.014, "niñas": 0.0025},
        "Venezuela": {"niños": 0.0138, "niñas": 0.0029},
        "Puerto Rico": {"niños": 0.0163, "niñas": 0.0033}
    },
    "prevalencia_camina_puntas_pie" : {
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
        
    },

"Prevalencia_Retraso_Lenguaje" : {
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
},

"Prevalencia_Contacto_Visual" : {
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
},

"prevalencia_comportamientos_repetitivos" : {
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
},

"prevalencia_sensibilidad_sensorial" : {
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
},

"incidencia_intereses_restringidos" : {
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
},

"prevalencia_dificultades_sociales" : {
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
},

"prevalencia_movimientos_repetitivos" : {
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
},
    
"dificultad_cambios_rutina" : {
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
},

"interes_patrones_secuencias" : {
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
},

"problemas_gastrointestinales" : {
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
},

"habilidades_excepcionales" : {
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
},

"prevalencia_comportamientos_autolesivos" : {
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
},

"prevalencia_problemas_emocionales" : {
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
    }

if __name__ == "_main_":
    main()


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
    if prematuro == 'Sí' and pais in Prevalencia_Prematuramente:
        probabilidad_base *= Prevalencia_Prematuramente[pais]

    # Ajustar la probabilidad según hipoxia al nacer
    if hipoxia == 'Sí' and pais in Prevalencia_Hipoxia:
        if sexo == 'Niño':
            probabilidad_base *= Prevalencia_Hipoxia[pais]["niños"]
        else:
            probabilidad_base *= Prevalencia_Hipoxia[pais]["niñas"]

    # Ajustar la probabilidad según camina en puntas de pie
    if camina_puntas_pie == 'Sí' and pais in prevalencia_camina_puntas_pie:
        probabilidad_base *= prevalencia_camina_puntas_pie[pais]

    # Ajustar la probabilidad según retraso en lenguaje si aplica
    if retraso_lenguaje == 'Sí' and pais in Prevalencia_Retraso_Lenguaje:
        if sexo == 'Niño':
            probabilidad_base *= Prevalencia_Retraso_Lenguaje[pais]["niños"]
        else:
            probabilidad_base *= Prevalencia_Retraso_Lenguaje[pais]["niñas"]

    # Ajustar la probabilidad según dificultades en el contacto visual
    if contacto_visual == 'Sí' and pais in Prevalencia_Contacto_Visual:
        if sexo == 'Niño':
            probabilidad_base *= Prevalencia_Contacto_Visual[pais]["niños"]
        else:
            probabilidad_base *= Prevalencia_Contacto_Visual[pais]["niñas"]

    # Ajustar la probabilidad según comportamientos repetitivos
    if comportamientos_repetitivos == 'Sí' and pais in prevalencia_comportamientos_repetitivos:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_comportamientos_repetitivos[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_comportamientos_repetitivos[pais]["niñas"]

    # Ajustar la probabilidad según sensibilidad sensorial
    if sensibilidad_sensorial == 'Sí' and pais in prevalencia_sensibilidad_sensorial:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_sensibilidad_sensorial[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_sensibilidad_sensorial[pais]["niñas"]

    # Ajustar la probabilidad según dificultades en el sueño
    if dificultades_sueno == 'Sí' and pais in prevalencia_dificultades_sueno:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_dificultades_sueno[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_dificultades_sueno[pais]["niñas"]

    # Ajustar la probabilidad según intereses restringidos
    if intereses_restringidos == 'Sí' and pais in prevalencia_intereses_restringidos:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_intereses_restringidos[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_intereses_restringidos[pais]["niñas"]

    # Ajustar la probabilidad según dificultades sociales
    if dificultades_sociales == 'Sí' and pais in prevalencia_dificultades_sociales:
        probabilidad_base *= prevalencia_dificultades_sociales[pais]["con_dificultades_sociales"]
    else:
        probabilidad_base *= prevalencia_dificultades_sociales[pais]["sin_dificultades_sociales"]

    # Ajustar la probabilidad según movimientos repetitivos
    if movimientos_repetitivos == 'Sí' and pais in prevalencia_movimientos_repetitivos:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_movimientos_repetitivos[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_movimientos_repetitivos[pais]["niñas"]

    # Ajustar la probabilidad según dificultad en cambios de rutina
    if dificultad_cambios_rutina == 'Sí' and pais in prevalencia_dificultad_cambios_rutina:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_dificultad_cambios_rutina[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_dificultad_cambios_rutina[pais]["niñas"]

    # Ajustar la probabilidad según interés en patrones o secuencias
    if interes_patrones_secuencias == 'Sí' and pais in prevalencia_interes_patrones_secuencias:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_interes_patrones_secuencias[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_interes_patrones_secuencias[pais]["niñas"]

    # Ajustar la probabilidad según problemas gastrointestinales
    if problemas_gastrointestinales == 'Sí' and pais in prevalencia_problemas_gastrointestinales:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_problemas_gastrointestinales[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_problemas_gastrointestinales[pais]["niñas"]

    # Ajustar la probabilidad según habilidades excepcionales
    if habilidades_excepcionales == 'Sí' and pais in prevalencia_habilidades_excepcionales:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_habilidades_excepcionales[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_habilidades_excepcionales[pais]["niñas"]

    # Ajustar la probabilidad según reacciones adversas a alimentos
    if reacciones_adversas_alimentos == 'Sí' and pais in prevalencia_reacciones_adversas_alimentos:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_reacciones_adversas_alimentos[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_reacciones_adversas_alimentos[pais]["niñas"]

    # Ajustar la probabilidad según comportamientos autolesivos
    if comportamientos_autolesivos == 'Sí' and pais in prevalencia_comportamientos_autolesivos:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_comportamientos_autolesivos[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_comportamientos_autolesivos[pais]["niñas"]

    # Ajustar la probabilidad según problemas emocionales
    if problemas_emocionales == 'Sí' and pais in prevalencia_problemas_emocionales:
        if sexo == 'Niño':
            probabilidad_base *= prevalencia_problemas_emocionales[pais]["niños"]
        else:
            probabilidad_base *= prevalencia_problemas_emocionales[pais]["niñas"]

    # Ajustar la probabilidad base para mantenerla dentro del rango del 30% al 70%
    probabilidad_base = max(min(probabilidad_base, 0.70), 0.30)

    return probabilidad_base




# Función para mostrar las opciones disponibles y capturar las respuestas del usuario
def obtener_respuestas():
    respuestas = {}

    # País de procedencia
    print("\n1. País de procedencia:")
    for idx, pais in enumerate(prevalencia_pais.keys()):
        print(f"   {idx + 1}. {pais}")
    opcion = input(f"Seleccione el número correspondiente a su país (1-{len(prevalencia_pais)}): ")
    try:
        indice_pais = int(opcion) - 1
        if 0 <= indice_pais < len(prevalencia_pais):
            pais = list(prevalencia_pais.keys())[indice_pais]
            respuestas['País'] = pais
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
        respuestas['Sexo'] = 'Niño'
    elif opcion == 'b':
        respuestas['Sexo'] = 'Niña'
    else:
        print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
        return obtener_respuestas()

    # Preguntas de Sí o No con cálculo de porcentaje
    preguntas = [
        ("Antecedentes familiares de autismo", 'Sí'),
        ("Infecciones maternas durante el embarazo", 'Sí'),
        ("Prematuridad", 'Sí'),
        ("Hipoxia al nacer (falta de oxígeno)", 'Sí'),
        ("Camina en puntas de pie", 'Sí'),
        ("Retraso en el desarrollo del lenguaje", 'Sí'),
        ("Dificultades con el contacto visual", 'Sí'),
        ("Comportamientos repetitivos", 'Sí'),
        ("Sensibilidad sensorial", 'Sí'),
        ("Dificultades para dormir", 'Sí'),
        ("Intereses restringidos", 'Sí'),
        ("Dificultades sociales", 'Sí'),
        ("Movimientos repetitivos", 'Sí'),
        ("Dificultad para adaptarse a cambios en la rutina", 'Sí'),
        ("Interés en patrones o secuencias", 'Sí'),
        ("Problemas gastrointestinales", 'Sí'),
        ("Habilidades excepcionales", 'Sí'),
        ("Reacciones adversas a alimentos", 'Sí'),
        ("Comportamientos autolesivos", 'Sí'),
        ("Problemas emocionales", 'Sí')
    ]

    for pregunta, respuesta_si in preguntas:
        print(f"\n{pregunta}:")
        print("   a) Sí")
        print("   b) No")
        opcion = input("Seleccione una opción (a/b): ").lower()
        if opcion == 'a':
            respuestas[pregunta] = 'Sí'
        elif opcion == 'b':
            respuestas[pregunta] = 'No'
        else:
            print("Opción no válida. Por favor, seleccione 'a' o 'b'.")
            return obtener_respuestas()

    # Calculando porcentajes basados en respuestas de "Sí"
    total_si = sum(1 for valor in respuestas.values() if valor == 'Sí')
    total_preguntas = len(preguntas) + 2  # +2 por País y Sexo

    # Mostrar porcentaje total basado en la base de datos
    porcentaje = total_si / total_preguntas * 100
    print(f"\nBasado en las respuestas proporcionadas, hay un {porcentaje}% de probabilidad de autismo según la base de datos.")

    return respuestas

# Ejemplo de uso
respuestas_usuario = obtener_respuestas()
print("\nRespuestas registradas:")
for pregunta, respuesta in respuestas_usuario.items():
    print(f"{pregunta}: {respuesta}")
  # Función para compilar el código
def compilar(respuestas):
    # Ajustes basados en respuestas del usuario
    probabilidad_base = 0.5  # Valor inicial de probabilidad base
    prevalencia_reacciones_adversas_alimentos = {
        "País1": {"niños": 0.2, "niñas": 0.3},
        "País2": {"niños": 0.25, "niñas": 0.35}
        # Agrega aquí el diccionario completo con las prevalencias por país
    }
    prevalencia_comportamientos_autolesivos = {
        "País1": {"niños": 0.1, "niñas": 0.15},
        "País2": {"niños": 0.12, "niñas": 0.18}
        # Agrega aquí el diccionario completo con las prevalencias por país
    }
    prevalencia_problemas_emocionales = {
        "País1": {"niños": 0.3, "niñas": 0.4},
        "País2": {"niños": 0.35, "niñas": 0.45}
        # Agrega aquí el diccionario completo con las prevalencias por país
    }

    # Ajustar la probabilidad según reacciones adversas a alimentos
    if respuestas.get("Reacciones adversas a alimentos") == 'Sí' and respuestas.get('País') in prevalencia_reacciones_adversas_alimentos:
        if respuestas.get('Sexo') == 'Niño':
            probabilidad_base *= prevalencia_reacciones_adversas_alimentos[respuestas.get('País')]["niños"]
        else:
            probabilidad_base *= prevalencia_reacciones_adversas_alimentos[respuestas.get('País')]["niñas"]

    # Ajustar la probabilidad según comportamientos autolesivos
    if respuestas.get("Comportamientos autolesivos") == 'Sí' and respuestas.get('País') in prevalencia_comportamientos_autolesivos:
        if respuestas.get('Sexo') == 'Niño':
            probabilidad_base *= prevalencia_comportamientos_autolesivos[respuestas.get('País')]["niños"]
        else:
            probabilidad_base *= prevalencia_comportamientos_autolesivos[respuestas.get('País')]["niñas"]

    # Ajustar la probabilidad según problemas emocionales
    if respuestas.get("Problemas emocionales") == 'Sí' and respuestas.get('País') in prevalencia_problemas_emocionales:
        if respuestas.get('Sexo') == 'Niño':
            probabilidad_base *= prevalencia_problemas_emocionales[respuestas.get('País')]["niños"]
        else:
            probabilidad_base *= prevalencia_problemas_emocionales[respuestas.get('País')]["niñas"]

    # Ajustar la probabilidad base para mantenerla dentro del rango del 30% al 70%
    probabilidad_base = max(min(probabilidad_base, 0.70), 0.30)

    return probabilidad_base

# Base de datos
def base_de_datos():
    password = "Trastorno_Del_Espectro_Autista_16_De_Diciembre"
    if input("Introduzca la contraseña para acceder a la base de datos: ") == password:
        print("Acceso a la base de datos concedido.")
        # Código para acceder y mostrar la base de datos
    else:
        print("Contraseña incorrecta. Acceso denegado.")

# Función principal para ejecutar el programa
def main():
    respuestas_usuario = obtener_respuestas()
    print("\nRespuestas registradas:")
    for pregunta, respuesta in respuestas_usuario.items():
        print(f"{pregunta}: {respuesta}")

    while True:
        opcion = input("\nSeleccione una opción:\n1. Compilar\n2. Base de Datos\n3. Finalizar\n")

        if opcion == '1':
            probabilidad = compilar(respuestas_usuario)
            print(f"Probabilidad ajustada: {probabilidad}")
        elif opcion == '2':
            base_de_datos()
        elif opcion == '3':
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

            #