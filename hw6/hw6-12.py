import base64


def encode_data_to_base64(data):
    message = data
    result_list = []
    for k in data:
        message_bytes = k.encode("utf-8")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("utf-8")
        result_list.append(base64_message)
    return result_list