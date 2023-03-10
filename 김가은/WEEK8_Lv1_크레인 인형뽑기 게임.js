function solution(board, moves) {
  const stack = [];
  let answer = 0;

  for (let a of moves) {
    let doll = 0;
    for (let i = 0; i < board.length; i++) {
      if (board[i][a - 1]) {
        doll = board[i][a - 1];
        board[i][a - 1] = 0;
        break;
      }
    }

    if (!doll) continue;

    if (stack.at(-1) === doll) {
      stack.pop();
      answer += 2;
    } else stack.push(doll);
  }
  return answer;
}
