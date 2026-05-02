class Solution {
public:
    string normalized(string s){
        string n = "";
        for(auto &ch : s){
            if(ch == ' ') continue;
            if(ch >= '0' && ch <= '9'){
                n += ch;
                continue;
            }
            if(ch >= 'A' && ch <= 'Z'){
                n += tolower(ch);
                continue;
            }
            if(ch >= 'a' && ch <= 'z'){
                n += ch;
            }
        }
        return n;
    }
    bool isPalindrome(string s) {
        string t = normalized(s);
        string t2 = t;
        cout<<t2<<" "<<t;
        reverse(t.begin(), t.end());
        return t2 == t;
    }
};
