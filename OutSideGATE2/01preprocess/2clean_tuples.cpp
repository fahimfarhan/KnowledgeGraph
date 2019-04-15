#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    string s, s1;
    int end;
    while(getline(cin,s1)){
        s = s1.substr(16);
        end = s.size() - 1;
        for(int i=end; i>0; i--){
            if(s[i]=='}'){  s[i] = ' '; break; }
        }
        for(int i=0; i<s.size()-1; i++){
            if( (s[i]=='u') && (s[i+1]=='=') ){
                s[i]=' '; s[i+1]=' ';
            }
        }
       for(int i=0; i<s.size()-1; i++){
            if( (s[i]=='v') && (s[i+1]=='=') ){
                s[i]=' '; s[i+1]=' ';
            }
        }

        for(int i=0; i<s.size()-1; i++){
            if( (s[i]=='e') && (s[i+1]=='=') ){
                s[i]=' '; s[i+1]=' ';
            }
        }
        cout<<s<<"\n";
    }
    return 0;
}