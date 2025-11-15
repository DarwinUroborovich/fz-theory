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

    This class implements the core mathematical components used in the
    article on FZ Theory: the manifestation probability in a
    pre-existential null domain (PND), critical tp thresholds, high-
    precision discrete analogues of the infinite-attempt process, a
    phenomenological "weight" model for the PND, the asymmetry function
    A(Φ) describing symmetry breaking between non-being and being, and
    a simple densification model ρ(t).

    FIXED:
    - Removed legacy unstable branches.
    - All formulas now use a single, mathematically consistent and
      numerically robust implementation that matches the published
      definitions.
    """

    @staticmethod
    def manifestation_probability(p: float, t: float) -> float:
        """
        Probability of distinction manifestation in the pre-existential
        null domain (PND) in the continuous model.

            P(t,p) = 1 - exp(-tp),

        implemented in a numerically stable form via:

            P = -expm1(-tp)   (since -expm1(-tp) = 1 - exp(-tp)).

        Parameters
        ----------
        p : float
            Probability of a single elementary manifestation
            (0 < p ≤ 1). Conceptually, this is the success probability
            of one "attempt" in the PND.
        t : float
            Measure of the capacity of possible distinctions (t > 0).
            In the theory, this plays the role of a non-metric attempt
            index rather than physical time.

        Returns
        -------
        float
            Manifestation probability (0 ≤ P ≤ 1).

        Raises
        ------
        ValueError
            If p <= 0 or t <= 0 (invalid parameters).
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
    def manifestation_probability_decimal(
        p_str: str,
        t_str: str,
        precision: int = 100
    ) -> Decimal:
        """
        High-precision Decimal version for critical points and discrete
        analogues of the infinite-attempt process.

        Computes the discrete expression

            P(N) = 1 - (1 - p)^N

        exactly (within the specified Decimal precision). For very small
        p and large N this matches, to high accuracy, the continuous
        model

            P(tp) = 1 - exp(-tp),

        with tp ≈ p · N.

        Parameters
        ----------
        p_str : str
            Probability of a single manifestation, as a string for high
            precision (e.g. "1e-20").
        t_str : str
            Measure of potential configurations (interpreted as N),
            as a string (e.g. "4.605170185988092e20").
        precision : int
            Decimal precision (number of significant digits) for the
            calculation.

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
        Compute the critical value of the product tp for a given
        manifestation probability in the continuous model

            P(tp) = 1 - exp(-tp).

        Examples:
            target_p = 0.99  →  tp ≈ ln(100)  ≈ 4.605170185988092
            target_p = 0.999 →  tp ≈ ln(1000) ≈ 6.907755278982137

        Parameters
        ----------
        target_p : float
            Desired manifestation probability (0 < target_p < 1).

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
    def nothing_weight(phi: float, scenario: str = "balanced") -> float:
        """
        Conceptual "weight" of the pre-existential null domain (PND),
        defined as

            E(Φ) = Φ · ρ(Φ),

        where ρ(Φ) is an effective structural density. In the theory,
        different qualitative scenarios for the evolution of the PND are
        captured by different exponents of Φ:

            'growth'    → ρ(Φ) = Φ^(-0.5)
                          → E(Φ) = Φ * Φ^(-0.5) = Φ^(0.5)
                          (diverges as Φ → ∞)

            'balanced'  → ρ(Φ) = Φ^(-1.0)
                          → E(Φ) = Φ * Φ^(-1.0) = 1
                          (remains constant for any Φ)

            'decay'     → ρ(Φ) = Φ^(-1.5)
                          → E(Φ) = Φ * Φ^(-1.5) = Φ^(-0.5)
                          (vanishes as Φ → ∞)

        Parameters
        ----------
        phi : float
            Current potential of nothingness (Φ > 0).
        scenario : str
            Evolution scenario: 'growth', 'balanced', or 'decay'.

        Returns
        -------
        float
            The "weight of the PND" E(Φ) for the given scenario.

        Raises
        ------
        ValueError
            If phi <= 0 or if an invalid scenario name is provided.
        """
        if phi <= 0:
            raise ValueError("phi must be positive")

        if scenario == "growth":
            rho = phi ** -0.5
        elif scenario == "balanced":
            rho = phi ** -1.0
        elif scenario == "decay":
            rho = phi ** -1.5
        else:
            raise ValueError("Invalid scenario: use 'growth', 'balanced', or 'decay'")

        return phi * rho

    @staticmethod
    def asymmetry(phi: float) -> float:
        """
        Symmetry-breaking function defining the emergence of distinction
        between non-being and being as the potential Φ of the PND grows.

        Analytic forms (equivalent):

            A(Φ) = tanh(ln Φ)
                 = (Φ² - 1) / (Φ² + 1)

        Properties:
            - A(1)   = 0
              (perfect symmetry: neither being nor non-being is preferred)
            - A(Φ) →  1    as Φ → ∞
              (maximal bias towards being)
            - A(Φ) → -1    as Φ → 0⁺
              (formal extension towards non-being)

        Parameters
        ----------
        phi : float
            Potential of nothingness (Φ > 0).

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
        Structure density evolution over an abstract evolution parameter t.

        Simple densification model:

            ρ(t) = ρ₀ · exp(k t),

        where ρ(t) can be interpreted as structural density of a world,
        a proto-world, or a nested reality level. This is a toy model
        used in the text to illustrate how "condensation" of reality can
        be described mathematically.

        Parameters
        ----------
        t : float
            Evolution parameter (can be meta-time or any analogous
            measure; not necessarily physical time).
        k : float
            Growth rate (k > 0).
        rho0 : float
            Initial density at t = 0.

        Returns
        -------
        float
            Density ρ(t) at the given t.

        Raises
        ------
        ValueError
            If k <= 0 (growth rate must be positive for exponential
            growth).
        """
        if k <= 0:
            raise ValueError("k must be positive")

        return rho0 * math.exp(k * t)
