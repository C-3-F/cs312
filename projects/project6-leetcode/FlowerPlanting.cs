namespace LeetCode.FlowerPlanting;

public class FlowerPlantingSolution
{
    public int[] GardenNoAdj(int n, int[][] paths)
    {
        Dictionary<int, List<int>> graph = new();
        for (int i = 0; i < n; i++)
        {
            graph[i] = new List<int>();
        }

        for (int i = 0; i < paths.Length; i++)
        {
            graph[paths[i][0] - 1].Add(paths[i][1] - 1);
            graph[paths[i][1] - 1].Add(paths[i][0] - 1);
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++)
        {
            bool[] colors = new bool[5];
            foreach (int neighbor in graph[i])
            {
                colors[result[neighbor]] = true;
            }

            for (int j = 1; j <= 4; j++)
            {
                if (!colors[j])
                {
                    result[i] = j;
                    break;
                }
            }
        }

        return result;
    }
}