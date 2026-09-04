from bareutils import parse_form_data


def test_parse_form_data() -> None:
    data = b"""\
--delimiter12345\r\n\
Content-Disposition: form-data; name="field1"\r\n\
\r\n\
value1\r\n\
--delimiter12345\r\n\
Content-Disposition: form-data; name="field2"; filename="example.txt"\r\n\
\r\n\
value2\r\n\
--delimiter12345--\r\n"""
    fields, files = parse_form_data(data, b"delimiter12345")
    assert fields == {
        'field1': ['value1']
    }
    assert files == {
        'field2': [
            {
                'filename': 'example.txt',
                'content_type': 'text/plain',
                'content': b'value2'
            }
        ]
    }


def test_parse_form_data_with_default_charset() -> None:
    data = b"""\
--delimiter12345\r\n\
Content-Disposition: form-data; name="field1"\r\n\
\r\n\
\xc2\xA9\r\n\
--delimiter12345\r\n\
Content-Disposition: form-data; name="field2"; filename="example.txt"\r\n\
\r\n\
value2\r\n\
--delimiter12345--\r\n"""
    fields, files = parse_form_data(data, b"delimiter12345")
    assert fields == {
        'field1': ["\u00a9"]
    }
    assert files == {
        'field2': [
            {
                'filename': 'example.txt',
                'content_type': 'text/plain',
                'content': b'value2'
            }
        ]
    }


def test_parse_form_data_with_global_charset() -> None:
    data = b"""\
--delimiter12345\r\n\
Content-Disposition: form-data; name="_charset_"\r\n\
\r\n\
iso-8859-1\r\n\
--delimiter12345\r\n\
Content-Disposition: form-data; name="field1"\r\n\
\r\n\
\xA9\r\n\
--delimiter12345\r\n\
Content-Disposition: form-data; name="field2"; filename="example.txt"\r\n\
\r\n\
value2\r\n\
--delimiter12345--\r\n"""
    fields, files = parse_form_data(data, b"delimiter12345")
    assert fields == {
        'field1': [b'\xA9'.decode('iso-8859-1')]
    }
    assert files == {
        'field2': [
            {
                'filename': 'example.txt',
                'content_type': 'text/plain',
                'content': b'value2'
            }
        ]
    }


def test_parse_form_data_with_local_charset() -> None:
    data = b"""\
--delimiter12345\r\n\
Content-Disposition: form-data; name="field1"; charset=iso-8859-1\r\n\
Content-Type: text/plain; charset=iso-8859-1\r\n\
\r\n\
\xA9\r\n\
--delimiter12345\r\n\
Content-Disposition: form-data; name="field2"; filename="example.txt"\r\n\
\r\n\
value2\r\n\
--delimiter12345--\r\n"""
    fields, files = parse_form_data(data, b"delimiter12345")
    assert fields == {
        'field1': [b'\xA9'.decode('iso-8859-1')]
    }
    assert files == {
        'field2': [
            {
                'filename': 'example.txt',
                'content_type': 'text/plain',
                'content': b'value2'
            }
        ]
    }
