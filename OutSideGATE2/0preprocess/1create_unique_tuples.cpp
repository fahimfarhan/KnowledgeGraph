#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    string s;
    set<string> st;
    while(getline(cin,s)){
        st.insert(s);
    }

    set<string>::iterator it;
    ;
    for(it=st.begin(); it!=st.end(); it++){
        s = (*it);
        cout<<(*it)<<"\n";
    }
    return 0;
}