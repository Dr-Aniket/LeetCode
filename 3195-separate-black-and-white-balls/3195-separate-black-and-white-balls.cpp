class Solution {
public:
    long long minimumSteps(string s) {
     long steps=0, counter=0;
     for(char c : s){
        if (c=='0')
            steps += counter;
        else
            counter++;
        
     }   

     return steps;
    }
};