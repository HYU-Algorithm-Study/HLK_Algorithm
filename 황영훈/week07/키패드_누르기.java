class Solution {
    public String solution(int[] numbers, String hand) {
        int lastLeftNumber = 10; // "*"은 10으로 치환
        int lastRightNumber = 12; // "#"은 12로 치환
        String answer = "";
        for (int number : numbers) {
            // 1, 4, 7 -> 왼손 사용
            if (number == 1 || number == 4 || number == 7) {
                answer += "L";
                lastLeftNumber = number;
            }
            // 3, 6, 9 -> 오른손 사용
            else if (number == 3 ||number == 6 || number == 9) {
                answer += "R";
                lastRightNumber = number;
            }
            // 2, 5, 8, 0 -> 가까운 손 사용
            else {
                // 0은 11로 치환
                if (number == 0) {
                    number = 11;
                }
                // 가까운 손 탐색 로직 수행
                String closeHand = getCloseHand(lastLeftNumber, lastRightNumber, number, hand);
                answer += closeHand;
                if (closeHand.equals("L")) {
                    lastLeftNumber = number;
                } else {
                    lastRightNumber = number;
                }
            }
        }
        return answer;
    }
    
    private String getCloseHand(int lastLeftNumber, int lastRightNumber, int number, String hand) {
        int leftDistance = Math.abs(number - lastLeftNumber) / 3 + Math.abs(number - lastLeftNumber) % 3;
        int rightDistance = Math.abs(number - lastRightNumber) / 3 + Math.abs(number - lastRightNumber) % 3;
        if (leftDistance < rightDistance) {
            return "L";
        }
        if (leftDistance > rightDistance) {
            return "R";
        }
        return (hand.equals("left")) ? "L" : "R";
    }
}