import unittest
import numpy as np
import math
from decimal import Decimal, getcontext

from src.core import FZVerifier


class TestFZTheory(unittest.TestCase):
    """
    English:
    Automated unit tests for verifying the core mathematical components
    of the FZ Theory in its current formal formulation: manifestation
    probability in a pre-existential null domain (PND), critical tp
    thresholds for P(t,p) = 1 - exp(-tp), asymptotic limits, high-
    precision Decimal calculations, structural weight scenarios and
    the asymmetry function A(Φ) used in the paper.

    Русский:
    Автоматические юнит-тесты для проверки ключевых математических
    компонентов Теории FZ в её текущей формализации: вероятность
    проявления в додекзистенциальной нулевой области (PND),
    критические значения tp для P(t,p) = 1 - exp(-tp), асимптотические
    пределы, высокоточная Decimal-арифметика, сценарии весовой
    функции и функция асимметрии A(Φ), используемая в статье.
    """

    def setUp(self):
        """
        English:
        Initialize the verifier and high-precision Decimal context.

        Русский:
        Инициализация проверяющего класса и установка высокой точности
        для Decimal-вычислений.
        """
        self.verifier = FZVerifier()
        getcontext().prec = 50

    def test_critical_point_99_percent(self):
        """
        English:
        Test the critical point where P = 0.99 in the continuous model

            P(tp) = 1 - exp(-tp),

        ensuring numerical correctness of tp = -ln(1 - 0.99) and its
        implementation via manifestation_probability(p, t) with
        tp = p * t.

        Русский:
        Проверка критической точки при P = 0.99 в непрерывной модели

            P(tp) = 1 - exp(-tp),

        убеждаемся, что tp = -ln(1 - 0.99) корректно воспроизводится
        через manifestation_probability(p, t), где tp = p * t.
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
        Asymptotic behavior for very large tp in the PND. When tp is
        sufficiently high, P(t,p) must saturate to 1.0 in double
        precision.

        Русский:
        Асимптотическое поведение при очень больших tp в PND. При
        достаточно больших значениях произведения tp вероятность
        P(t,p) должна насыщаться до 1.0 в double precision.
        """
        p = 1e-20
        t = 1e22
        calculated_p = self.verifier.manifestation_probability(p, t)

        self.assertEqual(calculated_p, 1.0)

    def test_decimal_precision(self):
        """
        English:
        High-precision verification using Decimal for a discrete analogue
        of the infinite-attempt process:

            P(N) = 1 - (1 - p)^N

        with p = 1e-20 and N ≈ 4.605170185988092e20, where P ≈ 0.99.
        This matches, to high precision, the continuous expression
        P(tp) = 1 - exp(-tp) with tp ≈ ln(100).

        Русский:
        Высокоточная проверка через Decimal для дискретного аналога
        процесса бесконечных попыток:

            P(N) = 1 - (1 - p)^N

        при p = 1e-20 и N ≈ 4.605170185988092e20, где P ≈ 0.99.
        Это с высокой точностью соответствует непрерывному выражению
        P(tp) = 1 - exp(-tp) при tp ≈ ln(100).
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
        Verification of the structural weight function E(Φ) = Φ · ρ(Φ)
        for three conceptual scenarios of the pre-existential null
        domain (PND): growth, balanced and decay. These correspond to
        different asymptotic behaviors of the effective “weight” as
        Φ → ∞.

        Русский:
        Проверка весовой функции E(Φ) = Φ · ρ(Φ) для трёх концептуальных
        сценариев додекзистенциальной нулевой области (PND): рост,
        баланс и распад. Они соответствуют различному асимптотическому
        поведению эффективного «веса» при Φ → ∞.
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
        Tests the asymmetry function A(Φ), which in the paper is given
        as

            A(Φ) = (Φ² - 1) / (Φ² + 1),

        and is here implemented in the equivalent analytic form
        A(Φ) = tanh(ln Φ). We check symmetry at Φ = 1, an intermediate
        regime around Φ ≈ 4.38 (A ≈ 0.9009) and near-complete bias for
        Φ → ∞.

        Русский:
        Тест функции асимметрии A(Φ), которая в статье задаётся как

            A(Φ) = (Φ² - 1) / (Φ² + 1),

        а здесь реализована в эквивалентной аналитической форме
        A(Φ) = tanh(ln Φ). Проверяем симметрию при Φ = 1, промежуточный
        режим около Φ ≈ 4.38 (A ≈ 0.9009) и практически полную
        асимметрию при Φ → ∞.
        """
        self.assertAlmostEqual(self.verifier.asymmetry(1.0), 0.0, places=15)

        calc_val = self.verifier.asymmetry(4.38)
        self.assertAlmostEqual(calc_val, 0.9009, places=3)

        self.assertAlmostEqual(self.verifier.asymmetry(1e10), 1.0, places=15)

    def test_numerical_stability(self):
        """
        English:
        Stress-tests numerical stability for extreme parameter values in
        the manifestation probability, including very large tp and
        validation of error handling for invalid inputs (p <= 0 or
        t <= 0).

        Русский:
        Стресс-тесты численной устойчивости для экстремальных значений
        в вероятности проявления, включая очень большие tp и проверку
        корректной обработки некорректных входов (p <= 0 или t <= 0).
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
