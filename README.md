## Testing helpers for Assignment 3 Question 2
 - The testing code is located in `test.py`
 - You'll need to make a slight modification to your `myunzip.py` and `myzip.py` to write to a custom output path so that they can be called like:
 ```

    command = f'python {myunzip_path} {file_path} {output_path}'
    command = f'python {myzip_path} {file_path} {window} {lookahead} {output_path}'

 ```
 - You'll need to change the path of the `myunzip_path` and `myzip_path` in `test.py` 
 - To add test files, add them to the `/original` directory
 - To exclude files, add them to the `exclude` variable at the bottom of `test.py`
 - Also you might wanna delete the files in `/decoded` and `/encoded` before you run the test
 - Feel free to make a PR to add tests! 