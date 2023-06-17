# soup.find_all(string='Fiction') #NO
# import re
# soup.find_all(string=re.compile('Fiction',re.I)) # I(IGNORECASE) - Игног регистра
# text_matches = soup.find_all(string=re.compile('Fiction',re.I))
# [text.strip() for text in text_matches]
#--------------------------------------------------------------
# all_text = list(soup.stripped_strings)
# [text for text in all_text if 'fiction' in text.lower()]
#-------------------------------------------------------------
# text_matches = soup.find_all('a',string=re.compile('Fiction',re.I)) # No
# all_text = list(soup.strings) #Навигация по тексту
# [text.parent for text in all_text if 'fiction' in text.lower() and text.parent.name == 'a']