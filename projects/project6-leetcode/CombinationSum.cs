namespace LeetCode.CombinationSum
{
    public class CombinationSumSolution
    {
        public IList<IList<int>> CombinationSum(int[] candidates, int target)
        {
            IList<IList<int>> result = new List<IList<int>>();
            IList<int> current = new List<int>();
            Backtrack(candidates, target, 0, current, result);
            return result;
        }

        private void Backtrack(int[] candidates, int target, int start, IList<int> current, IList<IList<int>> result)
        {
            if (target == 0)
            {
                result.Add(new List<int>(current));
                return;
            }

            for (int i = start; i < candidates.Length; i++)
            {
                if (candidates[i] <= target)
                {
                    current.Add(candidates[i]);
                    Backtrack(candidates, target - candidates[i], i, current, result);
                    current.RemoveAt(current.Count - 1);
                }
            }
        }
    }
}