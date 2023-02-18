function solution(s) {
  const answer = [0, 0];

  while (s !== "1") {
    answer[0]++;
    const leng = s.length;
    const newS = s.replace(/0/g, "");
    const newLeng = newS.length;
    s = newLeng.toString(2);
    answer[1] += leng - newLeng;
  }

  return answer;
}
