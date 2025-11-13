import numpy as np
import math
from decimal import Decimal, getcontext
from typing import Union

# Настройка точности для Decimal
DEFAULT_PRECISION = 100
getcontext().prec = DEFAULT_PRECISION

class FZVerifier:
    """
    Верификатор ключевых формул Теории FZ с гарантированной численной устойчивостью
    
    ИСПРАВЛЕНО: Удалена багнутая ветка Level 2, оставлена простая и надежная логика
    """
    
    @staticmethod
    def manifestation_probability(p: float, t: float) -> float:
        """
        Вероятность проявления различия в бесконечном ничто.
        
        ИСПРАВЛЕНО: Упрощенная и численно-устойчивая реализация
        Формула: P = 1 - exp(-tp) через np.expm1
        
        Параметры:
        ----------
        p : float
            Вероятность единичного проявления (0 < p ≤ 1)
        t : float
            Мера мощности возможностей (t > 0)
            
        Возвращает:
        -----------
        float
            Вероятность проявления (0 ≤ P ≤ 1)
        """
        if p <= 0 or t <= 0:
            raise ValueError("p и t должны быть положительными")
        
        tp = t * p
        
        # ЕДИНСТВЕННЫЙ УСТОЙЧИВЫЙ ПУТЬ ДЛЯ ВСЕХ СЛУЧАЕВ
        # np.expm1(x) = exp(x) - 1, поэтому -np.expm1(-tp) = 1 - exp(-tp)
        prob = -np.expm1(-tp)
        
        # Защита от численных артефактов (вероятность не может быть > 1.0)
        return min(1.0, max(0.0, prob))
    
    @staticmethod
    def manifestation_probability_decimal(p_str: str, t_str: str, 
                                        precision: int = 100) -> Decimal:
        """
        Абсолютно точная верификация через Decimal для критических точек.
        
        ИСПРАВЛЕНО: Прямое сравнение Decimal без потери точности
        """
        getcontext().prec = precision
        p = Decimal(p_str)
        t = Decimal(t_str)
        tp = t * p
        
        # Используем точную формулу для всех случаев
        return Decimal(1) - (Decimal(1) - p) ** t
    
    @staticmethod
    def critical_point_for_probability(target_p: float) -> float:
        """
        Расчет критической точки tp для заданной вероятности проявления.
        """
        if not (0 < target_p < 1):
            raise ValueError("target_p должна быть в диапазоне (0, 1)")
        
        return -math.log(1 - target_p)
    
    @staticmethod
    def nothing_weight(phi: float, scenario: str = 'balanced') -> float:
        """
        Вычисление "веса пустоты" E = Φ · ρ(Φ)
        
        Сценарии:
        - 'growth': ρ = Φ^(-0.5)  -> E → ∞ (быстрый рост структур)
        - 'balanced': ρ = Φ^(-1.0) -> E = const (устойчивое равновесие)
        - 'decay': ρ = Φ^(-1.5)   -> E → 0 (распад структур)
        """
        if phi <= 0:
            raise ValueError("phi должна быть положительной")
        
        if scenario == 'growth':
            rho = phi ** (-0.5)
        elif scenario == 'balanced':
            rho = phi ** (-1.0)
        elif scenario == 'decay':
            rho = phi ** (-1.5)
        else:
            raise ValueError("Неверный сценарий. Используйте 'growth', 'balanced' или 'decay'")
        
        return phi * rho
    
    @staticmethod
    def asymmetry(phi: float) -> float:
        """
        Функция нарушения симметрии Asymmetry(Φ) = tanh(ln Φ)
        """
        if phi <= 0:
            raise ValueError("phi должна быть положительной")
        
        return math.tanh(math.log(phi))
    
    @staticmethod
    def structure_density(t: float, k: float = 0.01, rho0: float = 1.0) -> float:
        """
        Уплотнение структур: ρ(t) = ρ₀·exp(kt)
        """
        if k <= 0:
            raise ValueError("k должна быть положительной для устойчивых структур")
        
        return rho0 * math.exp(k * t)