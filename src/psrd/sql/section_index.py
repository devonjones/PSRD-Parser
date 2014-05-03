def create_section_index_table(curs):
	sql = '\n'.join([
		"CREATE TABLE section_index (",
		"  section_index_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  search_name TEXT,",
		"  type TEXT",
		")"])
	curs.execute(sql)

def create_section_index_index(curs):
	sql = '\n'.join([
		"CREATE INDEX section_index_section_id",
		" ON section_index (section_id)"])
	curs.execute(sql)

	sql = '\n'.join([
		"CREATE INDEX section_index_search_name",
		" ON section_index (search_name)"])
	curs.execute(sql)

def update_link_create_index(curs):
	sql = '\n'.join([
		"UPDATE sections",
		" SET create_index = 1",
		" WHERE section_id IN (",
		"  SELECT s.section_id",
		"   FROM sections s",
		"    INNER JOIN link_details ld",
		"     ON s.url = ld.url)"])
	curs.execute(sql)

def fetch_indexable_sections(curs):
	sql = '\n'.join([
		"SELECT s.section_id, s.type, s.subtype, s.name, p.name AS parent_name, p.type as parent_type, s.create_index",
		" FROM sections AS s",
		"  INNER JOIN sections AS p",
		"   ON s.parent_id = p.section_id",
		" WHERE s.name IS NOT NULL",
		"  AND s.type != 'list'",
		"  AND s.type != 'link'",
		"  AND (s.create_index == 1",
		"   OR s.create_index IS NULL)",
		" ORDER BY s.section_id"])
	curs.execute(sql)

def strip_unindexed_urls(curs):
	sql = '\n'.join([
		"UPDATE sections",
		" SET url = NULL",
		" WHERE section_id NOT IN (",
		"  SELECT section_id",
		"   FROM section_index)",
		"  AND type != 'list'",
		"  AND parent_id NOT IN (",
		"   SELECT section_id",
		"    FROM sections",
		"     WHERE type == 'list')",
		"  AND parent_id NOT IN (",
		"   SELECT s.section_id",
		"    FROM sections s",
		"     INNER JOIN sections p",
		"      ON p.section_id = s.parent_id",
		"    WHERE p.type == 'list'",
		"     AND p.name LIKE 'Rules%')"])
	curs.execute(sql)

def count_sections_with_name(curs, name):
	sql = '\n'.join([
		"SELECT COUNT(*) AS cnt",
		" FROM sections AS s",
		"  INNER JOIN sections AS p",
		"   ON s.parent_id = p.section_id",
		" WHERE s.name IS NOT NULL",
		"  AND s.type != 'list'",
		"  AND s.type != 'link'",
		"  AND (s.create_index == 1",
		"   OR s.create_index IS NULL)",
		"  AND s.name = ?"])
	curs.execute(sql, [name])

def fetch_index(curs, section_id, name=None):
	values = [section_id]
	sqla = [
		"SELECT *",
		" FROM section_index",
		" WHERE section_id = ?"
		]
	if name:
		sqla.append("  AND search_name = ?")
		values.append(name)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def insert_index(curs, section_id, name, type_name):
	sql = '\n'.join([
		"INSERT INTO section_index",
		" (section_id, search_name, type)",
		"VALUES",
		" (?, ?, ?)"])
	curs.execute(sql, (section_id, name, type_name))

def fetch_central_index(curs):
	sql = '\n'.join([
		"SELECT s.section_id, s.parent_id, s.source,",
		"  (SELECT p.name",
		"   FROM sections p",
		"    WHERE s.parent_id = p.section_id",
		"   LIMIT 1) as parent_name,",
		"  s.type, s.subtype, s.name, si.search_name, s.description, s.url,",
		"  ftd.feat_type_description,",
		"  (SELECT c.description",
		"   FROM sections c",
		"    WHERE c.parent_id = s.section_id",
		"     AND c.name = 'Prerequisites'",
		"     AND s.type = 'feat'",
		"   LIMIT 1) as feat_prerequisites,",
		"   sa.attribute as skill_attribute,",
		"   sa.armor_check_penalty as skill_armor_check_penalty,",
		"   sa.trained_only as skill_trained_only,",
		"   sd.school as spell_school,",
		"   sd.subschool_text as spell_subschool_text,",
		"   sd.descriptor_text as spell_descriptor_text,",
		"   sd.level_text as spell_list_text,",
		"   sd.component_text as spell_component_text,",
		"   msd.spell_source as spell_source,",
		"   cd.creature_type,",
		"   cd.creature_subtype,",
		"   cd.super_race as creature_super_race,",
		"   cd.cr as creature_cr,",
		"   cd.xp as creature_xp,",
		"   cd.size as creature_size,",
		"   cd.alignment as creature_alignment",
		" FROM sections s",
		"  INNER JOIN section_index si",
		"   ON s.section_id = si.section_id",
		"  LEFT OUTER JOIN feat_type_descriptions ftd",
		"   ON s.section_id = ftd.section_id",
		"  LEFT OUTER JOIN skill_attributes sa",
		"   ON s.section_id = sa.section_id",
		"  LEFT OUTER JOIN spell_details sd",
		"   ON s.section_id = sd.section_id",
		"  LEFT OUTER JOIN mythic_spell_details msd",
		"   ON s.section_id = msd.section_id",
		"  LEFT OUTER JOIN creature_details cd",
		"   ON s.section_id = cd.section_id"])
	curs.execute(sql)
