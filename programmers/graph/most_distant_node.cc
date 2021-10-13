// https://programmers.co.kr/learn/courses/30/lessons/49189

#include <algorithm>
#include <queue>
#include <string>
#include <vector>

using namespace std;

struct vertex {
    int dist = INT32_MAX;
    vector<int> edges;
};
int solution(int n, vector<vector<int>> edge) {
    vector<vertex> graph(n + 1);
    for (const auto &e : edge) {
        graph[e[0]].edges.push_back(e[1]);
        graph[e[1]].edges.push_back(e[0]);
    }
    queue<pair<int, int>> q;
    graph[1].dist = 0;
    q.push({-1, 1});
    while (!q.empty()) {
        auto curr = q.front();
        q.pop();
        for (const auto &v : graph[curr.second].edges) {
            if (v != curr.first) {
                if (graph[curr.second].dist + 1 < graph[v].dist) {
                    graph[v].dist = graph[curr.second].dist + 1;
                    q.push({curr.second, v});
                }
            }
        }
    }
    sort(graph.begin() + 1, graph.end(), [](auto &l, auto &r) { return l.dist > r.dist; });
    int max_dist = graph[1].dist, cnt = 0;
    for (int i = 1; i <= n; i++) {
        if (graph[i].dist != max_dist)
            break;
        cnt++;
    }
    return cnt;
}
