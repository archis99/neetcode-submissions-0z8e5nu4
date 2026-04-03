class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subList = new ArrayList<>();

        recursion(0, nums, res, subList);
        return res;
    }

    private void recursion(int index, int[] nums, List<List<Integer>> res, List<Integer> subList) {
        if (index == nums.length) {
            res.add(new ArrayList<>(subList));
            return;
        }

        subList.add(nums[index]);
        recursion(index + 1, nums, res, subList);

        while (index + 1 < nums.length && nums[index] == nums[index + 1]) {
            index += 1;
        }

        subList.remove(subList.size() - 1);
        recursion(index + 1, nums, res, subList);

    }
}
