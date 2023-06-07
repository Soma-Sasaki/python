def encrypt_string(arg):
    back_arg = arg[::-1]
    replace_a = back_arg.replace('a', '0')
    replace_e = replace_a.replace('e', '1')
    replace_o = replace_e.replace('o', '2')
    replace_u = replace_o.replace('u', '3')
    result = replace_u + 'text'

    return result
encrypt_string("aaasd")    
