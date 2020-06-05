// method 1;

class Solution {
public:
    void reverseString(vector<char>& s) {
        int i = 0;
        int j = s.size()-1;
        while(i<=j)
        {
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i++;
            j--;
        }
    }
};

///////////////////////////////////////////////////////////////////////////////////////////////////////

// method 2 : 

class Solution {
public:
    void reverseString(vector<char>& s) {
        int i = 0;
        int j = s.size()-1;
        while(i<=j)
        {
            swap(s[i++], s[j--]);
        }
    }
};