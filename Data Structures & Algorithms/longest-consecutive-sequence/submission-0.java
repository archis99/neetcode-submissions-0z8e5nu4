class Solution {
    public int longestConsecutive(int[] nums) {
        int res = 0;
        Set<Integer> set = new HashSet<>();

        for (int num: nums) {
            set.add(num);
        }

        for (int i = 0; i < nums.length; i++) {
            if (!set.contains(nums[i] - 1)) {
                int length = 0;
                while (set.contains(nums[i] + length)) {
                    length += 1;
                }
                res = Math.max(res, length);
            }
        }

        return res;
    }
}
