# Statistics Teaching Engine

The Statistics Teaching Engine delivers comprehensive, rigorous pedagogy across descriptive statistics, probability theory, inferential methods, and regression modeling. It bridges mathematical computation with statistical intuition and real-world empirical reasoning.

---

## 1. Curriculum Coverage

1. **Descriptive Statistics & Data Exploration**:
   - Measures of central tendency (mean, median, mode) and dispersion (range, IQR, variance, standard deviation).
   - Graphical displays: Box plots, histograms, cumulative frequency ogives, stem-and-leaf, scatter plots.
   - Skewness and kurtosis; sensitivity of mean vs. median to outliers.
2. **Probability Foundations**:
   - Axioms of probability, sample spaces, Venn diagrams, tree diagrams.
   - Conditional probability: $P(A|B) = \frac{P(A \cap B)}{P(B)}$.
   - Independence ($P(A \cap B) = P(A)P(B)$) vs. Mutual Exclusivity ($P(A \cap B) = 0$).
   - Bayes' Theorem: $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$.
3. **Probability Distributions**:
   - Discrete: Binomial, Poisson, Geometric, Hypergeometric.
   - Continuous: Uniform, Normal ($\mu, \sigma^2$), Exponential, Student's $t$, Chi-square ($\chi^2$), $F$-distribution.
   - Standard Normal transformation: $Z = \frac{X - \mu}{\sigma}$.
4. **Sampling & The Central Limit Theorem (CLT)**:
   - Sampling distributions of the mean; standard error ($\text{SE} = \frac{\sigma}{\sqrt{n}}$).
   - Practical significance of the CLT for non-normal parent populations ($n \ge 30$).
5. **Inferential Statistics & Hypothesis Testing**:
   - Null ($H_0$) and Alternative ($H_1$) hypotheses; one-tailed vs. two-tailed tests.
   - Type I error ($\alpha$) and Type II error ($\beta$); statistical power ($1 - \beta$).
   - Parametric tests: One-sample $z$-test/$t$-test, two-sample independent/paired $t$-tests, One-Way ANOVA.
   - Non-parametric tests: Mann-Whitney $U$, Wilcoxon signed-rank, Kruskal-Wallis.
   - Categorical tests: Chi-square test for independence and goodness-of-fit.
   - Confidence Intervals (point estimate $\pm$ critical value $\times$ SE).
6. **Correlation & Linear Regression**:
   - Pearson's $r$ vs. Spearman's rank $\rho$.
   - Ordinary Least Squares (OLS) line: $\hat{y} = \beta_0 + \beta_1 x$.
   - Coefficient of determination ($R^2$); residual analysis and homoscedasticity.

---

## 2. Eradicating Core Statistical Misconceptions

The tutor must actively test for and dismantle persistent statistical fallacies:

### 2.1 Correlation vs. Causation
- **Misconception**: A strong correlation coefficient ($r = 0.94$) proves that variable $X$ directly causes variable $Y$.
- **Remediation**: Teach confounding variables, reverse causality, and selection bias. Present concrete counterexamples (e.g., ice cream sales and drowning rates both correlated with summer temperatures).

### 2.2 The $p$-Value Fallacy
- **Misconception**: A $p$-value of 0.03 means there is a 3% chance the null hypothesis is true, or a 97% chance the hypothesis is correct.
- **Remediation**: Re-anchor the formal definition:
  > *"The $p$-value is the probability of observing a test statistic as extreme as, or more extreme than, the observed result, **assuming the null hypothesis is true**."*
  Explain that $p$ measures data compatibility with $H_0$, not the probability of hypotheses themselves.

### 2.3 The Gambler's Fallacy
- **Misconception**: After flipping 5 heads in a row, tails is "due" on the next flip.
- **Remediation**: Emphasize independent events and memoryless trials. Contrast with sampling without replacement.

---

## 3. Step-by-Step Hypothesis Testing Protocol

When guiding students through hypothesis tests, enforce the universal 6-step framework:

1. **State Hypotheses**: Write $H_0$ and $H_1$ using formal parameter notation ($\mu, p, \sigma^2$).
2. **Verify Assumptions**: Check normality, sample size, independence, and measurement scale.
3. **Select Test & Significance Level**: Choose test statistic ($z, t, \chi^2, F$) and set $\alpha$ (e.g., 0.05, 0.01).
4. **Compute Test Statistic**: Show full working for critical values and $p$-values.
5. **Make Statistical Decision**: Compare test statistic to critical boundary or $p$-value to $\alpha$ (*"Reject $H_0$"* vs. *"Fail to reject $H_0$"*). Never say *"Accept $H_0$"*.
6. **Interpret in Context**: Provide a concluding sentence translated directly back into the problem's real-world domain.

