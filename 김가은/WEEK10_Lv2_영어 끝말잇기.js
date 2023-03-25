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

function solution2(n, words) {
  for (let i = 1; i < words.length; i++) {
    const answer = [Math.floor((i + 1) % n) || n, Math.floor(i / n) + 1];

    if (i !== words.indexOf(words[i])) return answer;
    if (words[i - 1].at(-1) !== words[i][0]) return answer;
  }

  return [0, 0];
}
