# Encadenamientos - Sistemas Expertos

Este proyecto contiene dos códigos principales que implementan técnicas de inferencia en sistemas expertos: encadenamiento hacia adelante y encadenamiento hacia atrás.

## Archivos

### 1. Encadenamiento_delantero.py

Implementa un sistema de **encadenamiento hacia adelante** (forward chaining) para recomendar botas en un contexto de juego, según hechos y reglas predefinidas.

- **forward_chaining()**:
  - Simula la entrada de hechos iniciales (por ejemplo, si hay una Morgana en el equipo rival, si hay muchos ataques básicos, etc.).
  - Aplica 7 reglas para deducir nuevos hechos y recomendaciones.
    Conclute la recomendacion de compra de las botas según la situación inferida.

### 2. Encadenamiento_trasero

Contiene la clase **MotorInferencia** que implementa un sistema de **encadenamiento hacia atrás** (backward chaining) para diagnóstico médico sencillo.

- **MotorInferencia**:
  - \***\*init**()\*\*: Inicializa la base de reglas y hechos conocidos.
  - **obtener_valor_hecho(sintoma)**: Consulta o pregunta el valor de un síntoma.
  - **verificar_meta(meta)**: Algoritmo de encadenamiento hacia atrás para verificar si se cumple una meta (enfermedad).
  - **mostrar_hechos_escenario(escenario_nombre, datos)**: Muestra los hechos de un escenario automático.
  - **menu()**: Permite elegir entre escenarios automáticos o modo personalizado, y ejecuta el diagnóstico.

## Uso

- Ejecuta cada archivo con Python según el tipo de inferencia que quieras probar.
- No requiere librerías externas.

---

Si agregas más archivos o métodos, recuerda actualizar este README.
