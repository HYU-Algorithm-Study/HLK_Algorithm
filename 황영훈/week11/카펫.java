import java.lang.Math;
import java.util.ArrayList;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        ArrayList<int[]> yellowCases = new ArrayList<>();

        // 노란색 격자 크기의 경우의 수 모두 구하기
        for (int i = 1; i <= Math.sqrt(yellow); i++) {
            if (yellow % i == 0) {
                int[] lengths = {yellow / i, i};
                yellowCases.add(lengths);
            }
        }

        // 갈색 격자 크기와 일치하는 경우 찾기
        for (int i = 0; i < yellowCases.size(); i++) {
            int width = yellowCases.get(i)[0];
            int height = yellowCases.get(i)[1];
            if (brown == (width + height + 2) * 2) {
                answer[0] = width + 2;
                answer[1] = height + 2;
                break;
            }
        }
        
        return answer;
    }
}