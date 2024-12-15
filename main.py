import streamlit as s


s.set_page_config(page_title="Mon an", page_icon=":hamburger:", layout="wide")
s.title("Mon an cua ban")
with s.form(key='my_form', clear_on_submit=True):
  kv = s.multiselect("Chon mon khai vi: ",['sup','salad','pizza'])
  mc = s.multiselect("Chon mon chinh: ",['com chien','ga nuong','bo xao'])
  mp = s.multiselect("Chon mon trang mieng: ",['banh bong lan','trai cay','banh chuoi'])
  submit = s.form_submit_button("Submit")
  if submit:
    if kv != mc != mp != '':
      s.write("Da nop thanh cong")
    if kv == '':
      s.write("Chua chon mon khai vi")
    if mc == '':
      s.write("Chua chon mon chinh")
    if mp == '':
      s.write("Chua chon mon trang mieng")
s.write("Mon khai vi ban chon: ")
for i in range(len(kv)):
  s.write('➕',kv[i])
s.write("Mon chinh ban chon: ")
for i in range(len(mc)):
  s.write('➕',mc[i])
s.write("Mon trang mieng ban chon: ")
for i in range(len(mp)):
  s.write('➕',mp[i])
  