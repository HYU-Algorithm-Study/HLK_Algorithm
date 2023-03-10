import java.util.ArrayList;

class Solution {
    public int solution(int n) {
        ArrayList<Integer> fiboNums = new ArrayList<>();
        fiboNums.add(0);
        fiboNums.add(1);
        for (int i = 2; i <= n; i++) {
            // 오버플로우를 방지하기 위해 미리 나눠서 리스트에 넣어준다.
            fiboNums.add((fiboNums.get(i - 1) + fiboNums.get(i - 2)) % 1234567);
        }
        return fiboNums.get(fiboNums.size() - 1);
    }
}