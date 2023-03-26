import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        // 검사한 단어 리스트
        ArrayList<String> checkedWords = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            checkedWords.add(words[i]);
            // 중복된 단어이면 종료
            if (hasDuplicateElements(checkedWords)) {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                return answer;
            }
            // 마지막 단어이면 종료
            if (i == words.length - 1) {
                break;
            }
            // 끝말잇기가 틀리면 종료
            if (words[i].charAt(words[i].length() - 1) != words[i + 1].charAt(0)) {
                answer[0] = (i+1) % n + 1;
                answer[1] = (i+1) / n + 1;
                return answer;
            }
        }
        return answer;
    }
    
    // 중복된 단어인지 검사하는 함수
    private boolean hasDuplicateElements(ArrayList<String> list) {
        HashSet<String> set = new HashSet<>(list);
        return list.size() != set.size();
    }
}