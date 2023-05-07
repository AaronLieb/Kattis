#include <bits/stdc++.h>
using namespace std;
vector<int> widths;
vector<int> heights;
int memo[5005][5005];
#define rep(i,a,b) for(int i = a; i <(b); ++i)
#define sz(x) (int)x.size()
int windows, maxsize;
template<class T>
struct RMQ{
    vector<vector<T>> jmp;
    RMQ(const vector<T> &V) : jmp(1,V){
        for(int pw = 1, k = 1; pw*2 <=V.size(); pw*=2,++k){
            jmp.emplace_back(sz(V)-pw*2+1);
            rep(j,0,sz(jmp[k]))
                jmp[k][j] = max(jmp[k-1][j], jmp[k-1][j+pw]);
        }
    }
    T query(int a, int b){
        assert(a<b);
        int dep = 31-__builtin_clz(b-a);
        return max(jmp[dep][a],jmp[dep][b-(1<<dep)]);
    }
};

int sum(int a,int b){
    int big = widths[b];
    int small = 0;
    if(a > 0){
        small = widths[a-1];
    }
    return big-small;
}

RMQ<int>* rmq;
int dp(int last, int index){
    if(index == windows){
        if(last != index) return rmq->query(last,index);
        return 0;
    }

    if(memo[last][index] != -1) return memo[last][index];
    int s = sum(last,index);
    if(s > maxsize) return 1e9;
    int a = dp(last,index+1);
    int b = dp(index+1,index+1) + rmq->query(last,index+1);
    return memo[last][index] = min(a,b);
}

int main(){
    cin >> windows >> maxsize;
    memset(memo,-1,sizeof(memo));
    widths = vector<int>(windows);
    heights = vector<int>(windows);
    for(int i = 0; i < windows; i++){
        int w,h; cin >> widths[i] >> heights[i];
    }

    rmq = new RMQ<int>(heights);
    partial_sum(widths.begin(),widths.end(),widths.begin());
    cout << dp(0,0);
    return 0;
}
