accented_string = u'Málaga'
# accented_string is of type 'unicode'
import unidecode
unaccented_string = unidecode.unidecode(accented_string)

print(unaccented_string)