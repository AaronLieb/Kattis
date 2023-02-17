#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const ll inf = 1LL << 62;
void floydWarshall(vector<vector<ll>>& m) {
  int n = sz(m);
  rep(i, 0, n) m[i][i] = min(m[i][i], 0LL);
  rep(k, 0, n) rep(i, 0, n) rep(j, 0, n)
    if (m[i][k] != inf && m[k][j] != inf) {
      auto newDist = max(m[i][k] + m[k][j], -inf);
      m[i][j] = min(m[i][j], newDist);
    }
  rep(k, 0, n) if (m[k][k] < 0) rep(i, 0, n) rep(j, 0, n)
    if (m[i][k] != inf && m[k][j] != inf) m[i][j] = -inf;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  cin.exceptions(cin.failbit);
  int n, m, q, u, v;
  ll w;
  while (1) {
    cin >> n >> m >> q;
    if (n == 0 && m == 0 && q == 0) return 0;
    vector<vector<ll>> g(n, vector<ll>(n, inf));
    for (int i = 0; i < m; ++i) {
      cin >> u >> v >> w;
      g[u][v] = w;
    }
    floydWarshall(g);
    for (int i = 0; i < q; ++i) {
      cin >> u >> v;
      w = g[u][v];
      if (w == inf) cout << "Impossible" << endl;
      else if (w == -inf) cout << "-Infinity" << endl;
      else cout << w << endl;
    }
    cout << endl;
  }
}
