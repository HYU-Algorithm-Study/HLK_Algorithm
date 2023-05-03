import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        String date;
        int year, month, period = 0, num = 1;
        ArrayList<Integer> result = new ArrayList<>();
        
        for (String privacy : privacies) {
            // 약관 종류 확인 후 유효기간 구하기
            for (String term : terms) {
                if (privacy.split(" ")[1].equals(term.split(" ")[0])) {
                    period = Integer.parseInt(term.split(" ")[1]);
                    break;
                }
            }
            // month와 year을 계산 후 전체 date 구하기
            month = Integer.parseInt(privacy.substring(5, 7)) + period;
            year = Integer.parseInt(privacy.substring(0, 4));
            if (month > 12) {
                year += (month - 1) / 12;
                month = (month % 12 == 0) ? 12 : month % 12;
            }
            date = year + String.format(".%02d", month) + privacy.substring(7,10);
            // 파기해야하는 개인정보 번호를 리스트에 저장하기
            if (date.compareTo(today) <= 0)
                result.add(num);
            num++;
        }
        // 정답 리스트를 배열로 바꾸기
        int[] answer = new int[result.size()];
        for (int i = 0; i < answer.length; i++)
            answer[i] = result.get(i);
        
        return answer;
    }
}