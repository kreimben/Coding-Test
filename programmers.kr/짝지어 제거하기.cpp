/*
https://school.programmers.co.kr/learn/courses/30/lessons/12973?language=python3
짝지어 제거하기
*/


/*
 * 정확성: 60.2
 * 효율성: 0.0
 * 합계: 60.2 / 100.0
 */

#include <iostream>
#include <string>
#include <stack>

using namespace std;

int solution(string s) {

    std::stack<char> list;
    std::string text = s;

    while (text.size()) {
        if (list.size() == 0) {
            list.push(text.at(0));
        } else if (list.top() == text.at(0)) {
            list.pop();
        } else if (list.top() != text.at(0)) {
            list.push(text.at(0));
        }

        text.erase(0, 1);
    }

    if (list.empty() && text.empty()) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    cout << solution("bbaa") << endl;
    cout << solution("baabaa") << endl;
    cout << solution("cdcd") << endl;

    return 0;
}