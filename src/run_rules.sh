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
./rules_parse.py -o $DATA_DIR -b "Core Rulebook" -t "Wondrous Items"        $WEB_DIR/pathfinderRPG/prd/magicItems/wondrousItems.html

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

# Advanced Class Guide
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Hybrid Classes"               $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/hybridClasses.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Designing Classes"            $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/designingClasses.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Class Options"                $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/index.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Alchemist"                    $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/alchemist.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Arcanist"                     $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/arcanist.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Barbarian"                    $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/barbarian.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Bard"                         $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/bard.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Bloodrager"                   $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/bloodrager.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Brawler"                      $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/brawler.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Cavalier"                     $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/cavalier.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Cleric"                       $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/cleric.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Druid"                        $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/druid.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Fighter"                      $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/fighter.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Gunslinger"                   $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/gunslinger.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Hunter"                       $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/hunter.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Inquisitor"                   $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/inquisitor.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Investigator"                 $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/investigator.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Magus"                        $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/magus.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Monk"                         $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/monk.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Oracle"                       $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/oracle.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Paladin"                      $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/paladin.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Ranger"                       $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/ranger.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Rogue"                        $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/rogue.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Shaman"                       $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/shaman.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Skald"                        $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/skald.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Slayer"                       $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/slayer.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Sorcerer"                     $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/sorcerer.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Summoner"                     $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/summoner.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Swashbuckler"                 $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/swashbuckler.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Warpriest"                    $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/warpriest.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Witch"                        $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/witch.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Wizard"                       $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/classOptions/wizard.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Adventuring Gear" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/adventuringGear.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Alchemical Remedies" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/alchemicalRemedies.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Alchemical Tools" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/alchemicalTools.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Alchemical Weapons" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/alchemicalWeapons.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Armor Special Abilities" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/armorSpecialAbilities.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Gear" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/index.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Rings" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/rings.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Rods" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/rods.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Specific Armors & Shields" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/specificArmorsShields.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Specific Weapons" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/specificWeapons.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Weapon Special Abilities" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/weaponSpecialAbilities.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Staves" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/staves.html
./rules_parse.py -o $DATA_DIR -b "Advanced Class Guide" -t "Wondrous Items" $WEB_DIR/pathfinderRPG/prd/advancedClassGuide/gear/wondrousItems.html

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
./rules_parse.py -o $DATA_DIR -b "Advanced Player's Guide" -t "Wondrous Items"  $WEB_DIR/pathfinderRPG/prd/advanced/magicItems/wondrousItems.html

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
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Class Word Lists"                  $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/classWordLists.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Effect Words"                      $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectwords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Meta Words" -n                     $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/metawords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Target Words" -n                   $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/targetwords.html

./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Acid Words" -n                     $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/acidWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Alignment Words" -n                $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/alignmentWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Animal Words" -n                   $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/animalWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Armor Words" -n                    $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/armorWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Binding Words" -n                  $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/bindingWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Body Words" -n                     $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/bodyWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Change Words" -n                   $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/changeWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Cold Words" -n                     $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/coldWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Command Words" -n                  $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/commandWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Concealing Words" -n               $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/concealingWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Death Words" -n                    $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/deathWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Destruction Words" -n              $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/destructionWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Detection Words" -n                $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/detectionWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Dispelling Words" -n               $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/dispellingWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Divination Words" -n               $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/divinationWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Electricity Words" -n              $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/electricityWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Fear Words" -n                     $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/fearWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Fire Words" -n                     $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/fireWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Flight Words" -n                   $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/flightWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Force Words" -n                    $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/forceWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Gravity Words" -n                  $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/gravityWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Healing Words" -n                  $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/healingWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Illumination Words" -n             $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/illuminationWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Illusion Words" -n                 $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/illusionWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Language Words" -n                 $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/languageWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Life Words" -n                     $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/lifeWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Pain Words" -n                     $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/painWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Power Words" -n                    $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/powerWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Sonic Words" -n                    $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/sonicWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Summoning Words" -n                $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/summoningWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Teleportation Words" -n            $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/teleportationWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Time Words" -n                     $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/timeWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Wall Words" -n                     $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/wallWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Weather Words" -n                  $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/weatherWords.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Magic" -t "Wounding Words" -n                 $WEB_DIR/pathfinderRPG/prd/ultimateMagic/wordsOfPower/effectWords/woundingWords.html


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

# Ultimate Campaign
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Character Background"        $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/characterBackground.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Early Life"                  $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/characterBackground/earlyLife.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Adolescence"                 $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/characterBackground/adolescence.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Adulthood"                   $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/characterBackground/adulthood.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Background Generator"        $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/characterBackground/backgroundGenerator.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Traits"                      $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/characterBackground/traits.html

./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Downtime"                    $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/downtime.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Downtime Activities"         $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/downtime/downtimeActivities.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Managers"                    $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/downtime/managers.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Rooms And Teams"             $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/downtime/roomsAndTeams.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Buildings And Organizations" $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/downtime/buildingsAndOrganizations.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Downtime Events"             $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/downtime/downtimeEvents.html

./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Campaign Systems"            $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Alignment"                   $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/alignment.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Bargaining"                  $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/bargaining.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Companions" -n               $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/companions.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Contacts"                    $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/contacts.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Exploration"                 $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/exploration.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Honor"                       $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/honor.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Investment"                  $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/investment.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Lineage"                     $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/lineage.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Magic Item Creation"         $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/magicItemCreation.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Relationships"               $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/relationships.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Reputation And Fame"         $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/reputationAndFame.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Retirement"                  $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/retirement.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Retraining"                  $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/retraining.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Taxation"                    $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/taxation.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Young Characters"            $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/campaignSystems/youngCharacters.html

./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Kingdoms And War"            $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/kingdomsAndWar.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Kingdom Building"            $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/kingdomsAndWar/kingdomBuilding.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Kingdom Turn Sequence"       $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/kingdomsAndWar/kingdomTurnSequence.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Optional Kingdom Rules"      $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/kingdomsAndWar/optionalKingdomRules.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Campaign" -t "Mass Combat"                 $WEB_DIR/pathfinderRPG/prd/ultimateCampaign/kingdomsAndWar/massCombat.html


# Game Mastery Guide
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Chases"                $WEB_DIR/pathfinderRPG/prd/mastery/chases.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Disasters"             $WEB_DIR/pathfinderRPG/prd/mastery/disasters.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Drugs and Addiction"   $WEB_DIR/pathfinderRPG/prd/mastery/drugsAndAddiction.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Fast Play Ship Combat" $WEB_DIR/pathfinderRPG/prd/mastery/fastPlayShipCombat.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Haunts"                $WEB_DIR/pathfinderRPG/prd/mastery/haunts.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "Hazards"               $WEB_DIR/pathfinderRPG/prd/mastery/hazards.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "NPC Boons"             $WEB_DIR/pathfinderRPG/prd/mastery/npcBoons.html
./rules_parse.py -o $DATA_DIR -b "Game Mastery Guide" -t "NPC Gallery"           $WEB_DIR/pathfinderRPG/prd/mastery/npcGallery.html


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

# Ultimate Equipment
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Arms And Armor"                     $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/armsAndArmor/index.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Armor"                              $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/armsAndArmor/armor.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Weapons"                            $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/armsAndArmor/weapons.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Special Materials"                  $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/armsAndArmor/materials.html

./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Gear"                               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/index.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Adventuring Gear"                   $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/adventuringGear.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Tools and Skill Kits"               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/toolsAndSkillKits.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Animals, Mounts, and Related Gear"  $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/animalsAndTransports.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Clothing"                           $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/clothing.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Entertainment and Trade Goods"      $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/entertainmentAndTradeGoods.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Food and Drink"                     $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/foodAndDrink.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Lodging and Services"               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/lodgingAndServices.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Alchemical Remedies"                $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/alchemicalRemedies.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Alchemical Tools"                   $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/alchemicalTools.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Alchemical Weapons"                 $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/alchemicalWeapons.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Poisons"                            $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/gear/poisons.html

./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Magic Arms and Armor"               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/magicArmsAndArmor/index.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Armor Special Abilities" -n         $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/magicArmsAndArmor/armorSpecialAbilities.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Specific Magic Armor and Shields"   $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/magicArmsAndArmor/specificMagicArmorShields.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Weapon Special Abilities"           $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/magicArmsAndArmor/weaponSpecialAbilities.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Specific Magic Weapons"             $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/magicArmsAndArmor/specificMagicWeapons.html

./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Rings, Rods & Staves"               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/ringsRodsStaves/index.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Rings"                              $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/ringsRodsStaves/rings.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Rods"                               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/ringsRodsStaves/rods.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Staves"                             $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/ringsRodsStaves/staves.html

./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Wondrous Items"                     $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/index.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Belt"                               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/belts.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Body"                               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/body.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Chest"                              $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/chest.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Eyes"                               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/eyes.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Feet"                               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/feet.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Hands"                              $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/hands.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Head"                               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/head.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Headbands"                          $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/headbands.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Neck"                               $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/neck.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Shoulders"                          $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/shoulders.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Wrists"                             $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/wrists.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Slotless"                          $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/wondrousItems/slotless.html

./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Artifacts and Other Items"          $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/artifactsAndOthers/index.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Artifacts"                          $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/artifactsAndOthers/artifacts.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Cursed Items"                       $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/artifactsAndOthers/cursedItems.html
./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Intelligent Items"                  $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/artifactsAndOthers/intelligentItems.html

./rules_parse.py -o $DATA_DIR -b "Ultimate Equipment" -t "Appendix"                           $WEB_DIR/pathfinderRPG/prd/ultimateEquipment/appendix.html

# NPC Codex
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Core Class NPCs"         $WEB_DIR/pathfinderRPG/prd/npcCodex/core/index.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Barbarian"               $WEB_DIR/pathfinderRPG/prd/npcCodex/core/barbarian.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Bard"                    $WEB_DIR/pathfinderRPG/prd/npcCodex/core/bard.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Cleric"                  $WEB_DIR/pathfinderRPG/prd/npcCodex/core/cleric.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Druid"                   $WEB_DIR/pathfinderRPG/prd/npcCodex/core/druid.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Fighter"                 $WEB_DIR/pathfinderRPG/prd/npcCodex/core/fighter.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Monk"                    $WEB_DIR/pathfinderRPG/prd/npcCodex/core/monk.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Paladin"                 $WEB_DIR/pathfinderRPG/prd/npcCodex/core/paladin.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Ranger"                  $WEB_DIR/pathfinderRPG/prd/npcCodex/core/ranger.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Rogue"                   $WEB_DIR/pathfinderRPG/prd/npcCodex/core/rogue.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Sorcerer"                $WEB_DIR/pathfinderRPG/prd/npcCodex/core/sorcerer.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Wizard"                  $WEB_DIR/pathfinderRPG/prd/npcCodex/core/wizard.html

./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Prestige Class NPCs"     $WEB_DIR/pathfinderRPG/prd/npcCodex/prestige/index.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Arcane Archer"           $WEB_DIR/pathfinderRPG/prd/npcCodex/prestige/arcaneArcher.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Arcane Trickster"        $WEB_DIR/pathfinderRPG/prd/npcCodex/prestige/arcaneTrickster.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Assassin"                $WEB_DIR/pathfinderRPG/prd/npcCodex/prestige/assassin.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Dragon Disciple"         $WEB_DIR/pathfinderRPG/prd/npcCodex/prestige/dragonDisciple.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Duelist"                 $WEB_DIR/pathfinderRPG/prd/npcCodex/prestige/duelist.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Eldritch Knight"         $WEB_DIR/pathfinderRPG/prd/npcCodex/prestige/eldritchKnight.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Loremaster"              $WEB_DIR/pathfinderRPG/prd/npcCodex/prestige/loremaster.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Mystic Theurge"          $WEB_DIR/pathfinderRPG/prd/npcCodex/prestige/mysticTheurge.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Pathfinder Chronicler"   $WEB_DIR/pathfinderRPG/prd/npcCodex/prestige/pathfinderChronicler.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Shadowdancer"            $WEB_DIR/pathfinderRPG/prd/npcCodex/prestige/shadowdancer.html

./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "NPC Class NPCs"          $WEB_DIR/pathfinderRPG/prd/npcCodex/npc/index.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Adept"                   $WEB_DIR/pathfinderRPG/prd/npcCodex/npc/adept.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Aristocrat"              $WEB_DIR/pathfinderRPG/prd/npcCodex/npc/aristocrat.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Commoner"                $WEB_DIR/pathfinderRPG/prd/npcCodex/npc/commoner.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Expert"                  $WEB_DIR/pathfinderRPG/prd/npcCodex/npc/expert.html
./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Warrior"                 $WEB_DIR/pathfinderRPG/prd/npcCodex/npc/warrior.html

#./rules_parse.py -o $DATA_DIR -b "NPC Codex" -t "Appendix"                $WEB_DIR/pathfinderRPG/prd/npcCodex/appendix.html

# Mythic Adventures
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Legendary Items" $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicItems/legendaryItems.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Artifacts"       $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicItems/artifacts.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Magic Items"     $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicItems/magicItems.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Hierophant"      $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicHeroes/hierophant.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Archmage"        $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicHeroes/archmage.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Champion"        $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicHeroes/champion.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Trickster"       $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicHeroes/trickster.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Guardian"        $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicHeroes/guardian.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Marshal"         $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicHeroes/marshal.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Mythic Items"    $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicItems.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Mythic Monsters" $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicMonsters.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Mythic Spells"   $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicSpells.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Glossary"        $WEB_DIR/pathfinderRPG/prd/mythicAdventures/Glossary.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Mythic Heroes"   $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicHeroes.html
./rules_parse.py -o $DATA_DIR -b "Mythic Adventures" -t "Mythic Game"     $WEB_DIR/pathfinderRPG/prd/mythicAdventures/mythicGame.html

# Pathfinder Campaign Setting: Technology Guide"
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Artifical Intelligence" $WEB_DIR/pathfinderRPG/prd/technologyGuide/ai.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Archtypes"       $WEB_DIR/pathfinderRPG/prd/technologyGuide/archetypes.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Armor"           $WEB_DIR/pathfinderRPG/prd/technologyGuide/armor.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Artifacts"       $WEB_DIR/pathfinderRPG/prd/technologyGuide/artifacts.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Crafting"        $WEB_DIR/pathfinderRPG/prd/technologyGuide/crafting.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Cybertech"       $WEB_DIR/pathfinderRPG/prd/technologyGuide/cybertech.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Introduction"    $WEB_DIR/pathfinderRPG/prd/technologyGuide/equipmentIntroduction.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Feats"           $WEB_DIR/pathfinderRPG/prd/technologyGuide/feats.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Gear"            $WEB_DIR/pathfinderRPG/prd/technologyGuide/gear.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Hazards"         $WEB_DIR/pathfinderRPG/prd/technologyGuide/hazards.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Pharmaceuticals" $WEB_DIR/pathfinderRPG/prd/technologyGuide/pharmaceuticals.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Skills"          $WEB_DIR/pathfinderRPG/prd/technologyGuide/skills.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Spells"          $WEB_DIR/pathfinderRPG/prd/technologyGuide/spells.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Technomancer"    $WEB_DIR/pathfinderRPG/prd/technologyGuide/technomancer.html
./rules_parse.py -o $DATA_DIR -b "Technology Guide"  -t "Weapons"         $WEB_DIR/pathfinderRPG/prd/technologyGuide/weapons.html

# Monster Codex
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Appendix"     $WEB_DIR/pathfinderRPG/prd/monsterCodex/appendix.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Boggards"     $WEB_DIR/pathfinderRPG/prd/monsterCodex/boggards.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Bugbears"     $WEB_DIR/pathfinderRPG/prd/monsterCodex/bugbears.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Drow"         $WEB_DIR/pathfinderRPG/prd/monsterCodex/drow.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Duergar"      $WEB_DIR/pathfinderRPG/prd/monsterCodex/duergar.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Fire Giants"  $WEB_DIR/pathfinderRPG/prd/monsterCodex/fireGiants.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Frost Giants" $WEB_DIR/pathfinderRPG/prd/monsterCodex/frostGiants.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Ghouls"       $WEB_DIR/pathfinderRPG/prd/monsterCodex/ghouls.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Gnolls"       $WEB_DIR/pathfinderRPG/prd/monsterCodex/gnolls.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Goblins"      $WEB_DIR/pathfinderRPG/prd/monsterCodex/goblins.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Hobgoblins"   $WEB_DIR/pathfinderRPG/prd/monsterCodex/hobgoblins.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Kobolds"      $WEB_DIR/pathfinderRPG/prd/monsterCodex/kobolds.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Lizardfolk"   $WEB_DIR/pathfinderRPG/prd/monsterCodex/lizardfolk.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Ogres"        $WEB_DIR/pathfinderRPG/prd/monsterCodex/ogres.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Orcs"         $WEB_DIR/pathfinderRPG/prd/monsterCodex/orcs.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Ratfolk"      $WEB_DIR/pathfinderRPG/prd/monsterCodex/ratfolk.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Sahuagin"     $WEB_DIR/pathfinderRPG/prd/monsterCodex/sahuagin.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Serpentfolk"  $WEB_DIR/pathfinderRPG/prd/monsterCodex/serpentfolk.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Troglodytes"  $WEB_DIR/pathfinderRPG/prd/monsterCodex/troglodytes.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Trolls"       $WEB_DIR/pathfinderRPG/prd/monsterCodex/trolls.html
./rules_parse.py -o $DATA_DIR -b "Monster Codex" -t "Vampires"     $WEB_DIR/pathfinderRPG/prd/monsterCodex/vampires.html

