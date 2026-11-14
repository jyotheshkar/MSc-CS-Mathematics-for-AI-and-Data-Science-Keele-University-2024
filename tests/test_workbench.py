"""Mathematical invariants and input-boundary checks for later reproductions."""
import copy
import math
import unittest

from src.workbench import bayes_posterior, demonstration, gradient_descent, solve_linear_system


class LinearSystemTests(unittest.TestCase):
    def assert_solution(self, matrix, rhs, expected):
        actual = solve_linear_system(matrix, rhs)
        for x, y in zip(actual, expected):
            self.assertAlmostEqual(x, y, places=10)
        for row, target in zip(matrix, rhs):
            self.assertAlmostEqual(math.fsum(a*x for a, x in zip(row, actual)), target, places=10)

    def test_assignment_system_and_residual(self):
        self.assert_solution([[8,7,3],[-7,-4,-4],[-6,5,-4]], [18,-11,-15], [5,-1,-5])

    def test_zero_leading_pivot_requires_row_exchange(self):
        self.assert_solution([[0,2],[3,4]], [4,11], [1,2])

    def test_scaling_and_input_immutability(self):
        matrix = [[1e-20, 2e-20], [3e-20, 4e-20]]
        rhs = [5e-20, 11e-20]
        original = copy.deepcopy((matrix, rhs))
        self.assert_solution(matrix, rhs, [1,2])
        self.assertEqual((matrix, rhs), original)

    def test_singular_and_numerically_singular_fail(self):
        for matrix in ([[1,2],[2,4]], [[0,0],[0,0]], [[1,0],[0,1e-14]]):
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                solve_linear_system(matrix, [1,2])

    def test_dimensions_and_nonfinite_inputs_fail(self):
        for matrix, rhs in [([],[]), ([[1,2]],[1]), ([[1]],[1,2]), ([[math.nan]],[1]), ([[1]],[math.inf]), ([[True]],[1]), (None,[1])]:
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                solve_linear_system(matrix, rhs)


class OptimisationTests(unittest.TestCase):
    def test_assignment_trace_and_descent(self):
        trace = gradient_descent()
        for row, expected in zip(trace, [5,3.6,2.48,1.584]):
            self.assertAlmostEqual(row['x'], expected)
        self.assertTrue(all(a['objective'] > b['objective'] for a,b in zip(trace, trace[1:])))

    def test_convergence_to_analytic_minimum(self):
        final = gradient_descent(start=-50, learning_rate=0.1, iterations=200)[-1]
        self.assertAlmostEqual(final['x'], -2)
        self.assertAlmostEqual(final['objective'], 2)
        self.assertAlmostEqual(final['gradient'], 0)

    def test_zero_iterations_and_stationary_start(self):
        self.assertEqual(len(gradient_descent(iterations=0)),1)
        self.assertTrue(all(row['x'] == -2 for row in gradient_descent(start=-2)))

    def test_invalid_rates_iterations_and_overflow_fail(self):
        for kwargs in [{'learning_rate':0},{'learning_rate':1},{'learning_rate':math.nan},{'start':math.inf},{'start':1e308},{'iterations':-1},{'iterations':1.5},{'iterations':True},{'iterations':10001}]:
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                gradient_descent(**kwargs)


class ProbabilityTests(unittest.TestCase):
    def test_synthetic_example_and_complement_identity(self):
        posterior = bayes_posterior(0.1,0.8,0.2)
        self.assertAlmostEqual(posterior,4/13)
        self.assertAlmostEqual(posterior + bayes_posterior(0.9,0.2,0.8),1)

    def test_uninformative_evidence_preserves_prior(self):
        for prior in (0,0.1,0.5,1):
            self.assertAlmostEqual(bayes_posterior(prior,0.25,0.25),prior)

    def test_certain_and_impossible_hypotheses(self):
        self.assertEqual(bayes_posterior(1,0.8,0.2),1)
        self.assertEqual(bayes_posterior(0,0.8,0.2),0)
        self.assertEqual(bayes_posterior(0.2,1,0),1)

    def test_invalid_and_undefined_probabilities_fail(self):
        for args in ((0,0,0),(1,0,0.1),(-0.1,0.5,0.5),(0.5,1.1,0.1),(math.nan,0.5,0.1),(0.5,math.inf,0.1),(True,0.5,0.1)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                bayes_posterior(*args)

    def test_demo_reports_provenance_and_finite_results(self):
        data = demonstration()
        self.assertIn('2026',data['edition'])
        self.assertIn('Synthetic',data['probability']['source'])
        self.assertLess(data['linear_algebra']['max_absolute_residual'],1e-10)


if __name__ == '__main__':
    unittest.main()
