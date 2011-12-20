#!/bin/bash

# Core Rulebook
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Getting Started"    ../web/paizo.com/pathfinderRPG/prd/gettingStarted.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Classes"            ../web/paizo.com/pathfinderRPG/prd/classes.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Using Skills"       ../web/paizo.com/pathfinderRPG/prd/usingSkills.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Skill Descriptions" ../web/paizo.com/pathfinderRPG/prd/skillDescriptions.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Equipment"          ../web/paizo.com/pathfinderRPG/prd/equipment.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Additional Rules"   ../web/paizo.com/pathfinderRPG/prd/additionalRules.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Combat"             ../web/paizo.com/pathfinderRPG/prd/combat.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Magic"              ../web/paizo.com/pathfinderRPG/prd/magic.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Prestige Classes"   ../web/paizo.com/pathfinderRPG/prd/prestigeClasses.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Gamemastering"      ../web/paizo.com/pathfinderRPG/prd/gamemastering.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Environment"        ../web/paizo.com/pathfinderRPG/prd/environment.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Creating NPCs"      ../web/paizo.com/pathfinderRPG/prd/creatingNPCs.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Magic Items"        ../web/paizo.com/pathfinderRPG/prd/magicItems.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Glossary"           ../web/paizo.com/pathfinderRPG/prd/glossary.html

./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Armor"                 ../web/paizo.com/pathfinderRPG/prd/magicItems/armor.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Artifacts"             ../web/paizo.com/pathfinderRPG/prd/magicItems/artifacts.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Cursed Items"          ../web/paizo.com/pathfinderRPG/prd/magicItems/cursedItems.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Intelligent Items"     ../web/paizo.com/pathfinderRPG/prd/magicItems/intelligentItems.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Magic Item Creation"   ../web/paizo.com/pathfinderRPG/prd/magicItems/magicItemCreation.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Potions"               ../web/paizo.com/pathfinderRPG/prd/magicItems/potions.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Rings"                 ../web/paizo.com/pathfinderRPG/prd/magicItems/rings.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Rods"                  ../web/paizo.com/pathfinderRPG/prd/magicItems/rods.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Scrolls"               ../web/paizo.com/pathfinderRPG/prd/magicItems/scrolls.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Specific Cursed Items" ../web/paizo.com/pathfinderRPG/prd/magicItems/specificCursedItems.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Staves"                ../web/paizo.com/pathfinderRPG/prd/magicItems/staves.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Wands"                 ../web/paizo.com/pathfinderRPG/prd/magicItems/wands.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Weapons"               ../web/paizo.com/pathfinderRPG/prd/magicItems/weapons.html
./rules_parse.py -o ../data/ -b "Core Rulebook" -t "Wonderous Items"       ../web/paizo.com/pathfinderRPG/prd/magicItems/wondrousItems.html

# Bestiary
./rules_parse.py -o ../data/ -b "Bestiary" -t "Introduction"            ../web/paizo.com/pathfinderRPG/prd/monsters/introduction.html
./rules_parse.py -o ../data/ -b "Bestiary" -t "Creature Types"          ../web/paizo.com/pathfinderRPG/prd/monsters/creatureTypes.html
./rules_parse.py -o ../data/ -b "Bestiary" -t "Monster Advancement"     ../web/paizo.com/pathfinderRPG/prd/monsters/monsterAdvancement.html
./rules_parse.py -o ../data/ -b "Bestiary" -t "Monster Cohorts"         ../web/paizo.com/pathfinderRPG/prd/monsters/monsterCohorts.html
./rules_parse.py -o ../data/ -b "Bestiary" -t "Monster Creation"        ../web/paizo.com/pathfinderRPG/prd/monsters/monsterCreation.html
./rules_parse.py -o ../data/ -b "Bestiary" -t "Monster Roles"           ../web/paizo.com/pathfinderRPG/prd/monsters/monsterRoles.html
./rules_parse.py -o ../data/ -b "Bestiary" -t "Monster As PCs"          ../web/paizo.com/pathfinderRPG/prd/monsters/monstersAsPCs.html
./rules_parse.py -o ../data/ -b "Bestiary" -t "Universal Monster Rules" ../web/paizo.com/pathfinderRPG/prd/monsters/encounterTables.html
./rules_parse.py -o ../data/ -b "Bestiary" -t "Encounter Tables"        ../web/paizo.com/pathfinderRPG/prd/monsters/universalMonsterRules.html

# Bestiary 2
./rules_parse.py -o ../data/ -b "Bestiary 2" -t "Monster Advancement"     ../web/paizo.com/pathfinderRPG/prd/additionalMonsters/monsterAdvancement.html
./rules_parse.py -o ../data/ -b "Bestiary 2" -t "Universal Monster Rules" ../web/paizo.com/pathfinderRPG/prd/additionalMonsters/universalMonsterRules.html
./rules_parse.py -o ../data/ -b "Bestiary" -t "Creature Types"            ../web/paizo.com/pathfinderRPG/prd/additionalMonsters/creatureTypes.html
./rules_parse.py -o ../data/ -b "Bestiary 2" -t "Monster Cohorts"         ../web/paizo.com/pathfinderRPG/prd/additionalMonsters/monsterCohorts.html

# Advanced Player's Guide
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Races"            ../web/paizo.com/pathfinderRPG/prd/advanced/advancedRaces.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Base Classes"     ../web/paizo.com/pathfinderRPG/prd/advanced/advancedBaseClasses.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Core Classes"     ../web/paizo.com/pathfinderRPG/prd/advanced/advancedCoreClasses.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Prestige Classes" ../web/paizo.com/pathfinderRPG/prd/advanced/advancedPrestigeClasses.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Barbarian"        ../web/paizo.com/pathfinderRPG/prd/advanced/coreClasses/barbarian.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Bard"             ../web/paizo.com/pathfinderRPG/prd/advanced/coreClasses/bard.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Cleric"           ../web/paizo.com/pathfinderRPG/prd/advanced/coreClasses/cleric.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Druid"            ../web/paizo.com/pathfinderRPG/prd/advanced/coreClasses/druid.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Fighter"          ../web/paizo.com/pathfinderRPG/prd/advanced/coreClasses/fighter.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Monk"             ../web/paizo.com/pathfinderRPG/prd/advanced/coreClasses/monk.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Paladin"          ../web/paizo.com/pathfinderRPG/prd/advanced/coreClasses/paladin.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Ranger"           ../web/paizo.com/pathfinderRPG/prd/advanced/coreClasses/ranger.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Rogue"            ../web/paizo.com/pathfinderRPG/prd/advanced/coreClasses/rogue.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Sorcerer"         ../web/paizo.com/pathfinderRPG/prd/advanced/coreClasses/sorcerer.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Wizard"           ../web/paizo.com/pathfinderRPG/prd/advanced/coreClasses/wizard.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Gear"             ../web/paizo.com/pathfinderRPG/prd/advanced/advancedGear.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "New Rules"        ../web/paizo.com/pathfinderRPG/prd/advanced/advancedNewRules.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Magic Items"      ../web/paizo.com/pathfinderRPG/prd/advanced/advancedMagicItems.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Armor"            ../web/paizo.com/pathfinderRPG/prd/advanced/magicItems/armor.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Cursed Items"     ../web/paizo.com/pathfinderRPG/prd/advanced/magicItems/cursedItems.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Major Artifacts"  ../web/paizo.com/pathfinderRPG/prd/advanced/magicItems/majorArtifacts.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Minor Artifacts"  ../web/paizo.com/pathfinderRPG/prd/advanced/magicItems/minorArtifacts.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Rings"            ../web/paizo.com/pathfinderRPG/prd/advanced/magicItems/rings.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Rods"             ../web/paizo.com/pathfinderRPG/prd/advanced/magicItems/rods.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Staves"           ../web/paizo.com/pathfinderRPG/prd/advanced/magicItems/staves.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Weapons"          ../web/paizo.com/pathfinderRPG/prd/advanced/magicItems/weapons.html
./rules_parse.py -o ../data/ -b "Advanced Player's Guide" -t "Wonderous Items"  ../web/paizo.com/pathfinderRPG/prd/advanced/magicItems/wondrousItems.html

# Ultimate Magic
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Spellcasting Class Options"        ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Alchemist"                         ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/alchemist.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Bard"                              ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/bard.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Cleric"                            ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/cleric.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Druid"                             ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/druid.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Inquisitor"                        ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/inquisitor.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Magus"                             ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/magus.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Monk"                              ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/monk.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Oracle"                            ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/oracle.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Paladin"                           ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/paladin.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Ranger"                            ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/ranger.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Sorcerer"                          ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/sorcerer.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Summoner"                          ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/summoner.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Witch"                             ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/witch.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Wizard"                            ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/wizard.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Updates"                           ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicAppendices.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Words of Power"                    ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/ultimateMagicWordsOfPower.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Mastering Magic"                   ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/magic/introduction.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Spellblights"                      ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/magic/spellblights.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Spell Duels"                       ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/magic/spellDuels.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Binding Outsiders"                 ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/magic/bindingOutsiders.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Building and Modifying Constructs" ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/magic/buildingAndModifyingConstructs.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Spellbooks"                        ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/magic/spellbooks.html
./rules_parse.py -o ../data/ -b "Ultimate Magic" -t "Designing Spells"                  ../web/paizo.com/pathfinderRPG/prd/ultimateMagic/magic/designingSpells.html

# Ultimate Combat
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Class Archetypes"            ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Alchemist"                   ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/alchemist.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Barbarian"                   ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/barbarian.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Bard"                        ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/bard.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Cavalier"                    ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/cavalier.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Cleric"                      ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/cleric.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Druid"                       ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/druid.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Fighter"                     ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/fighter.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Gunslinger"                  ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/gunslinger.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Inquisitor"                  ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/inquisitor.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Magus"                       ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/magus.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Monk"                        ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/monk.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Paladin"                     ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/paladin.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Ranger"                      ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/ranger.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Rogue"                       ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/rogue.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Wizard"                      ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/classArchetypes/wizard.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Mastering Combat"            ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/combat/introduction.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Eastern Armor and Weapons"   ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/combat/easternArmorAndWeapons.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Firearms"                    ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/combat/firearms.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Gladiator Weapons"           ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/combat/gladiatorWeapons.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Primitive Armor and Weapons" ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/combat/primitiveArmorAndWeapons.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Duels"                       ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/combat/duels.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Performance Combat"          ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/combat/performanceCombat.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Siege Engines"               ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/combat/siegeEngines.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Vehicles"                    ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/ultimateCombatVehicles.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Variant Rules"                    ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/variants/introduction.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Armor as Damage Reduction"                    ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/variants/armorAsDamageReduction.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Called Shots"                    ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/variants/calledShots.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Piecemeal Armor"                    ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/variants/piecemealArmor.html
./rules_parse.py -o ../data/ -b "Ultimate Combat" -t "Wounds and Vigor"                    ../web/paizo.com/pathfinderRPG/prd/ultimateCombat/variants/woundsAndVigor.html


# Game Mastery Guide
./rules_parse.py -o ../data/ -b "Game Mastery Guide" -t "Chases"                ../web/paizo.com/pathfinderRPG/prd/mastery/chases.html
./rules_parse.py -o ../data/ -b "Game Mastery Guide" -t "Disasters"             ../web/paizo.com/pathfinderRPG/prd/mastery/disasters.html
./rules_parse.py -o ../data/ -b "Game Mastery Guide" -t "Drugs and Addiction"   ../web/paizo.com/pathfinderRPG/prd/mastery/drugsAndAddiction.html
./rules_parse.py -o ../data/ -b "Game Mastery Guide" -t "Fast Play Ship Combat" ../web/paizo.com/pathfinderRPG/prd/mastery/fastPlayShipCombat.html
./rules_parse.py -o ../data/ -b "Game Mastery Guide" -t "Haunts"                ../web/paizo.com/pathfinderRPG/prd/mastery/haunts.html
./rules_parse.py -o ../data/ -b "Game Mastery Guide" -t "Hazards"               ../web/paizo.com/pathfinderRPG/prd/mastery/hazards.html
./rules_parse.py -o ../data/ -b "Game Mastery Guide" -t "NPC Boons"             ../web/paizo.com/pathfinderRPG/prd/mastery/nPCBoons.html
./rules_parse.py -o ../data/ -b "Game Mastery Guide" -t "NPC Gallery"           ../web/paizo.com/pathfinderRPG/prd/mastery/nPCGallery.html
./rules_parse.py -o ../data/ -b "Game Mastery Guide" -t "Planar Adventures"     ../web/paizo.com/pathfinderRPG/prd/mastery/planarAdventures.html
./rules_parse.py -o ../data/ -b "Game Mastery Guide" -t "Sanity and Madness"    ../web/paizo.com/pathfinderRPG/prd/mastery/sanityAndMadness.html
./rules_parse.py -o ../data/ -b "Game Mastery Guide" -t "Settlements"           ../web/paizo.com/pathfinderRPG/prd/mastery/settlements.html


