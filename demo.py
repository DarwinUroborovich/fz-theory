from src.core import FZVerifier

"""
Demonstration script for FZ Theory numerical components.

- Computes sample manifestation probabilities P(t,p) in the
  pre-existential null domain (PND).
- Shows a high-precision Decimal check for a critical point (P ≈ 0.99).
- Optionally plots P(tp) = 1 - exp(-tp) together with critical
  thresholds for P = 0.99 and P = 0.999, as used in the article.
"""

verifier = FZVerifier()

# Test 1: 99% critical point (continuous model)
p = 1e-20
t_99 = 4.605170185988092e20
prob_99 = verifier.manifestation_probability(p, t_99)
print(f"Critical Point 99%: P = {prob_99:.15f}")

# Test 2: Extreme value (saturation to 1)
p_extreme = 0.1
t_extreme = 1e5
prob_extreme = verifier.manifestation_probability(p_extreme, t_extreme)
print(f"Extreme Case: P = {prob_extreme}")

# Test 3: Decimal precision test (discrete analogue)
p_dec = "1e-20"
t_dec = "4.605170185988092e20"
prob_dec = verifier.manifestation_probability_decimal(p_dec, t_dec, precision=50)
print(f"Decimal High Precision: P = {prob_dec}")

# Demonstration: Plot manifestation probability curve P(tp) = 1 - exp(-tp)
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Matplotlib is not installed; skipping graph demonstration.")
else:
    # Compute P for a range of tp values (here p=1.0 so tp = t)
    xs = [0.0] + [x * 0.1 for x in range(1, 101)]
    ys = [0.0] + [verifier.manifestation_probability(1.0, x) for x in xs[1:]]

    plt.figure()
    plt.plot(xs, ys, label="$P(tp) = 1 - e^{-tp}$")

    # Mark critical points for 99% and 99.9%
    crit99 = verifier.critical_point_for_probability(0.99)   # ~4.6052
    crit999 = verifier.critical_point_for_probability(0.999) # ~6.9078

    plt.axhline(0.99, linestyle="--", label="P=0.99")
    plt.axvline(crit99, linestyle="--", label=f"tp={crit99:.2f}")
    plt.axhline(0.999, linestyle=":", label="P=0.999")
    plt.axvline(crit999, linestyle=":", label=f"tp={crit999:.2f}")

    plt.xlabel("tp (dimensionless product)")
    plt.ylabel("P (manifestation probability)")
    plt.title("Manifestation Probability vs tp (FZ Theory)")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("manifestation_probability_curve.png")
    print("Saved plot to manifestation_probability_curve.png")

    try:
        plt.show()
    except Exception:
        pass
