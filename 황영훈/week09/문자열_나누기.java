class Solution {
    public int solution(String s) {
        return splitString(s);
    }

    // 재귀함수로 구현
    private int splitString(String s) {
        // count 변수를 하나만 설정
        int count = 0;
        char x = s.charAt(0);
        for (int i = 0; i < s.length() - 1; i++) {
            // 같으면 문자면 1 증가, 다른 문자면 1 감소
            if (x == s.charAt(i)) {
                count++;
            } else {
                count--;
            }
            // 두 횟수가 같아지면 0
            if (count == 0) {
                return 1 + splitString(s.substring(i+1));
            }
        }
        // 두 횟수가 다른 상태에서 더 읽을 문자가 없으면 1 리턴
        return 1;
    }
}