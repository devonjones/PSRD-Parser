from psrd.sql.utils import test_args

#################
# Spell Details #
#################

def create_spell_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE spell_details (",
		"  spell_detail_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NO NULL,",
		"  school TEXT NOT NULL,",
		"  subschool TEXT,",
		"  descriptor_text TEXT,",
		"  level_text TEXT,",
		"  casting_time TEXT,",
		"  preparation_time TEXT,",
		"  range TEXT,",
		"  duration TEXT,",
		"  saving_throw TEXT,",
		"  spell_resistance TEXT,",
		"  as_spell_id INT",
		")"])
	curs.execute(sql)

def create_spell_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX spell_details_section_id",
		" ON spell_details (section_id)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX spell_details_school",
		" ON spell_details (school)"])
	curs.execute(sql)

def insert_spell_detail(curs, section_id, school=None, subschool=None, descriptor_text=None, level_text=None,
		casting_time=None, preparation_time=None, range=None, duration=None, saving_throw=None,
		spell_resistance=None, as_spell_id=None, **kwargs):
	values = [section_id, school, subschool, descriptor_text, level_text, casting_time, preparation_time, range, duration, saving_throw, spell_resistance, as_spell_id]
	testa = kwargs.copy()
	if testa.has_key('spell_detail_id'):
		del testa['spell_detail_id']
	if testa.has_key('level'):
		del testa['level']
	if testa.has_key('levels'):
		del testa['levels']
	if testa.has_key('descriptor'):
		del testa['descriptor']
	if testa.has_key('components'):
		del testa['components']
	if testa.has_key('effects'):
		del testa['effects']
	test_args(testa)
	sql = '\n'.join([
		"INSERT INTO spell_details",
		" (section_id, school, subschool, descriptor_text, level_text, casting_time, preparation_time, range, duration, saving_throw, spell_resistance, as_spell_id)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def update_spell_detail(curs, section_id, **kwargs):
	values = []
	sqla = [
		"UPDATE spell_details",
		" SET"]
	comma = " "
	for key in kwargs.keys():
		sqla.append(comma + key + " = ?")
		values.append(kwargs[key])
		comma = ", "
	sqla.append(" WHERE section_id = ?")
	values.append(section_id)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def delete_spell_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM spell_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_spell_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM spell_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

###############
# Spell Lists #
###############

def create_spell_lists_table(curs):
	sql = '\n'.join([
		"CREATE TABLE spell_lists (",
		"  spell_list_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NO NULL,",
		"  level INTEGER NOT NULL,",
		"  class TEXT,",
		"  magic_type TEXT",
		")"])
	curs.execute(sql)

def create_spell_lists_index(curs):
	sql = '\n'.join([
		"CREATE INDEX spell_lists_section_id",
		" ON spell_lists (section_id)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX spell_lists_level",
		" ON spell_lists (level)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX spell_lists_class",
		" ON spell_lists (class)"])
	curs.execute(sql)

def insert_spell_list(curs, section_id, level, class_name, magic_type):
	values = [section_id, level, class_name, magic_type]
	sql = '\n'.join([
		"INSERT INTO spell_lists",
		" (section_id, level, class, magic_type)",
		" VALUES",
		" (?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_spell_list(curs, section_id, class_name=None):
	values = [section_id]
	sqla = [
		"DELETE FROM spell_lists",
		" WHERE section_id = ?"]
	if class_name:
		sqla.append("  AND class = ?")
		values.append(class_name)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_spell_lists(curs, section_id, class_name=None):
	values = [section_id]
	sqla = [
		"SELECT *",
		" FROM spell_lists",
		" WHERE section_id = ?"]
	if class_name:
		sqla.append("  AND class = ?")
		values.append(class_name)
	sqla.append(" ORDER BY class")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

#####################
# Spell Descriptors #
#####################

def create_spell_descriptors_table(curs):
	sql = '\n'.join([
		"CREATE TABLE spell_descriptors (",
		"  spell_descriptor_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NO NULL,",
		"  descriptor TEXT NOT NULL",
		")"])
	curs.execute(sql)

def create_spell_descriptors_index(curs):
	sql = '\n'.join([
		"CREATE INDEX spell_descriptors_section_id",
		" ON spell_descriptors (section_id)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX spell_descriptors_descriptor",
		" ON spell_descriptors (descriptor)"])
	curs.execute(sql)

def insert_spell_descriptor(curs, section_id, descriptor):
	values = [section_id, descriptor]
	sql = '\n'.join([
		"INSERT INTO spell_descriptors",
		" (section_id, descriptor)",
		" VALUES",
		" (?, ?)"])
	curs.execute(sql, values)

def delete_spell_descriptor(curs, section_id, descriptor=None):
	values = [section_id]
	sqla = [
		"DELETE FROM spell_descriptors",
		" WHERE section_id = ?"]
	if descriptor:
		sqla.append("  AND descriptor = ?")
		values.append(descriptor)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_spell_descriptors(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM spell_descriptors",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

####################
# Spell Components #
####################

def create_spell_components_table(curs):
	sql = '\n'.join([
		"CREATE TABLE spell_components (",
		"  spell_component_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NO NULL,",
		"  component_type TEXT NOT NULL,",
		"  description TEXT,",
		"  notable INT NOT NULL",
		")"])
	curs.execute(sql)

def create_spell_components_index(curs):
	sql = '\n'.join([
		"CREATE INDEX spell_components_section_id",
		" ON spell_components (section_id)"])
	curs.execute(sql)

def insert_spell_component(curs, section_id, component_type, description, notable):
	values = [section_id, component_type, description, notable]
	sql = '\n'.join([
		"INSERT INTO spell_components",
		" (section_id, component_type, description, notable)",
		" VALUES",
		" (?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_spell_components(curs, section_id):
	values = [section_id]
	sqla = [
		"DELETE FROM spell_components",
		" WHERE section_id = ?"]
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_spell_components(curs, section_id):
	values = [section_id]
	sqla = [
		"SELECT *",
		" FROM spell_components",
		" WHERE section_id = ?"]
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

#################
# Spell Effects #
#################

def create_spell_effects_table(curs):
	sql = '\n'.join([
		"CREATE TABLE spell_effects (",
		"  spell_effect_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NO NULL,",
		"  name TEXT NOT NULL,",
		"  description TEXT NOT NULL",
		")"])
	curs.execute(sql)

def create_spell_effects_index(curs):
	sql = '\n'.join([
		"CREATE INDEX spell_effects_section_id",
		" ON spell_effects (section_id)"])
	curs.execute(sql)

def insert_spell_effect(curs, section_id, name, description):
	values = [section_id, name, description]
	sql = '\n'.join([
		"INSERT INTO spell_effects",
		" (section_id, name, description)",
		" VALUES",
		" (?, ?, ?)"])
	curs.execute(sql, values)

def delete_spell_effect(curs, section_id, name=None):
	values = [section_id]
	sqla = [
		"DELETE FROM spell_effects",
		" WHERE section_id = ?"]
	if name:
		sqla.append("  AND name = ?")
		values.append(name)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_spell_effects(curs, section_id, name=None):
	values = [section_id]
	sqla = [
		"SELECT *",
		" FROM spell_effects",
		" WHERE section_id = ?"]
	if name:
		sqla.append("  AND name = ?")
		values.append(name)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

#############
# Utilities #
#############

def fetch_complete_spell(curs, name):
	values = [name]
	sql = '\n'.join([
		"SELECT section_id, type, subtype, name, abbrev, source, description, body as text",
		" FROM sections",
		" WHERE name = ?",
		"  AND type = 'spell'"])
	curs.execute(sql, values)
	spell = curs.fetchone()
	if not spell:
		return None
	section_id = spell['section_id']
	fetch_spell_detail(curs, section_id)
	details = curs.fetchone()
	spell.update(details)
	fetch_spell_lists(curs, section_id)
	levels = curs.fetchall()
	spell['levels'] = list(levels)
	fetch_spell_descriptors(curs, section_id)
	descobjs = curs.fetchall()
	descriptors = []
	for descobj in descobjs:
		descriptors.append(descobj['descriptor'])
	spell['descriptor'] = descriptors
	fetch_spell_components(curs, section_id)
	compobjs = curs.fetchall()
	components = []
	for compobj in compobjs:
		components.append({'type': compobj['component_type'], 'text': compobj['description']})
	spell['components'] = components
	fetch_spell_effects(curs, section_id)
	effectobjs = curs.fetchall()
	effects = []
	for effectobj in effectobjs:
		effects.append({'name': effectobj['name'], 'text': effectobj['description']})
	spell['effects'] = effects
	return spell

def merge_spells(spell1, spell2):
	for key in spell1.keys():
		if not spell2.has_key(key):
			spell2[key] = spell1[key]
	spell2['as_spell_id'] = spell1['section_id']
	return spell2
