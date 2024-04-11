namespace LeetCode.Triangle;

public class TriangleSolution
{
    public int MinimumTotal(IList<IList<int>> triangle)
    {
        List<List<int>> minPaths = new List<List<int>>();
        for (int i = 0; i < triangle.Count; i++)
        {
            minPaths.Add(new List<int>());
            for (int j = 0; j < triangle[i].Count; j++)
            {
                if (i == 0)
                {
                    minPaths[i].Add(triangle[i][j]);
                }
                else
                {
                    if (j == 0)
                    {
                        minPaths[i].Add(triangle[i][j] + minPaths[i - 1][j]);
                    }
                    else if (j == triangle[i].Count - 1)
                    {
                        minPaths[i].Add(triangle[i][j] + minPaths[i - 1][j - 1]);
                    }
                    else
                    {
                        minPaths[i].Add(triangle[i][j] + Math.Min(minPaths[i - 1][j - 1], minPaths[i - 1][j]));
                    }
                }
            }
        }

        return minPaths[triangle.Count - 1].Min();
    }
}