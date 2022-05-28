from subprocess import run
from pathlib import Path
from filecmp import cmp

# Add the absolute path to your zip and unzip python files here
# e.g something like /Users/kevin/assignment_3/task2/ununzip.py
myunzip_path = "{YOUR PATH HERE}/assignment_3/task2/myunzip.py"
myzip_path = "{YOUR PATH HERE/assignment_3/task2/myzip.py"

decoded_texts_path = Path(__file__).parent / 'decoded'
encoded_texts_path = Path(__file__).parent / 'encoded'
original_texts_path = Path(__file__).parent / 'original' 

if not Path(myunzip_path).is_file() or not Path(myzip_path).is_file():
  raise FileNotFoundError("Please set your myunzip/myzip path")

def test(exclude=[]):
  all_original_texts = original_texts_path.glob("*.asc")
  original_file_paths = [file for file in all_original_texts if file.is_file() and file.name not in exclude]

  # Encode files
  for file_path in original_file_paths:
    command = f'python {myzip_path} {file_path} {4} {6} {encoded_texts_path}'
    result = run(command.split(' '))
    if result.returncode != 0:
      raise Exception(f"Error with file {file_path.name} during encoding")

  all_encoded_texts = encoded_texts_path.glob("*.asc.bin")
  encoded_file_paths = [file for file in all_encoded_texts if file.is_file() and file.name not in exclude]

  # Decode files
  for file_path in encoded_file_paths:
    command = f'python {myunzip_path} {file_path} {decoded_texts_path}'
    result = run(command.split(' '))
    if result.returncode != 0:
      raise Exception(f"Error with file {file_path.name} during decoding")

  all_decoded_texts = decoded_texts_path.glob("*.asc")
  decoded_file_paths = [file for file in all_decoded_texts if file.is_file() and file.name not in exclude]

  # Compare files
  for file_path in decoded_file_paths:
    original_file_path = original_texts_path / file_path.name
    are_files_same = cmp(original_file_path, file_path, shallow=False)
    if not are_files_same:
      raise Exception(f"Error with file {file_path.name} during decoding")

  print("All tests pass!")

  
if __name__ == "__main__":
  exclude = ["a10.asc", "empty.asc"]
  test(exclude)