def add_custom_errors(promo_code_form_):
    code_data = promo_code_form_.data.get('code')
    if not promo_code_form_.is_valid():
        pass
    if not code_data.startswith('2020'):
        promo_code_form_.add_error("code", "promo code is expired")
    if not code_data.endswith("django"):
        promo_code_form_.add_error("code", "checksum is invalid")
