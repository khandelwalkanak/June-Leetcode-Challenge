bool comp(const vector<int>& v1, const vector<int>& v2)
{
    return v1[0]>v2[0] || (v1[0] == v2[0] && v1[1]<v2[1]);
}
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) 
    {
        vector<vector<int>> res;
        sort(people.begin(), people.end(),comp);
        for(int i = 0; i < people.size(); i++)
        {
            if(people[i][1] == res.size())
            {
                res.push_back(people[i]);
            }
            else
            {
                res.insert(res.begin() + people[i][1], people[i]);
            }
        }
        return res;
    }
};