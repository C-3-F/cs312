namespace LeetCode.TwoSum;

public class TwoSumSolution
{
    public int[] TwoSum(int[] nums, int target)
    {
        Dictionary<int, int> map = new();
        for (int i = 0; i < nums.Length; i++)
        {
            int op = target - nums[i];
            if (map.ContainsKey(op))
            {
                return new int[] { map[op], i };
            }
            map[nums[i]] = i;
        }
        return new int[] { -1, -1 };
    }
}