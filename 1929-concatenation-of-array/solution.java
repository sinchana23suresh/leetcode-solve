// 1 ms | 46.4 MB
class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = 2*(nums.length);
        int[] ans = new int[n];
        int i = 0;
        while(i<n/2)
        {
            ans[i]=nums[i];
            ans[i+(n/2)]=nums[i];
            i++;
        }
        return ans;

    }
}