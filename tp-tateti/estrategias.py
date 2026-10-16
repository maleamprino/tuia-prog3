"""
Módulo de estrategias para el juego del Tateti

Este módulo contiene las estrategias para elegir la acción a realizar.
Los alumnos deben implementar la estrategia minimax.

Por defecto, se incluye una estrategia aleatoria como ejemplo base.
"""

import random
import math
from typing import List, Tuple
from tateti import Tateti, JUGADOR_MAX, JUGADOR_MIN

def estrategia_aleatoria(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia aleatoria: elige una acción al azar entre las disponibles.
  
    """
    acciones_disponibles = tateti.acciones(estado)
    if not acciones_disponibles:
        raise ValueError("No hay acciones disponibles")
    
    return random.choice(acciones_disponibles)

def _minimax_max(tateti: Tateti, estado: List[List[str]]) -> float:
    """Calcula recursivamente el valor minimax en un nodo MAX."""
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)
    
    valor = -math.inf
    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = max(valor, _minimax_min(tateti, sucesor))
    return valor

def _minimax_min(tateti: Tateti, estado: List[List[str]]) -> float:
    """Calcula recursivamente el valor minimax en un nodo MIN."""
    if tateti.test_terminal(estado):
        return tateti.utilidad(estado, JUGADOR_MAX)
    
    valor = math.inf
    for accion in tateti.acciones(estado):
        sucesor = tateti.resultado(estado, accion)
        valor = min(valor, _minimax_max(tateti, sucesor))
    return valor

def estrategia_minimax(tateti: Tateti, estado: List[List[str]]) -> Tuple[int, int]:
    """
    Estrategia minimax: elige la mejor acción usando el algoritmo minimax tal
    como se especifica en las diapositivas de la cátedra.
    """
    jugador_actual = tateti.jugador(estado)

    if jugador_actual == JUGADOR_MAX:
        sucs = {
            accion: _minimax_min(tateti, tateti.resultado(estado, accion))
            for accion in tateti.acciones(estado)
        }
        return max(sucs, key=sucs.get)
    else:
        sucs = {
            accion: _minimax_max(tateti, tateti.resultado(estado, accion))
            for accion in tateti.acciones(estado)
        }
        return min(sucs, key=sucs.get)

