// 최종 풀이
function solution(answers) {
  const arr = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];
  const numArr = [0, 0, 0];
  const answer = [];

  answers.forEach((a, i) => {
    arr.forEach((b, j) => {
      if (a === b[i % b.length]) numArr[j]++;
    });
  });

  numArr.forEach((a, i) => {
    if (a === Math.max(...numArr)) answer.push(i + 1);
  });

  return answer;
}
