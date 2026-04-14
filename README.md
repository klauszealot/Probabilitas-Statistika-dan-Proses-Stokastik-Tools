# Probability, Statistics, and Stochastic Processes Tools

A comprehensive Desktop GUI application for solving mathematical problems in Probability, Statistics, and Stochastic Processes. This tool is built using **Python**, **Tkinter**, **SciPy**, and **NumPy**.

## 🚀 Key Features

- **Intuitive Tabbed Interface:** Categorized modules for ease of use (Probability, Distributions, Sampling, Hypothesis, ANOVA).
- **Dynamic Input Parameters:** Effortlessly input variables like $n, r, p, \mu, \sigma$.
- **Instant Execution:** Supports keyboard "Enter" confirmation for quick calculations.
- **Scrollable Bento UI:** Modern and clean layout with horizontal input rows.
- **Robust Error Handling:** Validates mathematical domains, preventing crashes on zero-division or invalid inputs.

## 📊 Implemented Formulas

### 1. Probability & Combinatorics
- Basic Probability: $P(A) = n/N$
- Addition Rules (Disjoint & General)
- Conditional Probability: $P(B|A)$
- Bayes' Theorem (2-Point Analysis)
- Permutations ($nP_r$) & Combinations ($nC_r$)
- Expected Value $E(X)$ & Variance $\sigma^2$ (Discrete Random Variables)

### 2. Probability Distributions
- Binomial: $b(x; n, p)$ (PMF, Mean, Variance)
- Poisson: $p(x; \mu)$
- Normal Density Function (PDF)
- Z-Score Transformation: $Z = (X - \mu)/\sigma$

### 3. Sampling Distributions
- Standard Error of Mean (Finite & Infinite Populations)
- Standard Error of Proportion (Finite & Infinite Populations)

### 4. Parameter Estimation & Hypothesis Testing
- Confidence Intervals for Mean ($n \ge 30$ & $n < 30$)
- Proportion Estimation & Margin of Error
- One-Sample Z-Test & t-Test
- Two-Sample Z-Test (Difference in Means)
- One-Sample & Two-Sample Z-Tests for Proportions

### 5. Analysis of Variance (ANOVA)
- One-Way ANOVA (F-Statistic calculation)
- Two-Way ANOVA (Treatment & Block F-Statistics)

## 🛠️ Requirements & Installation

Ensure Python 3.10+ is installed. Install dependencies using:

```bash
pip install scipy numpy
```

## 💻 Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/klauszealot/Probabilitas-Statistika-dan-Proses-Stokastik-Tools.git
   ```
2. Run the application:
   ```bash
   python main.py
   ```

## 📄 License
This project is for educational purposes. Feel free to use and modify for learning!

---
*Created by [klauszealot](https://github.com/klauszealot)*
