// https://programmers.co.kr/learn/courses/30/lessons/43162

#include <stack>
#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int n_computer = computers.size(), cnt = 0;
    vector<int> visited(n_computer, 0);
    stack<int> network;
    for (int i = 0; i < n_computer; i++) {
        if (!visited[i]) {
            network.push(i);
            visited[i] = 1;
            while (!network.empty()) {
                auto curr = network.top();
                network.pop();
                for (int j = 0; j < n_computer; j++) {
                    if (!visited[j] && computers[curr][j]) {
                        network.push(j);
                        visited[j] = 1;
                    }
                }
            }
            cnt++;
        }
    }
    return cnt;
}