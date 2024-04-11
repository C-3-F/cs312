namespace LeetCode.NumberOfProvinces;

public class NumberOfProvincesSolution
{
    public int FindCircleNum(int[][] isConnected)
    {
        int n = isConnected.Length;
        bool[] visited = new bool[n];
        int result = 0;

        for (int i = 0; i < n; i++)
        {
            if (!visited[i])
            {
                DFS(isConnected, visited, i);
                result++;
            }
        }

        return result;
    }

    private void DFS(int[][] isConnected, bool[] visited, int i)
    {
        visited[i] = true;
        for (int j = 0; j < isConnected.Length; j++)
        {
            if (isConnected[i][j] == 1 && !visited[j])
            {
                DFS(isConnected, visited, j);
            }
        }
    }
}