from src.core import FZVerifier

verifier = FZVerifier()

# Тест 1: критическая точка 99%
p = 1e-20
t_99 = 4.605170185988092e20
prob_99 = verifier.manifestation_probability(p, t_99)
print(f"Критическая точка 99%: P = {prob_99:.15f}")

# Тест 2: экстремальное значение
p_extreme = 0.1
t_extreme = 1e5
prob_extreme = verifier.manifestation_probability(p_extreme, t_extreme)
print(f"Экстремальное значение: P = {prob_extreme}")

# Тест 3: Decimal
p_dec = "1e-20"
t_dec = "4.605170185988092e20"
prob_dec = verifier.manifestation_probability_decimal(p_dec, t_dec, precision=50)
print(f"Decimal: P = {prob_dec}")
