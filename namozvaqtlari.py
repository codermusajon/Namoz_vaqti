import requests
from bs4 import BeautifulSoup as BS
import lxml
from deep_translator import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

t = requests.get('https://namozvaqtlari.com/namoz/6-namoz-vaqtlari-toshkent.html')
html_t = BS(t.content, 'html.parser')
t_bomdod= html_t.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
t_btime= html_t.find('div', class_="namoz-time").find('div', class_='info').find('p').text

t_peshin= html_t.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
t_ptime= html_t.find('div', class_="namoz-time").find_all('p')[2].text.strip()

t_asr= html_t.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
t_atime= html_t.find('div', class_="namoz-time").find_all('p')[3].text.strip()

t_shom= html_t.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
t_stime= html_t.find('div', class_="namoz-time").find_all('p')[4].text.strip()

t_xufton= html_t.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
t_xtime= html_t.find('div', class_="namoz-time").find_all('p')[5].text.strip()

thistime= html_t.find('div', class_='thistime').text.strip()


j = requests.get('https://namozvaqtlari.com/namoz/13-jizzax-namoz-vaqtlari-bugungi-namoz-vaqti.html')
html_j = BS(j.content, 'html.parser')
j_bomdod= html_j.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
j_btime= html_j.find('div', class_="namoz-time").find('div', class_='info').find('p').text

j_peshin= html_j.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
j_ptime= html_j.find('div', class_="namoz-time").find_all('p')[2].text.strip()

j_asr= html_j.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
j_atime= html_j.find('div', class_="namoz-time").find_all('p')[3].text.strip()

j_shom= html_j.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
j_stime= html_j.find('div', class_="namoz-time").find_all('p')[4].text.strip()

j_xufton= html_j.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
j_xtime= html_j.find('div', class_="namoz-time").find_all('p')[5].text.strip()

a = requests.get('https://namozvaqtlari.com/namoz/7-andijon-namoz-vaqtlari-bugungi-namoz-vaqti.html')
html_a = BS(a.content, 'html.parser')
a_bomdod= html_a.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
a_btime= html_a.find('div', class_="namoz-time").find('div', class_='info').find('p').text

a_peshin= html_a.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
a_ptime= html_a.find('div', class_="namoz-time").find_all('p')[2].text.strip()

a_asr= html_a.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
a_atime= html_a.find('div', class_="namoz-time").find_all('p')[3].text.strip()

a_shom= html_a.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
a_stime= html_a.find('div', class_="namoz-time").find_all('p')[4].text.strip()

a_xufton= html_a.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
a_xtime= html_a.find('div', class_="namoz-time").find_all('p')[5].text.strip()


b = requests.get("https://namozvaqtlari.com/namoz/8-buxoro-namoz-vaqtlari-bugungi-namoz-vaqti.html")
html_b = BS(b.content, 'html.parser')
b_bomdod= html_b.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
b_btime= html_b.find('div', class_="namoz-time").find('div', class_='info').find('p').text

b_peshin= html_b.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
b_ptime= html_b.find('div', class_="namoz-time").find_all('p')[2].text.strip()

b_asr= html_b.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
b_atime= html_b.find('div', class_="namoz-time").find_all('p')[3].text.strip()

b_shom= html_b.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
b_stime= html_b.find('div', class_="namoz-time").find_all('p')[4].text.strip()

b_xufton= html_b.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
b_xtime= html_b.find('div', class_="namoz-time").find_all('p')[5].text.strip()

k = requests.get("https://namozvaqtlari.com/namoz/15-qarshi-namoz-vaqtlari-bugungi-namoz-vaqti.html")
html_k = BS(k.content, 'html.parser')
k_bomdod= html_k.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
k_btime= html_k.find('div', class_="namoz-time").find('div', class_='info').find('p').text

k_peshin= html_k.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
k_ptime= html_k.find('div', class_="namoz-time").find_all('p')[2].text.strip()

k_asr= html_b.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
k_atime= html_b.find('div', class_="namoz-time").find_all('p')[3].text.strip()

k_shom= html_b.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
k_stime= html_b.find('div', class_="namoz-time").find_all('p')[4].text.strip()

k_xufton= html_b.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
k_xtime= html_b.find('div', class_="namoz-time").find_all('p')[5].text.strip()

nv = requests.get("https://namozvaqtlari.com/namoz/12-navoiy-namoz-vaqtlari-bugungi-namoz-vaqti.html")
html_nv = BS(nv.content, 'html.parser')
nv_bomdod= html_nv.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
nv_btime= html_nv.find('div', class_="namoz-time").find('div', class_='info').find('p').text

nv_peshin= html_nv.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
nv_ptime= html_nv.find('div', class_="namoz-time").find_all('p')[2].text.strip()

nv_asr= html_nv.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
nv_atime= html_nv.find('div', class_="namoz-time").find_all('p')[3].text.strip()

nv_shom= html_nv.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
nv_stime= html_nv.find('div', class_="namoz-time").find_all('p')[4].text.strip()

nv_xufton= html_nv.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
nv_xtime= html_nv.find('div', class_="namoz-time").find_all('p')[5].text.strip()

na = requests.get("https://namozvaqtlari.com/namoz/11-namangan-namoz-vaqtlari-bugungi-namoz-vaqti.html")
html_na = BS(na.content, 'html.parser')
na_bomdod= html_na.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
na_btime= html_na.find('div', class_="namoz-time").find('div', class_='info').find('p').text

na_peshin= html_na.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
na_ptime= html_na.find('div', class_="namoz-time").find_all('p')[2].text.strip()

na_asr= html_na.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
na_atime= html_na.find('div', class_="namoz-time").find_all('p')[3].text.strip()

na_shom= html_na.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
na_stime= html_na.find('div', class_="namoz-time").find_all('p')[4].text.strip()

na_xufton= html_na.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
na_xtime= html_na.find('div', class_="namoz-time").find_all('p')[5].text.strip()

nu = requests.get("https://namozvaqtlari.com/namoz/14-nukus-namoz-vaqtlari-bugungi-namoz-vaqti.html")
html_nu = BS(nu.content, 'html.parser')
nu_bomdod= html_nu.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
nu_btime= html_nu.find('div', class_="namoz-time").find('div', class_='info').find('p').text

nu_peshin= html_nu.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
nu_ptime= html_nu.find('div', class_="namoz-time").find_all('p')[2].text.strip()

nu_asr= html_nu.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
nu_atime= html_nu.find('div', class_="namoz-time").find_all('p')[3].text.strip()

nu_shom= html_nu.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
nu_stime= html_nu.find('div', class_="namoz-time").find_all('p')[4].text.strip()

nu_xufton= html_nu.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
nu_xtime= html_nu.find('div', class_="namoz-time").find_all('p')[5].text.strip()

s = requests.get("https://namozvaqtlari.com/namoz/10-samarqand-namoz-vaqtlari-bugungi-namoz-vaqti.html")
html_s = BS(s.content, 'html.parser')
s_bomdod= html_s.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
s_btime= html_s.find('div', class_="namoz-time").find('div', class_='info').find('p').text

s_peshin= html_s.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
s_ptime= html_s.find('div', class_="namoz-time").find_all('p')[2].text.strip()

s_asr= html_s.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
s_atime= html_s.find('div', class_="namoz-time").find_all('p')[3].text.strip()

s_shom= html_s.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
s_stime= html_s.find('div', class_="namoz-time").find_all('p')[4].text.strip()

s_xufton= html_s.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
s_xtime= html_s.find('div', class_="namoz-time").find_all('p')[5].text.strip()

ma = requests.get("https://namozvaqtlari.com/namoz/18-margilon-namoz-vaqtlari-bugungi-namoz-vaqti.html")
html_te = BS(ma.content, 'html.parser')
te_bomdod= html_te.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
te_btime= html_te.find('div', class_="namoz-time").find('div', class_='info').find('p').text

te_peshin= html_te.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
te_ptime= html_te.find('div', class_="namoz-time").find_all('p')[2].text.strip()

te_asr= html_te.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
te_atime= html_te.find('div', class_="namoz-time").find_all('p')[3].text.strip()

te_shom= html_te.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
te_stime= html_te.find('div', class_="namoz-time").find_all('p')[4].text.strip()

te_xufton= html_te.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
te_xtime= html_te.find('div', class_="namoz-time").find_all('p')[5].text.strip()

gu = requests.get("https://namozvaqtlari.com/namoz/9-guliston-namoz-vaqtlari-bugungi-namoz-vaqti.html")
html_u = BS(gu.content, 'html.parser')
u_bomdod= html_u.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
u_btime= html_u.find('div', class_="namoz-time").find('div', class_='info').find('p').text

u_peshin= html_u.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
u_ptime= html_u.find('div', class_="namoz-time").find_all('p')[2].text.strip()

u_asr= html_u.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
u_atime= html_u.find('div', class_="namoz-time").find_all('p')[3].text.strip()

u_shom= html_u.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
u_stime= html_u.find('div', class_="namoz-time").find_all('p')[4].text.strip()

u_xufton= html_u.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
u_xtime= html_u.find('div', class_="namoz-time").find_all('p')[5].text.strip()

qo = requests.get("https://namozvaqtlari.com/namoz/16-qoqon-namoz-vaqtlari-bugungi-namoz-vaqti.html")
html_qo = BS(qo.content, 'html.parser')
qo_bomdod= html_qo.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
qo_btime= html_qo.find('div', class_="namoz-time").find('div', class_='info').find('p').text

qo_peshin= html_qo.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
qo_ptime= html_qo.find('div', class_="namoz-time").find_all('p')[2].text.strip()

qo_asr= html_qo.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
qo_atime= html_qo.find('div', class_="namoz-time").find_all('p')[3].text.strip()

qo_shom= html_qo.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
qo_stime= html_qo.find('div', class_="namoz-time").find_all('p')[4].text.strip()

qo_xufton= html_qo.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
qo_xtime= html_qo.find('div', class_="namoz-time").find_all('p')[5].text.strip()


kh = requests.get("https://namozvaqtlari.com/namoz/17-xiva-namoz-vaqtlari-bugungi-namoz-vaqti.html")
html_kh = BS(kh.content, 'html.parser')
kh_bomdod= html_kh.find('div', class_="namoz-time").find('div', class_='info').find('h2').text
kh_btime= html_kh.find('div', class_="namoz-time").find('div', class_='info').find('p').text

kh_peshin= html_kh.find('div', class_="namoz-time").find_all('h2')[2].text.strip()
kh_ptime= html_kh.find('div', class_="namoz-time").find_all('p')[2].text.strip()

kh_asr= html_kh.find('div', class_="namoz-time").find_all('h2')[3].text.strip()
kh_atime= html_kh.find('div', class_="namoz-time").find_all('p')[3].text.strip()

kh_shom= html_kh.find('div', class_="namoz-time").find_all('h2')[4].text.strip()
kh_stime= html_kh.find('div', class_="namoz-time").find_all('p')[4].text.strip()

kh_xufton= html_kh.find('div', class_="namoz-time").find_all('h2')[5].text.strip()
kh_xtime= html_kh.find('div', class_="namoz-time").find_all('p')[5].text.strip()






def city():
    return [
        [InlineKeyboardButton("Toshkent", callback_data=f"01")],
        [InlineKeyboardButton("Jizzax", callback_data=f"02")],
        [InlineKeyboardButton("Andijon", callback_data=f"03")],
        [InlineKeyboardButton("Buxoro", callback_data=f"04")],
        [InlineKeyboardButton("Qarshi", callback_data=f"05")],
        [InlineKeyboardButton("Navoiy", callback_data=f"06")],
        [InlineKeyboardButton("Namangan", callback_data=f"07")],
        [InlineKeyboardButton("Nukus", callback_data=f"08")],
        [InlineKeyboardButton("Samarqand", callback_data=f"09")],
        [InlineKeyboardButton("Marg`ilon", callback_data=f"10")],
        [InlineKeyboardButton("Guliston", callback_data=f"11")],
        [InlineKeyboardButton("Qo`qon", callback_data=f"12")],
        [InlineKeyboardButton("Xiva", callback_data=f"13")]


    ]


def back():
    return [
        [InlineKeyboardButton("Orqaga", callback_data=f"back1")]
    ]


def inline_handlerlar(update, context):
    query = update.callback_query
    data = query.data.split("_")

    if data[0] == "01":
        query.message.edit_text(f"Vaqt:  {thistime} \n {t_bomdod} : {t_btime} \n {t_peshin} : {t_ptime} \n {t_asr} : {t_atime} \n {t_shom} : {t_stime} \n {t_xufton} : {t_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "02":
        query.message.edit_text(f"Vaqt:  {thistime} \n {j_bomdod} : {j_btime} \n {j_peshin} : {j_ptime} \n {j_asr} : {j_atime} \n {j_shom} : {j_stime} \n {j_xufton} : {j_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "03":
        query.message.edit_text(f"Vaqt:  {thistime} \n {a_bomdod} : {a_btime} \n {a_peshin} : {a_ptime} \n {a_asr} : {a_atime} \n {a_shom} : {a_stime} \n {a_xufton} : {a_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "04":
        query.message.edit_text(f"Vaqt:  {thistime} \n {b_bomdod} : {b_btime} \n {b_peshin} : {b_ptime} \n {b_asr} : {b_atime} \n {b_shom} : {b_stime} \n {b_xufton} : {b_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "05":
        query.message.edit_text(f"Vaqt:  {thistime} \n {nv_bomdod} : {nv_btime} \n {k_peshin} : {k_ptime} \n {k_asr} : {k_atime} \n {k_shom} : {k_stime} \n {k_xufton} : {k_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "06":
        query.message.edit_text(f"Vaqt:  {thistime} \n {t_bomdod} : {t_btime} \n {nv_peshin} : {nv_ptime} \n {nv_asr} : {nv_atime} \n {nv_shom} : {nv_stime} \n {nv_xufton} : {nv_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "07":
        query.message.edit_text(f"Vaqt:  {thistime} \n {na_bomdod} : {na_btime} \n {na_peshin} : {na_ptime} \n {na_asr} : {na_atime} \n {na_shom} : {na_stime} \n {na_xufton} : {na_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "08":
        query.message.edit_text(f"Vaqt:  {thistime} \n {nu_bomdod} : {nu_btime} \n {nu_peshin} : {nu_ptime} \n {nu_asr} : {nu_atime} \n {nu_shom} : {nu_stime} \n {nu_xufton} : {nu_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "09":
        query.message.edit_text(f"Vaqt:  {thistime} \n {s_bomdod} : {s_btime} \n {s_peshin} : {s_ptime} \n {s_asr} : {s_atime} \n {s_shom} : {s_stime} \n {s_xufton} : {s_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "10":
        query.message.edit_text(f"Vaqt:  {thistime} \n {te_bomdod} : {te_btime} \n {te_peshin} : {te_ptime} \n {te_asr} : {te_atime} \n {te_shom} : {te_stime} \n {te_xufton} : {te_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "11":
        query.message.edit_text(f"Vaqt:  {thistime} \n {u_bomdod} : {u_btime} \n {u_peshin} : {u_ptime} \n {u_asr} : {u_atime} \n {u_shom} : {u_stime} \n {u_xufton} : {u_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "12":
        query.message.edit_text(f"Vaqt:  {thistime} \n {qo_bomdod} : {qo_btime} \n {qo_peshin} : {qo_ptime} \n {qo_asr} : {qo_atime} \n {qo_shom} : {qo_stime} \n {qo_xufton} : {qo_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))
    elif data[0] == "13":
        query.message.edit_text(f"Vaqt:  {thistime} \n {kh_bomdod} : {kh_btime} \n {kh_peshin} : {kh_ptime} \n {kh_asr} : {kh_atime} \n {kh_shom} : {kh_stime} \n {kh_xufton} : {kh_xtime}  \nManzilimiz: @namoz_infobot",
                                reply_markup=InlineKeyboardMarkup(back()))


    elif data[0] == 'back1':
        query.message.edit_text(
            f"Bu yerdan Shahar yoki viloyatni tanla 👇",
            reply_markup=InlineKeyboardMarkup(city()))


def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"""Salom {user.first_name} 🖐🏼\nBu yerdan Shahar yoki viloyatni tanla 👇""",
                              reply_markup=InlineKeyboardMarkup(city()))


def main():
    Token = "5635819457:AAH1JoxyAwlWV0JgqTakILYA-C44IODdCyQ"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()