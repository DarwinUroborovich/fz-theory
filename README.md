# **FZ THEORY**  
*Self-Saturation of Infinite Nothingness and the Evolution of Being*

[![Verification Status](https://github.com/DarwinUroborovich/fz-theory/actions/workflows/verification.yml/badge.svg)](https://github.com/DarwinUroborovich/fz-theory/actions)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.98765432.svg)](https://doi.org/10.5281/zenodo.98765432)

---

## 📌 Description (English)

The FZ Theory describes the origin of Being as an inevitable consequence of the infinite potentiality of “Nothing”.  
In the FZ model, “nothing” is not simple emptiness, but a state with infinite capacity for possible manifestations and zero initial distinctions.

Key result: **mathematical verification of the critical manifestation point**  
\[
\tau = t \cdot p = 4.60517
\]  
at which the probability of a distinction emerging reaches **99%**:
\[
P = 1 - e^{-\tau} = 0.99.
\]

The repository contains:

- a numerically stable implementation of the core equations;
- automated tests for critical thresholds and asymptotic regimes;
- LaTeX source for the FZ Theory paper (for arXiv submission).

---

## 📌 Описание (Russian)

Теория FZ описывает происхождение Бытия как неизбежное следствие бесконечной потенциальности «Ничто».  
В модели FZ «ничто» — это не просто пустота, а состояние с бесконечной мощностью возможных проявлений и нулевым набором исходных различий.

Ключевой результат: **математическая верификация критической точки проявления**  
\[
\tau = t \cdot p = 4.60517,
\]  
при которой вероятность возникновения различия достигает **99%**:
\[
P = 1 - e^{-\tau} = 0.99.
\]

Репозиторий содержит:

- численно устойчивую реализацию основных уравнений;
- автоматические тесты для критических точек и асимптотик;
- LaTeX-исходник статьи по Теории FZ (для arXiv).

---

## 🧪 Verification

The repository includes automated tests validating:

- the critical manifestation threshold \(\tau_{\mathrm{crit}} = 4.60517\);  
- asymptotic behavior for large \(t \cdot p\);  
- high-precision Decimal checks;  
- numerical stability of all core equations.

Run verification (from the project root):

```bash
python -m unittest validation.critical_tests
