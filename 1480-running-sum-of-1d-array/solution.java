// 0 ms | 44 MB

class Solution {
    public int[] runningSum(int[] nums) {

        int n = nums.length;
        int[] sumarr = new int[n];

        int sum = 0;
        int i = 0;

        while (i < n) {
            sum = sum + nums[i];
            sumarr[i] = sum;
            i++;
        }

        return sumarr;
    }
}
