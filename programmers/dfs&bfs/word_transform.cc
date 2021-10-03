// https://programmers.co.kr/learn/courses/30/lessons/43163

#include <stack>
#include <string>
#include <vector>

using namespace std;

struct transf {
    transf(int i, vector<int> &v) : idx(i), visited(v) {}
    int idx;
    vector<int> visited;
};
int solution(string begin, string target, vector<string> words) {
    int cnt, f, len = words.size(), w_len = begin.length(), min = INT32_MAX;
    stack<transf> stk;
    vector<int> v(len, 0);
    stk.push(transf(-1, v));
    while (!stk.empty()) {
        auto curr = stk.top();
        auto w = curr.idx == -1 ? begin : words[curr.idx];
        if (w == target) {
            cnt = 0;
            for (const auto &b : curr.visited)
                if (b)
                    cnt++;
            if (cnt < min)
                min = cnt;
        }
        stk.pop();
        for (int i = 0; i < len; i++) {
            if (i != curr.idx && !curr.visited[i]) {
                cnt = 0, f = 0;
                for (int j = 0; j < w_len; j++) {
                    if (words[i][j] != w[j])
                        if (!cnt)
                            cnt++;
                        else {
                            f = 1;
                            break;
                        }
                }
                if (!f) {
                    auto v_ = curr.visited;
                    v_[i] = 1;
                    stk.push(transf(i, v_));
                }
            }
        }
    }
    return min == INT32_MAX ? 0 : min;
}
