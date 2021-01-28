import unittest
from Dijkstra import Dijkstra as dij_sp

####Input format:
#### N = Number of nodes
#### E = Number of edges
#### Mat = A matrix of dimension Ex3
##### Each row of Mat consist of 3 integers. The first 2 integers denote the 2 nodes between which the
#### undirected edge exists. The third integer denotes the weight of edge between these corresponding nodes
#### S = source vertex to start Dijkstra Algorithm
    
class TestCases(unittest.TestCase):

    def testcase1(self):
        se = dij_sp()
        N = 5
        E = 6
        Mat = [[1, 2, 9], [1, 3, 6], [1, 4, 5], [1, 5, 3], [3, 2, 2], [3, 4, 4]]
        S = 1
        answer = [[0, 1],[8, 1],[6, 1], [5, 1], [3, 1]]
        self.assertEqual(se.Dijkstra_alg(N, E, Mat, S),answer)

    def testcase2(self):
        se = dij_sp()
        N = 5
        E = 6
        Mat = [[1, 3, 2], [1, 5, 3], [2, 5, 3], [4, 1, 1], [4, 2, 1], [4, 5, 4]]
        S = 4
        answer = [[1, 1],[1, 1],[3, 1], [0, 1], [4, 0]]
        self.assertEqual(se.Dijkstra_alg(N, E, Mat, S),answer)

    def testcase3(self):
        se = dij_sp()
        N = 5
        E = 6
        Mat = [[1, 2, 9], [1, 3, 6], [1, 4, 5], [1, 5, 3], [3, 2, 2], [3, 4, 4]]
        S = 2
        answer = [[8, 1],[0, 1],[2, 1], [6, 1], [11, 1]]
        self.assertEqual(se.Dijkstra_alg(N, E, Mat, S),answer)

    def testcase4(self):
        se = dij_sp()
        N = 4
        E = 4
        Mat = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]
        S = 1
        answer = [[0, 1],[24, 1],[3, 1], [15, 1]]
        self.assertEqual(se.Dijkstra_alg(N, E, Mat, S),answer)

    def testcase5(self):
        se = dij_sp()
        N = 4
        E = 5
        Mat = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12], [2, 4, 9]]
        S = 1
        answer = [[0, 1],[24, 0],[3, 1], [15, 1]]
        self.assertEqual(se.Dijkstra_alg(N, E, Mat, S),answer)

    def testcase6(self):
        se = dij_sp()
        N = 3
        E = 2
        Mat = [[1, 2, 5], [2, 3, 7]]
        S = 3
        answer = [[12, 1],[7, 1],[0, 1]]
        self.assertEqual(se.Dijkstra_alg(N, E, Mat, S),answer)

    def testcase7(self):
        se = dij_sp()
        N = 3
        E = 3
        Mat = [[1, 2, 4], [2, 3, 1], [1, 3, 5]]
        S = 1
        answer = [[0, 1],[4, 1],[5, 0]]
        self.assertEqual(se.Dijkstra_alg(N, E, Mat, S),answer)

if __name__ == '__main__':
    unittest.main()
