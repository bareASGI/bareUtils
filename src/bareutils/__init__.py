"""Exports from bareUtils"""

from .compression import (
    Compressor,
    CompressorFactory,
    make_gzip_compressobj,
    make_deflate_compressobj,
    make_compress_compressobj,
    compression_writer_adapter,
    compression_writer,
    Decompressor,
    DecompressorFactory,
    make_gzip_decompressobj,
    make_deflate_decompressobj,
    make_compress_decompressobj,
    compression_reader_adapter,
    compression_reader
)

from .cookies import (
    encode_set_cookie,
    decode_set_cookie,
    encode_cookies,
    decode_cookies
)

from .multipart import (
    MultipartFile,
    MultipartFormData,
    parse_form_data,
)

from .streaming import (
    text_reader,
    text_writer,
    bytes_reader,
    bytes_writer
)


__all__ = [

    # .compression
    'Compressor',
    'CompressorFactory',
    'Decompressor',
    'DecompressorFactory',
    'make_gzip_compressobj',
    'make_deflate_compressobj',
    'make_compress_compressobj',
    'compression_writer_adapter',
    'compression_writer',
    'make_gzip_decompressobj',
    'make_deflate_decompressobj',
    'make_compress_decompressobj',
    'compression_reader_adapter',
    'compression_reader',

    # .cookies
    "encode_set_cookie",
    "decode_set_cookie",
    "encode_cookies",
    "decode_cookies",

    # .multipart
    "MultipartFile",
    "MultipartFormData",
    "parse_form_data",

    # .streaming
    "text_writer",
    "text_reader",
    "bytes_writer",
    "bytes_reader",

]
