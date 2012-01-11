#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2011, Kovid Goyal <kovid@kovidgoyal.net>'
__docformat__ = 'restructuredtext en'

import os, io
from SimpleHTTPServer import SimpleHTTPRequestHandler

class HTTPRequestHandler(SimpleHTTPRequestHandler):
    '''
    Handle Range headers, as browsers insist on using range for <video> tags.
    Note: Range header is ignored when listing directories.
    '''

    server_version = "TestHTTP/1"
    protocol_version = 'HTTP/1.1'
    extensions_map = SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map.update({
        '': 'application/octet-stream', # Default
        '.py': 'text/plain',
        '.c': 'text/plain',
        '.h': 'text/plain',
        '.mp4' : 'video/mp4',
        '.ogg' : 'video/ogg',
        '.webm': 'video/webm',
    })
    # FAVICON {{{
    FAVICON = b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x00\x00\x00\x00h\x05\x00\x00\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00\x08\x00\x00\x00\x00\x00@\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x00(4\xdd\x00RWX\x00\x00\x00w\x00\x05N[\x00a`\xf1\x00.|\x8a\x00\x03\x03\xb7\x00\x1c)-\x00-,`\x00\x03\x02F\x00  \xbb\x00\x13\x13\x92\x00\x16\x16\xdc\x00\x08\x07!\x00\x17\x12d\x00:GJ\x00@?k\x00% w\x00\x01\x01\x9b\x00\x07\x03\xd2\x00\x01\x00[\x00\x12\x17\x18\x00\x11\x111\x00,,\xcb\x007M`\x00\x0e\x0e\xa4\x00\n\n\x83\x00#+R\x00"!\xe1\x00\x1f\x1aX\x00\x14\x14\xb2\x00\x0b\rO\x00\n\nq\x00\x08\x08\x92\x0032\xd6\x00))\xbc\x00\x08\x08<\x00\x11+2\x00\x02\x02\x86\x00%#l\x001E[\x00#"\xc5\x00\x15\x15\x9c\x00\r\r\x99\x00\x0f\x0f<\x00#"\\\x00\x1c\x1b\xe1\x00\n\t)\x00\x14\x1d\xd8\x00\x1f\x1fp\x00\x07\x07x\x00\x02\x02N\x00\x17.5\x00\x05\x05Y\x00\x01\x00T\x00\x1f\x1ew\x00\x06\x06~\x00\x0b\x0b\x1e\x00\x00\x00\xb3\x00\x08\tL\x00\x01\x01r\x00\x0b\x109\x00&&\xbe\x00\x04\x04\x89\x00\n\x05\xd2\x00\x08\x08\x81\x00\x03\x03\x9c\x00\x02\x02\xb5\x00\x02\x02[\x00\r\r\xa3\x00\x02\x02\x85\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x007\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16F58\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x04(H>1\x00\x00\x00\x00\x00\x00\x00\x00\x009A<E\x08\x14C3\x00\x00\x00\x00\x00\x00\x00\x00@4&D:;\x1c%\x00\x00\x00\x00\x00\x00\x00\x00+".\x1b\r\x18#\x0c\x00\x00\x00\x00\x00\x00\x00\x00/G\x1e\x19$\x0e-)\x00\x00\x00\x00\x00\x00\x00\x00\x1f \x06\x12\n0,\x13\x00\x00\x00\x00\x00\x00\x00\x00\x10\x15\x02\x1a*2B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x1d\x11\t?=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x03\x17\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x006\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\xfe\x7f\x00\x00\xfc?\x00\x00\xf8\x1f\x00\x00\xf0\x0f\x00\x00\xf0\x0f\x00\x00\xf0\x0f\x00\x00\xf0\x0f\x00\x00\xf0\x0f\x00\x00\xf0\x1f\x00\x00\xf8\x1f\x00\x00\xfc?\x00\x00\xfe\x7f\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00'
    # }}}

    def parse_range_header(self, size):
        start_range = 0
        end_range = -1
        rtype = 206 if 'Range' in self.headers else 200

        if "Range" in self.headers:
            s, e = self.headers['range'][6:].split('-', 1)
            sl = len(s)
            el = len(e)
            if sl > 0:
                start_range = int(s)
                if el > 0:
                    end_range = int(e) + 1
            elif el > 0:
                ei = int(e)
                if ei < size:
                    start_range = size - ei
        return rtype, start_range, end_range

    def send_file(self, f, mimetype, mtime):
        f.seek(0, 2)
        size = f.tell()
        f.seek(0)
        rtype, start_range, end_range = self.parse_range_header(size)

        if end_range <= start_range:
            end_range = size
        self.send_response(rtype)
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Range", 'bytes '
                + str(start_range) + '-' + str(end_range - 1) + '/' + str(size))
        self.send_header("Content-Type", str(mimetype))
        self.send_header("Content-Length", str(end_range - start_range))
        self.send_header("Last-Modified", self.date_time_string(int(mtime)))
        self.end_headers()
        return f, start_range, end_range

    def send_bytes(self, raw, mimetype, mtime):
        return self.send_file(io.BytesIO(raw), mimetype, mtime)

    def do_GET(self):
        f, start_range, end_range = self.send_head()
        if f:
            with f:
                f.seek(start_range, 0)
                chunk = 0x1000
                total = 0
                while True:
                    if start_range + chunk > end_range:
                        chunk = end_range - start_range
                    if chunk < 1:
                        break
                    try:
                        self.wfile.write(f.read(chunk))
                    except:
                        break
                    total += chunk
                    start_range += chunk

    def do_HEAD(self):
        f, start_range, end_range = self.send_head()
        if f:
            f.close()

    def send_head(self):
        if self.path == '/favicon.ico':
            return self.send_bytes(self.FAVICON, 'image/x-icon', 1326214111.485359)

        path = self.translate_path(self.path)
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                # redirect browser - doing basically what apache does
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return (None, 0, 0)
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                f = self.list_directory(path)
                f.seek(0, 2)
                sz = f.tell()
                f.seek(0)
                return (f, 0, sz)

        ctype = self.guess_type(path)
        try:
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return (None, 0, 0)
        fs = os.fstat(f.fileno())
        return self.send_file(f, ctype, fs.st_mtime)

