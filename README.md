# **FZ THEORY**  
*Self-Saturation of Infinite Nothingness and the Evolution of Being*

> Code: numerical verification of the core equations of the FZ Theory  
> Environment: Python + virtual environment (no Docker required)

---

## 📌 Description (English)

The FZ Theory describes the origin of being as an inevitable consequence of the infinite potentiality of “nothingness”.

In this model, **“nothing” is not emptiness**, but a state with:

- infinite potentiality (Φ → ∞),  
- zero initial distinctions,  
- no laws, no structure.

Assuming a non-zero probability \(p > 0\) for a minimal distinction and an unbounded measure \(t\) of potential configurations, the probability that at least one manifestation occurs is:

\[
P(t,p) = 1 - e^{-tp},
\]

so that \(P \to 1\) as \(tp \to \infty\).  
Being is therefore **mathematically inevitable** in an infinite nothingness with non-zero potential.

The repository contains:

- core implementation of the main FZ equations (`src/core.py`);  
- unit tests validating numerical behavior (`validation/critical_tests.py`);  
- a LaTeX manuscript with the full theory (`paper/main.tex`).  

---

## 📌 Описание (по-русски)

Теория FZ описывает происхождение бытия как **неизбежное следствие** бесконечной потенциальности «ничто».

В этой модели **«ничто» — не пустота**, а состояние с:

- бесконечной потенциальностью (Φ → ∞),  
- нулём исходных различий,  
- отсутствием законов и структуры.

Если вероятность минимального различия \(p > 0\), а мера возможных конфигураций \(t\) бесконечна, тогда вероятность хотя бы одного проявления:

\[
P(t,p) = 1 - e^{-tp},
\]

и при \(t p \to \infty\) мы получаем \(P \to 1\).  
То есть бытие в бесконечном «ничто» с ненулевой потенциальностью — **не случайность, а математическая неизбежность**.

В репозитории:

- реализация ключевых уравнений теории (`src/core.py`);  
- юнит-тесты для проверки численной устойчивости (`validation/critical_tests.py`);  
- LaTeX-статья с полным изложением теории (`paper/main.tex`).  

---

## 🧪 Verification (run tests)

**Prerequisites:**

- Python 3.10+ installed  
- Git installed  

### 1. Clone the repository

```bash
git clone https://github.com/DarwinUroborovich/fz-theory.git
cd fz-theory
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run tests

```bash
python -m unittest validation.critical_tests
```

If all tests pass (OK), the environment is correctly reproduced and the core equations are verified.

### 4. (Optional) Run demonstration script

```bash
python demo.py
```

This will output example calculations (critical points, extreme cases, high-precision verification) and display a simple plot showing how the manifestation probability  
\( P(t,p) \) saturates toward 1 as \( t p \) increases.

---
