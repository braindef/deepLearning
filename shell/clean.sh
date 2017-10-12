

cat $1 | tr [:upper:] [:lower:] | sed 's/[^a-zA-Z0-9]/ /g' | tr '\n' ' ' | sed -e 's/  / /g'   | sed -e 's/  / /g'  | sed -e 's/  / /g'  | sed -e 's/  / /g' 
