import sys
import importlib
import unittest
sys.path.append('../..')
quadraticEquationHaalsa = importlib.import_module(
    "quadratic-equation-haalsa.quadratic-equation-solver")


class quadraticEquationSolverTest(unittest.TestCase):

    def testShouldReturnNoSolutionIfAIsZero(self):
        self.assertEqual(quadraticEquationHaalsa
                         .solveQuadraticEquation(0, 23, 9),
                         "This equation has no solution")

    def testShouldReturnNoSolutionIfRootsAreImaginary(self):
        self.assertEqual(quadraticEquationHaalsa
                         .solveQuadraticEquation(19, 18, 5),
                         "This equation has no solution")

    def testshouldReturnSolution(self):
        self.assertEqual(quadraticEquationHaalsa
                         .solveQuadraticEquation(1, 9, 8),
                         (-1.0, -8.0))


if __name__ == "__main__":
    unittest.main()
