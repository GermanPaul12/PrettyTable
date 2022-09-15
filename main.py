from prettytable import PrettyTable
x = PrettyTable()

x.field_names = ['Name', 'Birthday']
x.add_row(['German', '12.12.2000'])
x.add_row(['Angi', '14.02.1998'])
print(x.get_string())


