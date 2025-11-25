def clear(rows=-1, rows_max=None, *, calling_line=True, absolute=None,
          store_max=[]):
    """clear(rows=-1, rows_max=None)
clear(0, -1) # Restore auto-determining rows_max
clear(calling_line=False) # Don't clear calling line
clear(absolute=5) # Absolutely clear out to 5 rows up"""
    from os import linesep
    if rows_max and rows_max != -1:
        store_max[:] = [rows_max, False]
    elif not store_max or store_max[1] or rows_max == -1 or absolute:
        try:
            from shutil import get_terminal_size
            columns_max, rows_max = get_terminal_size()
        except ImportError:
            columns_max, rows_max = 80, 24
        if absolute is None:
            store_max[:] = [rows_max, True]
    if store_max:
        if rows == -1:
            rows = store_max[0]
        elif isinstance(rows, float):
            rows = round(store_max[0] * rows)
        if rows > store_max[0] - 2:
            rows = store_max[0] - 2
    if absolute is None:
        s = ('\033[1A' + ' ' * 30 if calling_line else '') + linesep * rows
    else:
        s = '\033[{}A'.format(absolute + 2) + linesep
        if absolute > rows_max - 2:
            absolute = rows_max - 2
        s += (' ' * columns_max + linesep) * absolute + ' ' * columns_max
        rows = absolute
    print(s + '\033[{}A'.format(rows + 1))
    
"""
Possibili usi:

clear() # Clear all, TRIES to automatically get terminal height
clear(800, 24) # Clear all, set 24 as terminal (max) height
clear(12) # Clear half of terminal below if 24 is its height
clear(1000) # Clear to terminal height - 2 (24 - 2)
clear(0.5) # float factor 0.0 - 1.0 of terminal height (0.5 * 24 = 12)
clear() # Clear to rows_max - 2 of user given rows_max (24 - 2)
clear(0, 14) # Clear line, reset rows_max to half of 24 (14-2)
clear(0) # Just clear the line
clear(0, -1) # Clear line, restore auto-determining rows_max
clear(calling_line=False) # Clear all, don't clear calling line
clear(absolute=5) # Absolutely clear out to 5 rows up

"""
print("ciao"*100)

clear()

print("ciao")
