print("hay nhap ")
a = list(input())
for i in range(len(a)):
    if a[i] == ".":
        a.remove(a[i])
    if a[i] == " ":
        a[i] = "-"
    if a[i] == "ư" or a[i] == "ú" or a[i] == "ù" or a[i] == "ụ" or a[i] == "ủ" or a[i] == "ũ" or a[i] == "ứ" or a[i] == "ừ" or a[i] == "ự" or a[i] == "ử" or a[i] == "ữ":
        a[i] = "u"
    if a[i] == "á" or a[i] == "à" or a[i] == "ạ" or a[i] == "ả" or a[i] == "ã" or a[i] == "ă" or a[i] == "ắ" or a[i] == "ằ" or a[i] == "ặ" or a[i] == "ẳ" or a[i] == "ẵ" or a[i] == "â" or a[i] == "ấ" or a[i] == "ầ" or a[i] == "ậ" or a[i] == "ẩ" or a[i] == "ẫ":
        a[i] = "a"
    if a[i] == "é" or a[i] == "è" or a[i] == "ẹ" or a[i] == "ẻ" or a[i] == "ẽ" or a[i] == "ê" or a[i] == "ế" or a[i] == "ề" or a[i] == "ệ" or a[i] == "ể" or a[i] == "ễ":
        a[i] = "e"
    if a[i] == "ó" or a[i] == "ò" or a[i] == "ọ" or a[i] == "ỏ" or a[i] == "õ" or a[i] == "ơ" or a[i] == "ớ" or a[i] == "ờ" or a[i] == "ợ" or a[i] == "ở" or a[i] == "ỡ" or a[i] == "ô" or a[i] == "ố" or a[i] == "ồ" or a[i] == "ộ" or a[i] == "ổ" or a[i] == "ỗ":
        a[i] = "o"
    if a[i] == "í" or a[i] =="ì" or a[i] =="ị" or a[i] =="ỉ" or a[i] =="ĩ":
        a[i] = "i"
    if a[i] == "ý" or a[i] =="ỳ" or a[i] == "ỵ" or a[i] == "ỷ" or a[i] == "ỹ":
        a[i] = "y"
    if a[i] == "đ":
        a[i] = "d"
#string to list or diff
stri = ""
stri = stri+ "''"
for i in range(len(a)):
    stri = stri + a[i]
stri = stri + "''. "
print(stri.lower())



