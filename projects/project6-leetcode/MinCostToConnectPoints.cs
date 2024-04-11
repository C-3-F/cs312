namespace LeetCode.MinCostPoints;

public class MinCostPointsSolution
{
    public int MinCostConnectPoints(int[][] points)
    {
        int n = points.Length;
        int[] dist = new int[n];
        Array.Fill(dist, int.MaxValue);
        dist[0] = 0;
        bool[] visited = new bool[n];
        int result = 0;

        for (int i = 0; i < n; i++)
        {
            int minIndex = -1;
            int minDist = int.MaxValue;
            for (int j = 0; j < n; j++)
            {
                if (!visited[j] && dist[j] < minDist)
                {
                    minDist = dist[j];
                    minIndex = j;
                }
            }

            visited[minIndex] = true;
            result += minDist;

            for (int j = 0; j < n; j++)
            {
                int d = Math.Abs(points[minIndex][0] - points[j][0]) + Math.Abs(points[minIndex][1] - points[j][1]);
                if (!visited[j] && d < dist[j])
                {
                    dist[j] = d;
                }
            }
        }

        return result;
    }
}