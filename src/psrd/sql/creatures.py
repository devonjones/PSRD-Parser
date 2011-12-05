from psrd.sql.utils import test_args

def create_creature_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE creature_details (",
		"  creature_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
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
		"  vulnerability TEXT,"
		"  sr TEXT,"
		"  weaknesses TEXT,"
		"  speed TEXT,"
		"  melee TEXT,"
		"  ranged TEXT,"
		"  space TEXT,"
		"  reach TEXT,"
		"  special_attacks TEXT,"
		"  spell_like_abilities TEXT,"
		"  spells_prepared TEXT,"
		"  spells_known TEXT,"
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

def insert_creature_detail(curs, section_id,
		cr=None, xp=None, alignment=None, size=None, creature_type=None, creature_subtype=None,
		init=None, senses=None, aura=None,
		ac=None, hp=None, fortitude=None, reflex=None, will=None, resist=None, defensive_abilities=None,
		dr=None, immune=None, vulnerability=None, sr=None, weaknesses=None,
		speed=None, melee=None, ranged=None, space=None, reach=None, special_attacks=None,
		spell_like_abilities=None, spells_prepared=None, spells_known=None,
		strength=None, dexterity=None, constitution=None, intelligence=None, wisdom=None, charisma=None,
		base_attack=None, cmb=None, cmd=None, feats=None, skills=None, racial_modifiers=None, languages=None,
		special_qualities=None, gear=None,
		environment=None, organization=None, treasure=None, **kwargs):
	values = [section_id,
		cr, xp, alignment, size, creature_type, creature_subtype, init, senses, aura,
		ac, hp, fortitude, reflex, will, resist, defensive_abilities, dr, immune, vulnerability, sr, weaknesses,
		speed, melee, ranged, space, reach, special_attacks, spell_like_abilities, spells_prepared, spells_known,
		strength, dexterity, constitution, intelligence, wisdom, charisma, base_attack, cmb, cmd,
		feats, skills, racial_modifiers, languages, special_qualities, gear,
		environment, organization, treasure]
	test_args(kwargs)

	sql = '\n'.join([
		"INSERT INTO creature_details",
		" (section_id,",
		"  cr, xp, alignment, size, creature_type, creature_subtype, init, senses, aura,",
		"  ac, hp, fortitude, reflex, will, resist, defensive_abilities, dr, immune, vulnerability, sr,",
		"  weaknesses,",
		"  speed, melee, ranged, space, reach, special_attacks, spell_like_abilities, spells_prepared,",
		"  spells_known",
		"  strength, dexterity, constitution, intelligence, wisdom, charisma,",
		"  base_attack, cmb, cmd, feats, skills, racial_modifiers, languages, special_qualities, gear,",
		"  environment, organization, treasure)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"
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

