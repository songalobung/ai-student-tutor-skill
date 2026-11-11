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
