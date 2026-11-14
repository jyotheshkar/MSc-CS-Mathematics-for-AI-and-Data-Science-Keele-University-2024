# Coursework walkthrough

The student-authored report has three parts. This walkthrough describes the source, without replacing it or claiming that every historical calculation has been independently regraded.

## 1. Linear algebra

Part 1(A) solves the system

$$
\begin{aligned}
8x+7y+3z&=18\\
-7x-4y-4z&=-11\\
-6x+5y-4z&=-15.
\end{aligned}
$$

Gaussian elimination reduces the augmented matrix before back substitution. The worked solution is $(x,y,z)=(5,-1,-5)$. Substituting it into all three original equations gives the right-hand sides exactly.

Part 1(B) explores a determinant, inverse, transpose and trace using NumPy. Its particular matrix was constructed from a student identifier, so that numerical instance and its recoverable derivatives are omitted from the public edition. The source method remains described; the omission is documented rather than replaced with invented assessed work.

For AI and data science, these ideas underpin matrix transformations and solving systems. A matrix inverse can explain a derivation, while a numerical solver is generally a more appropriate implementation for obtaining a solution than explicitly forming the inverse.

## 2. Optimisation

The coursework differentiates a quotient, identifies candidate extrema on a bounded interval, and works through gradient descent. Extrema on a closed interval require considering endpoints as well as admissible critical points; denominators and domain restrictions matter.

One source example uses

$$f(x)=x^2+4x+6=(x+2)^2+2,\qquad f'(x)=2x+4.$$

The exact minimum is at $x=-2$, with $f(-2)=2$. With $x_0=5$ and learning rate $0.1$, the first three iterates are $3.6$, $2.48$ and $1.584$. The later workbench makes that update inspectable. A successful quadratic example does not establish that arbitrary non-convex objectives converge.

## 3. Probability

The report studies conditional probability, Bayes' theorem and contingency-table probabilities. The essential distinction is the conditioning event: $P(A\mid B)$ generally differs from $P(B\mid A)$.

$$P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E\mid H)P(H)+P(E\mid\neg H)P(\neg H)}.$$

The denominator must be positive. The new workbench uses a synthetic two-hypothesis example to exercise that contract. It does not relabel synthetic values as the original coursework data or as a real medical/operational decision.

## Reading the portfolio accurately

The original assignment demonstrates written mathematical reasoning and Python/NumPy use. The separately dated implementation adds automated checks for selected calculations. The final module mark is 91%; no separate mark for a section or later software is inferred from it.
