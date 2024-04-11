// See https://aka.ms/new-console-template for more information
using LeetCode.BinaryTreeTraversal;
using LeetCode.CombinationSum;
using LeetCode.CourseSchedule;
using LeetCode.FlowerPlanting;
using LeetCode.LowestCommonAncestor;
using LeetCode.MinCostPoints;
using LeetCode.NumberOfProvinces;
using LeetCode.PerfectSquares;
using LeetCode.QueueReconstruction;
using LeetCode.Triangle;
using LeetCode.Tribonacci;
using LeetCode.TwoSum;

Console.WriteLine("LeetCode");

// https://leetcode.com/problems/n-th-tribonacci-number/submissions/1228973371/
var tribonacci = new TribonacciSolution();
// Console.WriteLine("Tribonacci");
// Console.WriteLine(tribonacci.Tribonacci(25));

// https://leetcode.com/problems/combination-sum/submissions/1228977324/
var combinationSum = new CombinationSumSolution();
// Console.WriteLine("Combination Sum");
// Console.WriteLine(combinationSum.CombinationSum(new int[] { 2, 3, 6, 7 }, 7));

// https://leetcode.com/problems/min-cost-to-connect-all-points/submissions/1228982374/
var minCostConnectPoints = new MinCostPointsSolution();
// Console.WriteLine("Min Cost to Connect Points");
// Console.WriteLine(minCostConnectPoints.MinCostConnectPoints(new int[][] { new int[] { 0, 0 }, new int[] { 2, 2 }, new int[] { 3, 10 }, new int[] { 5, 2 }, new int[] { 7, 0 } }));

// https://leetcode.com/problems/number-of-provinces/submissions/1228989203/
var numberOfProvinces = new NumberOfProvincesSolution();
// Console.WriteLine("Number of Provinces");
// Console.WriteLine(numberOfProvinces.FindCircleNum(new int[][] { new int[] { 1, 1, 0 }, new int[] { 1, 1, 0 }, new int[] { 0, 0, 1 } }));

// https://leetcode.com/problems/perfect-squares/submissions/1228998330/
var perfectSquares = new PerfectSquaresSolution();
// Console.WriteLine("Perfect Squares");
// Console.WriteLine(perfectSquares.NumSquares(12));

// https://leetcode.com/problems/triangle/submissions/1229003890/
var triange = new TriangleSolution();
// Console.WriteLine("Triangle");
// Console.WriteLine(triange.MinimumTotal(new List<IList<int>> { new List<int> { 2 }, new List<int> { 3, 4 }, new List<int> { 6, 5, 7 }, new List<int> { 4, 1, 8, 3 } }));


// https://leetcode.com/problems/two-sum/submissions/1229008588/
var twoSum = new TwoSumSolution();
// Console.WriteLine("Two Sum");
// Console.WriteLine(twoSum.TwoSum(new int[] { 2, 7, 11, 15 }, 9));


// https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1229013160/
var binaryTreeLevelOrderTraversal = new BinaryTreeOrderTraversalSolution();
// Console.WriteLine("Binary Tree Level Order Traversal");
// Console.WriteLine(binaryTreeLevelOrderTraversal.LevelOrder(new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)))));

// https://leetcode.com/problems/flower-planting-with-no-adjacent/submissions/1229018753/
var flowerPlanting = new FlowerPlantingSolution();
// Console.WriteLine("Flower Planting With No Adjacent");
// Console.WriteLine(flowerPlantingWithNoAdjacent.GardenNoAdj(3, new int[][] { new int[] { 1, 2 }, new int[] { 2, 3 }, new int[] { 3, 1 } }));

// https://leetcode.com/problems/course-schedule/submissions/1229021894/
var courseSchedule = new CourseScheduleSolution();
// Console.WriteLine("Course Schedule");
// Console.WriteLine(courseSchedule.CanFinish(2, new int[][] { new int[] { 1, 0 } }));

// https://leetcode.com/problems/queue-reconstruction-by-height/submissions/1229027870/
var queueReconstruction = new QueueReconstructionSolution();
// Console.WriteLine("Queue Reconstruction By Height");
// Console.WriteLine(queueReconstructionByHeight.ReconstructQueue(new int[][] { new int[] { 7, 0 }, new int[] { 4, 4 }, new int[] { 7, 1 }, new int[] { 5, 0 }, new int[] { 6, 1 }, new int[] { 5, 2 } }));

// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1229039114/
var lowestCommonAncestor = new LowestCommonAncestorSolution();
// Console.WriteLine("Lowest Common Ancestor of a Binary Tree");
// Console.WriteLine(lowestCommonAncestor.LowestCommonAncestor(new TreeNode(3, new TreeNode(5, new TreeNode(6), new TreeNode(2, new TreeNode(7), new TreeNode(4))), new TreeNode(1, new TreeNode(0), new TreeNode(8))), new TreeNode(5), new TreeNode(1)).val);