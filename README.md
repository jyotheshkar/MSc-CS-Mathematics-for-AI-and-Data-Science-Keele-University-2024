# Mathematics for AI and Data Science · CSC-40072

**Jyothesh Karnam · MSc Computer Science · Keele University · 2023/24**

[![Checks](https://github.com/jyotheshkar/Mathematics-for-AI-and-Data-Science-CSC-40072-Keele-University-2024/actions/workflows/checks.yml/badge.svg)](https://github.com/jyotheshkar/Mathematics-for-AI-and-Data-Science-CSC-40072-Keele-University-2024/actions/workflows/checks.yml)

Worked mathematical reasoning across **linear algebra, optimisation and probability**, supported by my original coursework and a small reproducible study implementation.

| Academic record | Detail |
|---|---|
| Final module result | **91%** |
| Credits | **15 CATS** |
| Module | CSC-40072 — Mathematics for AI and Data Science |
| Academic year | 2023/24 |
| Official specification | [Keele's archived 2023/24 module page](https://www.keele.ac.uk/catalogue/2023-24/csc-40072.htm) |

The final module mark was checked against my final academic transcript, page 2, issued 15 January 2025. It covers the assessed module; separate report and weekly-task marks were not available. The transcript is kept private. The repository's `2024` suffix identifies the MSc academic period ending in 2024; the assignment files themselves date from November 2023.

## Explore the work

- [Original assignment and document provenance](docs/original/README.md) — my written reasoning, equations, calculations and Python screenshots, with identifier-based content redacted for publication.
- [Coursework walkthrough](docs/COURSEWORK.md) — what each part demonstrates and how it relates to AI and data science.
- [Module specification and evidence](docs/MODULE.md) — official academic scope and assessment structure.
- [Engineering decisions and verification](docs/ENGINEERING.md) — how the later implementation is bounded, tested and reproduced.

## Skills developed

| Area | Evidence in the original assignment | Relevance |
|---|---|---|
| Linear algebra | Gaussian elimination, back substitution, determinant, inverse, transpose and trace; NumPy calculations | Solving linear systems and reasoning about matrix operations |
| Calculus and optimisation | Differentiation, critical points, quotient rule and a gradient-descent example | Understanding how an objective changes and how iterative optimisation behaves |
| Probability | Conditional probability, Bayes' theorem and contingency tables | Updating beliefs and interpreting related events |
| Technical communication | Worked steps, mathematical notation, figures and explanations | Making numerical reasoning inspectable |

These are learning outcomes supported by the coursework, rather than claims of deployed AI systems or predictive performance.

## Run the reproducible examples

Requires **Python 3.11 or later**, with no third-party packages or API keys.

```bash
python -m src.workbench
python -m unittest discover -s tests -v
python scripts/verify_repository.py
```

The study workbench rechecks the assignment's three-equation system, demonstrates gradient descent on a quadratic, and includes an explicitly synthetic Bayesian example. See [the implementation notes](docs/ENGINEERING.md) for the exact input/output contract and limits.

The implementation and tests are **AI-assisted portfolio work dated 14 November 2026**. They were not submitted to Keele and are not the code that earned the module mark. The original coursework is retained as academic evidence; original errors, if present, are not silently corrected in it.

## Repository map

```text
docs/original/       Public copies of the student assignment and provenance
docs/COURSEWORK.md   Assignment walkthrough
docs/MODULE.md       Official module facts and evidence boundaries
docs/ENGINEERING.md  Decisions, numerical limits and verification
src/                Later Python study implementation
tests/              Mathematical and input-validation checks
scripts/            Local artifact and link verification
.github/workflows/  Automated repository checks
```

This is an independent student portfolio. Keele's name identifies the university and module, without implying university endorsement. Student work, university-authored material and later software retain their respective authorship; no blanket licence is applied to teaching material or third-party images.
