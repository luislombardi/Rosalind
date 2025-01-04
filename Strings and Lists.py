'''
Problem
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. 
In other words, we should include elements s[b] and s[d] in our slice.

Sample Dataset
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102
'''
with open("C:\\Users\\Usuario\\Downloads\\rosalind_ini3.txt") as infile:
    st1 = infile.readline().strip()  # Lee la primera línea y elimina los espacios en blanco
    st2 = infile.readline().strip().split()  # Lee la segunda línea, elimina espacios y divide

a, b, c, d = map(int, st2)  # Convierte los valores a enteros
print(st1[a:b+1], st1[c:d+1])


