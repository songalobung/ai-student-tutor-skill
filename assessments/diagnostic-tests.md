# Diagnostic Testing Protocols

The Diagnostic Testing framework enables rapid, precise identification of a student's current baseline knowledge, prerequisite gaps, and conceptual misunderstandings prior to initiating new instruction.

---

## 1. Diagnostic Architecture: The Prerequisite Triad

Before teaching an advanced target topic, administer a 3-part diagnostic sequence targeting:
1. **Upstream Prerequisite Fluency**: Essential foundational operations from previous academic years.
2. **Current Topic Baseline**: Basic definitions and elementary operations of the target topic.
3. **Application & Reasoning**: A non-routine problem revealing whether the student understands the underlying mechanism or has merely memorized a rule.

---

## 2. Multi-Subject Diagnostic Batteries

### 2.1 Mathematics: Calculus (Differentiation) Diagnostic
*Target Topic*: Product Rule, Quotient Rule, and Chain Rule ($dy/dx$).

1. **Question 1 (Algebraic Prerequisite - Indices)**:
   > Express $f(x) = \frac{3}{2\sqrt{x}} - \frac{4}{x^3}$ in index form ($a x^n$).
   - *Diagnostic Focus*: Checks mastery of negative and fractional indices. If the student fails this, they cannot differentiate algebraic fractions.
2. **Question 2 (Functional Prerequisite - Composition)**:
   > If $f(x) = \sin(x)$ and $g(x) = 3x^2 + 1$, write the composite function $f(g(x))$.
   - *Diagnostic Focus*: Distinguishes composition from multiplication $f(x) \cdot g(x)$.
3. **Question 3 (Fundamental Baseline - Polynomial Derivative)**:
   > Find $\frac{d}{dx}\left(5x^4 - 2x + 7\right)$ from first principles or standard power rule.
   - *Diagnostic Focus*: Checks power rule execution and derivative of a constant.
4. **Question 4 (Target Concept - Chain Rule Application)**:
   > Differentiate $y = (4x^3 - 5)^6$ with respect to $x$. Show each step.
   - *Diagnostic Focus*: Checks whether the student applies the outer derivative while multiplying by the inner derivative $\frac{du}{dx}$.

---

### 2.2 Physics: Mechanics (Newtonian Dynamics) Diagnostic
*Target Topic*: Friction, Inclined Planes, and Connected Particles.

1. **Question 1 (Vector Resolution)**:
   > A block of mass $m = 4\text{ kg}$ rests on a plane inclined at $30^\circ$ to the horizontal. Resolve the weight vector into components parallel and perpendicular to the slope.
   - *Diagnostic Focus*: Determines whether the student confuses $\sin(\theta)$ and $\cos(\theta)$ orientations.
2. **Question 2 (Conceptual Law Interpretation)**:
   > A spacecraft moves in deep space with its engines turned off at a constant velocity of $500\text{ m/s}$. What is the net horizontal force acting on it? Explain your reasoning.
   - *Diagnostic Focus*: Detects the Aristotelian misconception that continuous motion requires continuous applied force.
3. **Question 3 (Dynamics Calculation)**:
   > A $10\text{ N}$ horizontal force acts on a $2\text{ kg}$ block on a rough horizontal floor with coefficient of dynamic friction $\mu_k = 0.2$. Take $g = 9.8\text{ m/s}^2$. Calculate the resulting acceleration.
   - *Diagnostic Focus*: Verifies $F_{\text{net}} = ma$, $F_N = mg$, and $F_{\text{net}} = F_{\text{applied}} - f_k$.

---

### 2.3 Chemistry: Stoichiometry and Equilibrium Diagnostic
*Target Topic*: Le Chatelier's Principle & Acid-Base Titrations.

1. **Question 1 (Symbolic Balancing)**:
   > Balance: $\text{Fe}_2\text{O}_3(s) + \text{CO}(g) \to \text{Fe}(s) + \text{CO}_2(g)$.
   - *Diagnostic Focus*: Checks conservation of mass at the atomic level.
2. **Question 2 (The Mole Concept)**:
   > How many moles of sodium hydroxide ($\text{NaOH}$) are present in $25.0\text{ cm}^3$ of a $0.200\text{ mol/dm}^3$ aqueous solution?
   - *Diagnostic Focus*: Checks concentration-volume conversions ($\text{cm}^3$ to $\text{dm}^3$).
3. **Question 3 (Dynamic Equilibrium Reasoning)**:
   > For the exothermic Haber reaction: $\text{N}_2(g) + 3\text{H}_2(g) \rightleftharpoons 2\text{NH}_3(g)$ ($\Delta H = -92\text{ kJ/mol}$), state and explain the effect of increasing temperature on the yield of $\text{NH}_3$.
   - *Diagnostic Focus*: Detects whether student confuses equilibrium position (thermodynamics) with reaction rate (kinetics).

---

### 2.4 Economics: Market Failure & Elasticity Diagnostic
*Target Topic*: Government Intervention and Deadweight Loss.

1. **Question 1 (Elasticity Calculation & Interpretation)**:
   > When the price of good $X$ rises from \$10 to \$12, quantity demanded falls from 100 units to 70 units. Calculate Price Elasticity of Demand (PED) and state whether demand is price elastic or inelastic.
   - *Diagnostic Focus*: Checks PED formula ($\%\Delta Q_D / \%\Delta P$) and value interpretation ($|\text{PED}| > 1$).
2. **Question 2 (Diagrammatic Understanding)**:
   > If the government imposes a specific per-unit tax on suppliers, which curve shifts, in which direction, and by what vertical distance?
   - *Diagnostic Focus*: Checks supply curve shift mechanics and incidence of taxation.
3. **Question 3 (Normative vs. Positive Distinction)**:
   > Label each statement as Positive or Normative:
   > A: "An increase in minimum wage leads to higher teenage unemployment."
   > B: "The government ought to increase the minimum wage to alleviate poverty."
   - *Diagnostic Focus*: Detects ability to separate value judgments from empirical economic claims.

---

## 3. Diagnostic Decision Matrix

```
[Diagnostic Administered]
         |
         +--> Score < 50% on Prerequisite Question?
         |       |
         |       +--> STOP target topic. Route to Prerequisite Remediation Module.
         |
         +--> Prerequisite Mastered, but Base Concept Fails?
         |       |
         |       +--> Deliver Concrete Worked Example -> Guided Practice.
         |
         +--> All Diagnostic Questions Answered Correctly with Valid Working?
                 |
                 +--> Fast-track to Non-routine Extension and Synoptic Exam Practice.
```

