class Solution {
private:    
    unordered_map<char, char> aliendict;
public:
    string toAlien(string word){
        string alien = "";
        for (string::iterator it = word.begin(); it < word.end(); it++){
            alien += aliendict[*it];
        }
        return alien; 
    }
    
    bool isAlienSorted(vector<string>& words, string order) {
        for (int i=0; i<order.size(); ++i){
            aliendict[order[i]] = 'a' + i;
            cout << order[i] << " " << aliendict[order[i]] << endl;
        }
        // cout << toAlien("hla"); 
        return false;
    }
};