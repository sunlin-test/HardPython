import time

def test_needfiles(tmp_path):
    print(tmp_path)
    d = tmp_path / 'sub'
    print(d)
    # 真实创建子文件夹： 文件夹只能通过mkdir()创建，文件可以通过d/'文件名'直接创建
    d.mkdir()
    p = d / "Hello.txt"
    print(type(p))
    p.write_text("test")
    assert 0

