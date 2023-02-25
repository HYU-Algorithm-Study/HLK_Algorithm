// 최종 풀이 1
function solution(food) {
  const answer = [];

  for (let i = 1; i < food.length; i++) {
    answer.push(`${i}`.repeat(Math.floor(food[i] / 2)));
  }

  return answer.join("") + "0" + answer.reverse().join("");
}

// 최종 풀이 2
function solution2(food) {
  let answer = "";

  for (let i = 1; i < food.length; i++) {
    answer += `${i}`.repeat(Math.floor(food[i] / 2));
  }

  return answer + "0" + [...answer].reverse().join("");
}
