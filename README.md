# Exceptions handling

Using KeyError and TypeError, !r and sys.stderr to handle errors.

Create log() to demonstrate that the error handling is now showing 2 errors in the same :
ErrorType and ErrorValue.

```
Conversion error: KeyError('text')
in string_log
    return log(v)
    ValueError: math domain error
```

Add raise at the end of our exception handling to match conversion error to the new log() function:

```
Conversion error: KeyError('text')
in string_log
    v = convert(s)
in convert
    number += DIGIT_MAP[token]
    KeyError: 'text'
```