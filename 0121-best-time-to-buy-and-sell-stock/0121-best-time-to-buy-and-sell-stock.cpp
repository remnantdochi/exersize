class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        int answer = 0;
        vector<int> tmpmax(size,0);
        tmpmax.back() = prices.back();
        for (int i=size-2;i>=0;i--)
        {
            tmpmax[i] = tmpmax[i+1] > prices[i] ? tmpmax[i+1] : prices[i];
        }
        
        for (int i=0;i<size;i++)
        {
            answer = (tmpmax[i] - prices[i]) > answer ? tmpmax[i] - prices[i] : answer;
        }
        return answer;
    }
};