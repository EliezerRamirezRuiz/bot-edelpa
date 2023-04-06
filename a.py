my_list = [('ROBOT', 'ERROR: PALLET SIN MOSAICO', 'CORTE', '1093594193466757141/ORFvoLxFES6w0QoX_MC0A8XjoRcZegEQUOrexvhIjF7RAZBZrFqLUinHDRx_aplldqm-'), ('ROBOT', 'ERROR: PALLET CON MOSAICO', 'CORTE', '1093594193466757141/ORFvoLxFES6w0QoX_MC0A8XjoRcZegEQUOrexvhIjF7RAZBZrFqLUinHDRx_apljqwq-')]

my_dict = {}

for t in my_list:
    key = t[2]
    value = t[3]
    my_dict[key] = value

print(my_dict)