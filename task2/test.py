from subprocess import run
from pathlib import Path
from filecmp import cmp
from shutil import *

# Replace the paths below with ur own
# e.g something like /Users/kevin/assignment_3/task2/ununzip.py
myunzip_path = "/Users/kevin/Projects/FIT3155/assignments/assignment_3/task2/myunzip.py"
myzip_path = "/Users/kevin/Projects/FIT3155/assignments/assignment_3/task2/myzip.py"

decoded_texts_path = Path(__file__).parent / 'decoded'
encoded_texts_path = Path(__file__).parent / 'encoded'
original_texts_path = Path(__file__).parent / 'original'

# exclude = ["empty.asc", "a10.asc", "s.asc", "random_2.asc", "ipsum.asc", "empty.asc", "x.asc", "new_x.asc"]
exclude = []
exclude_bin = [filename + ".bin" for filename in exclude]
print(Path.cwd())

if not Path(myunzip_path).is_file() or not Path(myzip_path).is_file():
  raise FileNotFoundError("Please set your myunzip/myzip path")

def test(exclude=[], window: int = 4, lookahead: int = 6):
  all_original_texts = original_texts_path.glob("*.asc")
  original_file_paths = [file for file in all_original_texts if file.is_file()
                         and file.name not in exclude]

  # Encode files
  for file_path in original_file_paths:
    command = f'python {myzip_path} {file_path} {window} {lookahead}'
    result = run(command.split(' '))
    print(f'Encoding: {file_path.name}')
    if result.returncode != 0:
      raise Exception(f"Error with file {file_path.name} uring encoding")

  [move(file, encoded_texts_path / file.name) for file in Path.cwd().glob("*.asc.bin")]
  all_encoded_texts = encoded_texts_path.glob("*.asc.bin")
  encoded_file_paths = [file for file in all_encoded_texts if file.is_file()
                        and file.name not in exclude_bin]

  # Decode files
  for file_path in encoded_file_paths:
    command = f'python {myunzip_path} {file_path}'
    result = run(command.split(' '))
    print(f'Decoding: {file_path}')
    if result.returncode != 0:
      raise Exception(f"Error with file {file_path.name} during decoding")

  [move(file, decoded_texts_path / file.name) for file in Path.cwd().glob("*.asc")]
  decoded_file_paths = [file for file in decoded_texts_path.glob(
      "*.asc") if file.is_file() and file.name not in exclude]

  # Compare files
  for file_path in decoded_file_paths:
    original_file_path = original_texts_path / file_path.name
    are_files_same = cmp(original_file_path, file_path, shallow=False)
    print(f'Comparing: {file_path.name}')
    if not are_files_same:
      raise Exception(f"Error with file {file_path.name} during decoding")

  print("All tests pass!")


if __name__ == "__main__":
  # for window_size in range(0, 20, 4):
  #   for lookahead_size in range(0, 20, 4):
  #     test(exclude, window=window_size, lookahead=lookahead_size)
  test(exclude, window=4, lookahead=6)
