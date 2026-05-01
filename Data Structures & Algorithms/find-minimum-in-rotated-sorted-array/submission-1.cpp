class Solution {
public:
    // 0  1  2  3  4  5
    // 3, 4, 5, 6, 1, 2

    int findMin(vector<int> &nums) {
        int n = nums.size();
        int le = 0;
        int ri = n-1;
        int res = nums[le];
        while(le <= ri){
            if(nums[le] < nums[ri]){
                res = min(res, nums[le]);
                break;
            }
            int m = le + (ri-le)/2;
            res = min(res, nums[m]);
            if(nums[m] >= nums[le]){
                le = m + 1;
            }else{
                ri = m  -1;
            }
        }
        return res;
    }
};
