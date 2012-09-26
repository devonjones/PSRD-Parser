# PSRD Parser #
This program parses the text from the [Paizo Pathfinder Reference Document](http://paizo.com/pathfinderRPG/prd/) website and turns the data into a series of JSON files.  It then can transform those JSON files into an SQLite3 database intended for use with the [Pathfinder Open Reference](https://github.com/devonjones/PathfinderOpenReference) project.

# Database #

## QUERY METHODS ##

The functions, under src/psrd/sql, that select data from the database, will not return a list of rows. The cursor will be modified and it is up to the caller to extract rows from the cursor.

The functions, under src/psrd/sql, that insert data into the database, will not return the rowid. As above, the cursor will be modified and it is up to the caller to extract that information.

## HIERARCHY ##

The database's structure is a hierarchy.  It uses two forms of hierarchical structure because:

1. The two forms have different strengths and weaknesses
2. The database is meant to be generated once, and read many times, so the code for writing it can be reasonably centralized.

The first hierarchical structure is the simplest.  Each section has a section_id, and every section also has a parent_id.  The parent_id references the section_id of the node's parent in the hierarchy.  Other then the top node of the hierarchy, all sections have a parent_id.

The second hierarchical structure is detailed in the article by [Mike Hillyer](http://mikehillyer.com) entitled [Managing Hierarchical Data in MySQL](http://mikehillyer.com/articles/managing-hierarchical-data-in-mysql/). It is not as simple, but gives a build in way to be able to easily determine all sections that are below a section in the hierarchy, regardless of depth, in one query.

## TABLES ##

    sections
      section_id INTEGER PRIMARY KEY,           // Primary key
      type TEXT NOT NULL,                       // See TYPES below
      subtype TEXT,                             // See SUBTYPES below
      lft INTEGER NOT NULL,                     // Left side of the section's set, see HIERARCHY
      rgt INTEGER NOT NULL,                     // Right side of the section's set, see HIERARCHY
      parent_id INTEGER,                        // Id of the section's parent, see HIERARCHY
      name TEXT,                                // Section's name.  Text
      abbrev TEXT,                              // Section's abbreviation.  Text
      source TEXT NOT NULL,                     // Section's source book.  Text
      description TEXT,                         // Short description of section's contents. Text
      body TEXT);                               // Section's Body.  HTML


    ability_types                               // 1-n with sections
      ability_type_id INTEGER PRIMARY KEY,      // Primary Key
      section_id INTEGER NOT NULL,              // Related section
      ability_type TEXT);                       // One of (Extraordinary, Spell-Like, Supernatural)


    affliction_details                          // 1-1 with sections
      affliction_details_id INTEGER PRIMARY KEY,// Primary Key
      section_id INTEGER NOT NULL,              // Related section
      contracted TEXT,                          // How the affliction is contracted.  (examples: contact, contact or inhaled, etc) Text
      save TEXT,                                // Save to avoid effect.  (example: Fortitude DC 12) Text
      onset TEXT,                               // Time before the affliction impacts the sufferer.  (example: 2d4 weeks) Text
      frequency TEXT,                           // Save frequency.  (example: 1/round for 2 rounds) Text
      effect TEXT,                              // Effect of the affliction.  (example: 1d8 Dex damage) Text
      initial_effect TEXT,                      // Initial effect of the affliction.  (example: 1 Con drain) Text
      secondary_effect TEXT,                    // Secondary effect of the affliction.  (example: 1 Con damage) Text
      cure TEXT                                 // Cure.  (example: 1 save). Text


    animal_companion_details                    // 1-1 with sections
      animal_companion_details_id INTEGER PRIMARY KEY,
      section_id INTEGER NOT NULL,
      ac TEXT,
      attack TEXT,
      ability_scores TEXT,
      special_qualities TEXT,
      special_attacks TEXT,
      size TEXT,
      speed TEXT,
      level TEXT


    class_details                               // 1-1 with sections
      class_details_id INTEGER PRIMARY KEY,
      section_id INTEGER NOT NULL,
      alignment TEXT,  hit_die TEXT);


    creature_details                            // 1-1 with sections
      creature_details_id INTEGER PRIMARY KEY,
      section_id INTEGER NOT NULL,
      sex TEXT,
      super_race TEXT,
      level TEXT,
      cr TEXT,
      xp TEXT,
      alignment TEXT,
      size TEXT,
      creature_type TEXT,
      creature_subtype TEXT,
      init TEXT,
      senses TEXT,
      aura TEXT,
      ac TEXT,
      hp TEXT,
      fortitude TEXT,
      reflex TEXT,
      will TEXT,
      defensive_abilities TEXT,
      dr TEXT,
      resist TEXT,
      immune TEXT,
      sr TEXT,
      weaknesses TEXT,
      speed TEXT,
      melee TEXT,
      ranged TEXT,
      space TEXT,
      reach TEXT,
      special_attacks TEXT,
      strength TEXT,
      dexterity TEXT,
      constitution TEXT,
      intelligence TEXT,
      wisdom TEXT,
      charisma TEXT,
      base_attack TEXT,
      cmb TEXT,
      cmd TEXT,
      feats TEXT,
      skills TEXT,
      racial_modifiers TEXT,
      languages TEXT,
      special_qualities TEXT,
      gear TEXT,
      environment TEXT,
      organization TEXT,
      treasure TEXT


    database_version
      id INTEGER PRIMARY KEY,                   // Primary Key
      version INTEGER                           // Database's schema version


    feat_type_descriptions                      // 1-1 with sections
      feat_type_id INTEGER PRIMARY KEY,         // Primary Key
      section_id INTEGER NOT NULL,              // Related section
      feat_type_description TEXT                // Stores the complete list as one text string of the feat types.  Needed for performance.


    feat_types                                  // 1-n with sections
      feat_type_id INTEGER PRIMARY KEY,         // Primary Key
      section_id INTEGER NOT NULL,              // Related section
      feat_type TEXT                            // Stores one feat type.  Used for creating feat lists by type.


    item_details                                // 1-1 with sections
      item_details_id INTEGER PRIMARY KEY,
      section_id INTEGER NOT NULL,
      slot TEXT,
      cl TEXT,
      price TEXT,
      weight TEXT,
      requirements TEXT,
      skill TEXT,
      cr_increase TEXT,
      cost TEXT

    settlement_details                          // 1-1 with sections
      settlement_details_id INTEGER PRIMARY KEY,
      section_id INTEGER NOT NULL,
      alignment TEXT,
      settlement_type TEXT,
      size TEXT,
      corruption TEXT,
      crime TEXT,
      economy TEXT,
      law TEXT,
      lore TEXT,
      society TEXT,
      qualities TEXT,
      danger TEXT,
      disadvantages TEXT,
      government TEXT,
      population TEXT,
      base_value TEXT,
      purchase_limit TEXT,
      spellcasting TEXT,
      minor_items TEXT,
      medium_items TEXT,
      major_items TEXT


    skill_attributes                            // 1-1 with sections
      skill_attribute_id INTEGER PRIMARY KEY,
      section_id INTEGER NOT NULL,
      attribute TEXT,
      armor_check_penalty INT,
      trained_only INT


    spell_components                            // 1-n with sections
      spell_component_id INTEGER PRIMARY KEY,
      section_id INTEGER NO NULL,
      component_type TEXT NOT NULL,
      description TEXT,
      notable INT NOT NULL


    spell_descriptors                           // 1-n with sections
      spell_descriptor_id INTEGER PRIMARY KEY,
      section_id INTEGER NO NULL,
      descriptor TEXT NOT NULL


    spell_details                               // 1-1 with sections
      spell_detail_id INTEGER PRIMARY KEY,
      section_id INTEGER NO NULL,
      school TEXT NOT NULL,
      subschool TEXT,
      descriptor_text TEXT,
      level_text TEXT,
      casting_time TEXT,
      preparation_time TEXT,
      range TEXT,
      duration TEXT,
      saving_throw TEXT,
      spell_resistance TEXT,
      as_spell_id INT


    spell_effects                               // 1-n with sections
      spell_effect_id INTEGER PRIMARY KEY,
      section_id INTEGER NO NULL,
      name TEXT NOT NULL,
      description TEXT NOT NULL


    spell_lists                                 // 1-n with sections
      spell_list_id INTEGER PRIMARY KEY,
      section_id INTEGER NO NULL,
      level INTEGER NOT NULL,
      class TEXT,
      magic_type TEXT


    trap_details                                // 1-1 with sections
      trap_details_id INTEGER PRIMARY KEY,
      section_id INTEGER NOT NULL,
      trap_type TEXT,
      perception TEXT,
      disable_device TEXT,
      duration TEXT,
      effect TEXT,
      trigger TEXT,
      reset TEXT


    vehicle_details                             // 1-1 with sections
      vehicle_details_id INTEGER PRIMARY KEY,
      section_id INTEGER NOT NULL,
      size TEXT,
      vehicle_type TEXT,
      squares TEXT,
      cost TEXT,
      ac TEXT,
      hardness TEXT,
      hp TEXT,
      base_save TEXT,
      maximum_speed TEXT,
      acceleration TEXT,
      cmb TEXT,
      cmd TEXT,
      ramming_damage TEXT,
      propulsion TEXT,
      driving_check TEXT,
      forward_facing TEXT,
      driving_device TEXT,
      driving_space TEXT,
      decks TEXT,
      deck TEXT,
      weapons TEXT,
      crew TEXT,
      passengers TEXT


## TYPES ##

ability
* description: Contains any section that represents an ability.  Many subtypes are shared with section.  For example, rogue talents sometimes grant abilities, but not always.
* subtypes: barbarian_rage_power, bardic_performance, gunslinger_deed, magus_arcana, ninja_trick, rogue_advanced_talent, rogue_talent, summoner_evolution_1, summoner_evolution_2, summoner_evolution_3, summoner_evolution_4, witch_grand_hex, witch_hex, witch_major_hex
* tables: ability_types

affliction
* description: 
* subtypes: addiction, curse, disease, infestation, insanity, poison
* tables: affliction_details

animal_companion
* description: Section describes an animal companion
* subtypes: None
* tables: animal_companion_details

class
* description: Section describes a class
* subtypes: base, core, npc, prestige
* tables: class_details

class_archetype
* description: Section describes a class archetype
* subtypes: barbarian, bard, druid, fighter, monk, paladin, ranger, rogue
* tables: None

creature
* description: Section describes a creature, monster or npc
* subtypes: familiar
* tables: creature_details

feat
* description: Section describes a feat
* subtypes: None
* tables: feat_type_descriptions, feat_types

haunt
* description: Section describes a haunt (Game Mastery Guide)
* subtypes: None
* tables: None

item
* description: Section describes an item
* subtypes: armor, arms, belt, body, chest, eyes, feet, hands, head, headband, neck, ring, shield, shoulders, wrist
* tables: item_details

list
* description: A top level section made to hold all sections of a certain type (Feats, Spells, Rules from Ultimate Magic, etc
* subtypes: None
* tables: None

race
* description: Section describes a race
* subtypes: monster_race, standard_race
* tables: None

racial_trait
* description: Section describes a racial trait
* subtypes: dwarves, elves, gnomes, half-elves, half-orcs, halflings, humans
* tables: None

section
* description: Contains a section of text.  Subtype may indicate a special section subtype.
* subtypes: alchemist_discovery, arcane_school, barbarian_rage_power, cleric_domain, cleric_subdomain, condition, elemental_arcane_school, focused_arcane_school, ninja_trick, oracle_mystery, ranger_combat_style, rogue_advanced_talent, rogue_talent, sorcerer_bloodline, special_abilities, spellbook, warrior_order, witch_patron
* tables: None

settlement
* description: Section describes a settlement (Game Mastery Guide)
* subtypes: None
* tables: settlement_details

skill
* description: Section describes a skill
* subtypes: None
* tables: skill_attributes

spell
* description: Section describes a spell
* subtypes: None
* tables: spell_components, spell_descriptors, spell_details, spell_effects, spell_lists

table
* description: Section represents a table from the text.
* subtypes: None
* tables: None
* notes: Later the table should be broken down into rows to give access to the contained information.

trap
* description: Section describes a trap
* subtypes: None
* tables: trap_details

vehicle
* description: Section describes a vehicle (Ultimate Combat)
* subtypes: None
* tables: vehicle_details

