from typing import TypedDict

from . import header


class MultipartFile(TypedDict):
    filename: str
    content_type: str
    content: bytes


class MultipartFormData(TypedDict):
    fields: dict[str, list[str]]
    files: dict[str, list[MultipartFile]]


def _to_header(line: bytes) -> tuple[bytes, bytes]:
    name, sep, value = line.partition(b":")
    if not sep:
        raise ValueError(f"Malformed header line: {line.decode()}")
    return name.strip().lower(), value.strip()


def parse_form_data(
        data: bytes,
        boundary: bytes
) -> tuple[dict[str, list[str]], dict[str, list[MultipartFile]]]:
    delimiter = b"--" + boundary + b"\r\n"
    if not data.startswith(delimiter):
        raise ValueError("Data does not start with the expected boundary.")

    sentinal = b"\r\n--" + boundary + b"--\r\n"
    if not data.endswith(sentinal):
        raise ValueError("Data does not end with the expected boundary.")

    # Trim off the start boundary and the sentinal
    data = data[len(delimiter):-len(sentinal)]

    default_charset = 'utf-8'
    fields: dict[str, list[str]] = {}
    files: dict[str, list[MultipartFile]] = {}

    for part in data.split(delimiter):

        header_data, sep, content = part.partition(b"\r\n\r\n")
        if not sep:
            raise ValueError(
                "Malformed part: missing header/content separator.")

        headers = [
            _to_header(line)
            for line in header_data.split(b"\r\n")
        ]

        content_disposition = header.content_disposition(headers)
        if not content_disposition:
            raise ValueError("Missing Content-Disposition header.")

        disposition, params = content_disposition
        if disposition != b"form-data" or not params or b'name' not in params:
            raise ValueError("Invalid Content-Disposition header.")

        name = params[b"name"].decode()
        filename = params.get(b"filename")

        content_type = header.content_type(headers)
        if content_type is not None:
            media_type, content_params = content_type
        else:
            media_type, content_params = b"text/plain", None

        content = content.rstrip(b"\r\n")

        if filename is None:

            if name == "_charset_":
                default_charset = content.decode('ascii')
            else:
                if content_params is None or b"charset" not in content_params:
                    charset = default_charset
                else:
                    charset = content_params[b"charset"].decode('ascii')

                value = content.decode(charset)
                fields.setdefault(name, []).append(value)
        else:
            file: MultipartFile = {
                "filename": filename.decode(),
                "content_type": media_type.decode(),
                "content": content
            }
            files.setdefault(name, []).append(file)

    return fields, files
