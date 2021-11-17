#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    vector<vector<bool>> graph(n + 1, vector<bool>(n + 1));
    for (const auto &result : results)
        graph[result[0]][result[1]] = 1;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            for (int k = 1; k <= n; k++)
                if (graph[j][i] && graph[i][k])
                    graph[j][k] = 1;
    int n_ = 0, cnt;
    for (int i = 1; i <= n; i++) {
        cnt = 0;
        for (int j = 1; j <= n; j++)
            if (graph[i][j] || graph[j][i])
                cnt++;
        if (cnt == n - 1)
            n_++;
    }
    return n_;
}
