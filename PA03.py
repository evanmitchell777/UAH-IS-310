"""
Author: Evan Mitchell
Date: 9/17/21
Assignment: PA03_Processing_Big_List
Semester/Year: Fall 2021
Course Number and Title: IS310-01 Adcanced Computer Programming in Business 
About the Program: This program counts the how many times a name occurs in the list given
Input: list of names
Output: list of names and how many times they appear throughout the given list 
"""
print(__doc__)

from collections import Counter

#list of names 
names= ['Rosalinda', 'Betteanne', 'Larissa', 'Ame', 'Nelli', 'Fredericka', 'Shel', 'Maryann', 'Marie-Ann', 'Alica', 'Coreen',
'Ayn', 'Larissa', 'Korrie', 'Germain', 'Sigrid', 'Sigrid', 'Lydie', 'Kandace', 'Adelle', 'Rozanna', 'Ketti', 'Sigrid', 'Georgie', 
'Druci', 'Merl', 'Maribel', 'Rania', 'Marie-Ann', 'Kally', 'Katrina', 'Ketti', 'Harri', 'Gloria', 'Lynea', 'Myrtie', 'Rozanna', 'Zilvia', 
'Bibbye', 'Roxane', 'Fionna', 'Cammy', 'Ketti', 'Coreen', 'Maribel', 'Kathye', 'Larissa', 'Harri', 'Rozanna', 'Katrine', 'Bidget', 'Erinn', 
'Ricky', 'Maryann', 'Kally', 'Norry', 'Shandeigh', 'Maribel', 'Amalie', 'Fleur', 'Donni', 'Zilvia', 'Nani', 'Myrtie', 'Jaclyn', 
'Roxane', 'Mathilda', 'Harri', 'Rey', 'Maribel', 'Rey', 'Bidget', 'Fiann', 'Emlynne', 'Coreen', 'Ketti', 'Fionna', 'Kandace', 
'Harri', 'Katrine', 'Rey', 'Mina', 'Jaclyn', 'Opal', 'Karee', 'Margarete', 'Perl', 'Janina', 'Rosamund', 'Cindie', 'Alica', 'Merl',
'Britni', 'Lynea', 'Nelli', 'Georgie', 'Marylynne', 'Katrine', 'Lynea', 'Merl', 'Kandace', 'Mina', 'Kellie', 'Rania', 'Rania', 
'Jaimie', 'Maryann', 'Erinn', 'Valina', 'Shandeigh', 'Rosalinda', 'Dayna', 'Maryann', 'Adelle', 'Jaclyn', 'Nelli', 'Rey', 'Druci',
'Cher', 'Maribel', 'Marthe', 'Jessy', 'Kandace', 'Juditha', 'Myrtie', 'Maribel', 'Wynny', 'Sharona', 'Fionna', 'Hillary', 'Trisha',
'Germain', 'Shel', 'Bibbye', 'Idalina', 'Marthe', 'Dodie', 'Katrine', 'Katrina', 'Kerrin', 'Freida', 'Harri', 'Marya', 'Shel', 'Coreen',
'Kandace', 'Stefania', 'Harri', 'Bibbye', 'Rozanna', 'Kandace', 'Alica', 'Kandace', 'Kandace', 'Maryann', 'Erinn', 'Ame', 'Wynny', 'Merl',
'Myrtie', 'Cammy', 'Doria', 'Lynea', 'Cristal', 'Roxane', 'Bibbye', 'Jamima', 'Maryann', 'Myrtie', 'Sigrid', 'Merline', 'Merl', 'Janet',
'Lynea', 'Nani', 'Maryann', 'Giulia', 'Kandace', 'Lynea', 'Kandace', 'Rosalinda', 'Kala', 'Freida', 'Harri', 'Ayn', 'Merl', 'Maribel',
'Maryann', 'Merl', 'Kandace', 'Kerrin', 'Kally', 'Charmian', 'Fionna', 'Cristal', 'Kandace', 'Rozanna', 'Ketti', 'Shel', 'Bidget', 
'Lynea', 'Merl', 'Germain', 'Emmy', 'Lynea', 'Katrine', 'Fionna', 'Gloria', 'Rey', 'Kathye', 'Jaimie', 'Rozanna', 'Jazmin', 'Rosalinda', 
'Maribel', 'Dayna', 'Shel', 'Korrie', 'Bidget', 'Adriena', 'Sharona', 'Marya', 'Zilvia', 'Katrine', 'Rozanna', 'Harri', 'Sigrid', 'Marie-Ann',
'Jillayne', 'Aimil', 'Germain', 'Donni', 'Jordana', 'Fleur', 'Germain', 'Kerrin', 'Emlynne', 'Lydie', 'Korrie', 'Jazmin', 'Kathye', 'Fancie',
'Nelli', 'Rey', 'Emmy', 'Sigrid', 'Maribel', 'Dodie', 'Myrtie', 'Fredericka', 'Druci', 'Wynny', 'Maryann', 'Janina', 'Freida', 'Bambi', 'Jaimie',
'Sigrid', 'Fleur', 'Rebecka', 'Fanya', 'Maryann', 'Kala', 'Shel', 'Maribel', 'Coreen', 'Rania', 'Juditha', 'Norry', 'Kerrin', 'Trisha', 'Shandeigh',
'Cammy', 'Vin', 'Shel', 'Olympe', 'Opal', 'Kandace', 'Maribel', 'Ebonee', 'Roxane', 'Deana', 'Stefania', 'Sigrid', 'Marylynne', 'Rania', 'Raynell', 
'Farah', 'Myrtie', 'Faydra', 'Shel', 'Adelle', 'Scarlett', 'Nelli', 'Flor', 'Myrtie', 'Olympe', 'Vin', 'Ketti', 'Emlynne', 'Norry', 'Rebeka', 'Kathye',
'Rania', 'Gloria', 'Rozanna', 'Rozanna', 'Amalie', 'Drucie', 'Aimil', 'Sigrid', 'Maude', 'Emmy', 'Idalina', 'Georgie', 'Larissa', 'Janella', 'Kathye',
'Margarete', 'Myrtie', 'Sharona', 'Kala', 'Myrtie', 'Georgie', 'Claretta', 'Mina', 'Zilvia', 'Roxane', 'Adelle', 'Kellie', 'Rozanna', 'Jillayne', 
'Ingaborg', 'Myrtie', 'Maribel', 'Maryann', 'Jazmin', 'Amalie', 'Merl', 'Idalina', 'Rozanna', 'Amalie', 'Fiann', 'Raynell', 'Fionna', 'Maribel', 'Flor',
'Bidget', 'Coreen', 'Kandace', 'Adelle', 'Flor', 'Fancie', 'Myrtie', 'Alia', 'Freida', 'Cindie', 'Harri', 'Rey', 'Jaclyn', 'Maryann', 'Rozanna', 'Valina', 
'Valina', 'Natalee', 'Kandace', 'Fionna', 'Harri', 'Maryann', 'Dodie', 'Edy', 'Gloria', 'Perl', 'Lynea', 'Emmy', 'Maribel', 'Olympe', 'Malia', 'Faydra', 'Merline',
'Doria', 'Juditha', 'Gloria', 'Aimil', 'Izabel', 'Tamara', 'Trisha', 'Norry', 'Debbie', 'Adelle', 'Malia', 'Erinn', 'Marthe', 'Trisha', 'Maryann',
'Kandace', 'Trisha', 'Ame', 'Merl', 'Farah', 'Dodie', 'Rey', 'Lynea', 'Merl', 'Rosalinda', 'Harri', 'Fedora', 'Bidget', 'Audrie', 'Katrine', 'Sigrid',
'Jamima', 'Marsha', 'Alia', 'Germain', 'Rozanna', 'Ebonee', 'Doria', 'Janina', 'Janet', 'Amalie', 'Farah', 'Maribel', 'Flor', 'Valina', 'Kandace',
'Gretal', 'Maryann', 'Germain', 'Kerrin', 'Jaimie', 'Bidget', 'Cariotta', 'Bidget', 'Sigrid', 'Idalina', 'Taryn', 'Juditha', 'Gloria', 'Flor', 'Aimil',
'Nelli', 'Amalie', 'Ricky', 'Lynea', 'Merline', 'Lynea', 'Drucie', 'Fanya', 'Fiann', 'Karee', 'Ricky', 'Kandace', 'Ricky', 'Bibbye', 'Freida', 'Erinn', 'Merl',
'Georgie', 'Cristal', 'Jaimie', 'Bibbye', 'Sigrid', 'Maribel', 'Marie-Ann', 'Germain', 'Rozanna', 'Teddie', 'Emlynne', 'Adelle', 'Kala', 'Olympe', 'Flor', 'Malia',
'Sigrid', 'Rozanna', 'Maribel', 'Cariotta', 'Dodie', 'Emmy', 'Bibbye', 'Trisha', 'Doria', 'Maribel', 'Kandace', 'Lynea', 'Rey', 'Myrtie', 'Bidget', 'Kathye', 'Drucie', 'Maribel',
'Zilvia', 'Myrtie', 'Farah', 'Merl', 'Juditha', 'Merl', 'Maudie', 'Amalie', 'Farah', 'Zilvia', 'Fiann', 'Germain', 'Giulia', 'Margarete', 'Rozanna', 'Ketti', 'Sigrid', 'Dodie',
'Erinn', 'Harri', 'Rosalinda', 'Kandace', 'Emlynne', 'Sigrid', 'Harri', 'Kellie', 'Ingaborg', 'Gloria', 'Betteanne', 'Flor', 'Rozanna', 'Janella', 'Ame', 'Nelli', 'Stefania',
'Roxane', 'Harri', 'Sigrid', 'Maribel', 'Tootsie', 'Nani', 'Bidget', 'Maribel', 'Cher', 'Coreen', 'Lydie', 'Debera', 'Georgie', 'Fionna', 'Marylynne', 'Erinn', 'Ricky', 'Aline',
'Audrie', 'Kandace', 'Jaimie', 'Maryann', 'Ketti', 'Jaclyn', 'Emlynne', 'Marthe', 'Kellie', 'Fancie', 'Marsha', 'Emeline', 'Shandeigh', 'Audrie', 'Marya', 'Rania', 'Margarete',
'Faydra', 'Karee', 'Myrtie', 'Aimil', 'Jaclyn', 'Fleur', 'Brigid', 'Fiann', 'Aubrie', 'Amalie', 'Trisha', 'Harri', 'Nelli', 'Ketti', 'Emmy', 'Maudie', 'Korrie', 'Fedora', 
'Aubrie', 'Lydie', 'Kerrin', 'Jazmin', 'Adelle', 'Shandeigh', 'Lynea', 'Bidget', 'Cariotta', 'Zilvia', 'Kerrin', 'Rosamund', 'Ame', 'Olympe', 'Olympe', 'Kala', 'Maryann', 
'Valina', 'Merline', 'Lynea', 'Roxane', 'Rey', 'Rozanna', 'Marylynne', 'Ketti', 'Idalina', 'Dodie', 'Harri', 'Rey', 'Rozanna', 'Merline', 'Erinn', 'Fionna', 'Marylynne',
'Germain', 'Marylynne', 'Hanna', 'Drucie', 'Maribel', 'Kandace', 'Frederique', 'Jillayne', 'Rey', 'Edy', 'Alica', 'Auroora', 'Harri', 'Pammi', 'Gloria', 'Marylynne', 'Kathlin',
'Freida', 'Gilligan', 'Izabel', 'Rania', 'Freida', 'Adelle', 'Katrine', 'Myrtie', 'Brunhilda', 'Olympe', 'Teressa', 'Amalie', 'Sigrid', 'Trisha', 'Auroora', 'Marylynne',
'Aline', 'Flor', 'Erinn', 'Maribel', 'Jazmin', 'Maryann', 'Taryn', 'Scarlett', 'Marie-Ann', 'Aline', 'Amalie', 'Bidget', 'Stefania', 'Valina', 'Harri', 'Aimil', 'Pammi',
'Coreen', 'Katrine', 'Feodora', 'Cindie', 'Emlynne', 'Shaun', 'Shay', 'Germain', 'Rozanna', 'Margarete', 'Kerrin', 'Maribel', 'Malia', 'Bidget', 'Juditha', 'Trisha',
'Cristal', 'Ketti', 'Lynea', 'Amalie', 'Ayn', 'Kandace', 'Olympe', 'Trisha', 'Karee', 'Sigrid', 'Rozanna', 'Aimil', 'Sigrid', 'Lynea', 'Ame', 'Rey', 'Ketti', 'Maudie',
'Fredericka', 'Merl', 'Kerrin', 'Fiann', 'Ketti', 'Dayna', 'Marie-Ann', 'Fedora', 'Giulia', 'Lydie', 'Faydra', 'Chiquia', 'Trisha', 'Kerrin', 'Erinn', 'Kally', 'Vin',
'Rosamund', 'Myrtie', 'Dodie', 'Margarete', 'Laureen', 'Jamima', 'Harri', 'Rey', 'Debbie', 'Kala', 'Rey', 'Moria', 'Bidget', 'Coreen', 'Harri', 'Chiquia', 'Germain',
'Maribel', 'Kally', 'Kathye', 'Aline', 'Erinn', 'Ayn', 'Janina', 'Lynea', 'Kally', 'Cariotta', 'Feodora', 'Janet', 'Rosamund', 'Shandeigh', 'Faydra', 'Opal', 'Georgie',
'Giulia', 'Rozanna', 'Kerrin', 'Harri', 'Fedora', 'Ora', 'Sigrid', 'Shandeigh', 'Aura', 'Bidget', 'Cindie', 'Fleur', 'Bidget', 'Karee', 'Faydra', 'Rosalinda', 'Ebonee',
'Izabel', 'Hanna', 'Amalie', 'Malia', 'Gloria', 'Taryn', 'Giulia', 'Gretal', 'Hanna', 'Donni', 'Karee', 'Erinn', 'Perl', 'Alia', 'Scarlett', 'Fionna', 'Lydie', 'Myrtie',
'Robin', 'Janet', 'Ayn', 'Bambi', 'Idalina', 'Pammi', 'Rania', 'Scarlett', 'Cristal', 'Trisha', 'Drucie', 'Wilhelmina', 'Bidget', 'Korrie', 'Erinn', 'Fiann', 'Harri', 'Freida',
'Harri', 'Kally', 'Bidget', 'Olympe', 'Faina', 'Cammy', 'Bidget', 'Faydra', 'Rey', 'Fleur', 'Jaimie', 'Bambi', 'Erinn', 'Maribel', 'Kathye', 'Amalie', 'Bibbye', 'Brigid', 
'Stefania', 'Marie-Ann', 'Ricky', 'Mina', 'Valina', 'Bibbye', 'Adelle', 'Margarete', 'Prudence', 'Coreen', 'Marie-Ann', 'Ketti', 'Adelle', 'Wynny', 'Kathye', 'Bethany', 
'Georgie', 'Dodie', 'Rozanna', 'Frederique', 'Marylynne', 'Gretal', 'Maryann', 'Germain', 'Katrine', 'Aline', 'Fionna', 'Olympe', 'Zilvia', 'Nelli', 'Myrtie', 'Cristal',
'Gloria', 'Jaynell', 'Marya', 'Maribel', 'Jenelle', 'Giulia', 'Marie-Ann', 'Aline', 'Marsha', 'Auroora', 'Germain', 'Olympe', 'Sela', 'Marylynne', 'Maryann', 'Betteanne', 
'Raynell', 'Dora', 'Ketti', 'Maryann', 'Janella', 'Emmy', 'Debbie', 'Maryann', 'Adelle', 'Harri', 'Rania', 'Kala', 'Bidget', 'Zilvia', 'Coreen', 'Kailey', 'Wilhelmina', 'Doria', 
'Fedora', 'Lanni', 'Emlynne', 'Valina', 'Marie-Ann', 'Georgie', 'Marthe', 'Aline', 'Perl', 'Marie-Ann', 'Jordana', 'Amalie', 'Farah', 'Marie-Ann', 'Maribel', 'Germain', 'Harri', 
'Aline', 'Ricky', 'Deana', 
'Emeline', 'Kandace', 'Laureen', 'Fionna', 'Debbi', 'Maryann', 'Malia', 'Katrina', 'Rozanna', 'Malia', 'Fleur', 'Lydie', 'Dora', 'Brigid', 'Valina', 'Marie-Ann', 'Jazmin', 'Hanna',
'Rebecka', 'Flor', 'Merl', 'Cher', 'Audrie', 'Ariadne', 'Harri', 'Marya', 'Harri', 'Debera', 'Jenelle', 'Olympe', 'Merline', 'Denny', 'Harri', 'Jaine', 'Aura', 'Margareta',
'Rozanna', 'Doria', 'Rozanna', 'Rozanna', 'Ebonee', 'Maribel', 'Ayn', 'Maryann', 'Rey', 'Janet', 'Rozanna', 'Fionna', 'Rozanna', 'Nelli', 'Emmy', 'Ettie', 'Robin', 'Shandeigh', 
'Thomasina', 'Adelle', 'Maribel', 'Fredericka', 'Roseline', 'Nani', 'Katrine', 'Aline', 'Gloria', 'Olympe', 'Ariadne', 'Brigid', 'Trisha', 'Shandeigh', 'Maribel', 'Shay',
'Jenelle', 'Trisha', 'Trisha', 'Stefania', 'Kally', 'Jenelle', 'Adelle', 'Olenka', 'Danell', 'Harri', 'Kore', 'Kellie', 'Beatrice', 'Cristal', 'Doria', 'Shay', 'Roseline', 
'Maribel', 'Bidget', 'Zilvia', 'Marya', 'Fedora', 'Harri', 'Ketti', 'Betteanne', 'Jillayne', 'Kandace', 'Mina', 'Coreen', 'Kathlin', 'Idalina', 'Bidget', 'Kellie', 'Blaire',
'Erinn', 'Ketti', 'Trisha', 'Drucie', 'Taryn', 'Odille', 'Alica', 'Maryann', 'Kally', 'Jazmin', 'Amalie', 'Kailey', 'Tootsie', 'Wilhelmina', 'Olympe', 'Marylynne', 'Perl', 
'Emmey', 'Giulia', 'Coreen', 'Charmian', 'Ali', 'Margareta', 'Coreen', 'Korrie', 'Rosalinda', 'Brigid', 'Rania', 'Erinn', 'Calypso', 'Marthe', 'Rosalinda', 'Rebecka', 'Cher',
'Scarlett', 'Pammi', 'Shandeigh', 'Beatrice', 'Dora', 'Trisha', 'Ketti', 'Teressa', 'Maude', 'Janina', 'Lydie', 'Cindie', 'Bambi', 'Germain', 'Agretha', 'Jessy', 'Lydie', 
'Bride', 'Ricky', 'Ola',
'Bride', 'Fanya', 'Jazmin', 'Marya', 'Germain', 'Tamara', 'Aimil', 'Nani', 'Merl', 'Nanice', 'Frederique', 'Lydie', 'Adriena', 'Fionna', 'Conchita', 'Kandace', 'Olympe', 
'Rania', 'Margareta', 'Nani', 'Giulia', 'Uta', 'Dodie', 'Ora', 'Opal', 'Stefania', 'Kellie', 'Deana', 'Janella', 'Janina', 'Marylynne', 'Neely', 'Merl', 'Maud', 'Maribel', 
'Kellie', 'Debera', 'Farah', 'Adelle', 'Cindie', 'Kathlin', 'Kandace', 'Lauretta', 'Debbi', 'Rebeka', 'Rania', 'Kally', 'Teressa', 'Erinn', 'Kore', 'Kandace', 'Stefania',
'Drucie', 'Debera', 'Giulia', 'Maudie', 'Auroora', 'Charmian', 'Maryann', 'Germain', 'Mina', 'Rozanna', 'Flor', 'Ebonee', 'Marsha', 'Aila', 'Marylynne', 'Auroora', 'Dora', 
'Olympe', 'Natalee', 'Laureen', 'Fionna', 'Odille', 'Merl', 'Trisha', 'Amalie', 'Debera', 'Ketti', 'Ariadne', 'Rey', 'Aimil', 'Giulia', 'Teressa', 'Rori', 'Aline', 'Isabel',
'Kellie', 'Marie-Ann', 'Janina', 'Cristal', 'Jazmin', 'Juditha', 'Bibbye', 'Malia', 'Kellie', 'Charisse', 'Gnni', 'Rozanna', 'Charisse', 'Sela', 'Deana', 'Rozanna', 'Janina',
'Rosamund', 'Debbie', 'Ashlan', 'Larissa', 'Debera', 'Fredericka', 'Bethany', 'Faydra', 'Trisha', 'Madlin', 'Rori', 'Sashenka', 'Emmy', 'Debera', 'Janella', 'Marie-Ann',
'Natalee', 'Nickie', 'Ayn', 'Charmian', 'Malia', 'Trisha', 'Alica', 'Belinda', 'Norry', 'Winifred', 'Cristal', 'Rebeka', 'Ayn', 'Vittoria', 'Aline', 'Debbie', 'Bethany', 
'Charisse', 'Rozanna', 'Opal', 'Adan', 'Rey', 'Adriena', 'Rania', 'Rebeka', 'Kellie', 'Gilligan', 'Margareta', 'Tamara', 'Kathlin', 'Jazmin', 'Debbie', 'Fleur', 'Fredericka',
'Vittoria', 'Bidget', 'Lydie', 'Ettie', 'Stefania', 'Olenka', 'Ricky', 'Winifred', 'Fionna', 'Auroora', 'Shaun', 'Prudence', 'Charmian', 'Malia', 'Jessy', 'Merl', 'Edy', 
'Valina', 'Nani', 'Cher', 'Ketti',
'Stacee', 'Marys', 'Ketti', 'Ettie', 'Bidget', 'Shel', 'Aila', 'Danell', 'Katrine', 'Kerrin', 'Kaja', 'Terra', 'Coreen', 'Aline', 'Rosamund', 'Ariadne', 'Aimil', 'Janella',
'Charisse', 'Ricky', 'Kaja', 'Deana', 'Calypso', 'Wilhelmina', 'Rori', 'Malia', 'Debera', 'Nanice', 'Tracie', 'Wynny', 'Perl', 'Eulalie', 'Shel', 'Rosene', 'Lydie', 'Jaynell', 
'Stefania', 'Tootsie', 'Jazmin', 'Michaeline', 'Bethany', 'Maudie', 'Fawnia', 'Winifred', 'Belinda', 'Fedora', 'Brigid', 'Amalie', 'Helge', 'Jaimie', 'Coreen', 'Rosamund',
'Lucilia', 'Olympe', 'Jo-Anne', 'Harri', 'Harri', 'Amalie', 'Bethany', 'Alica', 'Rozanna', 'Sela', 'Deana', 'Sigrid', 'Teddie', 'Shel', 'Adelle', 'Uta', 'Emmey', 'Rebecka',
'Fancie', 'Doria', 'Charmian', 'Kandace', 'Cammy', 'Marys', 'Lisbeth', 'Dodie', 'Rori', 'Marie-Ann', 'Lotta', 'Uta', 'Teddie', 'Freida', 'Devinne', 'Margarete', 'Chiquia',
'Rosalinda', 'Zilvia', 'Jazmin', 'Bride', 'Sharai', 'Janina', 'Cariotta', 'Marylynne', 'Ariadne', 'Agathe', 'Merline', 'Laureen', 'Lotta', 'Ora', 'Fionna', 'Brunhilda', 
'Laureen', 'Vally', 'Kailey', 'Trisha', 'Rori', 'Kathye', 'Lydie', 'Laureen', 'Sela', 'Kandace', 'Frederique', 'Calypso', 'Fredericka', 'Edy', 'Marys', 'Bethany', 'Aubrie', 
'Lydie', 'Danell', 'Stacee', 'Adelle', 'Marylynne', 'Merl', 'Giulia', 'Zilvia', 'Marylynne', 'Hanna', 'Ashlan', 'Zilvia', 'Germain', 'Auroora', 'Teressa', 'Debera',
'Jillayne', 'Shel', 'Feodora', 'Lynea', 'Leandra', 'Marys', 'Flor', 'Hanna', 'Ayn', 'Valina', 'Charmian', 'Rozanna', 'Wynny',
'Erinn', 'Marya', 'Isabelle', 'Janina', 'Farah', 'Eilis', 'Jonell', 'Rey', 'Korrie', 'Rosamund', 'Germain', 'Margareta', 'Elyssa', 'Rebecca', 'Katrine', 'Jamima', 'Allx', 
'Rey', 'Marie-Ann', 'Conchita', 'Kathlin', 'Adelle', 'Olympe', 'Rosamund', 'Danell', 'Lynea', 'Ebonee', 'Kala', 'Rania', 'Kaila', 'Debbie', 'Elinor', 'Tillie', 'Marya', 
'Charmian', 'Sheeree', 'Valina', 'Farah', 'Gilli', 'Neely', 'Rey', 'Drucie', 'Druci', 'Rey', 'Maryann', 'Cariotta', 'Kellie', 'Shel', 'Alejandrina', 'Marie-Ann', 'Goldia',
'Bethany', 'Olympe', 'Olympe', 'Janella', 'Teressa', 'Opal', 'Erena', 'Daisi', 'Erena', 'Sidoney', 'Teressa', 'Rosalinda', 'Casandra', 'Madlin', 'Trisha', 'Nani', 'Kathlin', 
'Kore', 'Janina', 'Sibylle', 'Lydie', 'Cora', 'Mina', 'Fionna', 'Amalie', 'Honoria', 'Wilhelmina', 'Aila', 'Constanta', 'Doria', 'Gayel', 'Allx', 'Wynny', 'Sibylle', 'Fleur',
'Teddie', 'Margarete', 'Harri', 'Gerladina', 'Bobbee', 'Rozanna', 'Maryann', 'Rozanna', 'Kore', 'Nanice', 'Melisse', 'Tracie', 'Ola', 'Janella', 'Kathye', 'Gilda', 'Latisha',
'Kelcey', 'Madlin', 'Calypso', 'Debera', 'Ethelind', 'Ayn', 'Winifred', 'Babita', 'Sabra', 'Bibbye', 'Britni', 'Odille', 'Cariotta', 'Maryann', 'Ketti', 'Maud', 'Fiann', 
'Philomena', 'Jeannie', 'Shay', 'Jamima', 'Rozanna', 'Olympe', 'Terra', 'Irina', 'Auroora', 'Bidget', 'Janina', 'Caritta', 'Hillary', 'Gilda', 'Emeline', 'Joann', 'Bidget',
'Trixi', 'Perl', 'Jaclin', 'Tillie', 'Ali', 'Norry', 'Fanya', 'Hanna', 'Lurline', 'Emmy', 'Uta', 'Debi', 'Marys', 'Beryle', 'Harri', 'Winifred', 'Rania', 'Gilligan', 'Erinn', 
'Drucie', 'Debi', 'Maryann', 'Druci', 'Britni', 'Amalie', 'Doria', 'Fionna', 'Marylynne', 'Cariotta', 'Fanni', 'Beryle', 'Cindie', 'Jodee', 'Kaycee', 'Frederique', 'Alida', 
'Thomasina', 'Nani', 'Ann', 'Naoma', 'Marys', 'Tori', 'Debra', 'Bidget', 'Emlynne', 'Irina', 'Ayn', 'Debera', 'Ann', 'Violet', 'Ebonee', 'Emlynne', 'Karlyn', 'Perl', 'Alida', 
'Jackqueline', 'Flori', 'Berenice', 'Mina', 'Mina', 'Dodie', 'Nanice', 'Chryste', 'Dorolisa', 'Debbie', 'Jo-Anne', 'Carree', 'Gerladina', 'Bidget', 'Mina', 'Dodie', 'Adriena',
'Paola', 'Jasmine', 'Hillary', 'Malia', 'Jannelle', 'Brunhilda', 'Amalie', 'Olympe', 'Faina', 'Agretha', 'Indira', 'Marcie', 'Fedora', 'Selia', 'Ariadne', 'Elinor', 'Demeter',
'Auroora', 'Sisely', 'Olenka', 'Petronia', 'Randee', 'Hillary', 'Aeriel', 'Celene', 'Chryste', 'Lanni', 'Gnni', 'Agnesse', 'Emlynne', 'Calypso', 'Lonee', 'Jazmin', 'Randee', 
'Faydra', 'Adelle', 'Terri', 'Ashlan', 'Sheilah', 'Deana', 'Charisse', 'Roseline', 'Hildegarde', 'Charmian', 'Shelli', 'Hildegarde', 'Ali', 'Natalee', 'Aimil', 'Harriot', 
'Lindsay', 'Jordana', 'Freida', 'Jessamyn', 'Moria', 'Babita', 'Natalee', 'Theresa', 'Addy', 'Fancie', 'Sandi', 'Debera', 'Opal', 'Hildegarde', 'Hildegarde', 'Kaila', 'Hillary',
'Rebeca', 'Alejandrina', 'Olympe', 'Berni', 'Daisie', 'Ebonee', 'Katrina', 'Liva', 'Sela', 'Kaja', 'Larina', 'Ettie', 'Krystyna', 'Marta', 'Jackqueline', 'Sibelle', 'Melisse', 
'Guillemette', 'Kathlin', 'Lucilia', 'Miriam', 'Ingunna', 'Tracie', 'Myrtie', 'Angel', 'Bride', 'Ann-Marie', 'Merline', 'Madella', 'Terri', 'Cristen', 'Cristal', 'Sharai',
'Lauretta', 'Harriot', 'Jaimie', 'Alia', 'Dorolisa', 'Wilhelmina', 'Janella', 'Claretta', 'Ermentrude', 'Kathlin', 'Gusty', 'Allina', 'Beryle', 'Britni', 'Gail', 'Demeter', 'Gusty', 'Alica',
'Peggy', 'Eustacia', 'Alejandrina', 'Kathlin', 'Shelli', 'Lucilia', 'Timmi', 'Camel', 'Teressa', 'Jeannie', 'Rebeca', 'Emmy', 'Arlina', 'Marie-Ann', 'Rey', 'Barrie', 'Brunhilda',
'Aleta', 'Nicoli', 'Trisha', 'Belicia', 'Charisse', 'Hillary', 'Odille', 'Lotti', 'Irina', 'Uta', 'Claudine', 'Dora', 'Georgena', 'Goldia', 'Lynea', 'Helene', 'Celene', 'Henryetta', 'Dolly', 
'Steffie', 'Davita', 'Melodee', 'Ebonee', 'Karleen', 'Drucie', 'Debera', 'Blondie', 'Rori', 'Bambi', 'Crin', 'Mary', 'Allene', 'Winifred', 'Kay', 'Myrtie', 'Emmey', 'Madella', 'Alice', 'Kailey', 'Philomena', 'Wenonah', 'Marya', 'Lanie', 'Agnesse',
'Carri', 'Jaimie', 'Isabel', 'Eustacia', 'Augusta', 'Debra', 'Agretha', 'Kaila', 'Monah', 'Kerrin', 'Chryste', 'Karlotte', 'Kathye', 'Meris', 'Jess', 'Jenine', 'Janella', 'Dedra', 'Louella', 'Ertha', 'Ronny', 'Rozanna', 'Wendie', 'Atlanta', 'Aleta', 'Ted', 'Lucilia', 'Krystle', 'Ingunna', 'Fayth', 'Erminie', 'Dulcinea', 'Ilyse', 'Fawnia', 'Violet', 'Jeanette', 'Miguela', 'Jaimie', 'Silvia', 'Fawnia', 
'Ettie', 'Adel', 'Sandye', 'Colline', 'Athene', 'Cariotta', 'Linda', 'Madella', 
'Jodee', 'Ruby', 'Ianthe', 'Marianna', 'Krystle', 'Chryste', 'Frederique', 'Misty', 'Celestyna', 'Lurline', 'Concettina', 'Pammy', 'Odille', 'Sidoney', 'Dedie', 'Kassia', 'Brit', 'Agretha', 'Druci', 'Kellie', 'Sybyl', 'Casandra', 'Gerrie', 'Latashia', 'Chloris', 'Veronika', 'Lonee', 'Claretta', 'Marchelle', 'Emmalee', 'Hephzibah', 'Lenette', 'Laureen', 'Amata', 'Agathe', 'Sela', 'Trula', 'Laurel', 'Ronda', 'Vera', 'Nancy', 'Sharia', 'Nanice', 'Aleta', 'Emeline', 'Anthea', 'Kali', 
'Koo', 'Cindie', 'Gayel', 'Davita', 'Godiva', 'Berthe', 'Gwenny', 'Chelsea', 'Teressa', 'Lucilia', 'Madella', 'Shalna', 'Tilda', 'Suellen', 'Ebonee', 'Adrian', 'Manda', 'Bethany', 'Ted', 'Rora', 'Billy', 'Sandi', 'Rosemonde', 'Dollie', 'Shaun', 'Jemimah', 'Judie', 'Bernette', 'Valina', 'Kristan', 'Hedi', 'Kai', 'Sukey', 'Juliette', 'Carri', 'Marilee', 'Inna', 'Athene', 'Rozina', 'Dorolisa', 'Dorita', 'Kristyn', 'Esmaria', 'Vikky', 'Fionna', 'Ann-Marie', 'Marilyn', 'Gabriell', 'Sheilah', 'Brooke',
'Manda', 'Ethelyn', 'Odelinda', 'Perrine', 'Jacquetta', 'Kimberli', 'Ruthie', 'Lura', 'Randa', 'Del', 'Celestyn', 'Isahella', 'Penelope', 'Dona', 'Abagail', 'Cathy', 'Georgie', 'Brande', 'Karil', 'Kellie', 'Nichole', 'Laura', 'Rey', 'Electra', 'Sheila', 'Hortensia', 'Auroora', 'Aggi', 'Minny', 'Rozalin', 'Matelda', 'Corina', 'Luisa', 'Chiarra', 'Ericka', 'Nert',
'Brittaney', 'Rivi', 'Nanny', 'Sabine', 'Dorie', 'Bessy', 'Audry', 'Charisse', 'Nadia', 'Pen', 'Lanny', 'Emilee', 'Philippe', 'Rici', 'Cleo', 'Prue', 'Brietta', 'Marney', 'Audrey', 'Lexine', 'Nariko', 'Gratia', 'Bren', 'Kasey', 'Darryl', 'Jacquelynn', 'Fianna', 'Vivianna', 'Lanette', 'Rena', 'Lia', 'Lillian', 'Ainsley', 'Liesa', 'Madelina', 'Tallou']



#counts names in a list 

output_list = []
tested_names = []
#Checks through names 
for i,name in enumerate(names):
    occurance = 0
#makes sure name has not been tested 
    if name not in tested_names:
        tested_names.append(name)
        for i,testname in enumerate(names):
            if name == testname:
                occurance += 1 
            else:
                pass
        output_list.append([name,occurance])
    else:
        pass
    
    

 #prints and formats the list
for name_instance in sorted(output_list):
    print("{0}: {1}".format(name_instance[0],name_instance[1]))

