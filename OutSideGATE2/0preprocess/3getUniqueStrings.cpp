#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    set<string> st;
    string s1, s2, s3;
    while(cin>>s1>>s2>>s3){
        
            for(int i= s1.size()-1; i>0; i--){
                if(s1[i]==','){  s1[i]=' '; break; }
            }
            st.insert(s1);
            st.insert(s3);
    }

    set<string>::iterator it;
    string s;
    for(it=st.begin(); it!=st.end(); it++){
        s = (*it);
        if(s.size() >3)
            cout<<s<<"\n";
    }
    return 0;
}