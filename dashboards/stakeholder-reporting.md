# Teacher, Parent & Stakeholder Intelligence Dashboards

The Stakeholder Intelligence Dashboard generates structured, evidence-based academic progress reports for authorized educators, parents, and academic counselors.

> **Privacy & Consent Boundary**: Reports must be generated strictly with the student's or institution's explicit permission. Never collect, store, or output sensitive personal identifiable information (PII) such as home addresses or government identification numbers.

---

## 1. Teacher-Orchestrated Diagnostic Report

This report is designed for classroom teachers, saving instructional preparation time and highlighting exact prerequisite gaps across students:

```markdown
# 🍎 Educator Academic Diagnostic Summary
**Student / ID**: Learner_9281  
**Curriculum & Level**: Cambridge International A-Level (9709)  
**Subject**: Pure Mathematics 1  
**Reporting Period**: Last 14 Days  

### 1. Topic Mastery & Latent Knowledge Vector
| Syllabus Topic | Demonstrating Mastery | Independence Ratio | Status |
|---|---|---|---|
| Polynomial Algebra & Factor Theorem | 92% (Mastered) | 95% unassisted | Confirmed |
| Coordinate Geometry & Circles | 84% (Proficient) | 80% unassisted | On Track |
| Differentiation: Product & Quotient Rules | 76% (Developing) | 65% unassisted | In Progress |
| Differentiation: Chain Rule & Composition | 48% (Novice) | 30% unassisted | Needs Attention |

### 2. Persistent Misconceptions Identified
- **Item**: Chain Rule Composition
- **Root Cause**: Student consistently differentiates the outer function while omitting the inner derivative multiplication ($f'(g(x))$ instead of $f'(g(x)) \cdot g'(x)$).
- **Prerequisite Bottleneck**: Identified slight hesitation in composite function notation $f(g(x))$.

### 3. Recommended Classroom Intervention
- Brief 5-minute retrieval drill focusing on identifying the "inner" function $u = g(x)$ before attempting multi-term derivatives.
```

---

## 2. Parent & Student Weekly Progress Card

This report presents encouraging, accessible, and actionable feedback for parents and independent learners:

```markdown
# 🌟 Student Weekly Learning Progress Card
**Subject**: Science & Mathematics  
**Weekly Study Focus**: Newtonian Dynamics & Quadratic Equations  

### 📈 This Week's Highlights
- **Sessions Completed**: 4 practice sessions (Average duration: 25 minutes).
- **Mastery Achieved**: Mastered *Newton's First and Second Laws* with 90% unassisted accuracy!
- **Active Improvement**: Solved 12 multi-step physics problems from the UK GCSE past-paper question bank.

### 🎯 Next Week's Target
- We will be working on *Friction and Inclined Planes*.
- Quick tip for revision: Spend 10 minutes reviewing the difference between *mass* (in kg) and *weight* (force in Newtons).
```
