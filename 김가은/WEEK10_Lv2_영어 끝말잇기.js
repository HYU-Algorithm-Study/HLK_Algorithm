function solution(n, words) {
  const stack = [words[0][0]];
  let num = 0;

  for (let x of words) {
    const answer = [Math.floor((num + 1) % n) || n, Math.floor(num / n) + 1];

    if (stack.includes(x)) return answer;
    if (stack.at(-1).at(-1) !== x[0]) return answer;

    stack.push(x);
    num++;
  }

  return [0, 0];
}
