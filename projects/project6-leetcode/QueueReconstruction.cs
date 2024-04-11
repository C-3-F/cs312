namespace LeetCode.QueueReconstruction;

public class QueueReconstructionSolution
{
    public int[][] ReconstructQueue(int[][] people)
    {
        Array.Sort(people, (a, b) =>
        {
            if (a[0] == b[0])
            {
                return a[1] - b[1];
            }
            return b[0] - a[0];
        });

        List<int[]> result = new List<int[]>();
        foreach (int[] p in people)
        {
            result.Insert(p[1], p);
        }

        return result.ToArray();
    }
}