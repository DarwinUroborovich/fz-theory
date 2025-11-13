import numpy as np
import math
from decimal import Decimal, getcontext
from typing import Union

# Default precision for Decimal calculations
DEFAULT_PRECISION = 100
getcontext().prec = DEFAULT_PRECISION


class FZVerifier:
    """
    FZ Theory verification toolkit with numerically stable implementations.

    FIXED: Removed unstable Level 2 branch. All formulas now use the single,
    mathematically correct and numerically robust method.
    """

    @staticmethod
    def manifestation_probability(p: float, t: float) -> float:
        """
        Probability of distinction manifestation in infinite nothingness.

        Stable formulation:
            P = 1 - exp(-tp)
        implemented as:
            P = -expm1(-tp)

        Parameters
        ----------
        p : float
            Probability of a single elementary manifestation (0 < p ≤ 1)
        t : float
            Measure of the capacity of possible distinctions (t > 0)

        Returns
        -------
        float
            Manifestation probability (0 ≤ P ≤ 1)
        """
        if p <= 0 or t <= 0:
            raise ValueError("p and t must be positive")

        tp = t * p

        # Robust for all scales:
        #   expm1(x) = exp(x) - 1
        #   -expm1(-tp) = 1 - exp(-tp)
        prob = -np.expm1(-tp)

        # Clamp numerical artifacts
        return min(1.0, max(0.0, prob))

    @staticmethod
    def manifestation_probability_decimal(
        p_str: str,
        t_str: str,
        precision: int = 100
    ) -> Decimal:
        """
        High-precision Decimal version for critical points.

        No approximation — exact exponentiation using:
            P = 1 - (1 - p)^t
        """
        getcontext().prec = precision

        p = Decimal(p_str)
        t = Decimal(t_str)
        return Decimal(1) - (Decimal(1) - p) ** t

    @staticmethod
    def critical_point_for_probability(target_p: float) -> float:
        """
        Compute critical tp value for a given manifestation probability.

        Formula:
            tp = -ln(1 - P)
        """
        if not (0 < target_p < 1):
            raise ValueError("target_p must be in (0, 1)")

        return -math.log(1 - target_p)

    @staticmethod
    def nothing_weight(phi: float, scenario: str = 'balanced') -> float:
        """
        Weight of Nothingness: E = Φ · ρ(Φ)

        Scenarios:
            'growth'    → ρ = Φ^(-0.5)  → E → ∞
            'balanced'  → ρ = Φ^(-1.0) → E = const
            'decay'     → ρ = Φ^(-1.5) → E → 0
        """
        if phi <= 0:
            raise ValueError("phi must be positive")

        if scenario == 'growth':
            rho = phi ** (-0.5)
        elif scenario == 'balanced':
            rho = phi ** (-1.0)
        elif scenario == 'decay':
            rho = phi ** (-1.5)
        else:
            raise ValueError("Invalid scenario: use 'growth', 'balanced', or 'decay'")

        return phi * rho

    @staticmethod
    def asymmetry(phi: float) -> float:
        """
        Symmetry-breaking function:
            Asymmetry(Φ) = tanh(ln Φ)
        """
        if phi <= 0:
            raise ValueError("phi must be positive")

        return math.tanh(math.log(phi))

    @staticmethod
    def structure_density(t: float, k: float = 0.01, rho0: float = 1.0) -> float:
        """
        Structure density evolution:
            ρ(t) = ρ₀ · exp(kt)
        """
        if k <= 0:
            raise ValueError("k must be positive")

        return rho0 * math.exp(k * t)
