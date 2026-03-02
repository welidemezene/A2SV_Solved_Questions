#include <bits/stdc++.h>
 
using namespace std;
 
using li = long long;
 
int main() {
  int t;
  cin >> t;
  while (t--) {
    li n, x, k;
    cin >> n >> x >> k;
    string s;
    cin >> s;
    for (int i = 0; i < n; ++i) {
      x += (s[i] == 'L' ? -1 : +1);
      --k;
      if (!x) break;
    }
    li ans = 0;
    if (!x) {
      ans = 1;
      for (int i = 0; i < n; ++i) {
        x += (s[i] == 'L' ? -1 : +1);
        if (!x) {
          ans += k / (i + 1);
          break;
        }
      }
    }
    cout << ans << '\n';
  }
}