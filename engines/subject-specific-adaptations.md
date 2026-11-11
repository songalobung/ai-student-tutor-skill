# Subject-Specific Adaptations for Neuroinclusive & Attention-Friendly Teaching

This guide provides concrete, operational instructional templates showing how the **Attention-Friendly Teaching Engine** adapts across major academic disciplines, ensuring clarity and working-memory support while preserving academic depth.

---

## 1. Mathematics & Quantitative Computing

### Operational Rules
1. **One Operation Per Line**: Never combine algebraic expansion, variable grouping, and transposition into a single skipped step.
2. **Explicit Strategic Rationale**: Beside every intermediate step, state *why* that operation is mathematically required.
3. **Variable Identification First**: Identify parameters and target unknowns before writing the governing equation.

### Concrete Example: Integration by Parts (University / A-Level)
*Goal: Evaluate $\int x \cos(x) \, dx$.*

> ### Step 1: Identify Components (LIATE Rule)
> We choose our parts using the standard hierarchy:
> - Let $u = x$ (Algebraic term, easily differentiated).
> - Let $dv = \cos(x) \, dx$ (Trigonometric term, easily integrated).
>
> ### Step 2: Differentiate and Integrate
> - Differentiate $u$: $\frac{du}{dx} = 1 \implies du = dx$.
> - Integrate $dv$: $v = \int \cos(x) \, dx = \sin(x)$.
>
> ### Step 3: Apply the Integration by Parts Formula
> The formula is:
> $$\int u \, dv = u \cdot v - \int v \, du$$
>
> Substitute our pieces:
> $$\int x \cos(x) \, dx = (x)(\sin(x)) - \int \sin(x) \, dx$$
>
> ### Step 4: Evaluate the Remaining Integral
> - The integral of $\sin(x)$ is $-\cos(x)$.
> - Putting it together:
> $$\int x \cos(x) \, dx = x \sin(x) - (-\cos(x)) + C$$
> $$= x \sin(x) + \cos(x) + C$$
>
> *Quick Check*: What happens to the sign of the second term when we differentiate the result to verify?

---

## 2. Physics & Engineering Sciences

### Operational Rules
1. **The 4-Box Quantitative Framework**:
   - **Knowns**: Explicit list with SI units.
   - **Unknowns**: Target variable and target unit.
   - **Governing Law**: Algebraic formula in standard form.
   - **Substitution & Result**: Numbers substituted before final calculation.
2. **Explicit Physical Meaning**: Beside formulas, explain what the equation represents physically (e.g., $F=ma \implies$ acceleration is directly proportional to net force and inversely proportional to inertia).

---

## 3. Natural Sciences (Chemistry & Biology)

### Operational Rules
1. **Sequential Process Chunking**: In metabolic pathways or reaction mechanisms, break continuous flows into distinct numbered stages.
2. **Immediate Technical Jargon Anchors**: Follow every unfamiliar term with a 3-word plain-English anchor:
   - *"Phosphorylation (adding a phosphate molecule)..."*
   - *"Hydrophobic (water-fearing / non-polar)..."*
   - *"Catalyst (substance that speeds up reaction without being consumed)..."*
3. **Systemic Feedback Loops**: Use Mermaid flowcharts or clear ASCII sequences to visualize cyclical or regulated systems.

---

## 4. Humanities & Social Sciences (Economics, History, Law, Philosophy)

### Operational Rules
1. **Separate Causal Chains**: In History and Economics, clearly distinguish **Root Causes**, **Immediate Triggers**, and **Long-Term Consequences** using parallel bullet clusters.
2. **The 3-Part Argument Chunk**:
   - **Claim**: The central thesis point (1 sentence).
   - **Empirical/Textual Evidence**: Specific data, historical quote, or treaty clause.
   - **Evaluation / Analysis**: Why this matters or how critics respond.
3. **Positive vs. Normative Clarification**: In Economics, bold whether an assertion is an objective empirical relationship or a subjective policy goal.
