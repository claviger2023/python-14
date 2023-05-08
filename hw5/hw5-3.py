def sanitize_phone_number(phone):
    phone = phone.replace("+", "").replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
    return phone