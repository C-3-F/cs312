namespace LeetCode.Tribonacci;

public class TribonacciSolution {

    public int Tribonacci(int n) {
        
        List<int> solution = new List<int> { 0, 1, 1};
        for (int i = 3; i <= n; i++) {
            // Console.WriteLine(i);
            solution.Add(solution[i-1] + solution[i-2] + solution[i-3]);
        }

        return solution[n];
    }
}