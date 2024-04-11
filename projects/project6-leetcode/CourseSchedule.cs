namespace LeetCode.CourseSchedule;

public class CourseScheduleSolution
{
    public bool CanFinish(int numCourses, int[][] prerequisites)
    {
        Dictionary<int, List<int>> graph = new();
        for (int i = 0; i < numCourses; i++)
        {
            graph[i] = new List<int>();
        }

        for (int i = 0; i < prerequisites.Length; i++)
        {
            graph[prerequisites[i][0]].Add(prerequisites[i][1]);
        }

        bool[] completed = new bool[numCourses];
        bool[] recStack = new bool[numCourses];

        for (int i = 0; i < numCourses; i++)
        {
            if (IsCyclic(graph, completed, recStack, i))
            {
                return false;
            }
        }

        return true;
    }

    private bool IsCyclic(Dictionary<int, List<int>> graph, bool[] completed, bool[] recStack, int i)
    {
        if (recStack[i])
        {
            return true;
        }

        if (completed[i])
        {
            return false;
        }

        recStack[i] = true;
        completed[i] = true;

        foreach (int neighbor in graph[i])
        {
            if (IsCyclic(graph, completed, recStack, neighbor))
            {
                return true;
            }
        }

        recStack[i] = false;
        return false;
    }
}