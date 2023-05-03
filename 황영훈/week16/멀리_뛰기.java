class Solution {
    public long solution(int n) {
        int[] result = new int[2000];
        result[0] = 1;
        result[1] = 2;
        // 점화식을 이용해서 계산
        for (int i = 2; i < n; i++) {
            result[i] = result[i-1] + result[i-2];
            result[i] %= 1234567;
        }
        return result[n-1];
    }
}