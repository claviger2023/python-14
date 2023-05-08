def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    jp_phones = []
    ua_phones = []
    tw_phones = []
    sg_phones = []

    for phone in list_phones:
        new_phone = sanitize_phone_number(phone)
        if new_phone.find("81") == 0:
            jp_phones.append(new_phone)
        elif new_phone.find("65") == 0:
            sg_phones.append(new_phone)
        elif new_phone.find("886") == 0:
            tw_phones.append(new_phone)
        else:
            ua_phones.append(new_phone)

    new_list_phones = {
        "UA": ua_phones,
        "JP": jp_phones,
        "TW": tw_phones,
        "SG": sg_phones
    }
    
    return new_list_phones