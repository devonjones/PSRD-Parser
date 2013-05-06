def create_books_table(curs):
	sql = '\n'.join([
		"CREATE TABLE books (",
		"  book_id INTEGER PRIMARY KEY,",
		"  source TEXT,",
		"  db TEXT"
		")"])
	curs.execute(sql)

def insert_book(curs, source=None, db=None):
	source = source.replace(':', '')
	source = source.replace('&', 'and')
	source = source.replace('?', '')
	source = source.replace("'", '')
	values = [source, db]
	sql = '\n'.join([
		"INSERT INTO books",
		" (source, db)",
		" VALUES",
		" (?, ?)"])
	curs.execute(sql, values)
	return curs.lastrowid

def delete_book(curs, book_id):
	values = [book_id]
	sql = '\n'.join([
		"DELETE FROM books",
		" WHERE book_id = ?"])
	curs.execute(sql, values)

def fetch_menu(curs, book_id):
	values = [book_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM books",
		" WHERE book_id = ?"])
	curs.execute(sql, values)
