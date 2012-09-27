def create_section_sort_table(curs):
	sql = '\n'.join([
		"CREATE TABLE section_sort (",
		"  section_sort_id INTEGER PRIMARY KEY,",
		"  type TEXT NOT NULL",
		")"])
	curs.execute(sql)

def create_section_sort_index(curs):
	sql = '\n'.join([
		"CREATE INDEX section_sort_type",
		" ON section_sort (type)"])
	curs.execute(sql)

def fetch_sort(curs, type_name=None):
	values = [type_name]
	sqla = [
		"SELECT *",
		" FROM section_sort",
		]
	if type_name:
		sqla.append(" WHERE type = ?")
		values.append(type_name)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def insert_sort(curs, type_name):
	sql = '\n'.join([
		"INSERT INTO section_sort",
		" (type)",
		"VALUES",
		" (?)"])
	curs.execute(sql, [type_name])

def create_sorts(curs):
	select_section_types(curs)
	types = curs.fetchall()
	tlist = resort([t['type'] for t in types])
	for t in tlist:
		insert_sort(curs, t)

def resort(tlist):
	top = ['class', 'feat', 'race', 'creature', 'spell', 'skill']
	end = ['table', 'section', 'link']
	results = []
	results.extend(top)
	for t in tlist:
		if t not in top and t not in end:
			results.append(t)
	results.extend(end)
	return results

def select_section_types(curs):
	sql = '\n'.join([
		"SELECT DISTINCT type",
		" FROM sections"])
	curs.execute(sql)

