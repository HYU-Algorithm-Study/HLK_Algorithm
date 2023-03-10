class Solution {
    public int solution(int n) {
        int answer = n + 1;
        // 이진수로 변환 후 1의 개수 세기
        int count = countOne(Integer.toBinaryString(n));
        // 1의 개수가 같은 다음 큰 수 찾기
        while (count != countOne(Integer.toBinaryString(answer))) {
            answer += 1;
        }
        return answer;
    }
    
    private int countOne(String str) {
        return str.length() - str.replace("1", "").length();
    }
}