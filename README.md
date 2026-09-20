<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=20,6,11&height=120&text=Pattern%20Hitting%20Time&fontSize=36&fontColor=fff&desc=Markov%20Chain%20Analysis%20of%20Coin-Toss%20Patterns&descSize=14&descAlignY=75&fontAlignY=38" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white)](https://matplotlib.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

</div>

---

## The Puzzle

Why does **"HT"** appear faster than **"HH"** in fair coin tosses?

```
Expected steps to see "HT"  →  4 steps
Expected steps to see "HH"  →  6 steps
```

> Both patterns have the same per-step probability — yet one takes 50% longer to appear. This is a classic result in **stochastic processes** and is deeply relevant to **quant finance** (e.g., pattern recognition in price sequences, first-passage times in trading signals).

---

## The Intuition

At first glance, HT and HH seem equally likely. The difference lies in **self-overlap**.

| Pattern | Overlaps with itself? | Consequence |
|:--------|:---------------------|:------------|
| `HH` | ✅ Yes — a partial HH can seed the next HH | Process doesn't fully reset → longer wait |
| `HT` | ❌ No — after a failed attempt, clean restart | Process resets cleanly → shorter wait |

For example, in the sequence `HHH`:
- After seeing the first `H`, you already have a partial match for the **next** `HH`
- This means every failure partially advances the next attempt — making the expected wait longer, not shorter

---

## Mathematical Framework

This is computed using **Markov Chain hitting times**.

### State Space for "HH"

```
States: {∅, H, HH}
        ↑        ↑
    start    absorbing

Transitions:
  ∅ --H(½)--> H
  ∅ --T(½)--> ∅
  H --H(½)--> HH  ← absorb
  H --T(½)--> ∅   ← full reset
```

### Expected Hitting Time

Let **E_s** = expected steps to reach `HH` from state `s`:

```
E_∅ = 1 + ½·E_H + ½·E_∅
E_H = 1 + ½·0   + ½·E_∅

Solving: E_∅ = 6
```

For pattern `HT`, the equivalent system gives **E_∅ = 4**.

---

## What I Did

- **Modeled** the problem as a Markov chain with states representing partial pattern matches
- **Analytically solved** the linear system of expected value equations
- **Simulated** repeated coin-toss sequences to empirically measure hitting times
- **Averaged** over many trials to confirm theoretical predictions
- **Visualized** the distribution of hitting times for multiple patterns

---

## Key Concept

> **Hitting Time** — the first time a stochastic process reaches a given state or pattern. Fundamental in:
> - Option pricing (barrier options, first-passage pricing)
> - Algorithmic trading (signal detection latency)
> - Risk management (drawdown analysis)

---

## Running the Code

```bash
git clone https://github.com/abhilash9844/pattern-hitting-time-quant.git
cd pattern-hitting-time-quant
pip install numpy matplotlib
python simulation.py
```

---

## Visualizations

### Pattern vs Expected Hitting Time

> *(See `/plots/` directory for generated charts)*

---

## Why This Matters (Quant Perspective)

In financial time-series, the analogous question is:
*"How long until a price process first hits a level, or a chart pattern completes?"*

This is the **first-passage time** problem — the backbone of barrier option pricing and technical analysis validation.

---

<div align="center">

**[⬅ Back to Profile](https://github.com/abhilash9844)**

*Built with curiosity and Markov chains*

</div>
