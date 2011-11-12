def create_skill_attributes_table(curs):
	sql = '\n'.join([
		"CREATE TABLE skill_attributes (",
		"  skill_attribute_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  attribute TEXT,",
		"  armor_check_penalty INT,",
		"  trained_only INT",
		")"])
	curs.execute(sql)

def create_skill_attributes_index(curs):
	sql = '\n'.join([
		"CREATE INDEX skill_attributes_section_id",
		" ON skill_attributes (section_id)"])
	curs.execute(sql)

def insert_skill_attribute(curs, section_id, attribute, armor_check_penalty, trained_only):
	values = [section_id, attribute]
	if armor_check_penalty:
		values.append(1)
	else:
		values.append(0)
	if trained_only:
		values.append(1)
	else:
		values.append(0)
	sql = '\n'.join([
		"INSERT INTO skill_attributes",
		" (section_id, attribute, armor_check_penalty, trained_only)",
		" VALUES",
		" (?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_skill_attribute(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM skill_attributes",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_skill_attribute(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM skill_attributes",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_skills_by_quality(curs, attribute=None, armor_check_penalty=None, trained_only=None):
	values = []
	sqla = [
		"SELECT s.*",
		" FROM sections s, skill_attributes sa",
		" WHERE s.section_id = sa.section_id"]
	if attribute:
		sqla.append("  AND sa.attribute = ?")
		values.append(attribute)
	if armor_check_penalty != None:
		sqla.append("  AND sa.armor_check_penalty = ?")
		if armor_check_penalty:
			values.append(1)
		else:
			values.append(0)
	if trained_only != None:
		sqla.append("  AND sa.trained_only = ?")
		if trained_only:
			values.append(1)
		else:
			values.append(0)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)
