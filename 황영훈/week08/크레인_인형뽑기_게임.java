import java.util.ArrayList;
import java.util.Stack;

class Solution {

    public int solution(int[][] board, int[] moves) {
        // 터트린 인형 개수
        int count = 0;
        // 바구니 클래스
        Stack<Integer> basket = new Stack<>();
        // 크레인 작동 위치 모두 검사
        for (int move : moves) {
            // 1. 아이템 바구니로 옮기기
            pickItem(board, basket, move);
            // 2. 같은 아이템이면 터트리고 개수 업데이트
            count = popEqualItem(basket, count);
        }
        return count;
    }

    private void pickItem(int[][] board, Stack<Integer> basket, int move) {
        for (int i = 0; i < board[0].length; i++) {
            if (board[i][move - 1] != 0) {
                basket.push(board[i][move - 1]);
                board[i][move - 1] = 0;
                return;
            }
        }
    }

    private int popEqualItem(Stack<Integer> basket, int count) {
        if (basket.size() < 2) {
            return count;
        }
        // 위에서 두 개의 아이템이 같으면 둘 다 pop
        int topElement = basket.pop();
        if (topElement == basket.peek()) {
            basket.pop();
            count += 2;
        } else {
            basket.push(topElement);
        }
        return count;
    }

}