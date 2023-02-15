def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])# incorrect value, k = keys

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": " (Pacifier Suck)"}#changed the single quotation mark with a double quotation mark

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])#turned three arguments into one by closing it in square brackets defining it as an array

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''