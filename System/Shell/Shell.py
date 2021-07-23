import Shell_PY

prompt = "PB"

while True:

    # Interpreter cursor

    text = input('|'+ prompt +'|>')
    result, error = Shell_PY.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)