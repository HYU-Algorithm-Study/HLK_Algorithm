import java.util.Stack;

class Solution {
    public int solution(String s) {
        // 문자 하나씩 검사하기 위해 문자열 배열 생성
        String[] strArray = s.split("");
        // stack을 이용해 문제 해결
        Stack<String> stack = new Stack<>();
        // 문자 하나씩 검사
        for (int i = 0; i < s.length(); i++) {
            // 빈 스택이면 바로 push
            if (stack.isEmpty()) {
                stack.push(strArray[i]);
                continue;
            }
            // 두 문자가 같으면 pop, 다르면 push
            if (stack.peek().equals(strArray[i])) {
                stack.pop();
            } else {
                stack.push(strArray[i]);
            }
        }
        // 문자를 모두 검사한 후 stack이 비었으면 짝지어 제거하기 성공
        if (stack.isEmpty()) {
            return 1;
        }
        return 0;
    }
}