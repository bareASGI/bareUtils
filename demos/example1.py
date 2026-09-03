from bareutils import parse_form_data


def main() -> None:
    body = b"""\
--delimiter12345\r\n\
Content-Disposition: form-data; name="field1"\r\n\
\r\n\
value1\r\n\
--delimiter12345\r\n\
Content-Disposition: form-data; name="field2"; filename="example.txt"\r\n\
\r\n\
value2\r\n\
--delimiter12345--\r\n"""
    parsed_data = parse_form_data(body, b"delimiter12345")
    print(parsed_data)


if __name__ == "__main__":
    main()
