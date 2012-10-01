for i in `grep -l " <\/i>" *` ; do sed -i 's/ <\/i>/<\/i> /g' $i ; done
for i in `grep -l "<i>;<\/i>" *` ; do sed -i 's/<i>;<\/i>/;/g' $i ; done
for i in `grep -l ";<\/i>" *` ; do sed -i 's/;<\/i>/<\/i>;/g' $i ; done
for i in `grep -l "<i>\.<\/i>" *` ; do sed -i 's/<i>\.<\/i>/\./g' $i ; done
for i in `grep -l "\.<\/i>" *` ; do sed -i 's/\.<\/i>/<\/i>\./g' $i ; done
for i in `grep -l "\,<\/i>" *` ; do sed -i 's/\,<\/i>/<\/i>\,/g' $i ; done
for i in `grep -l "[a-z]<\/i>[A-Z]" *` ; do sed -i 's/\([a-z]\)<\/i>\([A-Z]\)/\1<\/i>: \2/g' $i ; done

