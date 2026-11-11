# Educational Research Foundations & Literature Library

The Student Academic Tutor is grounded in empirical cognitive science, meta-analytic educational psychology, Knowledge Tracing (KT), and international recommendations for ethical artificial intelligence in education. 

Every entry in this repository is strictly documented with verifiable bibliographic data, clear empirical scopes, and explicit methodological limits.

---

## 1. Verified Meta-Analyses on Tutoring & Intelligent Systems

### 1.1 Meta-Analyses on Computer-Based & Intelligent Tutoring
- **Citation**: Ma, W., Adesope, O. O., Nesbit, J. C., & Liu, Q. (2014). *Intelligent tutoring systems and learning outcomes: A meta-analysis*. Journal of Educational Psychology, 106(4), 901–918. DOI: [10.1037/a0037123](https://doi.org/10.1037/a0037123)
  - **Empirical Base**: 107 effect sizes across 14,321 participants.
  - **Findings**: ITS produced positive learning gains across various subject domains compared with teacher-led classroom instruction (Hedges' $g = 0.42$), non-ITS computer instruction ($g = 0.57$), and textbook/homework study ($g = 0.35$).
  - **Methodological Limits**: The effect sizes varied substantially depending on whether the comparison group received active human tutoring (where human tutors generally matched or exceeded ITS).
  - **Implementation**: Justifies personalized learner modeling and step-by-step problem guidance over unguided textbook problem solving.

- **Citation**: Steenbergen-Hu, S., & Cooper, H. (2014). *A meta-analysis of the effectiveness of intelligent tutoring systems on college students' learning*. Journal of Educational Psychology, 106(2), 331–347. DOI: [10.1037/a0034752](https://doi.org/10.1037/a0034752)
  - **Empirical Base**: 35 empirical studies involving 4,792 college participants.
  - **Findings**: Moderate positive effect ($g = 0.32$) for undergraduate students, with effectiveness highest when ITS supplemented rather than completely replaced conventional classroom instruction.
  - **Implementation**: Directly shapes higher education guidelines in `curricula/university/guide.md`.

- **Citation**: Huang, X., Craig, S. D., & Xie, K. (2021). *Effects of intelligent tutoring systems on learning outcomes and attitudes: A meta-analysis of randomized controlled trials*. Educational Research Review, 34, 100414. DOI: [10.1016/j.edurev.2021.100414](https://doi.org/10.1016/j.edurev.2021.100414)
  - **Empirical Base**: 45 randomized controlled trials ($N = 10,217$).
  - **Findings**: Significant overall benefit for academic performance ($g = 0.43$) and subject interest ($g = 0.22$), but no significant impact on lowering academic anxiety.
  - **Implementation**: The tutor must not rely on self-reported learner satisfaction or comfort as a proxy for verified conceptual understanding.

---

## 2. Cognitive Science: Retrieval, Spacing, and Cognitive Load

- **Citation**: Agarwal, P. K., Nunes, L. D., & Blunt, J. R. (2021). *Retrieval practice consistently benefits student learning: A systematic review of educational research*. Educational Psychology Review, 33(4), 1409–1453. DOI: [10.1007/s10648-021-09595-9](https://doi.org/10.1007/s10648-021-09595-9)
  - **Empirical Base**: 50 classroom experiments across diverse subject areas.
  - **Findings**: Active retrieval practice (low-stakes testing and recall without reference notes) demonstrated consistent moderate-to-large benefits for factual recall and conceptual transfer over passive review.
  - **Implementation**: Powers mandatory retrieval drills in `pedagogy/retrieval-practice.md` and `modes/revision.md`.

- **Citation**: Murray, S., Dunlosky, J., & Rawson, K. A. (2023). *Spacing versus massing in mathematical problem solving: A meta-analysis*. Educational Psychology Review, 35(3), 85. DOI: [10.1007/s10648-023-09796-0](https://doi.org/10.1007/s10648-023-09796-0)
  - **Empirical Base**: Systematic meta-analysis of distributed practice in mathematics.
  - **Findings**: Demonstrates consistent benefits of distributed/spaced practice over massed practice for delayed test retention ($g = 0.38$).
  - **Implementation**: Governs topic review intervals in `engines/revision-engine.md` and `pedagogy/spaced-repetition.md`.

- **Citation**: Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). *Cognitive architecture and instructional design: 20 years later*. Educational Psychology Review, 31(2), 261–292. DOI: [10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)
  - **Findings**: Synthesizes the Worked Example Effect, Split-Attention Effect, and Expertise Reversal Effect. Establishes that novice learners benefit substantially more from fully worked and faded completion examples than from unassisted problem solving.
  - **Implementation**: Informs `pedagogy/worked-examples.md` and the gradual release of responsibility (`pedagogy/scaffolding.md`).

- **Citation**: Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). *Learning styles: Concepts and evidence*. Psychological Science in the Public Interest, 9(3), 105–119. DOI: [10.1111/j.1539-6053.2009.01038.x](https://doi.org/10.1111/j.1539-6053.2009.01038.x)
  - **Findings**: Disproved the "Meshing Hypothesis" (the assumption that tailoring instruction to auditory, visual, or kinesthetic learning styles improves outcomes).
  - **Implementation**: Explicitly bans adapting lessons to hypothetical learning styles. The tutor adapts instead to subject demands and learner prior knowledge.

---

## 3. Knowledge Tracing & Student Modeling

- **Citation**: Corbett, A. T., & Anderson, J. R. (1994). *Knowledge tracing: Modeling the acquisition of procedural knowledge*. User Modeling and User-Adapted Interaction, 4(4), 253–278. DOI: [10.1007/BF01099821](https://doi.org/10.1007/BF01099821)
  - **Theoretical Base**: The canonical Bayesian Knowledge Tracing (BKT) formulation modeling latent learner mastery $P(L_n)$ across learning transitions $P(T)$, guess probabilities $P(G)$, and slip probabilities $P(S)$.
  - **Implementation**: Informs the probabilistic mastery thresholds in `engines/progress-engine.md`.

- **Citation**: Piech, C., Spencer, J., Huang, J., Ganguli, S., Sahami, M., Guibas, L., & Sohl-Dickstein, J. (2015). *Deep knowledge tracing*. Advances in Neural Information Processing Systems (NeurIPS 2015), 28, 505–513. [https://proceedings.neurips.cc/paper/2015/hash/bac9162b47c56fc8a4d2a519803d51b3-Abstract.html](https://proceedings.neurips.cc/paper/2015/hash/bac9162b47c56fc8a4d2a519803d51b3-Abstract.html)
  - **Findings**: Introduced Recurrent Neural Networks (LSTMs) to predict student performance across sequence tasks, showing improvements over traditional Markovian BKT on standard benchmarks (such as ASSISTments).
  - **Implementation**: Informs the transition from rigid point scoring to dynamic trajectory analysis in `engines/progress-engine.md`.

---

## 4. Human-AI Interaction & Ethical Guidelines

- **Citation**: UNESCO (2023). *Guidance for generative AI in education and research*. Paris: UNESCO Publishing. ISBN: 978-92-3-100609-8. [https://unesdoc.unesco.org/ark:/48223/pf0000386693](https://unesdoc.unesco.org/ark:/48223/pf0000386693)
  - **Core Principles**: Recommends human agency, pedagogical validation, data privacy, age-appropriate access restrictions, and safeguarding against intellectual dependency.
  - **Implementation**: Forms the foundation of `core/safeguarding.md` and `core/academic-integrity.md`.

- **Citation**: Hattie, J., & Timperley, H. (2007). *The power of feedback*. Review of Educational Research, 77(1), 81–112. DOI: [10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
  - **Findings**: Identified four levels of feedback: Task (FT), Process (FP), Self-Regulation (FR), and Self (FS). Feedback focused on personal praise (Self level) has low-to-negative effect sizes, whereas process-level and self-regulation feedback yield the highest learning gains ($d = 0.74$).
  - **Implementation**: Governs `engines/assessment-engine.md` and `assessments/marking-rubrics.md`. Feedback must target the process, mathematical reasoning, and error mechanisms rather than generic encouragement.
