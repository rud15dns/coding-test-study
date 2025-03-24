// BOJ 1389
#include <bits/stdc++.h>
using namespace std;

vector<int> bacon[104];
queue<pair<int, int>> q;
int visited[104];
int root[104];
vector<pair<int, int>> answer;
int N, M, cnt = INT_MAX, idx;

void bfs(int num) {
  q.push({num, 0});
  visited[num] = 1;
  int sum = 0;
  while (!q.empty()) {
    int now = q.front().first;
    int nowcnt = q.front().second;
    sum += nowcnt;
    q.pop();

    for (int i = 0; i < bacon[now].size(); i++) {
      int next = bacon[now][i];
      if (!visited[next]) {
        nowcnt++;
        q.push({next, nowcnt});
        nowcnt--;
        visited[next] = 1;
      }
    }
  }

  answer.push_back({num, sum});
}

int main() {
  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    int a, b;
    cin >> a >> b;
    bacon[a].push_back(b);
    bacon[b].push_back(a);
    root[a] = root[b] = 1;
  }

  for (int i = 1; i < 104; i++) {
    if (root[i]) {
      memset(visited, 0, sizeof(visited));
      bfs(i);
    }
  }

  for (auto ans : answer) {
    if (cnt > ans.second) {
      cnt = ans.second;
      idx = ans.first;
    }
  }
  cout << idx << endl;
}
