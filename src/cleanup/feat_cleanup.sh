for i in `grep -l ' class=\\"stat-block-1\\"' *` ; do sed -i 's
/ class=\\"stat-block-1\\"//g' $i ; done
