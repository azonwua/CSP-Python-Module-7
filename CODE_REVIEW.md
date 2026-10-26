# Code Review

## Part 1: Initial Observations (before refactoring)

I ran the original script and it printed the expected output, so it works. These are the three main problems I found:

1. **Unclear names.** `do_math_stuff`, `do_string_stuff`, `list_of_nums`, `result`, `x`, `s`, `list1`, and `list2` don't say what they do or hold. A reader has to study the code to figure out the purpose. Clear names make the code easier to read and understand.
2. **No documentation.** Neither function has a docstring, so there is no explanation of what the function does, what it takes in, or what it returns. Other developers would have to read the whole function body just to use it.
3. **Loops that can be simplified.** Both functions build their results with a loop, and `do_string_stuff` builds a string with `+=` and then has to `.strip()` the extra trailing space. A list comprehension and `join()` would be shorter and clearer. The number `5` is also hard-coded with no explanation.

## Part 3: Final Review (after refactoring)

**Did I address the three original issues?** Yes, all three.

1. **Unclear names:** I renamed the functions to `process_numbers` and `format_words`, the parameters to `numbers` and `words`, and the variables in `main()` to `sample_numbers`, `sample_words`, `processed_numbers`, and `formatted_words`. All follow PEP 8 `snake_case`. *Verified:* I re-read each name and asked whether a new developer could guess what it holds without reading the code.
2. **No documentation:** I added a PEP 257 docstring to every function (including `main`) covering purpose, parameters, and return value, plus a module docstring. I also added one comment that explains *why* `join()` is used instead of repeating what the code does. *Verified:* I checked that each function has a docstring and that `help(process_numbers)` displays it.
3. **Loops that can be simplified:** I replaced the number loop with a list comprehension and the string loop with `" ".join(...)` over a generator expression. I also replaced the hard-coded `5` with a named constant, `LONG_WORD_THRESHOLD`. *Verified:* I ran both versions and compared the output.

**Are the names clear and descriptive?** Yes. Each name now says what the function does or what the variable holds.

**Does each function have appropriate documentation?** Yes. Each function has a docstring explaining its purpose, parameters, and return value.

**Did the changes improve readability and maintainability?** Yes. The code is shorter, each function is a single clear expression, and the threshold can be changed in one place.

**Does the program still produce the expected output?** Yes. Running the refactored script prints:

```
Processed Numbers: [3, 4, 9, 8, 15, 12, 21]
Processed Strings: apple BANANA kiwi GRAPEFRUIT CHERRY
```

I also compared this with the original script's output using `diff`, and the two were identical.