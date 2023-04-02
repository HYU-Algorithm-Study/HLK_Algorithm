class Solution {
    public String solution(String[] survey, int[] choices) {
        // 변수 초기화
        String answer = "";
        int[] scores = new int[4];
        String[] leftTypes = {"R", "C", "J", "A"};
        String[] rightTypes = {"T", "F", "M", "N"};
        
        // 문항마다 성격유형과 점수를 계산
        for (int i = 0; i < choices.length; i++) {
            String type = "";
            int score = 0;
            if (choices[i] < 4) {
                type = survey[i].substring(0,1);
                score = 4 - choices[i];
            }
            if (choices[i] > 4) {
                type = survey[i].substring(1);
                score = choices[i] - 4;
            }
            for (int j = 0; j < 4; j++) {
                if (leftTypes[j].equals(type)) {
                    scores[j] += score;
                    break;
                }
                if (rightTypes[j].equals(type)) {
                    scores[j] -= score;
                    break;
                }
            }
        }
        
        // 더 높은 점수를 가진 유형을 선택
        for (int i = 0; i < 4; i++) {
            answer += (scores[i] >= 0) ? leftTypes[i] : rightTypes[i];
        }
        
        return answer;
    }
}