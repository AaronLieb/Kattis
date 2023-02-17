#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

double CIRCUM = 60 * M_PI;
double ARC = CIRCUM/28;

int main() {
  cin.tie(0)->sync_with_stdio(0);
  cin.exceptions(cin.failbit);
  int n;
  string t;
  cin >> n;
  vector<char> loop = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '\''};
  for (int i = 0; i < n; i++) {
    getline(cin, t);
    if (t.size() <= 0) {
      i--;
      continue;
    }
    for (int j = 0; j < t.size(); j++) {
      t[j] = tolower(t[j]);
    }
    double time = 0;
    int curr = distance(loop.begin(), find(loop.begin(), loop.end(), t[0]));
    for (char c : t) {
      int index = distance(loop.begin(), find(loop.begin(), loop.end(), c));
      int dis = abs(curr - index);
      if (dis > 13) {
        dis = 28 - dis;
      }
      time += ((double)dis * ARC)/15.0 + 1;
      curr = index;
    }
    cout << fixed << setprecision(10) << time << endl;
  }
}
