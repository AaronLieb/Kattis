#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

// return dist
ll recur(int cx, int cy, ll d, set<string> remain, const vector<pair<string, pii>>& g, ll& mind) {
  if (remain.empty()) { return d + cx + cy; }
  if (d + cx + cy >= mind) { return LLONG_MAX; }
  for (string r : remain) {
    for (auto point : g) {
      if (r == point.first) {
        int nx = point.second.first;
        int ny = point.second.second;
        int diff = abs(cx - nx) + abs(cy - ny);
        set<string> newRemain(remain);
        newRemain.erase(point.first);
        mind = min(recur(nx, ny, d + diff, newRemain, g, mind), mind);
      }
    }
  }
  return mind;
}

int main() {
  cin.tie(0)->sync_with_stdio(0);
  cin.exceptions(cin.failbit);
  int n, x, y;
  string name;
  cin >> n;
  vector<pair<string, pii>> g;
  set<string> pokemon;
  for (int i = 0; i < n; ++i) {
    cin >> x >> y >> name;
    pokemon.insert(name);
    g.push_back({name, {x, y}});
  }
  ll m = LLONG_MAX;
  cout << recur(0, 0, 0, pokemon, g, m) << endl;
}
