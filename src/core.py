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

    FIXED: Removed unstable Level 2 branch. All formulas now use a single,
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

        Raises
        ------
        ValueError
            If p <= 0 or t <= 0 (invalid parameters)
        """
        if p <= 0 or t <= 0:
            raise ValueError("p and t must be positive")

        tp = t * p

        # Robust for all scales:
        #   expm1(x) = exp(x) - 1
        #   -expm1(-tp) = 1 - exp(-tp)
        prob = -np.expm1(-tp)

        # Clamp numerical artifacts to [0, 1]
        return min(1.0, max(0.0, prob))

    @staticmethod
    def manifestation_probability_decimal(p_str: str, t_str: str, precision: int = 100) -> Decimal:
        """
        High-precision Decimal version for critical points.

        Computes P = 1 - (1 - p)^t exactly (within the specified precision).

        Parameters
        ----------
        p_str : str
            Probability of a single manifestation, as a string for high precision (e.g. "1e-20").
        t_str : str
            Measure of potential configurations, as a string (e.g. "4.605170185988092e20").
        precision : int
            Decimal precision (number of significant digits) for the calculation.

        Returns
        -------
        Decimal
            Manifestation probability as a Decimal object.

        Raises
        ------
        ValueError
            If p_str or t_str represent non-positive values.
        """
        getcontext().prec = precision

        p = Decimal(p_str)
        t = Decimal(t_str)
        if p <= 0 or t <= 0:
            raise ValueError("p and t must be positive")

        # Exact computation using Decimal:
        return Decimal(1) - (Decimal(1) - p) ** t

    @staticmethod
    def critical_point_for_probability(target_p: float) -> float:
        """
        Compute the critical value of the product tp for a given manifestation probability
        in the continuous model

            P(tp) = 1 - exp(-tp).

        For example:
            target_p = 0.99 → tp ≈ 4.605170185988092 (ln 100),
            target_p = 0.999 → tp ≈ 6.907755278982137 (ln 1000).

        Parameters
        ----------
        target_p : float
            Desired manifestation probability (0 < target_p < 1)

        Returns
        -------
        float
            The value of tp at which P = target_p.

        Raises
        ------
        ValueError
            If target_p is not in the interval (0, 1).
        """
        if not (0 < target_p < 1):
            raise ValueError("target_p must be in (0, 1)")

        return -math.log(1 - target_p)


    @staticmethod
    def nothing_weight(phi: float, scenario: str = 'balanced') -> float:
        """
        Weight of Nothingness: E = Φ · ρ(Φ)

        Based on different evolution scenarios for the "nothingness" state:
            'growth'    → ρ(Φ) = Φ^(-0.5)  → E = Φ * Φ^(-0.5) = Φ^0.5  (diverges as Φ → ∞)
            'balanced'  → ρ(Φ) = Φ^(-1.0)  → E = Φ * Φ^(-1.0) = 1      (constant for any Φ)
            'decay'     → ρ(Φ) = Φ^(-1.5)  → E = Φ * Φ^(-1.5) = Φ^(-0.5) (vanishes as Φ → ∞)

        Parameters
        ----------
        phi : float
            Current potential of nothingness (Φ > 0)
        scenario : str
            Evolution scenario: 'growth', 'balanced', or 'decay'

        Returns
        -------
        float
            The "weight of nothingness" E for the given scenario.

        Raises
        ------
        ValueError
            If phi <= 0 or if an invalid scenario name is provided.
        """
        if phi <= 0:
            raise ValueError("phi must be positive")

        if scenario == 'growth':
            rho = phi ** -0.5
        elif scenario == 'balanced':
            rho = phi ** -1.0
        elif scenario == 'decay':
            rho = phi ** -1.5
        else:
            raise ValueError("Invalid scenario: use 'growth', 'balanced', or 'decay'")

        return phi * rho

    @staticmethod
    def asymmetry(phi: float) -> float:
        """
        Symmetry-breaking function defining the emergence of distinction.

        Analytic forms:
            Asymmetry(Φ) = tanh(ln Φ)
                         = (Φ² - 1) / (Φ² + 1)

        Properties:
            - Asymmetry(1)   = 0   (perfect symmetry: neither being nor non-being is preferred)
            - Asymmetry(Φ) → 1    as Φ → ∞ (maximal bias towards being)
            - Asymmetry(Φ) → -1   as Φ → 0⁺ (formal extension towards non-being)

        Parameters
        ----------
        phi : float
            Potential of nothingness (Φ > 0)

        Returns
        -------
        float
            Asymmetry measure in the range (-1, 1).

        Raises
        ------
        ValueError
            If phi <= 0 (undefined for non-positive Φ).
        """
        if phi <= 0:
            raise ValueError("phi must be positive")

        # tanh(log Φ) ≡ (Φ² - 1) / (Φ² + 1)
        return math.tanh(math.log(phi))


    @staticmethod
    def structure_density(t: float, k: float = 0.01, rho0: float = 1.0) -> float:
        """
        Structure density evolution over "time" t.

        Model:
            ρ(t) = ρ₀ · exp(k t)

        Parameters
        ----------
        t : float
            Evolution parameter (usually time or analogous measure)
        k : float
            Growth rate (k > 0)
        rho0 : float
            Initial density at t=0

        Returns
        -------
        float
            Density at time t.

        Raises
        ------
        ValueError
            If k <= 0 (growth rate must be positive for exponential growth).
        """
        if k <= 0:
            raise ValueError("k must be positive")

        return rho0 * math.exp(k * t)
