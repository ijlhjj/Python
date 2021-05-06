""" 字符序列工具类模块

"""


def to_str(bytes_or_str):
    """
    字符序列类型转换：
        输入 bytes or str
        如果为 str，原样返回；
        如果为 bytes，以'utf-8'编码转换。
    """
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str

    return value


def to_bytes(bytes_or_str):
    """
    字符序列类型转换：
        输入 bytes or str
        如果为 bytes，原样返回；
        如果为 str，以'utf-8'编码转换。
    """
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str

    return value
