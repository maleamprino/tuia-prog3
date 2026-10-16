"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)

    Raises:
        ValueError: Si no hay acciones disponibles
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax.
    
    Args:
        tateti: Instancia de la clase Tateti
        estado: Estado actual del tablero
        
    Returns:
        Tuple[int, int]: Acción elegida (fila, columna)
        
    Raises:
        NotImplementedError: Hasta que el alumno implemente el algoritmo
    """
    def minimax(estado: List[List[str]]) -> float:
        if tateti.test_terminal(estado):
            return tateti.utilidad(estado)
        jugador = tateti.jugador(estado)
        acciones = tateti.acciones(estado)

        if jugador == JUGADOR_MAX:
            mejor_valor = float("-inf")

            for accion in acciones:
                nuevo_estado = tateti.resultado(estado, accion)
                valor = minimax(nuevo_estado)
                mejor_valor = max(mejor_valor, valor)
            
            return mejor_valor
        else:
            mejor_valor = float("inf")

            for accion in acciones:
                nuevo_estado = tateti.resultado(estado, accion)
                valor = minimax(nuevo_estado)
                mejor_valor = min(mejor_valor, valor)

            return mejor_valor
    jugador_actual = tateti.jugador(estado)
    mejor_accion = None

    if jugador_actual == JUGADOR_MAX:
        mejor_valor = float("-inf")

        for accion in tateti.acciones(estado):
            nuevo_estado = tateti.resultado(estado, accion)
            valor = minimax(nuevo_estado)

            if valor > mejor_valor:
                mejor_valor = valor
                mejor_accion = accion
    else:
        mejor_valor = float("inf")

        for accion in tateti.acciones(estado):
            nuevo_estado = tateti.resultado(estado, accion)
            valor = minimax(nuevo_estado)

            if valor < mejor_valor:
                mejor_valor = valor
                mejor_accion = accion
    
    return mejor_accion
