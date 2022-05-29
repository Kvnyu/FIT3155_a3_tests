from subprocess import run
from pathlib import Path
from filecmp import cmp

three_primes_path = "/Users/kevin/Projects/FIT3155/assignments/assignment_3/task1/threeprimes.py"
three_primes_path_parent = Path(three_primes_path).parent

for i in range(8, 1000):
  command = f'python {three_primes_path} {i}'
  result = run(command.split(" "))

  if result.returncode != 0:
    raise Exception(f"Error with number {i}")

  # output = Path(three_primes_path_parent) / "output_threeprimes.txt"
  with open(file=Path.cwd() / "output_threeprimes.txt") as f:
    line = f.readline().rstrip("\n").split(" ")
    if sum([int(x) for x in line]) != i:
      raise Exception(f"Error with number {i}")
    print(f'sum {line} == {i}')

print("all tests pass")