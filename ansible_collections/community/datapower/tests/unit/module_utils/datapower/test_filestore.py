from __future__ import absolute_import, division, print_function

__metaclass__ = type

from faker.factory import Factory

from ansible_collections.community.datapower.plugins.module_utils.datapower import files

def gen_lines():
    Faker = Factory.create
    fake = Faker()
    lines = []
    for _ in range(5):
        lines.append(fake.paragraph(nb_sentences=5, variable_nb_sentences=False))
    return lines


class MockLocalFile():
    def __init__(self, lines):
        self.lines = lines

    def get_lines(self):
        return self.lines


def test_get_file_diff_when_from_and_to_are_equal():
    from_lines = gen_lines()
    to_lines = from_lines.copy()
    from_local_file = MockLocalFile(from_lines)
    to_local_file = MockLocalFile(to_lines)
    assert files.get_file_diff(
        from_local_file,
        to_local_file,
        '/some/other/path/file.txt',
        'present'
    ) == []

def test_get_file_diff_when_from_and_to_are_different():
    from_lines = gen_lines()
    to_lines = gen_lines()
    from_local_file = MockLocalFile(from_lines)
    to_local_file = MockLocalFile(to_lines)

    assert files.get_file_diff(
        from_local_file,
        to_local_file,
        '/some/other/path/file.txt',
        'present'
    )[0:2] == ['*** before: /some/other/path/file.txt\n', '--- after: /some/other/path/file.txt\n']


def test_get_file_diff_when_state_is_present_and_from_local_file_is_none():
    to_lines = gen_lines()
    from_local_file = None
    to_local_file = MockLocalFile(to_lines)


    assert files.get_file_diff(
        from_local_file,
        to_local_file,
        '/some/other/path/file.txt',
        'present'
    ) ==  {'before': None, 'after': '/some/other/path/file.txt'}


def test_get_file_diff_when_state_is_absent_and_to_local_file_is_none():
    to_lines = gen_lines()
    from_local_file = MockLocalFile(to_lines)
    to_local_file =  None

    assert files.get_file_diff(
        from_local_file,
        to_local_file,
        '/some/other/path/file.txt',
        'absent'
    ) ==  {'before': '/some/other/path/file.txt', 'after': None}


def test_get_file_diff_when_state_is_absent_and_to_from_local_files_are_none():
    from_local_file = None
    to_local_file =  None

    assert files.get_file_diff(
        from_local_file,
        to_local_file,
        '/some/other/path/file.txt',
        'absent'
    ) ==  {'before': None, 'after': None}


def test_get_files_from_filestore_single_file():
    filestore_resp = {
        "_links": {
            "self": {
                "href": "/mgmt/filestore/default/local"
            },
            "doc": {
                "href": "/mgmt/docs/filestore"
            }
        },
        "filestore": {
            "location": {
                "name": "local:",
                "file": {
                    "name": "demo.txt",
                    "size": 12,
                    "modified": "2021-07-13 13:07:41",
                    "href": "/mgmt/filestore/default/local/demo.txt"
                },
                "directory": [
                    {
                        "name": "local:/snafu",
                        "href": "/mgmt/filestore/default/local/snafu"
                    },
                    {
                        "name": "local:/subdir",
                        "href": "/mgmt/filestore/default/local/subdir"
                    },
                    {
                        "name": "local:/foo",
                        "href": "/mgmt/filestore/default/local/foo"
                    },
                    {
                        "name": "local:/local",
                        "href": "/mgmt/filestore/default/local/local"
                    }
                ],
                "href": "/mgmt/filestore/default/local"
            }
        }
    }

    files_from_filestore = files.get_files_from_filestore(filestore_resp)
    assert files_from_filestore == ['/mgmt/filestore/default/local/demo.txt']


def test_get_files_from_filestore_multiple_files():
    filestore_resp = {
        "_links": {
            "self": {
                "href": "/mgmt/filestore/default/local"
            },
            "doc": {
                "href": "/mgmt/docs/filestore"
            }
        },
        "filestore": {
            "location": {
                "name": "local:",
                "file": [
                    {
                        "name": "demo.txt",
                        "size": 12,
                        "modified": "2021-07-13 13:07:41",
                        "href": "/mgmt/filestore/default/local/demo.txt"
                    },
                    {
                        "name": "demo2.txt",
                        "size": 12,
                        "modified": "2021-07-13 13:07:41",
                        "href": "/mgmt/filestore/default/local/demo2.txt"
                    },
                        {
                        "name": "demo3.txt",
                        "size": 12,
                        "modified": "2021-07-13 13:07:41",
                        "href": "/mgmt/filestore/default/local/demo3.txt"
                    }
                ],
                "directory": [
                    {
                        "name": "local:/snafu",
                        "href": "/mgmt/filestore/default/local/snafu"
                    },
                    {
                        "name": "local:/subdir",
                        "href": "/mgmt/filestore/default/local/subdir"
                    },
                    {
                        "name": "local:/foo",
                        "href": "/mgmt/filestore/default/local/foo"
                    },
                    {
                        "name": "local:/local",
                        "href": "/mgmt/filestore/default/local/local"
                    }
                ],
                "href": "/mgmt/filestore/default/local"
            }
        }
    }

    files_from_filestore = files.get_files_from_filestore(filestore_resp)
    assert files_from_filestore == [
        '/mgmt/filestore/default/local/demo.txt',
        '/mgmt/filestore/default/local/demo2.txt',
        '/mgmt/filestore/default/local/demo3.txt',
    ]


def test_get_parent_dir():
    path = '/some/test/path/file.txt'
    assert files.get_parent_dir(path) == '/some/test/path'

