# -*- encoding: utf-8 -*-

import yaml

filename = 'survey_jcafb_QSE15_data.yaml'

with open(filename, 'r') as f:
	doc = yaml.load(f)

text_file = open("Output.txt", "w")

for key1 in sorted(doc.keys()):
	print key1, doc[key1]['model'], doc[key1]['title'].encode("utf-8")
	text_file.write(doc[key1]['title'].encode("utf-8") + '\n')
	for key2 in sorted(doc[key1].keys()):
		if not key2.find('QSE15_'):
			print '    ', key2, doc[key1][key2]['model'], key2, doc[key1][key2]['title'].encode("utf-8")
			text_file.write('    ' + doc[key1][key2]['title'].encode("utf-8") + '\n')
			for key3 in sorted(doc[key1][key2].keys()):
				if not key3.find('QSE15_'):
					print '        ', key3, doc[key1][key2][key3]['model'], key3, doc[key1][key2][key3]['question'].encode("utf-8")
					text_file.write('        ' + doc[key1][key2][key3]['question'].encode("utf-8") + '\n')
					text_file.write('            (' + doc[key1][key2][key3]['type'] + ')\n')

					if  doc[key1][key2][key3]['type'] == 'comment':
						text_file.write('            ' + '____________________________________\n')
					if  doc[key1][key2][key3]['type'] == 'multiple_textboxes_diff_type':
						for key4 in sorted(doc[key1][key2][key3].keys()):
							if not key4.find('QSE15_'):
								print '            ', key4, doc[key1][key2][key3][key4]['model'], key4, doc[key1][key2][key3][key4]['answer'].encode("utf-8")
								text_file.write('            ' + doc[key1][key2][key3][key4]['answer'].encode("utf-8") + '____________________________________\n')
					else:
						for key4 in sorted(doc[key1][key2][key3].keys()):
							if not key4.find('QSE15_'):
								print '            ', key4, doc[key1][key2][key3][key4]['model'], key4, doc[key1][key2][key3][key4]['answer'].encode("utf-8")
								text_file.write('            ' + doc[key1][key2][key3][key4]['answer'].encode("utf-8") + '\n')
					try:
						if doc[key1][key2][key3]['is_comment_require'] == True:
							text_file.write('            ' + doc[key1][key2][key3]['comment_label'] + '____________________________________\n')
					except:
						pass

text_file.close()