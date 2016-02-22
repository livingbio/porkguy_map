# def csv_from_excel(fileName):
#     wb = xlrd.open_workbook(fileName)
#     sh = wb.sheet_by_index(0)
#     your_csv_file = open(fileName.replace(".xls",".csv"), 'wb')
#     wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
#     for rownum in xrange(sh.nrows):
#         wr.writerow([unicode(entry).encode("utf-8") for entry in sh.row_values(rownum)])
#     your_csv_file.close()
#     with open(fileName.replace(".xls",".csv"), 'rb') as f:
# 		data = csv.reader(f, delimiter=' ', quotechar='|')
#     return data

# # 103公益彩券回饋金計畫審核結果
# # 各縣市在不同檔案中
# # 0 編號
# # 1 社福機構
# # 5 審查結果
# # 7 核定內容
# import xlrd
# wb = xlrd.open_workbook('103(縣市).xls')
# sh = wb.sheet_by_index(0)
# for r in range(5,sh.nrows) :
# 	for c in [0,1] :
# 		print sh.cell(r,c).value.encode(encoding="cp950",errors="ignore"),"|",
# 	print sh.cell(r,5).value,"|"
# 	print sh.cell(r,7).value.encode(encoding="cp950",errors="ignore"),"|",
# 	print r

# # 102 公益彩券回饋金計畫審核結果
# #所有縣市的在不同分頁(sheet)裡
# wb = xlrd.open_workbook('102年回饋金補助審核結果.xls')
# sh = wb.sheet_by_index(2) #分頁index
# for r in range(5,sh.nrows) :
# 	for c in [0,1] :
# 		print sh.cell(r,c).value.encode(encoding="cp950",errors="ignore"),"|",
# 	print sh.cell(r,7).value,"|"
# 	print sh.cell(r,9).value.encode(encoding="cp950",errors="ignore"),"|",
# 	print r

# # 101 公益彩券回饋金計畫審核結果
# # 各縣市在不同檔案中
# # 0 編號
# # 1 社福機構
# # 7 審查結果
# # 9 核定內容
# wb = xlrd.open_workbook('101苗栗縣.xls')
# sh = wb.sheet_by_index(0)
# for r in range(5,sh.nrows) :
# 	for c in [0,1] :
# 		print sh.cell(r,c).value.encode(encoding="cp950",errors="ignore"),"|",
# 	print sh.cell(r,7).value,"|"
# 	print sh.cell(r,9).value.encode(encoding="cp950",errors="ignore"),"|",
# 	print r


# # 100 公益彩券回饋金計畫審核結果
# #所有縣市的在不同分頁(sheet)裡
# # 0 編號
# # 1 社福機構
# # 8 審查結果
# # 10 核定內容
# wb = xlrd.open_workbook('100年回饋金補助審核結果.xls')
# sh = wb.sheet_by_index(2) #分頁index
# for r in range(5,sh.nrows) :
# 	for c in [0,1] :
# 		print sh.cell(r,c).value.encode(encoding="cp950",errors="ignore"),"|",
# 	print sh.cell(r,8).value,"|"
# 	print sh.cell(r,10).value.encode(encoding="cp950",errors="ignore"),"|",
# 	print r

# #create data
# from apis.models import FundGet
# import xlrd

# wb = xlrd.open_workbook('./fundget/102.xls')
# sh_namelist = wb.sheet_names()

# for i in range(0, len(sh_namelist)):
#     location = sh_namelist[i].encode(encoding="utf-8",errors="ignore")
#     sh = wb.sheet_by_index(i)
#     for r in range(5,sh.nrows-1):
#         FundGet.objects.create(
#             index = sh.cell(r,0).value.encode(encoding="utf-8",errors="ignore"),
#             year = 103,
#             location = location,
#             org_name = sh.cell(r,1).value.encode(encoding="utf-8",errors="ignore"),
#             money = sh.cell(r,7).value,
#             content = sh.cell(r,9).value.encode(encoding="utf-8",errors="ignore")
#         )


# #creat data for 101 & 103
# import glob
# file101 = glob.glob("./fundget/103*.xls")

# for j in range(0,len(file101)) :
#     file101[j] = file101[j].replace("./fundget\\", "")
#     wb = xlrd.open_workbook('./fundget/'+file101[j])
#     sh = wb.sheet_by_index(0)
#     location = file101[j].replace("101", "").replace(".xls", "")
#     print location
#     location = location.decode(encoding="cp950",errors="ignore")
#     location = location.encode(encoding="utf-8",errors="ignore")
#     for r in range(5,sh.nrows-1):
#         FundGet.objects.create(
#             index = sh.cell(r,0).value.encode(encoding="utf-8",errors="ignore"),
#             year = 101,
#             location = location,
#             org_name = sh.cell(r,1).value.encode(encoding="utf-8",errors="ignore"),
#             money = sh.cell(r,7).value,
#             content = sh.cell(r,9).value.encode(encoding="utf-8",errors="ignore")
#         )


# file103 = glob.glob("./fundget/103*.xls")

# for j in range(0,len(file101)) :
#     file103[j] = file103[j].replace("./fundget\\", "")
#     wb = xlrd.open_workbook('./fundget/'+file103[j])
#     sh = wb.sheet_by_index(0)
#     location = file103[j].replace("103", "").replace(".xls", "")
#     print location
#     location = location.decode(encoding="cp950",errors="ignore")
#     location = location.encode(encoding="utf-8",errors="ignore")
#     for r in range(5,sh.nrows-1):
#         FundGet.objects.create(
#             index = sh.cell(r,0).value.encode(encoding="utf-8",errors="ignore"),
#             year = 103,
#             location = location,
#             org_name = sh.cell(r,1).value.encode(encoding="utf-8",errors="ignore"),
#             money = sh.cell(r,5).value,
#             content = sh.cell(r,7).value.encode(encoding="utf-8",errors="ignore")
#         )

# FundGet.objects.filter(year=101).delete()
# FundGet.objects.filter(location).delete()
# update(location='捷運大安站')


# # 公益彩券盈餘分配
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# from cStringIO import StringIO
# from apis.models import Surplus

# def convert(fname, pages=None):
#     if not pages:
#         pagenums = set()
#     else:
#         pagenums = set(pages)
#     output = StringIO()
#     manager = PDFResourceManager()
#     converter = TextConverter(manager, output, laparams=LAParams())
#     interpreter = PDFPageInterpreter(manager, converter)
#     infile = file(fname, 'rb')
#     for page in PDFPage.get_pages(infile, pagenums):
#         interpreter.process_page(page)
#     infile.close()
#     converter.close()
#     text = output.getvalue()
#     output.close
#     return text

# location = ['臺北市', '新北市', '臺中市', '臺南市', '高雄市', '宜蘭縣','桃園縣','新竹縣',
# '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '臺東縣', '花蓮縣', '澎湖縣',
# '基隆市', '新竹市', '嘉義市', '金門縣', '連江縣','fm06]

# for i in range(1,13) :
#     content = convert('./surplus/103'+str(i)+'.pdf')
#     str1 = content.replace(",", "").split("(G+H+I)\n\n")
#     str2 = str1[1].split("\n\n")[0].split("\n")
#     print i
#     money = []
#     for n in str2 :
#     	money.append(int(n))
#     for j in range(0, len(location)) :
#         place = location[j].decode(encoding="utf-8",errors="ignore")
#         print place
#         Surplus.objects.create(
#             year = 103,
#             month = i,
#             location = place,
#             surplus = money[j]
#         )


# curl "http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H
# "Cookie: ASPSESSIONIDQSQDABQB=BBCIAFLDBLDJIMGHNDJGJEJL;
# ASPSESSIONIDSQQQBARA=OJAPNIKDNAGBHAIEFDFFBHLC" -H "Origin:
# http://www.taiwanlottery.com.tw" -H "Accept-Encoding: gzip, deflate" -H
# "Accept-Language:
# zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2,ko;q=0.2" -H
# "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT
# 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107
# Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H
# "Accept:
# text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
# -H "Cache-Control: max-age=0" -H "Referer:
# http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H
# "Connection: keep-alive" --data
# "__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE="%"2FwEPDwUJNzkzNTQ1MDA0D2QWAgIBD2QWBgIDDxBkEBUXD"%"2Biri"%"2BmBuOaTh"%"2Be4o"%"2BW4ggnlj7DljJfluIIJ6auY6ZuE5biCCeaWsOWMl"%"2BW4ggnlrpzomK3nuKMJ5qGD5ZyS5biCCeaWsOeruee4ownoi5fmoJfnuKMJ5b2w5YyW57ijCeWNl"%"2BaKlee4ownpm7LmnpfnuKMJ5ZiJ576p57ijCeWxj"%"2Badsee4ownlj7DmnbHnuKMJ6Iqx6JOu57ijCea"%"2Bjua5lue4ownln7rpmobluIIJ5paw56u55biCCeWPsOS4reW4ggnlmInnvqnluIIJ5Y"%"2Bw5Y2X5biCCemHkemWgOe4ownpgKPmsZ"%"2FnuKMVFwEwATEBMgEzATQBNQE2ATcBOQIxMAIxMQIxMgIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNRQrAxdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgUPEGQQFQwL5Lit5q2j5Y2AICAL5aSn5ZCM5Y2AICAL5Lit5bGx5Y2AICAL5p2"%"2B5bGx5Y2AICAL5aSn5a6J5Y2AICAL6JCs6I"%"2Bv5Y2AICAL5L"%"2Bh576p5Y2AICAL5aOr5p6X5Y2AICAL5YyX5oqV5Y2AICAL5YWn5rmW5Y2AICAL5Y2X5riv5Y2AICAL5paH5bGx5Y2AICAVDAvkuK3mraPljYAgIAvlpKflkIzljYAgIAvkuK3lsbHljYAgIAvmnb7lsbHljYAgIAvlpKflronljYAgIAvokKzoj6"%"2FljYAgIAvkv6HnvqnljYAgIAvlo6vmnpfljYAgIAvljJfmipXljYAgIAvlhafmuZbljYAgIAvljZfmuK"%"2FljYAgIAvmloflsbHljYAgIBQrAwxnZ2dnZ2dnZ2dnZ2dkZAIJDxYCHgRUZXh0ZWRkdS"%"2FuLN4kanIE7j5czFI1OUTzzCTIlhQfL"%"2BDfWePshBY"%"3D&__EVENTVALIDATION="%"2FwEWJgKb2p6HBgKd5I"%"2FlCgKNi6WLBgKSi6WLBgKTi6WLBgKQi6WLBgKRi6WLBgKWi6WLBgKXi6WLBgKUi6WLBgKKi6WLBgKSi"%"2BWIBgKSi"%"2BmIBgKSi"%"2B2IBgKSi9mIBgKSi92IBgKSi8GIBgKSi4WLBgKSi4mLBgKTi"%"2BWIBgKTi"%"2BmIBgKTi"%"2B2IBgKTi9GIBgKTi9WIBgKTi9mIBgKWgqizDALh4LOxBgKUguClBwLng9WlBwKe4cfeDALqtcDwAQKc9sCfAQKX3t"%"2B4BgKz4driDQKg4d"%"2BJCgLw8aLlCgL"%"2B0NalBwKM54rGBvMlBUeSNs4ncoushv"%"2BQTQVvwd"%"2Bw3vrNcN7M2e6zUPM4&DropDownList1=1&DropDownList2="%"E4"%"B8"%"AD"%"E6"%"AD"%"A3"%"E5"%"8D"%"80++&Button1="%"E6"%"9F"%"A5"%"E8"%"A9"%"A2"
# --compressed

# curl "http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H
# "Cookie: ASPSESSIONIDQSQDABQB=BBCIAFLDBLDJIMGHNDJGJEJL;
# ASPSESSIONIDSQQQBARA=OJAPNIKDNAGBHAIEFDFFBHLC" -H "Origin:
# http://www.taiwanlottery.com.tw" -H "Accept-Encoding: gzip, deflate" -H
# "Accept-Language:
# zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2,ko;q=0.2" -H
# "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT
# 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107
# Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H
# "Accept:
# text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
# -H "Cache-Control: max-age=0" -H "Referer:
# http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H
# "Connection: keep-alive" --data
# "__EVENTTARGET=DropDownList1&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE="%"2FwEPDwUJNzkzNTQ1MDA0D2QWAgIBD2QWBgIDDxBkEBUXD"%"2Biri"%"2BmBuOaTh"%"2Be4o"%"2BW4ggnlj7DljJfluIIJ6auY6ZuE5biCCeaWsOWMl"%"2BW4ggnlrpzomK3nuKMJ5qGD5ZyS5biCCeaWsOeruee4ownoi5fmoJfnuKMJ5b2w5YyW57ijCeWNl"%"2BaKlee4ownpm7LmnpfnuKMJ5ZiJ576p57ijCeWxj"%"2Badsee4ownlj7DmnbHnuKMJ6Iqx6JOu57ijCea"%"2Bjua5lue4ownln7rpmobluIIJ5paw56u55biCCeWPsOS4reW4ggnlmInnvqnluIIJ5Y"%"2Bw5Y2X5biCCemHkemWgOe4ownpgKPmsZ"%"2FnuKMVFwEwATEBMgEzATQBNQE2ATcBOQIxMAIxMQIxMgIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNRQrAxdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBZmQCBQ8QZA8WAWYWARAFEuiri"%"2BWFiOmBuOaTh"%"2Be4o"%"2BW4ggUBMGdkZAIJDxYCHgRUZXh0ZWRkd"%"2BTuIrQ"%"2FF8WUr6a"%"2FseU20Sjr4NH"%"2FLgXmxkH7MtCnbaQ"%"3D&__EVENTVALIDATION="%"2FwEWGwLUqtGAAwKd5I"%"2FlCgKNi6WLBgKSi6WLBgKTi6WLBgKQi6WLBgKRi6WLBgKWi6WLBgKXi6WLBgKUi6WLBgKKi6WLBgKSi"%"2BWIBgKSi"%"2BmIBgKSi"%"2B2IBgKSi9mIBgKSi92IBgKSi8GIBgKSi4WLBgKSi4mLBgKTi"%"2BWIBgKTi"%"2BmIBgKTi"%"2B2IBgKTi9GIBgKTi9WIBgKTi9mIBgKOi6WLBgKM54rGBsIHFqCV0TzwENfeTcuCJaINSvb6OFvVtTwP1JeOQ4X"%"2B&DropDownList1=1&DropDownList2=0"
# --compressed

# curl "http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H "Cookie: ASPSESSIONIDQSQDABQB=BBCIAFLDBLDJIMGHNDJGJEJL; ASPSESSIONIDSQQQBARA=OJAPNIKDNAGBHAIEFDFFBHLC" -H "Origin: http://www.taiwanlottery.com.tw" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2,ko;q=0.2" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Cache-Control: max-age=0" -H "Referer: http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H "Connection: keep-alive" --data "__EVENTTARGET=DropDownList1&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE="%"2FwEPDwUJNzkzNTQ1MDA0D2QWAgIBD2QWBgIDDxBkEBUXD"%"2Biri"%"2BmBuOaTh"%"2Be4o"%"2BW4ggnlj7DljJfluIIJ6auY6ZuE5biCCeaWsOWMl"%"2BW4ggnlrpzomK3nuKMJ5qGD5ZyS5biCCeaWsOeruee4ownoi5fmoJfnuKMJ5b2w5YyW57ijCeWNl"%"2BaKlee4ownpm7LmnpfnuKMJ5ZiJ576p57ijCeWxj"%"2Badsee4ownlj7DmnbHnuKMJ6Iqx6JOu57ijCea"%"2Bjua5lue4ownln7rpmobluIIJ5paw56u55biCCeWPsOS4reW4ggnlmInnvqnluIIJ5Y"%"2Bw5Y2X5biCCemHkemWgOe4ownpgKPmsZ"%"2FnuKMVFwEwATEBMgEzATQBNQE2ATcBOQIxMAIxMQIxMgIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNRQrAxdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgUPEGQQFQwL5Lit5q2j5Y2AICAL5aSn5ZCM5Y2AICAL5Lit5bGx5Y2AICAL5p2"%"2B5bGx5Y2AICAL5aSn5a6J5Y2AICAL6JCs6I"%"2Bv5Y2AICAL5L"%"2Bh576p5Y2AICAL5aOr5p6X5Y2AICAL5YyX5oqV5Y2AICAL5YWn5rmW5Y2AICAL5Y2X5riv5Y2AICAL5paH5bGx5Y2AICAVDAvkuK3mraPljYAgIAvlpKflkIzljYAgIAvkuK3lsbHljYAgIAvmnb7lsbHljYAgIAvlpKflronljYAgIAvokKzoj6"%"2FljYAgIAvkv6HnvqnljYAgIAvlo6vmnpfljYAgIAvljJfmipXljYAgIAvlhafmuZbljYAgIAvljZfmuK"%"2FljYAgIAvmloflsbHljYAgIBQrAwxnZ2dnZ2dnZ2dnZ2dkZAIJDxYCHgRUZXh0BaA8PHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlpKfpvo3ooZcxMTjomZ88L3RkPjx0ZD7oqLHlpJrnpo"%"2FkvIHmpa3npL48L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlpKfpvo3ooZcyMjHomZ8x5qiTPC90ZD48dGQ"%"2B6YeR5L6G55m86LOT5p6c5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5aSn6b6N6KGXMzA46JmfPC90ZD48dGQ"%"2B5pel55ub5ZWG6KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5aSq5Y6f6LevMjAz6JmfPC90ZD48dGQ"%"2B6ZuZ6YCj55m85b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5aSq5Y6f6LevNTbomZ88L3RkPjx0ZD7ph5HmspnloKHlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlpKrljp"%"2Fot684MeiZnzwvdGQ"%"2BPHRkPuawuOemj"%"2BWVhuihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOW3v"%"2BawkeWkp"%"2BmBk"%"2BS4gOautTIwOeiZnzwvdGQ"%"2BPHRkPuS6rOermeW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOawkeeUn"%"2Bilv"%"2Bi3rzEwMeiZnzwvdGQ"%"2BPHRkPue0heeri"%"2BeZvOaKleazqOermTwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOawkeeUn"%"2Bilv"%"2Bi3rzE2OeS5izHomZ88L3RkPjx0ZD7okoLogIDllYbooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmsJHnlJ"%"2Fopb"%"2Fot68xODDkuYsx6JmfPC90ZD48dGQ"%"2B5Zac5b6e5aSp6ZmN5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5rCR55Sf6KW"%"2F6LevMjUy6JmfPC90ZD48dGQ"%"2B5a"%"2BM5pmf5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5rCR55Sf6KW"%"2F6LevMzYx6JmfPC90ZD48dGQ"%"2B5aSn55y"%"2B5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5rCR55Sf6KW"%"2F6LevOTDomZ88L3RkPjx0ZD7lr7bpupfml7rlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmsJHml4"%"2Fopb"%"2Fot68xOTnomZ88L3RkPjx0ZD7pkZLmoZPlvanliLjllYbooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmsJHml4"%"2Fopb"%"2Fot68yMjPkuYsz6JmfPC90ZD48dGQ"%"2B56aP56W"%"2F5aO95b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5rCR5peP6KW"%"2F6LevMjY56JmfMeaokzwvdGQ"%"2BPHRkPuaymeeRquS8gealreihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOawkeaXj"%"2Bilv"%"2Bi3rzI5MOiZnzwvdGQ"%"2BPHRkPuWEhOS5i"%"2BS4reW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOawkeasiuilv"%"2Bi3rzE0NOW3tzjomZ88L3RkPjx0ZD7osqHlhYPllYbooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmsJHmrIropb"%"2Fot68yMjbomZ88L3RkPjx0ZD7lpKfmqYvpoK3lvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmsJHmrIropb"%"2Fot68yMzjomZ88L3RkPjx0ZD7pgKPku7LlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2FkuozmrrUxNTDomZ88L3RkPjx0ZD7mqILlhITnmbzmipXms6jnq5k8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2FkuozmrrUxNjbomZ88L3RkPjx0ZD7ph5Hml7ros5PmnpzlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2FkuozmrrUxOTXkuYsx6JmfPC90ZD48dGQ"%"2B5aW96LKh6aCt5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5bu25bmz5YyX6Lev5LqM5q61MjI26JmfPC90ZD48dGQ"%"2B5aSn56i75Z"%"2BV5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5bu25bmz5YyX6Lev5LqM5q61NjLomZ88L3RkPjx0ZD7lhITlpJrlpJrlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2FkuInmrrUyMuS5izTomZ88L3RkPjx0ZD7ph5HkvobosrflvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2FkuInmrrUzNuS5izLomZ88L3RkPjx0ZD7pgIHlhITmqILlhaznm4rlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2Flm5vmrrUxM"%"2BiZnzwvdGQ"%"2BPHRkPumAo"%"2BeZvOW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOW7tuW5s"%"2BWMl"%"2Bi3r"%"2BWbm"%"2BautTIw6JmfPC90ZD48dGQ"%"2B6YCj5pe65b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5bu25bmz5YyX6Lev5Zub5q61MjTomZ88L3RkPjx0ZD7kuIDlvJjlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2Flm5vmrrU0OeiZnzwvdGQ"%"2BPHRkPuiyoeWvjOaXuuaKleazqOermTwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOW7tuW5s"%"2Bi3r"%"2BS6jOautTEwM"%"2BiZnzwvdGQ"%"2BPHRkPuWQiOWIqeeZvOaKleazqOermTwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOaJv"%"2BW"%"2Bt"%"2Bi3r"%"2BS4gOautTEy6JmfPC90ZD48dGQ"%"2B56aP6YGL5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5om"%"2F5b636Lev5LiA5q61MzHomZ8x5qiTPC90ZD48dGQ"%"2B5YWt5pif5peX6Imm5ZWG6KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5om"%"2F5b636Lev5LiJ5q61MTQ46JmfPC90ZD48dGQ"%"2B56aP55uK5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5om"%"2F5b636Lev5LiJ5q61MTY06JmfMeaokzwvdGQ"%"2BPHRkPum0u"%"2BWQieW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOaJv"%"2BW"%"2Bt"%"2Bi3r"%"2BS4ieautTIzMeiZnzwvdGQ"%"2BPHRkPuaUj"%"2BS"%"2BhueZvOW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOaYjOWQieihlzExMuiZnzwvdGQ"%"2BPHRkPuecvuS"%"2BhueZvOWVhuihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOaYjOWQieihlzIx6JmfPC90ZD48dGQ"%"2B6LOT5p6c55m85b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A6ZW35a6J6KW"%"2F6LevMzM45LmLMeiZnzwvdGQ"%"2BPHRkPuS6qOW9qeWVhuihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOWNl"%"2BS6rOilv"%"2Bi3rzE2M"%"2BiZnzwvdGQ"%"2BPHRkPuS"%"2BhuW"%"2Bl"%"2Bm7g"%"2BmHkeWfjuW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOWNl"%"2BS6rOilv"%"2Bi3rzE4N"%"2BiZnzwvdGQ"%"2BPHRkPuazleS4u"%"2BWFrOW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOWNl"%"2BS6rOilv"%"2Bi3rzM2MOiZnzHmqJM8L3RkPjx0ZD7nqannmbzlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDljZfkuqzopb"%"2Fot684MeiZnzwvdGQ"%"2BPHRkPueZvOiyoeiyk"%"2BW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOmHjeaFtuWMl"%"2Bi3r"%"2BS4gOautTg15LmLMeiZnzwvdGQ"%"2BPHRkPuWWnOWvjOW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOmHjeaFtuWMl"%"2Bi3r"%"2BS4gOautTg3LTHomZ88L3RkPjx0ZD7msLjkuqjlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDph43mhbbljJfot6"%"2FkuozmrrUxMjDomZ88L3RkPjx0ZD7ph5HkuInop5LlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDph43mhbbljJfot6"%"2FkuozmrrUxMzXomZ88L3RkPjx0ZD7mlofnmbzmipXms6jnq5k8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDph43mhbbljJfot6"%"2FkuozmrrUxNDXomZ8x5qiTPC90ZD48dGQ"%"2B5byY5LuB6aOf5ZOB5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A6YeN5oW25YyX6Lev5LiJ5q61MjUw5LmLMuiZnzwvdGQ"%"2BPHRkPuS4ieeZvOW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOmHjeaFtuWMl"%"2Bi3r"%"2BS4ieautTI4MeiZnzwvdGQ"%"2BPHRkPuWIqeawkeWVhuihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOmHjeaFtuWMl"%"2Bi3r"%"2BS4ieautTI4MuiZnzwvdGQ"%"2BPHRkPuW5uOemj"%"2BWPsOeBo"%"2BW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOmHjeaFtuWMl"%"2Bi3r"%"2BS4ieautTY16JmfPC90ZD48dGQ"%"2B6YeR6YO95b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A6YWS5rOJ6KGXMTIw6JmfPC90ZD48dGQ"%"2B5re75aW96YGL5oqV5rOo56uZPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A6YWS5rOJ6KGXMzLkuYsx6JmfPC90ZD48dGQ"%"2B6YeR5bm46YGL6LOT5p6c5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A6JCs5YWo6KGXMzHomZ88L3RkPjx0ZD7lh7rpgYvllYbooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlr6flpI"%"2Fot68xMznomZ88L3RkPjx0ZD7ph5HlvpflhITlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlr6flpI"%"2Fot68xNDfomZ88L3RkPjx0ZD7lhITkvoboiIjlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmrbjnto"%"2FooZcxNjjkuYsx6JmfMeaokzwvdGQ"%"2BPHRkPuWEhOiyoeWIqeaKleazqOermTwvdGQ"%"2BPC90cj5kZIHVr1lmLXr"%"2Bpaz9z4hqWWMsdeDz6daO1eigCzTleijw&__EVENTVALIDATION="%"2FwEWJgKsyPDrBAKd5I"%"2FlCgKNi6WLBgKSi6WLBgKTi6WLBgKQi6WLBgKRi6WLBgKWi6WLBgKXi6WLBgKUi6WLBgKKi6WLBgKSi"%"2BWIBgKSi"%"2BmIBgKSi"%"2B2IBgKSi9mIBgKSi92IBgKSi8GIBgKSi4WLBgKSi4mLBgKTi"%"2BWIBgKTi"%"2BmIBgKTi"%"2B2IBgKTi9GIBgKTi9WIBgKTi9mIBgKWgqizDALh4LOxBgKUguClBwLng9WlBwKe4cfeDALqtcDwAQKc9sCfAQKX3t"%"2B4BgKz4driDQKg4d"%"2BJCgLw8aLlCgL"%"2B0NalBwKM54rGBsElAjoHbSdOY2J022"%"2BAzr"%"2BbuK9B4gAcDS22FHIg7PTe&DropDownList1=2&DropDownList2="%"E5"%"A4"%"A7"%"E5"%"90"%"8C"%"E5"%"8D"%"80++" --compressed
# curl "http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H "Cookie: ASPSESSIONIDQSQDABQB=BBCIAFLDBLDJIMGHNDJGJEJL; ASPSESSIONIDSQQQBARA=OJAPNIKDNAGBHAIEFDFFBHLC" -H "Origin: http://www.taiwanlottery.com.tw" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2,ko;q=0.2" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Cache-Control: max-age=0" -H "Referer: http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H "Connection: keep-alive" --data "__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE="%"2FwEPDwUJNzkzNTQ1MDA0D2QWAgIBD2QWBgIDDxBkEBUXD"%"2Biri"%"2BmBuOaTh"%"2Be4o"%"2BW4ggnlj7DljJfluIIJ6auY6ZuE5biCCeaWsOWMl"%"2BW4ggnlrpzomK3nuKMJ5qGD5ZyS5biCCeaWsOeruee4ownoi5fmoJfnuKMJ5b2w5YyW57ijCeWNl"%"2BaKlee4ownpm7LmnpfnuKMJ5ZiJ576p57ijCeWxj"%"2Badsee4ownlj7DmnbHnuKMJ6Iqx6JOu57ijCea"%"2Bjua5lue4ownln7rpmobluIIJ5paw56u55biCCeWPsOS4reW4ggnlmInnvqnluIIJ5Y"%"2Bw5Y2X5biCCemHkemWgOe4ownpgKPmsZ"%"2FnuKMVFwEwATEBMgEzATQBNQE2ATcBOQIxMAIxMQIxMgIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNRQrAxdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgJkAgUPEGQQFSYL5paw6IiI5Y2AICAL5YmN6YeR5Y2AICAL6IuT6ZuF5Y2AICAL6bm95Z"%"2BV5Y2AICAL6byT5bGx5Y2AICAL5peX5rSl5Y2AICAL5YmN6Y6u5Y2AICAL5LiJ5rCR5Y2AICAL5qWg5qKT5Y2AICAL5bCP5riv5Y2AICAL5bem54ef5Y2AICAL5LuB5q2m5Y2AICAL5aSn56S"%"2B5Y2AICAL5bKh5bGx5Y2AICAL6Lev56u55Y2AICAL6Zi"%"2F6JOu5Y2AICAL55Sw5a"%"2Bu5Y2AICAL54eV5bei5Y2AICAL5qmL6aCt5Y2AICAL5qKT5a6Y5Y2AICAL5b2M6ZmA5Y2AICAL5rC45a6J5Y2AICAL5rmW5YWn5Y2AICAL6bOz5bGx5Y2AICAL5aSn5a"%"2Bu5Y2AICAL5p6X5ZyS5Y2AICAL6bOl5p2"%"2B5Y2AICAL5aSn5qi55Y2AICAL5peX5bGx5Y2AICAL576O5r"%"2BD5Y2AICAL5YWt6b6c5Y2AICAL5YWn6ZaA5Y2AICAL5p2J5p6X5Y2AICAL55Sy5LuZ5Y2AICAL5qGD5rqQ5Y2AICAN6YKj55Gq5aSP5Y2AIAvojILmnpfljYAgIAvojITokKPljYAgIBUmC"%"2BaWsOiIiOWNgCAgC"%"2BWJjemHkeWNgCAgC"%"2BiLk"%"2BmbheWNgCAgC"%"2Bm5veWfleWNgCAgC"%"2Bm8k"%"2BWxseWNgCAgC"%"2BaXl"%"2Ba0peWNgCAgC"%"2BWJjemOruWNgCAgC"%"2BS4ieawkeWNgCAgC"%"2BaloOaik"%"2BWNgCAgC"%"2BWwj"%"2Ba4r"%"2BWNgCAgC"%"2BW3pueHn"%"2BWNgCAgC"%"2BS7geatpuWNgCAgC"%"2BWkp"%"2BekvuWNgCAgC"%"2BWyoeWxseWNgCAgC"%"2Bi3r"%"2BerueWNgCAgC"%"2BmYv"%"2BiTruWNgCAgC"%"2BeUsOWvruWNgCAgC"%"2BeHleW3ouWNgCAgC"%"2Bapi"%"2BmgreWNgCAgC"%"2Baik"%"2BWumOWNgCAgC"%"2BW9jOmZgOWNgCAgC"%"2BawuOWuieWNgCAgC"%"2Ba5luWFp"%"2BWNgCAgC"%"2Bmzs"%"2BWxseWNgCAgC"%"2BWkp"%"2BWvruWNgCAgC"%"2Bael"%"2BWckuWNgCAgC"%"2BmzpeadvuWNgCAgC"%"2BWkp"%"2BaoueWNgCAgC"%"2BaXl"%"2BWxseWNgCAgC"%"2Be"%"2Bjua"%"2Fg"%"2BWNgCAgC"%"2BWFrem"%"2BnOWNgCAgC"%"2BWFp"%"2BmWgOWNgCAgC"%"2Badieael"%"2BWNgCAgC"%"2BeUsuS7meWNgCAgC"%"2Bahg"%"2Ba6kOWNgCAgDemCo"%"2BeRquWkj"%"2BWNgCAL6IyC5p6X5Y2AICAL6IyE6JCj5Y2AICAUKwMmZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAIJDxYCHgRUZXh0BaA8PHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlpKfpvo3ooZcxMTjomZ88L3RkPjx0ZD7oqLHlpJrnpo"%"2FkvIHmpa3npL48L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlpKfpvo3ooZcyMjHomZ8x5qiTPC90ZD48dGQ"%"2B6YeR5L6G55m86LOT5p6c5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5aSn6b6N6KGXMzA46JmfPC90ZD48dGQ"%"2B5pel55ub5ZWG6KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5aSq5Y6f6LevMjAz6JmfPC90ZD48dGQ"%"2B6ZuZ6YCj55m85b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5aSq5Y6f6LevNTbomZ88L3RkPjx0ZD7ph5HmspnloKHlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlpKrljp"%"2Fot684MeiZnzwvdGQ"%"2BPHRkPuawuOemj"%"2BWVhuihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOW3v"%"2BawkeWkp"%"2BmBk"%"2BS4gOautTIwOeiZnzwvdGQ"%"2BPHRkPuS6rOermeW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOawkeeUn"%"2Bilv"%"2Bi3rzEwMeiZnzwvdGQ"%"2BPHRkPue0heeri"%"2BeZvOaKleazqOermTwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOawkeeUn"%"2Bilv"%"2Bi3rzE2OeS5izHomZ88L3RkPjx0ZD7okoLogIDllYbooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmsJHnlJ"%"2Fopb"%"2Fot68xODDkuYsx6JmfPC90ZD48dGQ"%"2B5Zac5b6e5aSp6ZmN5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5rCR55Sf6KW"%"2F6LevMjUy6JmfPC90ZD48dGQ"%"2B5a"%"2BM5pmf5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5rCR55Sf6KW"%"2F6LevMzYx6JmfPC90ZD48dGQ"%"2B5aSn55y"%"2B5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5rCR55Sf6KW"%"2F6LevOTDomZ88L3RkPjx0ZD7lr7bpupfml7rlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmsJHml4"%"2Fopb"%"2Fot68xOTnomZ88L3RkPjx0ZD7pkZLmoZPlvanliLjllYbooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmsJHml4"%"2Fopb"%"2Fot68yMjPkuYsz6JmfPC90ZD48dGQ"%"2B56aP56W"%"2F5aO95b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5rCR5peP6KW"%"2F6LevMjY56JmfMeaokzwvdGQ"%"2BPHRkPuaymeeRquS8gealreihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOawkeaXj"%"2Bilv"%"2Bi3rzI5MOiZnzwvdGQ"%"2BPHRkPuWEhOS5i"%"2BS4reW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOawkeasiuilv"%"2Bi3rzE0NOW3tzjomZ88L3RkPjx0ZD7osqHlhYPllYbooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmsJHmrIropb"%"2Fot68yMjbomZ88L3RkPjx0ZD7lpKfmqYvpoK3lvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmsJHmrIropb"%"2Fot68yMzjomZ88L3RkPjx0ZD7pgKPku7LlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2FkuozmrrUxNTDomZ88L3RkPjx0ZD7mqILlhITnmbzmipXms6jnq5k8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2FkuozmrrUxNjbomZ88L3RkPjx0ZD7ph5Hml7ros5PmnpzlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2FkuozmrrUxOTXkuYsx6JmfPC90ZD48dGQ"%"2B5aW96LKh6aCt5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5bu25bmz5YyX6Lev5LqM5q61MjI26JmfPC90ZD48dGQ"%"2B5aSn56i75Z"%"2BV5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5bu25bmz5YyX6Lev5LqM5q61NjLomZ88L3RkPjx0ZD7lhITlpJrlpJrlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2FkuInmrrUyMuS5izTomZ88L3RkPjx0ZD7ph5HkvobosrflvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2FkuInmrrUzNuS5izLomZ88L3RkPjx0ZD7pgIHlhITmqILlhaznm4rlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2Flm5vmrrUxM"%"2BiZnzwvdGQ"%"2BPHRkPumAo"%"2BeZvOW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOW7tuW5s"%"2BWMl"%"2Bi3r"%"2BWbm"%"2BautTIw6JmfPC90ZD48dGQ"%"2B6YCj5pe65b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5bu25bmz5YyX6Lev5Zub5q61MjTomZ88L3RkPjx0ZD7kuIDlvJjlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlu7blubPljJfot6"%"2Flm5vmrrU0OeiZnzwvdGQ"%"2BPHRkPuiyoeWvjOaXuuaKleazqOermTwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOW7tuW5s"%"2Bi3r"%"2BS6jOautTEwM"%"2BiZnzwvdGQ"%"2BPHRkPuWQiOWIqeeZvOaKleazqOermTwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOaJv"%"2BW"%"2Bt"%"2Bi3r"%"2BS4gOautTEy6JmfPC90ZD48dGQ"%"2B56aP6YGL5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5om"%"2F5b636Lev5LiA5q61MzHomZ8x5qiTPC90ZD48dGQ"%"2B5YWt5pif5peX6Imm5ZWG6KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5om"%"2F5b636Lev5LiJ5q61MTQ46JmfPC90ZD48dGQ"%"2B56aP55uK5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A5om"%"2F5b636Lev5LiJ5q61MTY06JmfMeaokzwvdGQ"%"2BPHRkPum0u"%"2BWQieW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOaJv"%"2BW"%"2Bt"%"2Bi3r"%"2BS4ieautTIzMeiZnzwvdGQ"%"2BPHRkPuaUj"%"2BS"%"2BhueZvOW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOaYjOWQieihlzExMuiZnzwvdGQ"%"2BPHRkPuecvuS"%"2BhueZvOWVhuihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOaYjOWQieihlzIx6JmfPC90ZD48dGQ"%"2B6LOT5p6c55m85b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A6ZW35a6J6KW"%"2F6LevMzM45LmLMeiZnzwvdGQ"%"2BPHRkPuS6qOW9qeWVhuihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOWNl"%"2BS6rOilv"%"2Bi3rzE2M"%"2BiZnzwvdGQ"%"2BPHRkPuS"%"2BhuW"%"2Bl"%"2Bm7g"%"2BmHkeWfjuW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOWNl"%"2BS6rOilv"%"2Bi3rzE4N"%"2BiZnzwvdGQ"%"2BPHRkPuazleS4u"%"2BWFrOW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOWNl"%"2BS6rOilv"%"2Bi3rzM2MOiZnzHmqJM8L3RkPjx0ZD7nqannmbzlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDljZfkuqzopb"%"2Fot684MeiZnzwvdGQ"%"2BPHRkPueZvOiyoeiyk"%"2BW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOmHjeaFtuWMl"%"2Bi3r"%"2BS4gOautTg15LmLMeiZnzwvdGQ"%"2BPHRkPuWWnOWvjOW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOmHjeaFtuWMl"%"2Bi3r"%"2BS4gOautTg3LTHomZ88L3RkPjx0ZD7msLjkuqjlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDph43mhbbljJfot6"%"2FkuozmrrUxMjDomZ88L3RkPjx0ZD7ph5HkuInop5LlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDph43mhbbljJfot6"%"2FkuozmrrUxMzXomZ88L3RkPjx0ZD7mlofnmbzmipXms6jnq5k8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDph43mhbbljJfot6"%"2FkuozmrrUxNDXomZ8x5qiTPC90ZD48dGQ"%"2B5byY5LuB6aOf5ZOB5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A6YeN5oW25YyX6Lev5LiJ5q61MjUw5LmLMuiZnzwvdGQ"%"2BPHRkPuS4ieeZvOW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOmHjeaFtuWMl"%"2Bi3r"%"2BS4ieautTI4MeiZnzwvdGQ"%"2BPHRkPuWIqeawkeWVhuihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzI"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOmHjeaFtuWMl"%"2Bi3r"%"2BS4ieautTI4MuiZnzwvdGQ"%"2BPHRkPuW5uOemj"%"2BWPsOeBo"%"2BW9qeWIuOihjDwvdGQ"%"2BPC90cj48dHIgY2xhc3M9dGRBXzE"%"2BPHRkPuWPsOWMl"%"2BW4gjwvdGQ"%"2BPHRkPuWkp"%"2BWQjOWNgDwvdGQ"%"2BPHRkPuWPsOWMl"%"2BW4guWkp"%"2BWQjOWNgOmHjeaFtuWMl"%"2Bi3r"%"2BS4ieautTY16JmfPC90ZD48dGQ"%"2B6YeR6YO95b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A6YWS5rOJ6KGXMTIw6JmfPC90ZD48dGQ"%"2B5re75aW96YGL5oqV5rOo56uZPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMT48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A6YWS5rOJ6KGXMzLkuYsx6JmfPC90ZD48dGQ"%"2B6YeR5bm46YGL6LOT5p6c5b2p5Yi46KGMPC90ZD48L3RyPjx0ciBjbGFzcz10ZEFfMj48dGQ"%"2B5Y"%"2Bw5YyX5biCPC90ZD48dGQ"%"2B5aSn5ZCM5Y2APC90ZD48dGQ"%"2B5Y"%"2Bw5YyX5biC5aSn5ZCM5Y2A6JCs5YWo6KGXMzHomZ88L3RkPjx0ZD7lh7rpgYvllYbooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlr6flpI"%"2Fot68xMznomZ88L3RkPjx0ZD7ph5HlvpflhITlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8yPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDlr6flpI"%"2Fot68xNDfomZ88L3RkPjx0ZD7lhITkvoboiIjlvanliLjooYw8L3RkPjwvdHI"%"2BPHRyIGNsYXNzPXRkQV8xPjx0ZD7lj7DljJfluII8L3RkPjx0ZD7lpKflkIzljYA8L3RkPjx0ZD7lj7DljJfluILlpKflkIzljYDmrbjnto"%"2FooZcxNjjkuYsx6JmfMeaokzwvdGQ"%"2BPHRkPuWEhOiyoeWIqeaKleazqOermTwvdGQ"%"2BPC90cj5kZKRdH1JYpxtV"%"2B"%"2BqJui1Xv8q5WomPjfX"%"2BHFHjn7"%"2FLN720&__EVENTVALIDATION="%"2FwEWQALLjrnaDgKd5I"%"2FlCgKNi6WLBgKSi6WLBgKTi6WLBgKQi6WLBgKRi6WLBgKWi6WLBgKXi6WLBgKUi6WLBgKKi6WLBgKSi"%"2BWIBgKSi"%"2BmIBgKSi"%"2B2IBgKSi9mIBgKSi92IBgKSi8GIBgKSi4WLBgKSi4mLBgKTi"%"2BWIBgKTi"%"2BmIBgKTi"%"2B2IBgKTi9GIBgKTi9WIBgKTi9mIBgKe1rLtBAKvsurQDALls7X9DgLHvvvFBAKq6oulBwLwrIaHAwKvsr6wAwLyiuD6BgK7k9jcCQK4raHlCgKCieLSCgK6uJS2DALi4Pv8CwKYxOmlBwKa66SRDAL"%"2F3cOLCgLp1pKyDAKs1YBGAuqivvcDAqr3i6gMAoz5pMcPAuHCsd4MAs6kiOcJAorQjKUHAp7hu7IMArHY2YMEAuHKgO4EAuDgh9ICAu6s1qUHApnPgbYHAszs980IApnip6EHArWJzbgGAqnW"%"2FpALAryl68kFArrTysQMAtzG"%"2FbkGAtLGzc4LAoznisYG8dl"%"2B0sYDnCbSf0lLS8omj4d"%"2F58Os2KOl25yYLrgTW3A"%"3D&DropDownList1=2&DropDownList2="%"E6"%"96"%"B0"%"E8"%"88"%"88"%"E5"%"8D"%"80++&Button1="%"E6"%"9F"%"A5"%"E8"%"A9"%"A2" --compressed
# import urllib
# import urlparse
# import requests
# url = "http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx"
# data = '__EVENTTARGET=DropDownList1&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE="%"2FwEPDwUJNzkzNTQ1MDA0D2QWAgIBD2QWBgIDDxBkEBUXD"%"2Biri"%"2BmBuOaTh"%"2Be4o"%"2BW4ggnlj7DljJfluIIJ6auY6ZuE5biCCeaWsOWMl"%"2BW4ggnlrpzomK3nuKMJ5qGD5ZyS5biCCeaWsOeruee4ownoi5fmoJfnuKMJ5b2w5YyW57ijCeWNl"%"2BaKlee4ownpm7LmnpfnuKMJ5ZiJ576p57ijCeWxj"%"2Badsee4ownlj7DmnbHnuKMJ6Iqx6JOu57ijCea"%"2Bjua5lue4ownln7rpmobluIIJ5paw56u55biCCeWPsOS4reW4ggnlmInnvqnluIIJ5Y"%"2Bw5Y2X5biCCemHkemWgOe4ownpgKPmsZ"%"2FnuKMVFwEwATEBMgEzATQBNQE2ATcBOQIxMAIxMQIxMgIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNRQrAxdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBZmQCBQ8QZA8WAWYWARAFEuiri"%"2BWFiOmBuOaTh"%"2Be4o"%"2BW4ggUBMGdkZAIJDxYCHgRUZXh0ZWRkd"%"2BTuIrQ"%"2FF8WUr6a"%"2FseU20Sjr4NH"%"2FLgXmxkH7MtCnbaQ"%"3D&__EVENTVALIDATION="%"2FwEWGwLUqtGAAwKd5I"%"2FlCgKNi6WLBgKSi6WLBgKTi6WLBgKQi6WLBgKRi6WLBgKWi6WLBgKXi6WLBgKUi6WLBgKKi6WLBgKSi"%"2BWIBgKSi"%"2BmIBgKSi"%"2B2IBgKSi9mIBgKSi92IBgKSi8GIBgKSi4WLBgKSi4mLBgKTi"%"2BWIBgKTi"%"2BmIBgKTi"%"2B2IBgKTi9GIBgKTi9WIBgKTi9mIBgKOi6WLBgKM54rGBsIHFqCV0TzwENfeTcuCJaINSvb6OFvVtTwP1JeOQ4X"%"2B&DropDownList1=1&DropDownList2=0'
# data = urlparse.parse_qs(data)
# req = requests.post(url, data)

# htmlfile = open("5.html", "w")
# htmlfile.write(req.content)
# htmlfile.close()

# curl "http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H "Cookie: ASPSESSIONIDQSQDABQB=BBCIAFLDBLDJIMGHNDJGJEJL; ASPSESSIONIDSQQQBARA=OJAPNIKDNAGBHAIEFDFFBHLC" -H "Origin: http://www.taiwanlottery.com.tw" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2,ko;q=0.2" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Cache-Control: max-age=0" -H "Referer: http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H "Connection: keep-alive" --data "__EVENTTARGET=DropDownList1&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE="%"2FwEPDwUJNzkzNTQ1MDA0D2QWAgIBD2QWBgIDDxBkEBUXD"%"2Biri"%"2BmBuOaTh"%"2Be4o"%"2BW4ggnlj7DljJfluIIJ6auY6ZuE5biCCeaWsOWMl"%"2BW4ggnlrpzomK3nuKMJ5qGD5ZyS5biCCeaWsOeruee4ownoi5fmoJfnuKMJ5b2w5YyW57ijCeWNl"%"2BaKlee4ownpm7LmnpfnuKMJ5ZiJ576p57ijCeWxj"%"2Badsee4ownlj7DmnbHnuKMJ6Iqx6JOu57ijCea"%"2Bjua5lue4ownln7rpmobluIIJ5paw56u55biCCeWPsOS4reW4ggnlmInnvqnluIIJ5Y"%"2Bw5Y2X5biCCemHkemWgOe4ownpgKPmsZ"%"2FnuKMVFwEwATEBMgEzATQBNQE2ATcBOQIxMAIxMQIxMgIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNRQrAxdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBZmQCBQ8QZA8WAWYWARAFEuiri"%"2BWFiOmBuOaTh"%"2Be4o"%"2BW4ggUBMGdkZAIJDxYCHgRUZXh0ZWRkd"%"2BTuIrQ"%"2FF8WUr6a"%"2FseU20Sjr4NH"%"2FLgXmxkH7MtCnbaQ"%"3D&__EVENTVALIDATION="%"2FwEWGwLUqtGAAwKd5I"%"2FlCgKNi6WLBgKSi6WLBgKTi6WLBgKQi6WLBgKRi6WLBgKWi6WLBgKXi6WLBgKUi6WLBgKKi6WLBgKSi"%"2BWIBgKSi"%"2BmIBgKSi"%"2B2IBgKSi9mIBgKSi92IBgKSi8GIBgKSi4WLBgKSi4mLBgKTi"%"2BWIBgKTi"%"2BmIBgKTi"%"2B2IBgKTi9GIBgKTi9WIBgKTi9mIBgKOi6WLBgKM54rGBsIHFqCV0TzwENfeTcuCJaINSvb6OFvVtTwP1JeOQ4X"%"2B&DropDownList1=2&DropDownList2=0"
# curl "http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H
# "Cookie: ASPSESSIONIDQSQDABQB=BBCIAFLDBLDJIMGHNDJGJEJL;
# ASPSESSIONIDSQQQBARA=OJAPNIKDNAGBHAIEFDFFBHLC" -H "Origin:
# http://www.taiwanlottery.com.tw" -H "Accept-Encoding: gzip, deflate" -H
# "Accept-Language:
# zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2,ko;q=0.2" -H
# "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT
# 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107
# Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H
# "Accept:
# text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
# -H "Cache-Control: max-age=0" -H "Referer:
# http://www.taiwanlottery.com.tw/Lotto/se/salelocation.aspx" -H
# "Connection: keep-alive" --data
# "__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE="%"2FwEPDwUJNzkzNTQ1MDA0D2QWAgIBD2QWBgIDDxBkEBUXD"%"2Biri"%"2BmBuOaTh"%"2Be4o"%"2BW4ggnlj7DljJfluIIJ6auY6ZuE5biCCeaWsOWMl"%"2BW4ggnlrpzomK3nuKMJ5qGD5ZyS5biCCeaWsOeruee4ownoi5fmoJfnuKMJ5b2w5YyW57ijCeWNl"%"2BaKlee4ownpm7LmnpfnuKMJ5ZiJ576p57ijCeWxj"%"2Badsee4ownlj7DmnbHnuKMJ6Iqx6JOu57ijCea"%"2Bjua5lue4ownln7rpmobluIIJ5paw56u55biCCeWPsOS4reW4ggnlmInnvqnluIIJ5Y"%"2Bw5Y2X5biCCemHkemWgOe4ownpgKPmsZ"%"2FnuKMVFwEwATEBMgEzATQBNQE2ATcBOQIxMAIxMQIxMgIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNRQrAxdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgJkAgUPEGQQFSYL5paw6IiI5Y2AICAL5YmN6YeR5Y2AICAL6IuT6ZuF5Y2AICAL6bm95Z"%"2BV5Y2AICAL6byT5bGx5Y2AICAL5peX5rSl5Y2AICAL5YmN6Y6u5Y2AICAL5LiJ5rCR5Y2AICAL5qWg5qKT5Y2AICAL5bCP5riv5Y2AICAL5bem54ef5Y2AICAL5LuB5q2m5Y2AICAL5aSn56S"%"2B5Y2AICAL5bKh5bGx5Y2AICAL6Lev56u55Y2AICAL6Zi"%"2F6JOu5Y2AICAL55Sw5a"%"2Bu5Y2AICAL54eV5bei5Y2AICAL5qmL6aCt5Y2AICAL5qKT5a6Y5Y2AICAL5b2M6ZmA5Y2AICAL5rC45a6J5Y2AICAL5rmW5YWn5Y2AICAL6bOz5bGx5Y2AICAL5aSn5a"%"2Bu5Y2AICAL5p6X5ZyS5Y2AICAL6bOl5p2"%"2B5Y2AICAL5aSn5qi55Y2AICAL5peX5bGx5Y2AICAL576O5r"%"2BD5Y2AICAL5YWt6b6c5Y2AICAL5YWn6ZaA5Y2AICAL5p2J5p6X5Y2AICAL55Sy5LuZ5Y2AICAL5qGD5rqQ5Y2AICAN6YKj55Gq5aSP5Y2AIAvojILmnpfljYAgIAvojITokKPljYAgIBUmC"%"2BaWsOiIiOWNgCAgC"%"2BWJjemHkeWNgCAgC"%"2BiLk"%"2BmbheWNgCAgC"%"2Bm5veWfleWNgCAgC"%"2Bm8k"%"2BWxseWNgCAgC"%"2BaXl"%"2Ba0peWNgCAgC"%"2BWJjemOruWNgCAgC"%"2BS4ieawkeWNgCAgC"%"2BaloOaik"%"2BWNgCAgC"%"2BWwj"%"2Ba4r"%"2BWNgCAgC"%"2BW3pueHn"%"2BWNgCAgC"%"2BS7geatpuWNgCAgC"%"2BWkp"%"2BekvuWNgCAgC"%"2BWyoeWxseWNgCAgC"%"2Bi3r"%"2BerueWNgCAgC"%"2BmYv"%"2BiTruWNgCAgC"%"2BeUsOWvruWNgCAgC"%"2BeHleW3ouWNgCAgC"%"2Bapi"%"2BmgreWNgCAgC"%"2Baik"%"2BWumOWNgCAgC"%"2BW9jOmZgOWNgCAgC"%"2BawuOWuieWNgCAgC"%"2Ba5luWFp"%"2BWNgCAgC"%"2Bmzs"%"2BWxseWNgCAgC"%"2BWkp"%"2BWvruWNgCAgC"%"2Bael"%"2BWckuWNgCAgC"%"2BmzpeadvuWNgCAgC"%"2BWkp"%"2BaoueWNgCAgC"%"2BaXl"%"2BWxseWNgCAgC"%"2Be"%"2Bjua"%"2Fg"%"2BWNgCAgC"%"2BWFrem"%"2BnOWNgCAgC"%"2BWFp"%"2BmWgOWNgCAgC"%"2Badieael"%"2BWNgCAgC"%"2BeUsuS7meWNgCAgC"%"2Bahg"%"2Ba6kOWNgCAgDemCo"%"2BeRquWkj"%"2BWNgCAL6IyC5p6X5Y2AICAL6IyE6JCj5Y2AICAUKwMmZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAIJDxYCHgRUZXh0ZWRksCBXzeN5axvkI9Q0s9PDO8fRXkcfwL"%"2FqXBtHq6iCKZM"%"3D&__EVENTVALIDATION="%"2FwEWQAKqiKa9AQKd5I"%"2FlCgKNi6WLBgKSi6WLBgKTi6WLBgKQi6WLBgKRi6WLBgKWi6WLBgKXi6WLBgKUi6WLBgKKi6WLBgKSi"%"2BWIBgKSi"%"2BmIBgKSi"%"2B2IBgKSi9mIBgKSi92IBgKSi8GIBgKSi4WLBgKSi4mLBgKTi"%"2BWIBgKTi"%"2BmIBgKTi"%"2B2IBgKTi9GIBgKTi9WIBgKTi9mIBgKe1rLtBAKvsurQDALls7X9DgLHvvvFBAKq6oulBwLwrIaHAwKvsr6wAwLyiuD6BgK7k9jcCQK4raHlCgKCieLSCgK6uJS2DALi4Pv8CwKYxOmlBwKa66SRDAL"%"2F3cOLCgLp1pKyDAKs1YBGAuqivvcDAqr3i6gMAoz5pMcPAuHCsd4MAs6kiOcJAorQjKUHAp7hu7IMArHY2YMEAuHKgO4EAuDgh9ICAu6s1qUHApnPgbYHAszs980IApnip6EHArWJzbgGAqnW"%"2FpALAryl68kFArrTysQMAtzG"%"2FbkGAtLGzc4LAoznisYGCWBBRZNn7fvhsyJWGvuMJgK"%"2BbEoPZxWo59R7rKDYbDg"%"3D&DropDownList1=2&DropDownList2="%"E5"%"89"%"8D"%"E9"%"87"%"91"%"E5"%"8D"%"80++&Button1="%"E6"%"9F"%"A5"%"E8"%"A9"%"A2"
# --compressed
