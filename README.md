# **FZ THEORY**  
*Self-Saturation of a Pre-Existential Null Domain and the Emergence of Being*  

> Code: numerical verification of the core equations of the FZ Theory  
> Environment: Python + virtual environment (no Docker required)  

---

## 📌 Description (English)

FZ Theory analyzes the emergence of being from what is informally called “nothing”.

In this framework, “nothing” is defined in a strictly technical sense as a **pre-existential null domain (PND)** — a formal ontological condition with:

- no structure,  
- no laws,  
- no degrees of freedom,  
- no metric,  
- no pre-given physical content,  
- no constraints on what may, in principle, be realized.

Because a PND imposes no limitations, it permits an **unbounded sequence of independent trials**, modeled by a **non-metric attempt index** \( t \) (this is *not* physical time, but an abstract measure of how many candidate configurations have been “tried”).

Assuming a non-zero probability \( p > 0 \) that a single trial yields a stable, self-consistent configuration, the probability that at least one manifestation occurs after \( t \) independent attempts is

\[
P(t,p) = 1 - e^{-tp}.
\]

As \( tp \to \infty \), we obtain \( P(t,p) \to 1 \).  
Under an unconstrained null domain with non-zero potentiality, the emergence of at least one stable world thus becomes a **mathematical inevitability**.

Within the full theoretical framework, a world is considered **fully realized** only as part of a **minimal self-consistent pair (MSCP)**:  

- a stable configuration of effective laws and structures,  
- together with a minimal observer capable of distinguishing and registering its boundaries.  

This observer–world pair is the first realized “something” emerging from the PND and provides the basis for further **nested realities** and **condensation** (increasing structural density at subsequent levels of reality).

This repository contains:

- the core implementation of the main FZ equations in `src/core.py` (including the manifestation probability \( P(t,p) \) and related functions);  
- numerical tests in `validation/critical_tests.py` that reproduce the key regimes discussed in the paper (critical thresholds, extreme probabilities, high-precision checks);  
- a LaTeX manuscript with the full theory in `paper/main.tex`;  
- the compiled English PDF of the article (e.g. `paper/main.pdf`), summarizing the complete conceptual and mathematical framework.

---

## 📌 Описание (по-русски)

Теория FZ рассматривает возникновение бытия из состояния, условно называемого «ничто», определяемого в строго техническом смысле как **додекзистенциальная нулевая область (PND, pre-existential null domain)** — формальное онтологическое состояние:

- без структуры,  
- без законов,  
- без степеней свободы,  
- без метрики,  
- без исходного физического содержания,  
- без ограничений на возможные проявления.

Так как такая область не накладывает ограничений, она допускает **неограниченную последовательность независимых попыток**, описываемых **неметрическим индексом попыток** \( t \) (это не физическое время, а абстрактная мера количества “проб” конфигураций).

При ненулевой вероятности возникновения стабильной конфигурации \( p > 0 \) вероятность того, что хотя бы одно успешное проявление произойдёт за \( t \) попыток, задаётся выражением

\[
P(t,p) = 1 - e^{-tp}.
\]

При \( tp \to \infty \) получаем \( P(t,p) \to 1 \).  
Таким образом, в бесконечной додекзистенциальной нулевой области с ненулевой потенциальностью возникновение хотя бы одного стабильного мира становится **математически неизбежным**.

В полном рамках теории мир считается **полностью реализованным** только как часть **минимальной самосогласованной пары (MSCP)**, включающей:

- стабильную конфигурацию законов и структур,  
- минимального наблюдателя, способного различать и фиксировать её границы.  

Эта пара «мир–наблюдатель» представляет собой первое реализованное «что-то» из PND и задаёт основу для последующего появления **вложенных миров** и их **конденсации** (роста структурной плотности на последующих уровнях реальности).

В репозитории:

- реализация ключевых уравнений теории в `src/core.py` (включая вероятность проявления \( P(t,p) \) и связанные функции);  
- юнит-тесты в `validation/critical_tests.py`, воспроизводящие основные режимы, обсуждаемые в статье (критические пороги, экстремальные вероятности, высокоточные проверки);  
- полный LaTeX-текст статьи в `paper/main.tex`;  
- собранный PDF-файл статьи на английском языке (например, `paper/main.pdf`), содержащий полное концептуальное и математическое изложение теории.

---

# 🧪 Verification (run tests + venv + demo)

## 1. Create virtual environment and install dependencies

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run tests
python -m unittest validation.critical_tests

# Optional demo
python demo.py
