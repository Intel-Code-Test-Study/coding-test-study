function findPrimesInRange(a, b) {
  if (a > b) (start = b), (end = a);
  else (start = a), (end = b);

  let primes = [];
  for (let num = start; num <= end; num++) {
    let isPrime = true;
    for (let i = 2; i < num; i++) {
      if (num % i === 0) {
        isPrime = false;
        break;
      }
    }
    if (num > 1 && isPrime) {
      primes.push(num);
    }
  }
  if (primes.length === 0) return 'C';
  total_sum = primes.reduce((acc, cur) => {
    return acc + cur;
  }, 0);
  return total_sum % 2 === 0 ? 'A' : 'B';
}

// 예제 사용
const result = findPrimesInRange(10, 50);
console.log(`두 수 ${start}와 ${end} 사이의 소수 여부:`, result);
