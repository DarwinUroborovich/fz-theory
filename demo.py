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
