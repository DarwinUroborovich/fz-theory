# **FZ THEORY**  
*Self-Saturation of a Pre-Existential Null Domain and the Emergence of Being*  

> Code: numerical verification of the core equations of the FZ Theory  
> Environment: Python + virtual environment (no Docker required)  

---

## 📌 Description (English)

FZ Theory analyzes the emergence of being from what is informally called “nothing”.

In this framework, “nothing” is defined in a strictly technical sense as a **pre-existential null domain (PND)** — a formal condition with:  
- no structure,  
- no laws,  
- no degrees of freedom,  
- no metric,  
- no constraints on what may potentially manifest.

Because a PND imposes no limitations, it permits an **unbounded sequence of independent trials**, modeled by a **non-metric attempt index** \( t \) (not physical time).

Assuming a non-zero probability \( p > 0 \) that a trial yields a stable, self-consistent configuration, the probability that at least one manifestation occurs after \( t \) independent attempts is:
\[
P(t,p) = 1 - e^{-tp}.
\]

As \( tp \to \infty \), we obtain \( P \to 1 \).  
Thus, the emergence of being becomes a **mathematical inevitability** under an unconstrained null domain.

This repository contains:  
- the core FZ equations (`src/core.py`),  
- numerical tests (`validation/critical_tests.py`),  
- the full LaTeX manuscript (`paper/main.tex`).  

---

## 📌 Описание (по-русски)

Теория FZ рассматривает возникновение бытия из состояния, условно называемого «ничто», определяемого как **додекзистенциальная нулевая область (PND)** — формальное состояние:  
- без структуры,  
- без законов,  
- без степеней свободы,  
- без метрики,  
- без ограничений на проявления.

Так как такая область не накладывает ограничений, она допускает **неограниченную последовательность попыток**, описываемых неметрическим индексом \( t \).

При вероятности стабильной конфигурации \( p > 0 \):
\[
P(t,p) = 1 - e^{-tp}.
\]

При \( tp \to \infty \) получаем \( P \to 1 \).  
Возникновение бытия становится **математически неизбежным** при ненулевой вероятности стабильной структуры.

В репозитории:  
- реализация уравнений (`src/core.py`),  
- юнит-тесты (`validation/critical_tests.py`),  
- полная статья (`paper/main.tex`).  

---

# 🧪 Verification (run tests + venv + demo)

## **Create venv + Install + Run Tests + Run Demo (ALL-IN-ONE)**

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run tests
python -m unittest validation.critical_tests

# Optional demo
python demo.py
