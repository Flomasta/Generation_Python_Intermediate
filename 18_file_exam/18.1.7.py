translate_dict = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
    'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch',
    'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*',
    'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je',
    'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya',
}

with open('../txt_files_for_part_files_and_files_exam/cyrillic.txt', 'r', encoding='utf-8') as file:
    lst = []
    for i in list(file.read()):
        if translate_dict.get(i):
            lst.append(translate_dict[i])
        else:
            lst.append(i)
    txt = ''.join(lst)
with open('../txt_files_for_part_files_and_files_exam/transliteration.txt', 'w', encoding='utf-8') as transliteration:
    transliteration.write(txt)

# Транслитерация 🌶️
# Транслитерация — передача знаков одной письменности знаками другой письменности, при которой каждый знак (или последовательность знаков) одной системы письма передаётся соответствующим знаком (или последовательностью знаков) другой системы письма.
#
# Вам доступен текстовый файл cyrillic.txt, содержащий текст. Напишите программу для транслитерации этого файла, то есть замены кириллических символов на латинские в соответствии с предложенной таблицей. Все остальные символы надо оставить без изменений. Результат транслитерации требуется записать в файл transliteration.txt.
#
# Кириллица 	Латиница	Кириллица	Латиница	Кириллица	Латиница
# а	a	к	k	х	h
# б	b	л	l	ц	c
# в	v	м	m	ч	ch
# г	g	н	n	ш	sh
# д	d	о	o	щ	shh
# е	e	п	p	ъ	*
# ё	jo	р	r	ы	y
# ж	zh	с	s	ь	'


# з	z	т	t	э	je
# и	i	у	u	ю	ju
# й	j	ф	f	я	ya
# Формат входных данных
# На вход программе ничего не подается.
#
# Формат выходных данных
# Программа должна создать файл с именем transliteration.txt в соответствии с условием задачи.
#
# Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
#
# Примечание 2. Обратите внимание, что заглавные буквы должны заменяться на соответствующие им заглавные же буквы, но если транслитерационная последовательность состоит из нескольких символов, то заглавным будет только первый из них: «С» на «S», а «Я» на «Ya».
#
# Примечание 3. Если бы файл cyrillic.txt содержал текст:
#
# Президент США Дональд Трамп продолжил обмен выпадами с руководством КНДР.
# We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to help him: they don’t want the truth to be exposed.
# то содержимое файла transliteration.txt будет:
#
# Prezident SShA Donal'd Tramp prodolzhil obmen vypadami s rukovodstvom KNDR.
# We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to help him: they don’t want the truth to be exposed.
# Примечание 4. Указанный файл можно скачать по ссылке.
