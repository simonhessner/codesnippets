#!/usr/bin/python3

def print_table_row(data, maxlengths, padding, alignment):
	print("|".join(['{0:{align}{len}}'.format(data[i], len=maxlengths[i]+padding, align=alignment[i]) for i in range(len(data))]))

def print_table(header, data, padding=3, alignment=None, line_every=-1):
	columns = len(header)

	if not alignment:
		alignment = ["^"] * columns

	lenghts    = [[len(item[i]) for i in range(columns)] for item in data]
	maxlengths = [len(h) for h in header]
	
	for clength in lenghts:
		for i in range(columns):
			maxlengths[i] = max(maxlengths[i], clength[i])
	
	print_table_row(header, maxlengths, padding, alignment)
	sepline = "-"*(sum(maxlengths) + padding * columns)
	print(sepline)
	for i, item in enumerate(data):
		print_table_row(item, maxlengths, padding, alignment)
		if line_every > 0 and (i+1)%line_every == 0 and i  != len(data)-1:
			print(sepline)



items = [["This", "is"], 
         ["a", "test"], 
         ["Python", "strings"], 
         ["are", "awesome"]]

print_table(["Column A", "Column B"], items, 10)