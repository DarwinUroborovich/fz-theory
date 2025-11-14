import unittest
import numpy as np
import math
from decimal import Decimal, getcontext

from src.core import FZVerifier

class TestFZTheory(unittest.TestCase):
    """
    English:
    Automated unit tests for verifying the core mathematical components
    of the FZ Theory. Tests cover critical probability thresholds,
    asymptotic limits, high-precision Decimal calculations, structural
    weight functions and numerical stability.

    Русский:
    Автоматические юнит-тесты для проверки ключевых математических
    компонентов Теории FZ. Тесты охватывают критические вероятностные
    точки, асимптотические пределы, высокоточную Decimal-арифметику,
    структурные весовые функции и численную устойчивость.
    """

    def setUp(self):
        """Initialize verifier and high-precision context (EN/RU) — Инициализация и высокий precision."""
        self.verifier = FZVerifier()
        getcontext().prec = 50

    def test_critical_point_99_percent(self):
        """
        English:
        Test the critical point where P = 0.99, ensuring numerical
        correctness for tp = -ln(1 - 0.99).

        Русский:
        Проверка критической точки при P = 0.99. Убеждаемся, что tp =
        -ln(1 - 0.99) даёт корректную численную оценку.
        """
        target_p = 0.99
        critical_tp = self.verifier.critical_point_for_probability(target_p)

        p = 1e-20
        t = critical_tp / p
        calculated_p = self.verifier.manifestation_probability(p, t)

        self.assertAlmostEqual(
            calculated_p, target_p, places=15
        )

    def test_extreme_limit(self):
        """
        English:
        Asymptotic behavior for very large tp. When tp is sufficiently
        high, P must saturate to 1.0 in double precision.

        Русский:
        Асимптотическое поведение при больших tp. При достаточно больших
        значениях вероятность должна насыщаться до 1.0.
        """
        p = 1e-20
        t = 1e22
        calculated_p = self.verifier.manifestation_probability(p, t)

        self.assertEqual(calculated_p, 1.0)

    def test_decimal_precision(self):
        """
        English:
        High-precision verification using Decimal for tp ≈ ln(100)
        where P ≈ 0.99.

        Русский:
        Высокоточная проверка через Decimal для tp ≈ ln(100),
        когда вероятность ≈ 0.99.
        """
        p_str = "1e-20"
        t_str = "4.605170185988092e20"

        calculated_p = self.verifier.manifestation_probability_decimal(
            p_str, t_str, precision=50
        )
        expected_p = Decimal("0.99")

        error = abs(calculated_p - expected_p)
        self.assertLess(error, Decimal("1e-15"))

    def test_nothing_weight_scenarios(self):
        """
        English:
        Verification of structural weight functions for growth, balance
        and decay scenarios.

        Русский:
        Проверка весовых функций трёх сценариев: рост, баланс, распад.
        """
        phi = 1e20

        growth_weight = self.verifier.nothing_weight(phi, "growth")
        self.assertAlmostEqual(growth_weight, 1e10, places=5)

        balanced_weight = self.verifier.nothing_weight(phi, "balanced")
        self.assertAlmostEqual(balanced_weight, 1.0, places=10)

        decay_weight = self.verifier.nothing_weight(phi, "decay")
        self.assertAlmostEqual(decay_weight, 1e-10, places=15)

    def test_asymmetry_function(self):
        """
        English:
        Tests the asymmetry function for symmetry preservation, middle
        regime and near-full asymmetry.

        Русский:
        Тест функции асимметрии: полная симметрия, промежуточный режим,
        почти полная асимметрия.
        """
        self.assertAlmostEqual(self.verifier.asymmetry(1.0), 0.0, places=15)

        calc_val = self.verifier.asymmetry(4.38)
        self.assertAlmostEqual(calc_val, 0.9009, places=3)

        self.assertAlmostEqual(self.verifier.asymmetry(1e10), 1.0, places=15)

    def test_numerical_stability(self):
        """
        English:
        Stress-tests numerical stability for extreme parameter values,
        including very large tp and validation of error handling.

        Русский:
        Стресс-тесты численной устойчивости для экстремальных значений,
        включая большие tp и корректную обработку ошибок.
        """
        p = 1e-100
        t = 1e102
        prob = self.verifier.manifestation_probability(p, t)
        self.assertEqual(prob, 1.0)

        with self.assertRaises(ValueError):
            self.verifier.manifestation_probability(-1e-20, 1e20)
        with self.assertRaises(ValueError):
            self.verifier.manifestation_probability(1e-20, -1e20)

if __name__ == '__main__':
    unittest.main(verbosity=2)
