namespace LeetCode.PerfectSquares;

public class PerfectSquaresSolution
{
    public int NumSquares(int n)
    {
        List<int> squares = new();
        for (int i = 1; i * i <= n; i++)
        {
            squares.Add(i * i);
        }

        List<int> subProblems = new() { 0 };

        for (int i = 1; i <= n; i++)
        {
            int min = int.MaxValue;
            foreach (int square in squares)
            {
                if (i - square >= 0)
                {
                    min = Math.Min(min, subProblems[i - square] + 1);
                }
            }
            subProblems.Add(min);
        }

        return subProblems[n];
    }
}