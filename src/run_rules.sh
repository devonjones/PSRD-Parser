#!/bin/bash
set -e

source dir.conf

# OGL
./rules_parse.py -o $DATA_DIR -b "OGL" -t "OGL" $WEB_DIR/pathfinderRPG/prd/openGameLicense.html 

# Core Rulebook
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Getting Started"    $WEB_DIR/pathfinderRPG/prd/gettingStarted.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Classes"            $WEB_DIR/pathfinderRPG/prd/classes.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Using Skills"       $WEB_DIR/pathfinderRPG/prd/usingSkills.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Skill Descriptions" $WEB_DIR/pathfinderRPG/prd/skillDescriptions.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Equipment"          $WEB_DIR/pathfinderRPG/prd/equipment.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Additional Rules"   $WEB_DIR/pathfinderRPG/prd/additionalRules.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Combat"             $WEB_DIR/pathfinderRPG/prd/combat.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Magic"              $WEB_DIR/pathfinderRPG/prd/magic.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Prestige Classes"   $WEB_DIR/pathfinderRPG/prd/prestigeClasses.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Gamemastering"      $WEB_DIR/pathfinderRPG/prd/gamemastering.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Environment"        $WEB_DIR/pathfinderRPG/prd/environment.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Creating NPCs"      $WEB_DIR/pathfinderRPG/prd/creatingNPCs.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Magic Items"        $WEB_DIR/pathfinderRPG/prd/magicItems.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Glossary"           $WEB_DIR/pathfinderRPG/prd/glossary.html

./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Armor"                 $WEB_DIR/pathfinderRPG/prd/magicItems/armor.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Artifacts"             $WEB_DIR/pathfinderRPG/prd/magicItems/artifacts.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Cursed Items"          $WEB_DIR/pathfinderRPG/prd/magicItems/cursedItems.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Intelligent Items"     $WEB_DIR/pathfinderRPG/prd/magicItems/intelligentItems.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Magic Item Creation"   $WEB_DIR/pathfinderRPG/prd/magicItems/magicItemCreation.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Potions"               $WEB_DIR/pathfinderRPG/prd/magicItems/potions.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Rings"                 $WEB_DIR/pathfinderRPG/prd/magicItems/rings.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Rods"                  $WEB_DIR/pathfinderRPG/prd/magicItems/rods.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Scrolls"               $WEB_DIR/pathfinderRPG/prd/magicItems/scrolls.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Specific Cursed Items" $WEB_DIR/pathfinderRPG/prd/magicItems/specificCursedItems.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Staves"                $WEB_DIR/pathfinderRPG/prd/magicItems/staves.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Wands"                 $WEB_DIR/pathfinderRPG/prd/magicItems/wands.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Weapons"               $WEB_DIR/pathfinderRPG/prd/magicItems/weapons.html
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Wonderous Items"       $WEB_DIR/pathfinderRPG/prd/magicItems/wondrousItems.html

# Bestiary
./rules_parse.py -o $DATA_DIR -b "Bestiary" -t "Introduction"            $WEB_DIR/pathfinderRPG/prd/monsters/introduction.html
./rules_parse.py -o $DATA_DIR -b "Bestiary" -t "Creature Types"          $WEB_DIR/pathfinderRPG/prd/monsters/creatureTypes.html
./rules_parse.py -o $DATA_DIR -b "Bestiary" -t "Monster Advancement"     $WEB_DIR/pathfinderRPG/prd/monsters/monsterAdvancement.html
./rules_parse.py -o $DATA_DIR -b "Bestiary" -t "Monster Cohorts"         $WEB_DIR/pathfinderRPG/prd/monsters/monsterCohorts.html
./rules_parse.py -o $DATA_DIR -b "Bestiary" -t "Monster Creation"        $WEB_DIR/pathfinderRPG/prd/monsters/monsterCreation.html
./rules_parse.py -o $DATA_DIR -b "Bestiary" -t "Monster Roles"           $WEB_DIR/pathfinderRPG/prd/monsters/monsterRoles.html
./rules_parse.py -o $DATA_DIR -b "Bestiary" -t "Monster As PCs"          $WEB_DIR/pathfinderRPG/prd/monsters/monstersAsPCs.html
./rules_parse.py -o $DATA_DIR -b "Bestiary" -t "Universal Monster Rules" $WEB_DIR/pathfinderRPG/prd/monsters/universalMonsterRules.html
./rules_parse.py -o $DATA_DIR -b "Bestiary" -t "Encounter Tables"        $WEB_DIR/pathfinderRPG/prd/monsters/encounterTables.html

# Bestiary 2
#./rules_parse.py -o $DATA_DIR -b "Bestiary 2" -t "Monster Advancement"     $WEB_DIR/pathfinderRPG/prd/additionalMonsters/monsterAdvancement.html
#./rules_parse.py -o $DATA_DIR -b "Bestiary 2" -t "Universal Monster Rules" $WEB_DIR/pathfinderRPG/prd/additionalMonsters/universalMonsterRules.html
#./rules_parse.py -o $DATA_DIR -b "Bestiary 2" -t "Creature Types"          $WEB_DIR/pathfinderRPG/prd/additionalMonsters/creatureTypes.html
#./rules_parse.py -o $DATA_DIR -b "Bestiary 2" -t "Monster Cohorts"         $WEB_DIR/pathfinderRPG/prd/additionalMonsters/monsterCohorts.html

# Bestiary 3
#./rules_parse.py -o $DATA_DIR -b "Bestiary 3" -t "Creature Types"          $WEB_DIR/pathfinderRPG/prd/bestiary3/creatureTypes.html
#./rules_parse.py -o $DATA_DIR -b "Bestiary 3" -t "Monster Advancement"     $WEB_DIR/pathfinderRPG/prd/bestiary3/monsterAdvancement.html
#./rules_parse.py -o $DATA_DIR -b "Bestiary 3" -t "Monster Cohorts"         $WEB_DIR/pathfinderRPG/prd/bestiary3/monsterCohorts.html
#./rules_parse.py -o $DATA_DIR -b "Bestiary 3" -t "Universal Monster Rules" $WEB_DIR/pathfinderRPG/prd/bestiary3/universalMonsterRules.html

# Advanced Player's Guide
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Races"            $WEB_DIR/pathfinderRPG/prd/advanced/advancedRaces.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Base Classes"     $WEB_DIR/pathfinderRPG/prd/advanced/advancedBaseClasses.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Core Classes"     $WEB_DIR/pathfinderRPG/prd/advanced/advancedCoreClasses.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Prestige Classes" $WEB_DIR/pathfinderRPG/prd/advanced/advancedPrestigeClasses.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Barbarian"        $WEB_DIR/pathfinderRPG/prd/advanced/coreClasses/barbarian.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Bard"             $WEB_DIR/pathfinderRPG/prd/advanced/coreClasses/bard.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Cleric"           $WEB_DIR/pathfinderRPG/prd/advanced/coreClasses/cleric.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Druid"            $WEB_DIR/pathfinderRPG/prd/advanced/coreClasses/druid.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Fighter"          $WEB_DIR/pathfinderRPG/prd/advanced/coreClasses/fighter.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Monk"             $WEB_DIR/pathfinderRPG/prd/advanced/coreClasses/monk.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Paladin"          $WEB_DIR/pathfinderRPG/prd/advanced/coreClasses/paladin.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Ranger"           $WEB_DIR/pathfinderRPG/prd/advanced/coreClasses/ranger.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Rogue"            $WEB_DIR/pathfinderRPG/prd/advanced/coreClasses/rogue.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Sorcerer"         $WEB_DIR/pathfinderRPG/prd/advanced/coreClasses/sorcerer.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Wizard"           $WEB_DIR/pathfinderRPG/prd/advanced/coreClasses/wizard.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Gear"             $WEB_DIR/pathfinderRPG/prd/advanced/advancedGear.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "New Rules"        $WEB_DIR/pathfinderRPG/prd/advanced/advancedNewRules.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Magic Items"      $WEB_DIR/pathfinderRPG/prd/advanced/advancedMagicItems.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Armor"            $WEB_DIR/pathfinderRPG/prd/advanced/magicItems/armor.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Cursed Items"     $WEB_DIR/pathfinderRPG/prd/advanced/magicItems/cursedItems.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Major Artifacts"  $WEB_DIR/pathfinderRPG/prd/advanced/magicItems/majorArtifacts.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Minor Artifacts"  $WEB_DIR/pathfinderRPG/prd/advanced/magicItems/minorArtifacts.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Rings"            $WEB_DIR/pathfinderRPG/prd/advanced/magicItems/rings.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Rods"             $WEB_DIR/pathfinderRPG/prd/advanced/magicItems/rods.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Staves"           $WEB_DIR/pathfinderRPG/prd/advanced/magicItems/staves.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Weapons"          $WEB_DIR/pathfinderRPG/prd/advanced/magicItems/weapons.html
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Wonderous Items"  $WEB_DIR/pathfinderRPG/prd/advanced/magicItems/wondrousItems.html

# Ultimate Magic
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Spellcasting Class Options"        $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Alchemist"                         $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/alchemist.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Bard"                              $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/bard.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Cleric"                            $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/cleric.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Druid"                             $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/druid.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Inquisitor"                        $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/inquisitor.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Magus"                             $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/magus.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Monk"                              $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/monk.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Oracle"                            $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/oracle.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Paladin"                           $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/paladin.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Ranger"                            $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/ranger.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Sorcerer"                          $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/sorcerer.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Summoner"                          $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/summoner.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Witch"                             $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/witch.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Wizard"                            $WEB_DIR/pathfinderRPG/prd/ultimateMagic/spellcastingClassOptions/wizard.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Updates"                           $WEB_DIR/pathfinderRPG/prd/ultimateMagic/ultimateMagicAppendices.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Words of Power"                    $WEB_DIR/pathfinderRPG/prd/ultimateMagic/ultimateMagicWordsOfPower.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Mastering Magic"                   $WEB_DIR/pathfinderRPG/prd/ultimateMagic/magic/introduction.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Spellblights"                      $WEB_DIR/pathfinderRPG/prd/ultimateMagic/magic/spellblights.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Spell Duels"                       $WEB_DIR/pathfinderRPG/prd/ultimateMagic/magic/spellDuels.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Binding Outsiders"                 $WEB_DIR/pathfinderRPG/prd/ultimateMagic/magic/bindingOutsiders.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Building and Modifying Constructs" $WEB_DIR/pathfinderRPG/prd/ultimateMagic/magic/buildingAndModifyingConstructs.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Spellbooks"                        $WEB_DIR/pathfinderRPG/prd/ultimateMagic/magic/spellbooks.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Designing Spells"                  $WEB_DIR/pathfinderRPG/prd/ultimateMagic/magic/designingSpells.html

# Ultimate Combat
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Class Archetypes"            $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Alchemist"                   $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/alchemist.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Barbarian"                   $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/barbarian.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Bard"                        $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/bard.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Cavalier"                    $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/cavalier.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Cleric"                      $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/cleric.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Druid"                       $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/druid.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Fighter"                     $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/fighter.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Gunslinger"                  $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/gunslinger.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Inquisitor"                  $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/inquisitor.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Magus"                       $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/magus.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Monk"                        $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/monk.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Paladin"                     $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/paladin.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Ranger"                      $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/ranger.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Rogue"                       $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/rogue.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Wizard"                      $WEB_DIR/pathfinderRPG/prd/ultimateCombat/classArchetypes/wizard.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Mastering Combat"            $WEB_DIR/pathfinderRPG/prd/ultimateCombat/combat/introduction.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Eastern Armor and Weapons"   $WEB_DIR/pathfinderRPG/prd/ultimateCombat/combat/easternArmorAndWeapons.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Firearms"                    $WEB_DIR/pathfinderRPG/prd/ultimateCombat/combat/firearms.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Gladiator Weapons"           $WEB_DIR/pathfinderRPG/prd/ultimateCombat/combat/gladiatorWeapons.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Primitive Armor and Weapons" $WEB_DIR/pathfinderRPG/prd/ultimateCombat/combat/primitiveArmorAndWeapons.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Duels"                       $WEB_DIR/pathfinderRPG/prd/ultimateCombat/combat/duels.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Performance Combat"          $WEB_DIR/pathfinderRPG/prd/ultimateCombat/combat/performanceCombat.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Siege Engines"               $WEB_DIR/pathfinderRPG/prd/ultimateCombat/combat/siegeEngines.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Vehicles"                    $WEB_DIR/pathfinderRPG/prd/ultimateCombat/ultimateCombatVehicles.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Variant Rules"               $WEB_DIR/pathfinderRPG/prd/ultimateCombat/variants/introduction.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Armor as Damage Reduction"   $WEB_DIR/pathfinderRPG/prd/ultimateCombat/variants/armorAsDamageReduction.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Called Shots"                $WEB_DIR/pathfinderRPG/prd/ultimateCombat/variants/calledShots.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Piecemeal Armor"             $WEB_DIR/pathfinderRPG/prd/ultimateCombat/variants/piecemealArmor.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Combat" -t "Wounds and Vigor"            $WEB_DIR/pathfinderRPG/prd/ultimateCombat/variants/woundsAndVigor.html


# Game Mastery Guide
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Chases"                $WEB_DIR/pathfinderRPG/prd/mastery/chases.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Disasters"             $WEB_DIR/pathfinderRPG/prd/mastery/disasters.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Drugs and Addiction"   $WEB_DIR/pathfinderRPG/prd/mastery/drugsAndAddiction.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Fast Play Ship Combat" $WEB_DIR/pathfinderRPG/prd/mastery/fastPlayShipCombat.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Haunts"                $WEB_DIR/pathfinderRPG/prd/mastery/haunts.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Hazards"               $WEB_DIR/pathfinderRPG/prd/mastery/hazards.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "NPC Boons"             $WEB_DIR/pathfinderRPG/prd/mastery/nPCBoons.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "NPC Gallery"           $WEB_DIR/pathfinderRPG/prd/mastery/nPCGallery.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Planar Adventures"     $WEB_DIR/pathfinderRPG/prd/mastery/planarAdventures.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Sanity and Madness"    $WEB_DIR/pathfinderRPG/prd/mastery/sanityAndMadness.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Settlements"           $WEB_DIR/pathfinderRPG/prd/mastery/settlements.html


# Advanced Race Guide
./rules_parse.py -o $DATA_DIR -b "Advanced Race Guide" -t "Age, Height & Weight"    $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/ageHeightWeight.html
./rules_parse.py -o $DATA_DIR -b "Advanced Race Guide" -t "Core Races"              $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/coreRaces.html
./rules_parse.py -o $DATA_DIR -b "Advanced Race Guide" -t "Featured Races"          $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/featuredRaces.html
./rules_parse.py -o $DATA_DIR -b "Advanced Race Guide" -t "Race Builder"            $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/raceBuilder.html
./rules_parse.py -o $DATA_DIR -b "Advanced Race Guide" -t "Uncommon Races"          $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/uncommonRaces.html
./rules_parse.py -o $DATA_DIR -b "Advanced Race Guide" -t "Example Races"           $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/raceBuilder/exampleRaces.html
./rules_parse.py -o $DATA_DIR -b "Advanced Race Guide" -t "Racial Qualities"        $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/raceBuilder/racialQualities.html
./rules_parse.py -o $DATA_DIR -b "Advanced Race Guide" -t "Racial Traits"           $WEB_DIR/pathfinderRPG/prd/advancedRaceGuide/raceBuilder/racialTraits.html

