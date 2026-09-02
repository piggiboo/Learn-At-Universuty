s1 = "Python is a powerful high-level, object-oriented programming language created by Guido van Rossum."
s2 = "It has simple easy-to-use syntax, making it the perfect language for someone trying to learn computer programming for the first time."
s3 = "Professionally, Python is great for backend web development, data analysis, artificial intelligence, and scientific computing."
Total_chr = len(s1) + len(s2) + len(s3)
print (f"Total characters in string s1, s2 and s3 are {Total_chr} characters.")
total_worlds = len(s1.split()) + len(s2.split()) + len(s3.split())
print(f"Total words in string s1, s2 and s3 are {total_worlds} words.")
i = s1[-20],s1[-3],s1[-81]
s2_clean = s2.replace(" ", "")
ii = s2_clean[44-1],s2_clean[4-1]
s3_clean = s3.replace(" ", "")
iii = s3_clean[-31],s3_clean[-9]
print (f"The secret code is {''.join(i)}{''.join(ii)}{''.join(iii)}")