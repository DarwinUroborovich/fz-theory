from src.core import FZVerifier

verifier = FZVerifier()

# Test 1: 99% critical point
p = 1e-20
t_99 = 4.605170185988092e20
prob_99 = verifier.manifestation_probability(p, t_99)
print(f"Critical Point 99%: P = {prob_99:.15f}")

# Test 2: Extreme value
p_extreme = 0.1
t_extreme = 1e5
prob_extreme = verifier.manifestation_probability(p_extreme, t_extreme)
print(f"Extreme Case: P = {prob_extreme}")

# Test 3: Decimal precision test
p_dec = "1e-20"
t_dec = "4.605170185988092e20"
prob_dec = verifier.manifestation_probability_decimal(p_dec, t_dec, precision=50)
print(f"Decimal High Precision: P = {prob_dec}")

# Demonstration: Plot manifestation probability curve
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Matplotlib is not installed; skipping graph demonstration.")
else:
    # Compute P for a range of tp values
    xs = [0.0] + [x * 0.1 for x in range(1, 101)]
    ys = [0.0] + [verifier.manifestation_probability(1.0, x) for x in xs[1:]]
    plt.figure()
    plt.plot(xs, ys, label="$P = 1 - e^{-tp}$")
    # Mark critical points for 99% and 99.9%
    crit99 = verifier.critical_point_for_probability(0.99)  # ~4.6052
    crit999 = verifier.critical_point_for_probability(0.999)  # ~6.9078
    plt.axhline(0.99, color='gray', linestyle='--', label='P=0.99')
    plt.axvline(crit99, color='gray', linestyle='--', label=f"tp={crit99:.2f}")
    plt.axhline(0.999, color='gray', linestyle=':', label='P=0.999')
    plt.axvline(crit999, color='gray', linestyle=':', label=f"tp={crit999:.2f}")
    plt.xlabel("tp (dimensionless product)")
    plt.ylabel("P (manifestation probability)")
    plt.title("Manifestation Probability vs tp")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("manifestation_probability_curve.png")
    print("Saved plot to manifestation_probability_curve.png")
    try:
        plt.show()
    except Exception:
        pass
