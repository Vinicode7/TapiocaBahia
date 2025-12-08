from flask import redirect

# Redireciona para o WhatsApp do restaurante
def ir_whatsapp():
    numero = "5511919478993"  # coloque o número do restaurante
    return redirect(f"https://wa.me/{numero}")

# Redireciona para Instagram
def ir_instagram():
    url = "https://www.instagram.com/tapioca_do_bahia/"
    return redirect(url)

# Redireciona para TikTok
def ir_tiktok():
    url = "https://www.tiktok.com/@tapiocadobahia.01"
    return redirect(url)

# Redireciona para Facebook
def ir_facebook():
    url = "https://www.facebook.com//tapiocadobahia/?ref=_xav_ig_profile_page_web#"
    return redirect(url)
