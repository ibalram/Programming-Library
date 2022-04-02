#include <stdio.h>

// #include<bits/stdc++.h>
// using namespace std;
// int numBooks(int option1, int option2=0){
//     switch(option1)
//     return 0;
// }

int main(){

    // if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
    int option1, option2;
    printf("Please enter your type(1 for student, 2 for teacher, 3 for employee):\n");
    scanf("%d", &option1);
    // break;
    // int numberOfBooks;
    switch(option1){
        case 1:
            printf("Enter your level(1 for Elementry, 2 for High school):\n");
            scanf("%d", &option2);
            switch(option2){
                case 1:
                    printf("You can borrow 3 books\n");
                    break;
                case 2:
                    printf("You can borrow 4 books\n");
                    break;
                default:
                    break;
            }
            break;
        case 2:
            printf("You can borrow 8 books\n");
            break;
        case 3:
            printf("You can borrow 5 books\n");
            break;
        default:
            break;

    }

    return 0;
}





// #include<bits/stdc++.h>
// using namespace std;

// typedef long long ll;
// typedef unsigned long long ull;
// typedef long double ld;
// #define endl "\n"
// const ll mod = 1e9+7;
// const int mxn = 2e5+2;


// void solve(){

// }

// int main(){
//     if(FILE*f=fopen(string("in.txt").c_str(),"r")){fclose(f),freopen("in.txt","r",stdin);}
//     else {ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
//     int t = 1;
//     // cin>>t;
//     while(t-->0) solve();
//     return 0;
// }
