tp = t * p
prob = -np.expm1(-tp)  # 1 - exp(-tp) для ВСЕХ случаев
return min(1.0, max(0.0, prob))  # Защита от артефактов