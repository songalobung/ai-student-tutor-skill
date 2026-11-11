# Professional & Applied Sciences Subject Knowledge Pack

**Pack Module**: `subjects\professional-applied.md`

**Description**: Comprehensive pedagogical engines for Engineering, Law, Medicine & Health Sciences, Accounting, and Environmental Science.

**Included Sources**: Engineering, Law, Medicine & Health, Accounting, Environmental Science


---


## Module: Engineering

*Source: `subjects/engineering/engine.md`*


# Engineering Sciences Teaching Engine

The Engineering Sciences Teaching Engine delivers rigorous instruction in foundational engineering mechanics, electrical circuits, materials science, thermodynamics, fluid dynamics, and systems engineering across secondary (A-Level Design & Technology/Engineering, AP Physics C) and undergraduate engineering degrees (Mechanical, Electrical, Civil, Chemical).

---

## 1. Core Engineering Disciplines

1. **Statics & Structural Mechanics**:
   - Static equilibrium: $\sum \vec{F} = 0$, $\sum \vec{M} = 0$.
   - Truss analysis: Method of Joints and Method of Sections.
   - Shear force diagrams (SFD) and Bending moment diagrams (BMD) for simply supported and cantilever beams.
   - Stress, strain, Young's modulus ($E = \frac{\sigma}{\epsilon}$), Poisson's ratio, Hooke's Law in 3D.
   - Flexural bending formula: $\frac{\sigma}{y} = \frac{M}{I} = \frac{E}{R}$.
2. **Dynamics & Kinematics of Machines**:
   - Planar kinematics of rigid bodies: Instantaneous centers of zero velocity.
   - Work-energy theorem and impulse-momentum equations.
   - Vibration analysis: Single degree of freedom (SDOF) un-damped and damped free vibrations ($m\ddot{x} + c\dot{x} + kx = 0$), natural frequency $\omega_n = \sqrt{k/m}$, damping ratio $\zeta = \frac{c}{2\sqrt{km}}$, resonance.
3. **Fluid Mechanics**:
   - Hydrostatics: Pressure head ($P = \rho g h$), buoyant force (Archimedes' principle).
   - Fluid dynamics: Continuity equation ($\dot{m} = \rho A v = \text{const}$).
   - Bernoulli's equation: $P + \frac{1}{2}\rho v^2 + \rho g z = \text{const}$ (along a streamline, inviscid, incompressible, steady flow).
   - Pipe flow: Reynolds number ($Re = \frac{\rho v D}{\mu}$), laminar vs. turbulent flow, Darcy-Weisbach head loss equation.
4. **Thermodynamics & Heat Transfer**:
   - First and Second Laws of Thermodynamics for closed systems and open control volumes.
   - Thermodynamic cycles: Carnot, Rankine, Brayton, Otto, Diesel.
   - Modes of heat transfer: Conduction (Fourier's Law $q = -k A \frac{dT}{dx}$), Convection (Newton's Law of Cooling $q = h A (T_s - T_\infty)$), Radiation (Stefan-Boltzmann Law $E = \epsilon \sigma A T^4$).
5. **Electrical & Electronic Engineering**:
   - Circuit laws: Kirchhoff's Current Law (KCL), Kirchhoff's Voltage Law (KVL).
   - Network theorems: Thévenin and Norton equivalent circuits, Superposition, Maximum Power Transfer ($R_L = R_{th}$).
   - AC circuit analysis: Phasors, complex impedance ($Z_R = R, Z_L = j\omega L, Z_C = \frac{1}{j\omega C}$), power factor.
   - Operational amplifiers (Op-Amps): Inverting, non-inverting, summing, and differential amplifier configurations under ideal assumptions ($R_{in} \to \infty, A_{OL} \to \infty, i_+ = i_- = 0$).

---

## 2. Engineering Problem-Solving Protocol

Enforce the standard 5-step engineering problem formulation:
1. **Given & Schematic**: Sketch a clean, labeled diagram with coordinate axes.
2. **Assumptions**: State all idealizations explicitly (e.g., steady-state, incompressible fluid, massless beam, frictionless hinge).
3. **Governing Laws**: Write the fundamental physical equation in algebraic form before substituting numerical values.
4. **Calculations**: Show intermediate algebraic rearrangements, track significant figures, and carry units through every substitution line.
5. **Sanity Check & Reality Validation**: Check order of magnitude, dimensional consistency, and sign orientations.


---


## Module: Law

*Source: `subjects/law/engine.md`*


# Law & Jurisprudence Teaching Engine

The Law Teaching Engine provides structured instruction in legal reasoning, case analysis, constitutional law, contract law, tort law, criminal law, and jurisprudence across secondary (A-Level Law) and undergraduate law degree (LL.B / J.D.) programs.

---

## 1. Core Substantive Legal Disciplines

1. **The Legal System & Sources of Law**:
   - Primary legislation (statutory interpretation: Literal, Golden, Mischief rules; purposive approach).
   - Judicial precedent (*stare decisis*): *Ratio decidendi* (binding rule) vs. *Obiter dicta* (persuasive comments), distinguishing precedents, reversing, overruling.
   - Court hierarchies, judicial review, civil vs. criminal procedural distinctions.
2. **Criminal Law**:
   - The dual requirement: *Actus Reus* (guilty act/omission) + *Mens Rea* (guilty mind: intention vs. recklessness vs. negligence; strict liability).
   - Causation: Factual causation ("But-for" test - *R v White*) and Legal causation (operative and substantial cause, thin skull rule, *novus actus interveniens*).
   - Offenses: Fatal offenses (Murder, Voluntary/Involuntary Manslaughter), Non-fatal offenses (Assault, Battery, ABH, GBH), Property offenses (Theft, Robbery, Burglary).
   - Defenses: Self-defense, necessity, duress, insanity, automatism, intoxication.
3. **Tort Law**:
   - Negligence framework:
     1. Duty of care (*Caparo v Dickman* / *Donoghue v Stevenson* / *Robinson v Chief Constable of West Yorkshire Police*).
     2. Breach of duty (Objective reasonable person standard, risk factors).
     3. Causation and remoteness of damage (*The Wagon Mound*).
   - Specialized torts: Occupiers' liability, Private nuisance, Vicarious liability, Rylands v Fletcher.
4. **Contract Law**:
   - Formation: Offer, acceptance (postal rule), consideration (adequacy vs. sufficiency), intention to create legal relations.
   - Vitiating factors: Misrepresentation, mistake, duress, undue influence.
   - Breach and remedies: Expectation damages, liquidated damages vs. penalty clauses, specific performance, frustration.
5. **Jurisprudence & Legal Theory**:
   - Natural Law (Aquinas, Fuller, Finnis) vs. Legal Positivism (Austin, Hart, Kelsen).
   - Ronald Dworkin's Interpretivism (rights as trumps, one right answer thesis).
   - Critical Legal Studies, Feminist jurisprudence, Legal Realism.

---

## 2. Legal Problem Solving: The IRAC Method

The tutor strictly enforces the **IRAC (Issue, Rule, Application, Conclusion)** protocol for legal problem scenarios:

```
[Scenario Presented: Defendant throws a stone aiming at A, misses, and shatters B's window]
                                   |
                                   v
[Issue]: "Does the doctrine of transferred malice apply to transfer intent from an offense
          against the person (assault) to an offense against property (criminal damage)?"
                                   |
                                   v
[Rule]: "Under Pembliton (1874), the doctrine of transferred malice can only operate where the
         intended crime and the actual crime committed are of the same legal nature/type."
                                   |
                                   v
[Application]: "The defendant intended an offense against the person (battery), but the
                resulting harm was to property. Since these are distinct categories of offenses,
                the malice cannot be transferred to form the mens rea for criminal damage."
                                   |
                                   v
[Conclusion]: "The defendant cannot be convicted of intentional criminal damage via transferred
               malice, though liability for recklessness remains an alternative consideration."
```

---

## 3. Legal Case Citation & Jurisprudential Standards

- When citing legal cases, require correct case names and core *ratio decidendi* (e.g., *Donoghue v Stevenson [1932] AC 562* - neighbor principle).
- Distinguish between **Ratio** (binding precedent) and **Obiter** (persuasive dicta).
- In essays, evaluate statutory reform proposals, law commission reports, and competing public policy justifications.


---


## Module: Medicine & Health

*Source: `subjects/medicine-health/engine.md`*


# Medicine, Physiology & Health Sciences Teaching Engine

The Medicine & Health Sciences Teaching Engine delivers instruction across medical physiology, pathology, pharmacology, anatomy, microbiology, and clinical epidemiology for pre-medical, nursing, pharmacy, and undergraduate clinical degree programs.

---

## 1. Core Medical Science Disciplines

1. **Cardiovascular & Respiratory Physiology**:
   - Cardiac electrophysiology: Action potentials in nodal cells vs. ventricular myocytes; ECG waveforms ($P$ wave, $QRS$ complex, $T$ wave).
   - Hemodynamics: Cardiac Output ($CO = HR \times SV$), Mean Arterial Pressure ($MAP = CO \times SVR + CVP$), Frank-Starling mechanism, Laplace's Law.
   - Respiratory mechanics: Lung volumes/capacities (Tidal, FRC, FEV1/FVC ratio in obstructive vs. restrictive lung diseases), ventilation-perfusion ($V/Q$) mismatch, oxygen-hemoglobin dissociation curve (Bohr effect, 2,3-BPG shifts).
2. **Renal & Acid-Base Physiology**:
   - Glomerular filtration rate (GFR), Starling forces, tubuloglomerular feedback, Renin-Angiotensin-Aldosterone System (RAAS).
   - Countercurrent multiplication in the Loop of Henle.
   - Acid-Base disorders: Davenport diagram, Henderson-Hasselbalch equation ($\text{pH} = \text{p}K_a + \log\frac{[\text{HCO}_3^-]}{0.03 \times P\text{CO}_2}$), metabolic/respiratory acidosis and alkalosis, anion gap calculation.
3. **Pharmacology & Pharmacokinetics**:
   - Pharmacokinetics: Absorption, Distribution, Metabolism (Phase I cytochrome P450 vs. Phase II conjugation), Elimination.
   - Core parameters: Volume of distribution ($V_d = \frac{D}{C_0}$), Clearance ($CL = k_e \times V_d$), Half-life ($t_{1/2} = \frac{0.693 \times V_d}{CL}$), Steady-state concentration.
   - Pharmacodynamics: Agonists, competitive antagonists (parallel right-shift of dose-response curve, unchanged $E_{\max}$), non-competitive antagonists (decreased $E_{\max}$), therapeutic index ($TI = \frac{TD_{50}}{ED_{50}}$).
4. **Immunology & Medical Microbiology**:
   - Innate immunity (complement cascade pathways, phagocytes, Toll-like receptors) vs. Adaptive immunity (MHC Class I vs. Class II antigen presentation, CD4+ T helper cells, CD8+ cytotoxic T cells, B-cell receptor somatic hypermutation).
   - Hypersensitivity reactions (Gell & Coombs classification: Type I IgE anaphylaxis, Type II cytotoxic, Type III immune-complex, Type IV delayed-type cell-mediated).
   - Bacterial taxonomy (Gram-positive vs. Gram-negative cell wall architecture, endotoxins vs. exotoxins) and antimicrobial mechanisms (beta-lactams, aminoglycosides, fluoroquinolones, macrolides).

---

## 2. Clinical Diagnostic Reasoning: The Differential Diagnosis (DDx)

The tutor trains students using the **VINDICATE** clinical mnemonic for organizing differential diagnoses:
- **V**: Vascular (e.g., myocardial infarction, stroke, pulmonary embolism)
- **I**: Infectious / Inflammatory (e.g., pneumonia, appendicitis, meningitis)
- **N**: Neoplastic (e.g., leukemia, carcinoma, lymphoma)
- **D**: Degenerative / Deficiency (e.g., Alzheimer's, osteoarthritis, vitamin deficiency)
- **I**: Iatrogenic / Intoxication (e.g., adverse drug reaction, overdose)
- **C**: Congenital / Genetic (e.g., cystic fibrosis, sickle cell disease)
- **A**: Autoimmune (e.g., lupus, rheumatoid arthritis, Crohn's)
- **T**: Traumatic / Toxic (e.g., subdural hematoma, pneumothorax)
- **E**: Endocrine / Metabolic (e.g., diabetic ketoacidosis, hyperthyroidism)

---

## 3. Strict Boundary Warning
The tutor functions strictly as an **educational teaching engine for students**. It must explicitly refuse to diagnose real patients, interpret live clinical medical records, or provide personal medical treatment plans, redirecting users to licensed healthcare professionals (see `core/safeguarding.md`).


---


## Module: Accounting

*Source: `subjects/accounting/engine.md`*


# Accounting Teaching Engine

The Accounting Teaching Engine provides specialized instructional protocols for financial accounting, management accounting, and financial reporting across secondary (IGCSE, GCSE, CBSE, A-Level) and undergraduate business curricula.

---

## 1. Pedagogical Core: The Dual-Aspect Concept

Accounting instruction must be anchored in the fundamental accounting equation:

$$\text{Assets} = \text{Liabilities} + \text{Equity}$$

Students frequently struggle when memorizing debit/credit rules mechanically without understanding transaction effects. The tutor enforces the **DEAD CLIC** framework:

- **Debit Increases**: **D**ebit: **E**xpenses, **A**ssets, **D**rawings.
- **Credit Increases**: **C**redit: **L**iabilities, **I**ncome, **C**apital.

---

## 2. Curriculum Coverage

1. **Foundations**: Source documents (invoices, credit notes, receipts), books of prime entry, double-entry ledger bookkeeping.
2. **Trial Balance & Error Correction**: Extraction of trial balances, suspense accounts, errors not affecting the trial balance (omission, commission, principle, original entry, reversal, compensating).
3. **Period-End Adjustments**: Accruals, prepayments, depreciation (straight-line, reducing balance), allowances for irrecoverable debts.
4. **Financial Statements**:
   - Statement of Profit or Loss (Income Statement): Revenue, Cost of Sales, Gross Profit, Operating Expenses, Net Profit.
   - Statement of Financial Position (Balance Sheet): Non-current assets, current assets, current liabilities, working capital, non-current liabilities, equity/capital structure.
   - Statement of Cash Flows (Operating, Investing, Financing activities).
5. **Partnerships and Companies**: Partnership profit & loss appropriation, goodwill, revaluation, limited liability company equity, dividends, debentures.
6. **Management & Cost Accounting**: Cost classification (fixed, variable, semi-variable, stepped), break-even analysis, marginal costing vs. absorption costing, budgeting, variance analysis.
7. **Ratio Analysis & Performance Interpretation**:
   - *Profitability*: Gross margin, net margin, ROCE.
   - *Liquidity*: Current ratio, acid test (quick) ratio.
   - *Efficiency*: Inventory turnover, trade receivables collection period, trade payables payment period.
   - *Solvency/Gearing*: Debt-to-equity, interest cover.

---

## 3. Instructional Protocols & Ledgers

### 3.1 Standard T-Account Formatting
All journal entries and ledger accounts presented by the tutor must follow formal structured layouts:

```
                  Bank Account (Asset)
Debit ($)                                           Credit ($)
--------------------------------------------------------------
Date   Details       Amount   | Date   Details          Amount
Jan 01 Capital       10,000   | Jan 03 Rent Expense        800
Jan 12 Sales Revenue  2,400   | Jan 15 Office Equipment  3,500
                              | Jan 31 Balance c/d       8,100
--------------------------------------------------------------
Total                12,400   | Total                   12,400
==============================================================
Feb 01 Balance b/d    8,100   |
```

### 3.2 Error Diagnosis in Suspense Accounts
When students encounter unbalanced accounts:
1. Identify the discrepancy value in the trial balance.
2. Check for transposition errors (divisible by 9).
3. Check for single-sided entry or omission of half an entry.
4. Draft correction journals debiting/crediting the Suspense account until reduced to zero.

---

## 4. Financial Statement Interpretation

Move students beyond mechanical arithmetic into analytical evaluation:
- *Scenario*: "Company A's gross profit margin increased from 25% to 32%, but net profit margin dropped from 12% to 6%. Explain the managerial implications."
- Guide the student to analyze operating expenses, overhead control, administrative inflation, or debt servicing costs rather than merely repeating the percentages.


---


## Module: Environmental Science

*Source: `subjects/environmental-science/engine.md`*


# Environmental Science & Ecology Teaching Engine

The Environmental Science Teaching Engine delivers interdisciplinary instruction bridging ecology, earth systems, atmospheric chemistry, energy resources, conservation biology, and environmental policy across secondary (AP Environmental Science, IB Environmental Systems and Societies - ESS, A-Level) and undergraduate levels.

---

## 1. Curriculum Coverage

1. **Earth Systems & Atmospheric Dynamics**:
   - Biogeochemical cycles: Carbon, Nitrogen, Phosphorus, Hydrologic cycles; residence times, sources, and sinks.
   - Atmospheric layers, Coriolis effect, Hadley/Ferrel/Polar circulation cells, El Niño–Southern Oscillation (ENSO).
   - Soil science: Soil horizons ($O, A, B, C$), soil texture triangle, cation exchange capacity (CEC), salinization, erosion.
2. **Ecosystem Ecology & Biodiversity**:
   - Trophic levels, 10% ecological efficiency rule, gross vs. net primary productivity ($\text{NPP} = \text{GPP} - R$).
   - Population dynamics: Exponential ($J$-curve) vs. Logistic ($S$-curve) growth, carrying capacity ($K$), $r$-selected vs. $K$-selected species.
   - Island biogeography theory, habitat fragmentation, corridors, endangered species legislation.
3. **Global Climate Change & Atmospheric Chemistry**:
   - The greenhouse effect: Absorption spectra of $\text{CO}_2, \text{CH}_4, \text{N}_2\text{O}, \text{H}_2\text{O}$, radiative forcing.
   - Positive feedback loops (albedo loss, permafrost thaw) vs. negative feedback loops.
   - Ocean acidification ($\text{CO}_2 + \text{H}_2\text{O} \to \text{H}_2\text{CO}_3 \to \text{H}^+ + \text{HCO}_3^-$) and calcium carbonate dissolution.
   - Stratospheric ozone depletion: Halocarbons (CFCs), UV-induced chlorine catalytic cycles, Montreal Protocol.
   - Photochemical smog (NOx, VOCs, tropospheric ozone, PANs) and acid deposition ($\text{SO}_2, \text{NO}_x$).
4. **Energy Resources & Sustainable Technology**:
   - Non-renewable: Coal, oil, natural gas (fracking), nuclear fission (fuel cycle, half-life waste management).
   - Renewable: Solar photovoltaic/thermal, wind, hydroelectric, geothermal, biomass, hydrogen fuel cells.
   - Energy return on energy invested (EROEI) and electrical grid distribution.
5. **Water & Aquatic Systems**:
   - Freshwater depletion: Aquifer overdraft, drip irrigation vs. flood irrigation.
   - Water pollution: Eutrophication sequence (nutrient influx $\to$ algal bloom $\to$ death $\to$ microbial decomposition $\to$ hypoxia/anoxia $\to$ fish kills).
   - Wastewater treatment: Primary (physical), secondary (biological aeration), tertiary (chemical disinfection).

---

## 2. Quantitative Calculations in Environmental Science

The tutor must guide students through standard AP/IB environmental calculations:
1. **Rule of 70 (Doubling Time)**: $\text{Doubling Time (years)} = \frac{70}{\text{Growth Rate (\%) aproxx}}$.
2. **Productivity Calculations**: $\text{NPP} = \text{GPP} - R_{\text{autotrophic}}$.
3. **Trophic Energy Transfer**: Converting Joules across trophic tiers ($10\%$ rule).
4. **Dimensional Conversions**: Converting barrels of oil to kilowatt-hours ($\text{kWh}$), parts per million ($\text{ppm}$) to percent, metric tons of $\text{CO}_2$.

---

## 3. Systems Thinking & Policy Evaluation

Enforce the **Systems Framework**:
- Distinguish between **Open, Closed, and Isolated Systems**.
- Analyze environmental dilemmas using the **Tragedy of the Commons** framework (Hardin).
- Evaluate mitigation vs. adaptation policies: Carbon tax vs. Cap-and-Trade vs. Command-and-Control regulation.


---
