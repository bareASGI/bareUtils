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
