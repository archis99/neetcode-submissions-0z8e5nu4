class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subList = new ArrayList<>();

        recursion(0, nums, target, 0, subList, res);

        return res;
    }

    private void recursion(int index, int[] nums, int target, int sum, 
                            List<Integer> subList, List<List<Integer>> res) {

        
        if (target == sum) {
            res.add(new ArrayList<>(subList));
            return;
        }

        if (index == nums.length || sum > target) {
            return;
        }

        subList.add(nums[index]);
        // Using same index for adding same element
        // Adding to the sum
        recursion(index, nums, target, sum + nums[index], subList, res);

        subList.remove(subList.size() - 1);
        // Using the next index
        recursion(index + 1, nums, target, sum, subList, res);
    }
}
