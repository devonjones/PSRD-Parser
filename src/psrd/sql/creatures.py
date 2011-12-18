from psrd.sql.utils import test_args

def create_creature_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE creature_details ("
		"  creature_details_id INTEGER PRIMARY KEY,"
		"  section_id INTEGER NOT NULL,"
		"  sex TEXT,"
		"  super_race TEXT,"
		"  level TEXT,"
		"  cr TEXT,"
		"  xp TEXT,"
		"  alignment TEXT,"
		"  size TEXT,"
		"  creature_type TEXT,"
		"  creature_subtype TEXT,"
		"  init TEXT,"
		"  senses TEXT,"
		"  aura TEXT,"
		"  ac TEXT,"
		"  hp TEXT,"
		"  fortitude TEXT,"
		"  reflex TEXT,"
		"  will TEXT,"
		"  defensive_abilities TEXT,"
		"  dr TEXT,"
		"  resist TEXT,"
		"  immune TEXT,"
		"  sr TEXT,"
		"  weaknesses TEXT,"
		"  speed TEXT,"
		"  melee TEXT,"
		"  ranged TEXT,"
		"  space TEXT,"
		"  reach TEXT,"
		"  special_attacks TEXT,"
		"  strength TEXT,"
		"  dexterity TEXT,"
		"  constitution TEXT,"
		"  intelligence TEXT,"
		"  wisdom TEXT,"
		"  charisma TEXT,"
		"  base_attack TEXT,"
		"  cmb TEXT,"
		"  cmd TEXT,"
		"  feats TEXT,"
		"  skills TEXT,"
		"  racial_modifiers TEXT,"
		"  languages TEXT,"
		"  special_qualities TEXT,"
		"  gear TEXT,"
		"  environment TEXT,"
		"  organization TEXT,"
		"  treasure TEXT"
		")"])
	curs.execute(sql)

def create_creature_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX creature_details_section_id",
		" ON creature_details (section_id)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX creature_details_creature_type",
		" ON creature_details (creature_type)"])
	curs.execute(sql)

def insert_creature_detail(curs, section_id,
		sex=None, super_race=None, level=None, cr=None, xp=None, alignment=None, size=None, creature_type=None,
		creature_subtype=None, init=None, senses=None, aura=None,
		ac=None, hp=None, fortitude=None, reflex=None, will=None, resist=None, defensive_abilities=None,
		dr=None, immune=None, sr=None, weaknesses=None,
		speed=None, melee=None, ranged=None, space=None, reach=None, special_attacks=None,
		strength=None, dexterity=None, constitution=None, intelligence=None, wisdom=None, charisma=None,
		base_attack=None, cmb=None, cmd=None, feats=None, skills=None, racial_modifiers=None, languages=None,
		special_qualities=None, gear=None,
		environment=None, organization=None, treasure=None, **kwargs):
	values = [section_id,
		sex, super_race, level, cr, xp, alignment, size, creature_type, creature_subtype, init, senses, aura,
		ac, hp, fortitude, reflex, will, resist, defensive_abilities, dr, immune, sr, weaknesses,
		speed, melee, ranged, space, reach, special_attacks,
		strength, dexterity, constitution, intelligence, wisdom, charisma, base_attack, cmb, cmd,
		feats, skills, racial_modifiers, languages, special_qualities, gear,
		environment, organization, treasure]
	targs = kwargs.copy()
	if targs.has_key('spells'):
		del targs['spells']
	test_args(targs)

	sql = '\n'.join([
		"INSERT INTO creature_details",
		" (section_id,",
		"  sex, super_race, level, cr, xp, alignment, size, creature_type, creature_subtype, init, senses, aura,",
		"  ac, hp, fortitude, reflex, will, resist, defensive_abilities, dr, immune, sr, weaknesses,",
		"  speed, melee, ranged, space, reach, special_attacks,",
		"  strength, dexterity, constitution, intelligence, wisdom, charisma,",
		"  base_attack, cmb, cmd, feats, skills, racial_modifiers, languages, special_qualities, gear,",
		"  environment, organization, treasure)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"
		"  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,",
		"  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,",
		"  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_creature_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM creature_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_creature_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM creature_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def create_creature_spells_table(curs):
	sql = '\n'.join([
		"CREATE TABLE creature_spells ("
		"  creature_spells_id INTEGER PRIMARY KEY,"
		"  section_id INTEGER NOT NULL,"
		"  name TEXT,"
		"  body TEXT"
		")"])
	curs.execute(sql)

def create_creature_spells_index(curs):
	sql = '\n'.join([
		"CREATE INDEX creature_spells_section_id",
		" ON creature_spells (section_id)"])
	curs.execute(sql)

def insert_creature_spell(curs, section_id, name, body):
	values = [section_id, name, body]
	sql = '\n'.join([
		"INSERT INTO creature_spells",
		" (section_id, name, body)",
		" VALUES",
		" (?, ?, ?)"])
	curs.execute(sql, values)

def delete_creature_spell(curs, section_id, name=None):
	values = [section_id]
	sqla = [
		"DELETE FROM creature_spells",
		" WHERE section_id = ?"]
	if name:
		sqla.append("  AND name = ?")
		values.append(name)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_creature_spells(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM creature_spells",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

