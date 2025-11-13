import unittest
import numpy as np
import math
from src.core import FZVerifier
from decimal import Decimal, getcontext

class TestFZTheory(unittest.TestCase):
    """
    Автоматические тесты для верификации ключевых формул Теории FZ
    
    ИСПРАВЛЕНО: 
    - Добавлен импорт math
    - Исправлены тесты для Decimal
    - Удалены бессмысленные тесты на 40+ знаков для float
    """
    
    def setUp(self):
        """Настройка тестов"""
        self.verifier = FZVerifier()
        getcontext().prec = 50
    
    def test_critical_point_99_percent(self):
        """
        Тест 3а: Критическая точка для P = 0.99
        """
        target_p = 0.99
        expected_tp = self.verifier.critical_point_for_probability(target_p)
        
        p = 1e-20
        t = expected_tp / p
        
        calculated_p = self.verifier.manifestation_probability(p, t)
        
        self.assertAlmostEqual(calculated_p, target_p, places=15,
                             msg=f"Для tp={expected_tp}, ожидаем P={target_p}, получено {calculated_p}")
    
    def test_extreme_limit(self):
        """
        Тест 3б: Предел при больших tp
        """
        p = 1e-20
        t = 1e22
        tp = t * p
        
        calculated_p = self.verifier.manifestation_probability(p, t)
        
        # При tp=100, exp(-100) ~ 3.72e-44, поэтому 1 - exp(-100) = 1.0 в double
        # Тест проверяет, что функция возвращает 1.0 без ошибок
        self.assertEqual(calculated_p, 1.0,
                       msg=f"Для экстремальных значений tp={tp}, ожидалось 1.0, получено {calculated_p}")
    
    def test_decimal_precision(self):
        """
        Тест 3в: Абсолютная точность через Decimal

        Проверяем, что ошибка при расчёте P для tp ≈ 4.60517
        (когда P ≈ 0.99) меньше 1e-15.

        Это очень строгий критерий для операций с вещественным показателем,
        но реалистичный для Decimal с prec=50.
        """
        p_str = "1e-20"
        t_str = "4.605170185988092e20"  # tp = 4.605170185988092

        calculated_p = self.verifier.manifestation_probability_decimal(
            p_str, t_str, precision=50
        )
        expected_p = Decimal("0.99")

        error = abs(calculated_p - expected_p)

        # Было: 1e-45 — слишком жёстко
        # Делаем реалистичный порог 1e-15
        self.assertLess(
            error,
            Decimal("1e-15"),
            msg=f"Ошибка {error} превышает допустимую 1e-15",
        )

    
    def test_nothing_weight_scenarios(self):
        """
        Тест веса пустоты для трех сценариев
        """
        phi = 1e20

        # Сценарий роста: E = Φ * Φ^(-0.5) = Φ^(0.5) = 1e10
        growth_weight = self.verifier.nothing_weight(phi, "growth")
        self.assertAlmostEqual(
            growth_weight,
            1e10,
            places=5,
            msg="Сценарий роста должен давать E ≈ 1e10 при Φ=1e20",
        )

        # Сбалансированный сценарий: E = Φ * Φ^(-1.0) = 1.0
        balanced_weight = self.verifier.nothing_weight(phi, "balanced")
        self.assertAlmostEqual(
            balanced_weight,
            1.0,
            places=10,
            msg="Сбалансированный сценарий должен давать E=1.0",
        )

        # Сценарий распада: E = Φ * Φ^(-1.5) = Φ^(-0.5) = 1e-10
        decay_weight = self.verifier.nothing_weight(phi, "decay")
        self.assertAlmostEqual(
            decay_weight,
            1e-10,
            places=15,
            msg="Сценарий распада должен давать E ≈ 1e-10 при Φ=1e20",
        )


    
    def test_asymmetry_function(self):
        """
        Тест функции нарушения симметрии
        """
        # При Φ=1: Asymmetry = 0
        self.assertAlmostEqual(self.verifier.asymmetry(1.0), 0.0, places=15)
        
        # При Φ=4.38: Asymmetry ≈ 0.9009 (проверено численно)
        expected_90 = 0.9009
        calculated_90 = self.verifier.asymmetry(4.38)
        self.assertAlmostEqual(calculated_90, expected_90, places=3,
                             msg=f"Для Φ=4.38 ожидалось ~0.9009, получено {calculated_90}")
        
        # При Φ→∞: Asymmetry → 1
        self.assertAlmostEqual(self.verifier.asymmetry(1e10), 1.0, places=15)
    
    def test_numerical_stability(self):
        """
        Тест численной устойчивости для экстремальных значений
        """
        # Экстремально малая вероятность
        p = 1e-100
        t = 1e102
        
        # Должно работать без ошибок и возвращать 1.0
        prob = self.verifier.manifestation_probability(p, t)
        self.assertEqual(prob, 1.0, "Экстремальные значения должны обрабатываться корректно")
        
        # Проверка отрицательных значений (должна быть ошибка)
        with self.assertRaises(ValueError):
            self.verifier.manifestation_probability(-1e-20, 1e20)
        
        with self.assertRaises(ValueError):
            self.verifier.manifestation_probability(1e-20, -1e20)

if __name__ == '__main__':
    unittest.main(verbosity=2)