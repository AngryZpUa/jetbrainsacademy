def get_cleaned_data(raw_data):
    data = PromoCodeForm(raw_data)
    if data.is_valid():
        return data.cleaned_data
    return {}
