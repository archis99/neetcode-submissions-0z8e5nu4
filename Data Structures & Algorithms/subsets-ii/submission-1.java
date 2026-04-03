class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        recursion(0, nums, new ArrayList<>(), res);
        return res;
    }

    private void recursion(int index, int[] nums, List<Integer> subList, List<List<Integer>> res) {
        if (index == nums.length) {
            res.add(new ArrayList<>(subList));
            return;
        }

        subList.add(nums[index]);
        recursion(index + 1, nums, subList, res);

        subList.remove(subList.size() - 1);

        while (index + 1 < nums.length && nums[index] == nums[index + 1]) {
            index += 1;
        }
        recursion(index + 1, nums, subList, res);
    }
}
